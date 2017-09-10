---
title: why loopback
description: loopback 能做什么 ? 解决了什么 ?
date: 2017-09-03
---

## 场景

### 应用场景的复杂度决定相关技术的生态质量

* (2015年前后)前端的场景复杂度提升 -> 更多的实践, 思考, 产物(轮子)
* 而 ES20xx, web spec 等, 均是次要因素
* 社区变化迅猛的根本原因是场景复杂度提升, 没有这个前提, 轮子出不来(或无人问津)
* 只要场景复杂度能再次提升, 社区的浪潮就会再来 (^_^)

* `loopback (v4)` 是 `node` 社区开始成熟的标志之一
  - 之前的 `node` 社区就是 `不成熟`, `callback` 之类的问题只是表象
  - 如果技术痛点可以解决, 但推进缓慢, 只能是因为: `不够痛` (痛的人不多, 痛的不够深)
  - 业务场景复杂度不够是根本原因, 这才是 `推动力`

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
