---
title: why typescript
description: 单纯罗列一些小的场景
date: 2017-11-03
---

## 概述

* 不做任何宽泛的对比, 文章已经很多了
* 罗列一些平时码代码遇到的一些小坑
* 此时, 心中或许会默念, 卧槽, 要是 `ts` 就直接报错了

## 难以避免的小错误

### 01: 漏写 await

* 场景如下

```js
const transaction = await sequelize.transaction()

// ...
try {
  await Model.create(data, {
    transaction
  })

  transaction.commit() // 此处, 疏忽了 await
}
// ...
```

* 上述错误自然可以通过 `单元测试` 排除
* 但在业务代码中, 单元测试覆盖到这种程度的投入是很大的 (几乎不现实)

### 02: 参数容易传错 且 不易发现

* `sequelize` 中传递 `transaction` 如下

```js
// ...
await Model.findOne({
  where: {
    name: 'hi',
    // ...
  },
  transaction
})
// ...
```
