---
title: 从一个典型的场景看 rxjs 的应用
description: 记最近的一个案例
date: 2017-11-19
---

### 题记

社区内有不少关于 `rxjs` 的优质文章, 但大多数的视角从介绍 `rxjs` 的概念入手.
最近正好在一个典型的业务场景中用到了 `rxjs` 解决一些数据管理的问题, 对相关的核心代码做了下总结梳理.
希望能够从业务实现的角度切入, 看看 `rxjs` 的使用. 对于场景中用到的 `rxjs` 的相关概念, 由于篇幅原因,
仅做简单介绍, 但是会在文末列出一些个人觉得写得很好的文章, 作为补充.

业务场景很常见, 基本做过 `admin` 类的前端开发的同学都很熟悉.
页面上方是 `条件筛选区`, 比如: `时间范围`, `数据类型` 等.
页面下方就是一张 `table` 展示查询结果.

是不是 90% 的 admin 页面都长得这式样 :) 但是, 也有一些特别的地方, 或者场景特殊限制.

### 需求一: 异步请求并发, 但响应结果保持时序

1. 由于后端数据量大, 查询逻辑非常复杂, 单次查询耗时 `500ms - 3000ms` 不等, 甚至更长
2. 使用者是运营人员, 操作会很频繁, 不接受每次变更查询条件后手动点击 `查询` 按钮触发查询, 即: 筛选条件变更, 自动查询

原本, 常见的场景中, 不会有用户操作是 `秒级` 的, 咱也不是秒杀下单.
同时, 大多的前后端业务交互的 http 请求也基本在数百毫秒.
但由于上述条件限制, 相关的技术需求就是:

前端会发送 n 次 http request, 但 response 的时序很大概率是乱序的,
需要保证 response 按照 request 的时序排序, 永远取最新值 render.

```
request 顺序:
A -> B -> C -> D
但 response 的顺序可能是:
A -> C -> D -> B
```

我们先行定义一些基础代码如下:

```js
// 假设我们的查询条件定义如下
let opts = { /* ... */ }

// 当用户变更查询条件时, 视图层做相应变更
opts = Object.assign({}, opts, {
  /* ... */
})

// 假设 http request 函数如下
async function request(query) {
  /* ... */
}
```

上述的需求再细化, 有如下几点:

1. 请求行为是随着用户操作不断进行的, 也就是 `无限`
2. 不能将请求同步化, 上文提到, 我们的请求比较耗时
3. 结果必须是最后一次请求的结果, 否则, 查询结果与筛选条件不一致
4. 当后一次请求结束时 (拿到结果), 在这之前发出的所有请求其实都无意义了 (至少对前端是如此 >_<)

不知道读者朋友有没有能用很少代码便实现上述需求的,
至少我个人琢磨了下, 实现上述需求还是需要一定代码量的.

如果使用 `rxjs`, 这种需求是可以轻易解决的

```js
Observable.interval(500)
  .map(() => opts)
  .distinctUntilChanged()
  .switchMap(opts => request(opts))
  .subscribe(data => {
    /* render */
  })
```

上述 `5行` 代码便满足了我们的需求, 此处做一个简单的说明

* `.interval(500)` 创建了一个数字队列, 每隔 `500ms` 发出一个数字 (数字时间流).
这里其实把他用作定时器, 模拟用户行为

```js
Observable.interval(500)
  .subscribe(n => console.log(n))
// output: 0, 1, 2, 3, 4, 5 ...
```

* `.map()` 在这里我们直接返回了 `opts`
* `.distinctUntilChanged()` 保证了只有当前值与先前值不一样时才会发送 (注: 不会做深度比较)

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

* `.switchMap()` 在这里不去深入挖掘 `switchMap` 的功能, 网上有不少讲解 `switchMap`, `mergeMap`, `*Map` 的优质文章
  - 此处, 由于 `request` 返回的是一个 `Promise`, `switchMap` 在处理新的请求时, 会忽略之前的请求, 只处理最新的一个
  - 如果, 我们的实现是使用 `Observable.ajax`, 是 `cancelable` 的, 则先前的 `http` 请求会被 `cancel`

其实, 写到这里, 大家也就能感受到 `rxjs` 的强大.
但是, 个人却在此处想说的是, 我并不赞同将 `rxjs` 应用到所有场景.
个人只是在部分复杂场景使用 `rxjs`, 毕竟, 大多场景下, 没有请求队列, 也不需要 `cancel request`

### 需求二: 合并外部事件

在我们当前的页面区域, 相当于一个 `bashboard` 页面. 在我们的业务场景中, 运营人员可以直接进入该页面,
同时, 是可以在其他的数据实体页面点击某一数据行, 跳转进入该页面的. (比如: 用户列表, 点击某一用户). 此时:

  - 查询条件会在点击数据行时诞生 (外部页面), 同时查询条件复杂 (如包含嵌套的 object 等). 不适合作为 querystring 传入
  - 点击数据行 -> 转为查询参数的逻辑希望聚合在当前页面的代码逻辑内


此时, 我们添加如下代码

```js
const subject = new ReplaySubject()

export function gotoDashboardFromUserList(user) {
  const opts = {
    // ...
  }

  subject.next(opts)
}
```

我们原有的查询代码则相应的合并这个 `subject`

```js
// 添加如下 一行

  .merge(subject)

// 则现有代码为

Observable.interval(500)
  .merge(subject)
  .map(() => opts)
  .distinctUntilChanged()
  .switchMap(opts => request(opts))
  .subscribe(data => {
    /* render */
  })
```

与此同时, 在我们的整个 `admin` 系统中, 是有实时的消息推送的, 会有一个消息列表.
其中, 部分消息类型需要触发 `dashboard` 刷新 (如果当前页面是 `dashboard`).

### 事件回放

有一天, 运营同学跑过来说, 我们平时查询很快啊, 有时候需要回顾, 但忘记之前是哪些筛选条件了 (尼玛, 这是金鱼记忆么 ?).
总之, 你给我加个历史记录, 我可以回退查询 !

OK, 最终梳理的需求如下, 保留最近的 `7` 次查询条件, 可以点击 `返回` 按钮执行上一次查询 (直至无法继续返回),
在返回过程中, 一但再次便跟条件触发查询, 历史记录栈塞入当前此次查询. 示意如下:

```
A -> B -> C -> D -> E -> F
// 返回, 返回, 返回
A -> B -> C
// 又查询了一次
A -> B -> C -> G
```

### 异步属性依赖

原本, 文章写到这也就结束了, 但奈何需求还没做完啊 ! 准确说, 还没开始做 ...

上文提到, 筛选条件比较复杂, 其中有些筛选条件还是有关系依赖的.
比如: 性别选择完之后, 胸围的选项肯定是不一样的 (开个玩笑).
并且, 我们的(部分)筛选条件是不固定的, 即 `维度一` 的选项是动态的,
需要 `http` 请求获取, 依赖 `维度一` 的 `维度二`, 也是动态的.
而且, 有一定的实时性要求, 且选项不少.

直接说重点就是: `不能缓存在本地`, `不能一次性获取`, `我们的依赖层级是: 最多三层`

### See also

* [RxJS 入门指引和初步应用](https://github.com/xufei/blog/issues/44)
