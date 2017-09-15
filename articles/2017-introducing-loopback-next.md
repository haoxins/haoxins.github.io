---
title: 初识 loopback
description: 现代化的 node.js API 框架
date: 2017-08-31
---

## 概述

[loopback v4][lb-repo-url] 是 [strongloop][sl-org-url] 团队打造的新一代 node.js APIs 框架.
原本的 `loopback v3` 基于 [express][express-url], 而在 `v4` 当中则不再依赖.

相较于 `rails`, `django`, `meteor` 等框架, `loopback` 最大的差异在于: 仅提供 `API service`.
后面会有一篇文章再论述 [loopback的前端快速整合方案](articles/2017-loopback-and-angular-admin.md).

* 特点
  - 快速开发, 高效实现业务逻辑
  - 高度可配置, 可扩展
  - 强大的命令行工具, 简单的命令便可产出完整的 `API service`, 定义 `model` 等
  - 便于测试
  - 完善的周边生态, 丰富的组件库
  - 充分利用 `TypeScript` 语法特性
  - 符合 [OpenAPI][open-api-url] 规范

* 功能
  - `代码即文档`: 不是说好的代码就是文档, 而是直接根据代码定义输出完备的 APIs 文档
  - `角色, 权限`: 自带强大的, 灵活的 `role`, `permission` 功能
  - `model, schema`: 支持各种主流的和非主流的数据库, 可靠的 `类ORM` 实现
  - `client SDK`: 可以直接生成各平台SDK, `web`, `ios`, `android` 等

* 生态
  - [extensions](https://github.com/strongloop/loopback-next/issues/512)

* 门槛
  - 会有一定的学习成本

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

## 相关文章

* [详解 Loopback Sequence](articles/todo.md)
* [详解 Loopback Route And Controller](articles/todo.md)
* [详解 Loopback Context](articles/todo.md)
* [详解 Loopback Dependency Injection](articles/todo.md)
* [详解 Loopback Repository](articles/todo.md)
* [详解 Loopback Component](articles/todo.md)
* [详解 Loopback Extension](articles/todo.md)

## 其他特性

* [gRPC 集成](https://github.com/strongloop/loopback-next/issues/521)
* [Serverless 支持](https://github.com/strongloop/loopback-next/issues/257)
* [UML generator](https://github.com/strongloop/loopback-next/issues/345)

## 题外

* 对我个人而言, 看着一个不错的项目 `从 0 到 1 到 N 再到 N + X`,
* 并能参与其中, `有所思考`, `有所贡献`, `有所收获`, 实属快意之事 ~

## 参考文章

* [Crafting LoopBack Next](https://github.com/strongloop/loopback-next/wiki/Crafting-LoopBack-Next)

## License
MIT

[lb-repo-url]: https://github.com/strongloop/loopback-next
[express-url]: https://github.com/expressjs/express
[sl-org-url]: https://github.com/strongloop
[open-api-url]: https://www.openapis.org
