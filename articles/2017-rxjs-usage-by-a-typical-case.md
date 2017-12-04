---
title: 从一个典型的场景看 rxjs 的应用
description: 记最近的一个案例
date: 2017-11-19
---

### 题记

社区内有不少关于 `rxjs` 的优质文章, 但大多数的视角从介绍 `rxjs` 的概念或内部实现入手.
最近正好在一个业务场景中用到了 `rxjs`, 对相关的主要功能代码做了下总结梳理.
希望能够从业务实现的角度切入, 看看 `rxjs` 的运用.
对于文中涉及到的 `rxjs` 的相关概念, 由于篇幅原因,仅做简单介绍,
但是会在文末列出一些个人觉得写得挺好的文章, 作为补充.

### 背景

这次的业务场景很常见, 基本做过 `admin` 类的前端开发的同学都很熟悉.
页面上方是 `条件筛选区`, 比如: `时间范围`, `数据类型` 等等.
页面下方就是一张 `table` 展示查询结果.

是不是 `90%` 的 `admin` 页面都长得这式样 :)
但是, 也有一些特别的地方, 或者场景的额外限制.

### 需求一: 异步请求并发, 但响应结果保持时序

1. 由于后端数据量大, 查询逻辑复杂, 单次查询耗时在 `500ms ~ 3000ms` 不等, 甚至更长
2. 使用者是运营人员, 操作很频繁, 不接受每次变更查询条件后手动点击 `查询` 按钮查询, 即: 筛选条件变更, 自动查询

原本, 常见的场景中, 不会有用户操作是 `秒级` 的, 咱也不是秒杀下单.
同时, 大多的前后端业务交互的 `http` 请求也基本在数百毫秒.
但由于上述条件限制, 相关的技术需求便是:

前端会发送 n 次 `http request`, 但 `response` 的时序很大概率是乱序的,
需要保证 `response` 按照 `request` 的时序排序, 永远取最新值 `render`.

```
request 顺序:
A -> B -> C -> D
但 response 的顺序可能是:
A -> C -> D -> B
```

为了简化篇幅, 我们先行定义一些基础代码如下:

```js
// 假设我们的查询条件定义如下
let opts = { /* code */ }

// 当用户变更查询条件时, 视图层做相应变更
opts = Object.assign({}, opts, {
  /* code */
})

// 假设 http request 函数如下
async function request(query) {
  /* code */
}
```

上述的需求再细化, 有如下几点:

1. 请求行为是随着用户操作不断进行的, 也就是 `无限`
2. 不能将请求同步化, 上文提到, 我们的请求比较耗时
3. 结果必须是最后一次请求的结果, 否则, 实际结果的查询结果与筛选条件不一致
4. 当后一次请求结束时 (结果返回), 在这之前发出的所有请求其实都无意义了 (姑且撇开后端不论)

不知道读者朋友有没有能用很少代码便实现上述需求的,
至少我个人琢磨了下, 实现上述需求还是需要一定代码量的.

但是如果使用 `rxjs`, 这种需求是可以轻易解决的

```js
Observable.interval(500)
  .map(() => opts)
  .distinctUntilChanged()
  .switchMap(opts => request(opts))
  .subscribe(data => {
    /* render */
  })
```

上述 `5行` 代码便满足了我们的需求, 此处做一个简单的拆解说明

* `.interval(500)` 创建了一个数字流, 每隔 `500ms` 发出一个数字. 这里其实把他用作定时器

```js
Observable.interval(500)
  .subscribe(n => console.log(n))
// 输出: 0, 1, 2, 3, 4, 5 ...
```

* `.map()` 在这里我们直接返回了 `opts`
* `.distinctUntilChanged()` 保证了只有当前值与先前值不一样时才会发送 (注: 不会做深度比较), 参看下方代码

```js
Observable.interval(500)
  .distinctUntilChanged()
  .subscribe(v => console.log(v))
// 0, 1, 2, 3, 4 ...

Observable.of(1, 2, 3, 3, 2, 1)
  .distinctUntilChanged()
  .subscribe(v => console.log(v))
// 1, 2, 3, 2, 1

const a = b = { name: 'ms' }
Observable.of({ name: 'ms' }, a, b, 'bingo')
  .distinctUntilChanged()
  .subscribe(v => console.log(v))
// { name: 'ms' }, { name: 'ms' }, 'bingo'
```

* `.switchMap()` 在这里不去深入挖掘其功能, 网上有不少讲解 `switchMap`, `mergeMap`, `*Map` 的优质文章
  - 此处, 由于 `request` 返回的是一个 `Promise`, `switchMap` 在处理新的请求时, 会忽略之前的请求, 只处理最新的一个
  - 如果, 我们的实现是使用 `Observable.ajax`, 是 `cancelable` 的, 则先前的 `http` 请求会被 `cancel` 掉

其实, 写到这里, 大家也就能感受到 `rxjs` 的一些强大功能, 但我们的需求还没结束.

### 需求二: 合并外部事件

在当前的页面区域, 类似于一个 `bashboard`. 在我们的业务场景中, 运营人员可以直接进入该页面,
但同时, 是可以在其他的数据实体页面点击某一数据行, 跳转进入该页面的.
(比如: 用户列表, 点击某一用户). 此时:

  - 查询条件会根据所点击数据行确定 (外部页面), 同时查询条件复杂 (如包含嵌套的 object 等). 不适合作为 `querystring` 传入
  - 点击数据行 -> 转为查询参数的逻辑希望聚合在当前页面的代码逻辑内


此时, 我们添加如下代码

```js
const clickItem$ = new ReplaySubject(1)

export function gotoDashboardFromUserList(user) {
  const opts = {
    // ...
  }

  clickItem$.next(opts)
}
```

