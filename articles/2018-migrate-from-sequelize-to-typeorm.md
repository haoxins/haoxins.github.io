---
title: migrate to typeorm from sequelize
description: 一个更加开发友好的 ORM 框架
date: 2018-01-11
---

## Why ?

- `声明`: 本人暂未在生产环境使用 `typeorm` :)

### 传参更人性化, 不容易犯一些低级错误

* 比如: 在 `sequelize` 中的 `findOne`, 常见使用如下

```js
await User.findOne({
  where: {
    type: 10
  }
})
```

笔者有时候会忘记 `where` (尤其是在一段时间不用 `sequelize` 之后), 即:

```js
await User.findOne({
  type: 10
})
```

而在 `typeorm` 中

```ts
await connection
  .getRepository(User)
  .createQueryBuilder('user')
  .where('user.type = :type', {type: 10})
```

上述代码其实还不够明显, 试着对比如下两段代码

* `sequelize`

```js
await User.find({
  where: { // 不要觉得不可思议, 这里忘记 where 不是啥低概率事件
    age: {
      [Op.gt]: 17
    }
  },
  order: [['id', 'DESC']],
  offset: 1, // 如果参数传的足够多, 传参出错其实是不容易发现的
  limit: 2
})
```

* `typeorm`

```ts
// 当把查询的 n 个条件用链式写法拆分之后, 其实更利于开发
await connection
  .getRepository(User)
  .createQueryBuilder('user')
  .where('user.age > :age', {age: 17})
  .orderBy({
    'user.id': 'DESC'
  })
  .limit(2)
  .offset(1)
  .getMany()
```

### join 查询的方式

### 事务的使用更直观, 代码不易出疏忽

