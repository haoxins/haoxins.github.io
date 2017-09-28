---
title: Context and Dependency Injection
description: Loopback 上下文 和 依赖注入
date: 2017-09-24
---

## Context

* 说白了, 就是一个 `Class`, 用以管理 `state`, `dependency`, `config` 等 `everything`
* `Application` extends `Context`
* `Loopback` 有两种 `Level` 的 `Context`
  - `Application-level`
  - `Request-level`

### Application-level

```ts
import { Application } from '@loopback/core'
const app = new Application() // `app` is a Application-level `Context`
```

* 生命周期: 整个 `process` 的存续时间
* `app` 创建时 `初始化`, 全局可 `w/r`

### Request-level

```ts
class MySequence extends DefaultSequence {
  handle(req: ParsedRequest, res: ServerResponse) {
    const any = this.ctx.getSync('anything')
    res.end('bingo ~')
  }
}
```

* 生命周期: 整个 `req -> res` 的存续时间
* extends `application level` context

### 常见的使用场景

```ts
const app = new Application()
app.bind('hello').to('world')
console.log(app.getSync('hello'))
```

* 其他 ... TODOs

## Dependency Injection

* 相关概念网上已经有很多介绍了
* 咱说的 `糙` 一点, 就是 `get/set` `爽` 一点

```ts
import { Application } from '@loopback/core'

const app = new Application()

app.bind('name').to('John')

class HelloController {
  constructor(@inject('name') name: string) {
    this.name = name
  }
  greet(name: string) {
    return `Hello ${name || this.name}`
  }
}
```

### 实现原理

### 常见的使用场景
