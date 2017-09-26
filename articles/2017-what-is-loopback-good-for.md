---
title: why loopback next(v4)
description: loopback 能做什么 ? 解决了什么 ?
date: 2017-09-03
---

## 场景

### 应用场景的复杂度决定相关技术的生态质量

* (2015前后)前端的场景复杂度提升 -> 更多的实践, 思考, 产物(轮子)
  - 而 ES20xx, web spec 等, 均是次要因素
* 场景复杂度提升 -> 变化, 积累
* node.js 的 server 场景明显不足 (不成熟)
  - 此处是个人言论

### 没有 `loopback next`, 不谈 `Node.js is Enterprise Ready` !

* 面对常规的业务场景, 需要集成化的解决方案
* 但也不要对 `loopback next` 期望过高. 毕竟, 这是很难玩出新姿势的领域
* [案例](https://github.com/yorkie/me/issues/10)

### Loopback-next 团队成员

* [bajtos](https://www.linkedin.com/in/bajtos)
* [ritchie martori ](https://www.linkedin.com/in/ritchie-martori-9548325)
* [superkhau](https://www.linkedin.com/in/superkhau)
* [raymondfeng 专业写文档](https://www.linkedin.com/in/raymondfeng)
* [crandmck](https://www.linkedin.com/in/crandmck)
  - 专业写文档的, 还有博客
  - 顺便吐个槽, 第一次看到职位: `document team lead`

### LB3 ~ LB4

### 很多时候, 你并不需要高度可扩展

* 从 `loopback auth` 谈起

### 大多数码农都不愿意写文档

* 大多数文档是缺失的
* 大多数文档是过时的
* 文档离代码越近, 越受重视, 维护的质量越高
  - 很多码农对代码有质量要求, 但对文档没有

### 没有适合所有场景的模式, 但可以应对主流场景

* 不是所有项目都会迭代, 都有机会迭代
* 不同的项目就是有不同的优先级

### 测试很重要, 别说后面会补

* 有比没有好
* 早写比晚写好
* `TypeScript` 真的代替不了 `tests`
* 一开始没有, 基本上就不会有了
* 矫枉不过正, 测试不是越多越好
  - [the-ideal-test-suite](https://github.com/strongloop/loopback-next/wiki/Thinking-in-LoopBack#the-ideal-test-suite)

### 我不认为 TypeScript 多么神奇, 但物尽其用

* 再次强调, `TypeScript` 真的代替不了 `tests`

### 所有的优秀项目, 都是想法的集合

* 仅: 抛砖引玉 ~
* 愿: 各有所好 ~

## 题外

* 在 `Github` 等社区, 越是牛逼的人, 说 `Interesting, I didn't know about that.` 的频率越高 ~
  - 碎碎念: 这或许也可以作为量化团队技术氛围的指标 :)

https://github.com/strongloop/loopback-next/issues/537
