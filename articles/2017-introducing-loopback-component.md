---
title: loopback component
description: 简介
date: 2017-09-24
---

## 什么是 component ?

* 在 `loopback` 中, `component` 可以实现如下功能
  - 与 `controller` 交互
  - 为 `context` 注入自定义的值
  - 与 `model` 交互
  - 与 `repository` 交互

* 大体上, `loopback` 中的 `component` 的定位类似于 `koa` 和 `express` 中的 `middleware`

## component 的使用

* 以 `authentication` 为例

```ts
import {Application} from '@loopback/core'
import {AuthenticationComponent} from '@loopback/authentication'

const app = new Application()
app.component(AuthenticationComponent)
```

* 也可以在实例化 `Application` 时定义

```ts
const app = new Application({
  components: [AuthenticationComponent],
})
```

## 如何自定义 component ?

* 先来看一个最简单的 `component`

```ts
// component
import {Component, ProviderMap} from '@loopback/core'

class MyComponent implements Component {
  providers?: ProviderMap
  constructor() {
    this.providers = {
      'my-component.my-value': MyValueProvider
    }
  }
}

// provider
import {Provider} from '@loopback/context'

export class MyValueProvider implements Provider<string> {
  // 这里使用 async 仅仅是说明: provider 可以是异步的
  async value() {
    return 'Hello world'
  }
}
```

```ts
// application
import {
  Application,
  inject,
  param,
  get
} from '@loopback/core'

const app = new Application()

app.component(MyComponent)

class MyController {
  greeting: string

  constructor(@inject('my-component.my-value') greeting: string) {
    this.greeting = greeting
  }

  @get('/')
  hello() {
    return this.greeting
  }
}

app.controller(MyController)

app.start()
```


* `component` 通过 `class` 定义, 当 `component` 在 `application` 中实例化时
