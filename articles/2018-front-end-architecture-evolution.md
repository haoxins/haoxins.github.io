
### 关于 CSS 的处理

一上来就说这个, 不是因为他最重要, 而是我觉得现有的解决方案已经很好了, 衡量标准如下:

1. 支持最小粒度的 css 复用 (粒度有多小)
  - 命名 class name 有时真的很纠结
  - 如果依赖 css selector, 一旦 html 变化, 呵呵, 而且, 难看
2. 天然的配合组件化
  - 其实可以很直观的衡量, 就是 css 如何最完美的和 html 整合
  - 我越发的觉得 css 应该与 html 整合在一起
3. 相较于 flexbox, grid layout 在部分场景能更加降低 html 层次
  - 之前需要 html 添加层次来完成布局, grid layout 直接可以做到
  - chrome devtool 对 grid layout 的支持也是相当的棒
4. 与 js 结合的便利性
  - 最常见的场景是动画, 即动画除了过渡效果外, 还与组件状态(用户操作)密切相关
  - 在常规的场景中, 通过 class name 的增删达到目的
  - 有时候, 你需要配置 asset host, 比如: `//xxx.cdn.com`, 同时需要在 css, js 中用到

* 最终必须亮出自己的明确观点: `styled components`

### 前端开发普遍存在的挑战

* 数据一致性
* 校验统一
* 用户一套流程导致的代码逻辑的强内聚
* UI, action, data 如何分离与统一
* 多端时代, model 与 view 尽可能分离, 尽可能复用一套逻辑
  - 小程序
  - web (跨view层框架, vue react ...)
  - app (甚至)
* view 层的主流解决方案基本都是OK的, react, vue
  - 个人认为 react 更优, 但截至 react@16, vue@2, 没有质的区别
  - 至于 react-native, react-ar, react-vr 之流, 道阻且长
* model 层实践至今, 众人应该认识到: 没有银弹, 所以:
  - 框架简单, 与view层弱相关, 设计理念中规中矩(不要主张过强), 能够很便利的解决90%的常规业务场景即可
  - 以redux为例, 主张过强的反弹是: 1. 使用者大都不会严格遵守, 2. 遇到edge cases依旧需要外部方案
  - mobx 适合, 可用于项目级别, 也可以用于组件级别
  - redux 一来繁琐, 二来矫枉过正
  - rxjs 太重且学习曲线大

### 前端需要什么样的基础设施

场景四: 外部事件源
例如: 某一数据状态, 依赖于 localStorage 的某一值, 该值会变化 (城市, 类目缓存在本地, 但会变化, 更新频率低)


场景三: 异步属性依赖(更新)
场景: 用户下单 user 切换 product, (1. productId 变更 -> product) . 随着 product 的变更,
拉取关联数据 评论, 猜你喜欢, 图片

场景二: 状态同步(状态冗余)
这其实也是双向绑定容易出问题的地方, 也就是表示同一个状态位的state存在多个地方.
比如: 从一个表格中标记选中了几行.
一般: 如果选择了第三方表格组件, 可能组件内部存了一份
在组件外部, 相关逻辑会需要这个状态位, 也会存一份

这种场景适合单向数据流, 而非双向绑定

场景一: 最典型的OO场景
class Person {}

// person1, person2, person3
实际场景: 聊天室


场景二: 多处数据 (联动&组合) (不同数据实体间, 或 同一数据实体在多个地方使用)
自行脑补画面 - 1
左侧是用户信息页, 右侧是用户 timeline. 左侧给用户加了条 跟进 -> timeline (1 -> 1 联动)
自行补充类似场景
2 - 米奇跟进框
当前客户变更 -> 跟进的客户 不变
修改了跟进客户联系人 -> 跟进的客户 联系人 选项相应变化
其他 events
组合数据通道越多, rxjs 的优势越大 (无组合, 无优势)
除了PC端 (大屏), 直接跃入脑海的是 -> (VR/AR 场景)


场景四: 频率限制
某一 SB, 死命点击 刷新 按钮, 并发 ...
input 输入时, 调 api search
确保最后一次变更调 API
搜索结果返回的 时序


场景五: 状态联动 (同一数据实体的状态变更) vs 场景二
step1 - 选择某一状态 -> step2 - 可选状态基于前者
从 list -> detail, 在 detail 点击 下一个/上一个
关联其他数据联动


场景五: 行为触发 (events)
某一行为的发生, 触发其他行为
比如: user call xxx, mark xxx done, refresh timeline
从某种意义上来说, events 和双向绑定有类似的地方.
只要限制住 events chain 的层级, 可以大大简化代码逻辑
最常见的是单层 发布, 订阅. emit('xx') -> on('xx')
但是, 一旦形成 events chain, 那就麻烦了. (代码逻辑难以厘清)
坏的实践

// file: user-list.js
event.emit('xx call oo', ...)
...

// file: timeline.js

event.on('xx call oo', () => {
  event.emit('another event')
})
可能导致事件死循环

场景七: 表单编辑
双向绑定
表单本身其实也是无法组件化的 (1. 普通意义的表单, 2. 无需组件化)
此时的单向数据流是 繁琐的


重新审视 app 场景, 从 state 角度, 所有导致 state 变更的源头
user actions - events
server push - events
flux 最初的模式 - events
rx* 在其他端 (swift) 解决 async & events, 在 web 前端 主要是 events

app -> state 是永远的 堆积, 这是一个较大的挑战
所有的场景都是有 context 的, pre state -> current -> next



