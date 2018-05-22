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

### 03: 参数类型忽略

* 我们可能会定义一些常量, 比如: `const USER_TYPE_XXX = 1`
* 然后我们会在代码中做比对, `if (type === USER_TYPE_XXX)`
* 有的时候我们会忽略掉类型, 比如: `request.query.type` 是 `string`

### 04: 后端API返回字段变更了

* 字段名变了
* 删除了某字段

### 04: 难以避免的类型错误

* 一般在新代码开发时, 可能不太容易犯此类错误, 考虑如下case:
  - 一开始吧啦吧啦写了个功能, 有某个计算属性值 `xPrice` 之类, 组件中其他地方有值比较之类的, 如:

```js
computed: {
  xPrice() {
    return ...
  }
}

if (xPrice > ...) {
  ...
}
```

  - 某一天, 产品说, `price` 精确到 `xx` 位, 于是, 改为:

```js
computed: {
  xPrice() {
    return (...).toFixed(xx) // BUG 诞生了
  }
}
```

* `null >= 0`, `null <= 0`