我们原有的查询代码则相应的合并这个 `clickItem$`

```js
// 添加如下 一行

  .merge(clickItem$)

// 则现有代码为

Observable.interval(500)
  .merge(clickItem$)
  .map(() => opts)
  .distinctUntilChanged()
  .switchMap(opts => request(opts))
  .subscribe(data => {
    /* render */
  })
```

与此同时, 在我们的整个 `admin` 系统中, 是有实时的消息推送的, 会有一个消息列表.
其中, 部分消息类型需要触发 `dashboard` 刷新 (如果当前页面是 `dashboard`).

为了简化代码, 此处简写推送的消息为:

```js
const message$ = new ReplaySubject()
```

我们只需要再加一个 `.merge` 即可

```js
  .merge(message$.filter(v => {
    if (/* 某些类别的消息 */) {
      return true
    } else {
      return false
    }
  }))
```

在上述代码中, 我们用到了 `ReplaySubject`, 不同于 `Subject`,

=== 补充说明 1

需求还没有结束 ~

### 查询回退/前进

有一天, 运营同学跑过来说, 我们平时查询很频繁啊, 有时候需要返回上一次,
但忘记之前是哪些筛选条件了 (尼玛, 这是金鱼记忆么 ?).
总之, 你得给我加个历史记录, 我可以回退查询, 也得可以前进 !

OK, 最终梳理的需求如下, 保留最近的 `7` 次查询条件, 可以点击 `后退` 按钮执行上一次查询 (直至无法继续回退),
在回退过程中, 一但有操作变更条件触发查询 (操作筛选区域), 历史记录栈塞入当前此次查询. 流程示意如下:

```
A -> B -> C -> D -> E -> F
// 后退, 后退, 后退
A -> B -> C
// 前进
A -> B -> C -> D
// 又查询了一次
A -> B -> C -> D -> G
```

此处, 我们按照常规思路, 定义两个数组, 保存 `undos` 和 `redos`

```js
let undos = []
let redos = []
const size = 7
```

* 然后需要保存查询记录, 只需要变更 `map` 操作即可

```js
  .map(opts => {
    undos = undos.concat(opts).reverse()
      .slice(0, size).reverse()
    redos = []
    return opts
  })
```

* 同时, 我们需要监听 `前进/后退` 按钮事件并 `触发查询`,

```js
const redoUndo$ = new Subject()

Observable
  .fromEvent(undoBtn, 'click')
  .subscribe(() => {
    const o = undos.pop()

    if (!o) return

    redos.push(o)

    redoUndo$.next(o)
  })

Observable
  .fromEvent(redoBtn, 'click')
  .subscribe(() => {
    const o = redos.pop()

    if (!o) return

    undos.push(o)

    redoUndo$.next(o)
  })
```

* 此时, 我们的查询 `workflow` 需要合并 `redoUndo$`, 代码变更为如下:

```js

Observable.interval(500)
  .merge(clickItem$)
  .merge(message$.filter(/* code */))
  .map(opts => {
    undos = undos.concat(opts).reverse()
      .slice(0, size).reverse()
    redos = []
    return opts
  })
  .distinctUntilChanged()
  .merge(redoUndo$)
  .switchMap(opts => request(opts))
  .subscribe(data => {
    /* render */
  })
```

### 子视图切换

运营人员再次提出了需求, 查询出的数据行, 支持点击展示详情页.
  - 在详情页会需要额外的 `http` 请求拉取额外信息
  - 进入详情页之后, 支持 `上一个/下一个/返回` 操作

与上述场景类似, 我们同样监听按钮点击事件, 并合并入查询流程, 但是略有差异

```js
let currentIndex = 0

const gotoAction$ = new BehaviorSubject({
  type: 'back'
})

Observable
  .fromEvent(preBtn, 'click')
  .subscribe(() => gotoAction$.next({action: 'pre'}))

Observable
  .fromEvent(nextBtn, 'click')
  .subscribe(() => gotoAction$.next({action: 'next'}))

Observable
  .fromEvent(backToListBtn, 'click')
  .subscribe(() => gotoAction$.next({action: 'back'}))
```

* 相应的, 我们的查询流程的末尾部分也要做相应的调整

```js
  .switchMap(opts => request(opts))
  .combineLatest(event)
  .switchMap(async ([items, action]) => {
    if (action.type === 'next') {
      /* code */
    } else if (action.type === 'pre') {
      /* code */
    } else {
      /* code */
    }
  })
  .subscribe(v => console.log('done:', v))
```

* 此处, 我们用到了 `BehaviorSubject`, 其与 `ReplaySubject` 的差异是:

=== 额外说明 2

* 此处, 我们使用了 `combineLatest` 而非 `merge`, 这两者的差异有为何 ?

=== 额外说明 3

### 异步属性依赖

原本, 文章写到这也就结束了, 但奈何需求远还没做完啊 !

上文提到, 筛选条件比较复杂, 其中有些筛选条件还是有关系依赖的.
比如: 性别选择完之后, 胸围的选项肯定是不一样的 (仅仅举个栗子).
并且, 我们的(部分)筛选条件是不固定的, 即 `维度一` 的选项是动态的,
需要 `http` 请求获取, 基于 `维度一` 的 `维度二`, 也是动态的.
而且, 有一定的实时性要求, 且选项不少.

说白了就是: `不能缓存在本地`, `不能一次性获取`, `我们的依赖层级是: 最多三层`

我们一期需求先告一段落, 下次接着实现: 二期需求 ~

### See also

* [RxJS 入门指引和初步应用](https://github.com/xufei/blog/issues/44)