之前的解决方案
双向绑定
双向绑定有其适用场景 (比如: 表单编辑)
只要双向绑定不形成 多层依赖, 便是 可控, 便利 (一夫一妻 <-> 多角关系)
完全否定双向绑定的价值是 sb 的
变更追踪困难
// 仅作示例, 忽略语法细节
// file a
const a = {...}

if (xxx) {
  a.xxx = ooo
}

...
// file b
const b = bind(a)

if (zzz) {
  b.zzz = ...
}
单向数据流
不形成 责任反馈 的 单向关系. 不负责 -> 无麻烦
action -> data change
one store vs multi stores
one store -> 业务组件无法分离
store 复杂 -> 必须 reducer -> action chain 较长 -> 状态逻辑分离 store (redux), state (react component)
multi store
store 间通讯
rxjs
rxjs 并没有解决问题, (逻辑溜不溜, 归根到底还是看谁写的)
rxjs 提供了解决工具






目标
业务组件可拆分
状态逻辑高内聚
组件间通讯 (store) 便利
允许多种数据模式 - 单向数据流, 双向绑定
无框架 (无限制是把双刃剑)
为何是此时此刻
rx 社区 成熟了
这不是前端社区的浪潮, 这是几乎所有 C 端 (ios, android, wpf, 其他) 社区的统一作战
BTW: redux 在 mobile 端也有实践, 但少有人问津
相较于其他平台, 前端 标准 支持. (换种说法: rxjs 的 lib 会比较 小)
我始终坚信微软 是 C 端开发的, 真正的先行者
component, reactive, ...
然后
rx 是有学习曲线的
rx 更要求使用者的自我代码驾驭能力
其实 rx 可以和现有的一些设计模式结合, 如若不, 其实是 需要 使用者 自行 解决的
rx 不是解决了 上层的数据模式, 是 不限制上层的数据模式
换句话说: 再写不好代码, 就再也不能把脏水泼到 angular, redux 身上了
类似于现在 各种 轻量级的 web 框架



redux
成也 one store, 败也 one store
业务组件拆分几乎不可能
stateless 组件实现代价高
reducer, action 繁琐
业务组件独立的场景在类似于 `admin` 之类的后台 app 中或许不多,
但在其他复杂场景中的 需求 还是比较常见的. 这是 `one store` 的硬伤.

action, reducer 的模式略显繁琐, 这也直接导致的 很多 component 内部
会维护 state, `state` vs `store` 其实已经导致了逻辑不统一.
密切相关的逻辑, 应该集中在一处: 比如, 切换某一个组件的视图状态.

难免纠结于某一逻辑:

`放在 component` vs `放在 action`;
`放在 action` vs `放在 reducer`;
`放在 reducer` vs `放在 component`;
......
events or push data 集成

async & await 解决的是 async pull 且 only one result
比如: ws push msgs
比如: get data -> 1. service worker return -> 2. api refresh -> 3. server push
React 其实 还不够 只做 view

React - not just view, but should be!
React 官方宣称 only view

但是: state -> model
input -> state => controller
render -> view
lifecycle hooks -> oh my god
only view! only view! only view!



从 redux & react 汲取到的
单向数据流
(多层次)双向意味着: 变更不可(难)追踪
stateless component
逻辑 分离 & 内聚
JSX, 不管你 喜欢 vs 厌恶. 你不得不承认: 这是中庸之选
cycle.js: jsx
skatejs: jsx
vuejs: jsx
不是最好, 但最通用
redux & flux 是前端社区 真正意义 上的, 第一次 模式 的探讨.
mvc, mvvm 等在前端社区其实只是比较浅的概念, 没有真正的实践落地.
双向绑定 只是个 function, 谈不上 pattern.
时机背景, 当 spa 不再被强调时, 其实 spa 才真正迎来一定的 业务复杂度
时机背景, flux 推出之初并未 火 起来, 而是慢慢发展了近1年
时机背景, spa 框架混战(2013~2014?)后, spa 才慢慢流行.
此时: spa 的复杂度还没上来, dev 们正沉浸在 ng1 的各种快感中, DI, T Bind, router, module
时机背景, ng1赢得spa框架霸主地位后, 宣布 ng2 计划 -> React 爆炸
spa 复杂度上升, (ng1) 背锅, 各种面临的挑战 全是 ng1 的设计缺陷
换言之, 近2年, 前端社区才真正 认真 思考 & 面对 复杂度 的挑战, 之前:
浏览器兼容
现代浏览器兼容性问题少多了, 还有的问题基本也被 stackoverflow 搞定了
module, dom 等温饱问题还没解决
h5 的欢腾带来一些东西吸引了社区的过度关注: canvas, wegGL, ......
鼓吹者们撸起袖子, 到处喊着 占领全世界
没有 mobile 的浪潮, 也不会有今天的 复杂度 盛世
startup 们开始 推行 api only server
业务, 需求 没堆积起来?
社区前10%人群质量提高?


Why rxjs ?
ES201x 标准落地 Observable
rxswift, rxandroid, rxjava, rx**** 完善的社区支持
just library, not framework
统一所有 data source 的处理
pull: promise, async & await
push
event
stream
one action -> multi responses
助力: stateless component
真正的 组件化
多平台, 统一(类似) 的组件化实现模式
如果只保留一个理由: redux 很难剥离业务组件 (真正的组件化)



### 矫枉不过正



### 可能超前的想法

组件级 ABCD 测试, 灰度发布等

### See Also

https://www.zhihu.com/question/277623017/answer/409520763

