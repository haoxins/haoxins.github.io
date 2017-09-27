---
title: loopback sequence
description: 什么是 sequence ? 如何自定义 sequence ? sequence 的设计优势
date: 2017-09-24
---

## 什么是 sequence ?

* `sequence` 是一个 `work flow`, 是 `request` 到 `response` 的 `work flow`
* 先来个 `hello world`, 虽然完全无法体现 `sequence` 的作用 :)

```ts
import {Application} from '@loopback/core'

const app = new Application()

app.handler(async (sequence, request, response) => {
  sequence.send(response, `hello, world`)
})

app.start()
```

## default sequence

```ts
class DefaultSequence {
  async handle(req: ParsedRequest, res: ServerResponse) {
    try {
      const route = this.findRoute(req)
      const params = this.parseParams(req, route)
      const result = await this.invoke(route, params)
      await this.send(res, result)
    } catch(err) {
      await this.reject(res, err)
    }
  }
}
```

## custom sequence

* 自定义 `sequence` 有多种方式
  - `extends` `DefaultSequence`
  - `implements` `SequenceHandler` (注: 这里是 `TypeScript` 体现语法优势的一个小点)
  - `sequence function`

* 其实, 在 `hello world` 中, 我们已经通过 `sequence function` 的方式自定义了 `sequence`

```ts
app.handler(async function fn(sequence, request, response) => {
  sequence.send(response, `hello, world`)
})

// 在 loopback core 的内部, 会做如下转换:
// ...
class SequenceFromFunction extends DefaultSequence {
  async handle(req: ParsedRequest, res: ServerResponse) {
    await Promise.resolve(fn(this, request, response))
  }
}

this.sequence(SequenceFromFunction)
// ...
```

* extends DefaultSequence 的方式如下:

```ts
import {
  DefaultSequence,
  ParsedRequest,
  CoreBindings,
  Application,
  inject,
  Send
} from '@loopback/core'

import {
  ServerResponse
} from 'http'

const app = new Application()

class MySequence extends DefaultSequence {
  async handle(req: ParsedRequest, res: ServerResponse) {
    console.log('oh ~')
    res.end('bingo ~')
  }
}

app.sequence(MySequence)

app.start()
```

* `implements` `SequenceHandler` 的方式如下:

```ts
import {
  SequenceHandler,
  ParsedRequest,
  CoreBindings,
  Application,
  inject,
  Send
} from '@loopback/core'

import {
  ServerResponse
} from 'http'

const app = new Application()

class MySequence implements SequenceHandler {
  constructor(@inject(CoreBindings.SequenceActions.SEND) private send: Send) {}
  async handle(req: ParsedRequest, res: ServerResponse) {
    console.log('oh ~')
    this.send(res, 'bingo ~')
  }
}

app.sequence(MySequence)

app.start()
```

## sequence 的设计优势

* 上述示例比较简单, 但也能大致勾勒出 `sequence` 模式的优势
  - 便于全局扩展一些功能
  - 如有需要, 完全可以自定义 `核心逻辑`, 组合使用 `Router`, `Controller`, `Component` ... 等
  - 可以在 `loopback` 中直接使用既有的项目代码: `express`, `koa` 等
