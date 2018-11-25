---
title: 初识 loopback
description: 现代化的 node.js API 框架
date: 2017-08-31
---

## Hello, world!

```ts
import {Application} from '@loopback/core'

const app = new Application()

app.handler(async (sequence, request, response) => {
  sequence.send(response, `hello, world`)
})

app.start()
```

## 10min 简单概览

* 说明: `loopback` 的写法比较灵活多样, 此处为了减少篇幅, 会使用我个人偏好的方式

### 定义 Controller

```ts
import {
  Application,
  param,
  get
} from '@loopback/core'

const app = new Application()

class MyController {
  @get('/')
  @param.query.string('name')
  hello(name: string) {
    return `hello, ${name}`
  }
}

app.controller(MyController)

app.start()
```

### 上下文: Context

### 依赖注入: Dependency Injection

### Repository

* 配置数据源

```ts
import {
  DataSourceConstructor
} from '@loopback/repository'

const db = new DataSourceConstructor({
  connector: 'memory',
  name: 'db'
})
```

* 定义 Model

```ts
import {
  property,
  Entity,
  model
} from '@loopback/repository'

@model()
class User extends Entity {
  @property({type: 'number', id: true})
  id: number

  @property({type: 'string'})
  name: string
}
```

* 定义 Repository

```ts
import {
  DefaultCrudRepository
} from '@loopback/repository'

class UserRepository extends DefaultCrudRepository<User, typeof User.prototype.id> {
  constructor() {
    super(User, db)
  }
}
```

* 定义 Controller, 并绑定 Repository

```ts
import {
  repository
} from '@loopback/repository'

import {
  Application,
  inject,
  param,
  post,
  get
} from '@loopback/core'

const app = new Application()

class UserController {
  constructor(
    @repository('user')
    public repository: UserRepository
  ) {}
  @post('/')
  @param.body('userInstance', {type: 'object'})
  async create(userInstance: User) {
    return await this.repository.create(userInstance)
  }
  @get('/')
  async query() {
    return await this.repository.find()
  }
}

app.bind('repositories.user').toClass(UserRepository)

app.controller(UserController)

app.start()
```

## 核心概念

### Sequence

https://github.com/strongloop/loopback-next/wiki/Sequence

* `Application` 与 `Sequence` 一一对应

* `Elements`

## Thinking in LoopBack

* [官方Wiki地址](https://github.com/strongloop/loopback-next/wiki/Thinking-in-LoopBack)

## 其他特性

* [gRPC 集成](https://github.com/strongloop/loopback-next/issues/521)
* [Serverless 支持](https://github.com/strongloop/loopback-next/issues/257)

## 参考文章

* [Crafting LoopBack Next](https://github.com/strongloop/loopback-next/wiki/Crafting-LoopBack-Next)

[lb-repo-url]: https://github.com/strongloop/loopback-next
[express-url]: https://github.com/expressjs/express
[sl-org-url]: https://github.com/strongloop
[open-api-url]: https://www.openapis.org
