---
title: Web
description: 槛菊愁烟兰泣露, 罗幕轻寒, 燕子双飞去. 明月不谙离恨苦, 斜光到晓穿朱户.
date: 2021-04-05
---

## 2022

- Bye Bye!

- [workerd](https://github.com/cloudflare/workerd)
  - Cloudflare's JavaScript/Wasm Runtime
  - 哈哈哈, 又一个

- [bun](https://github.com/oven-sh/bun)
  - All in one fast & easy-to-use tool.
  - Instead of 1,000 node_modules for development,
    you only need bun.
  - 能不能冲击 Node.js? 难!
  - 但是反而会冲击 Deno!

- [Announcing the Web-interoperable Runtimes Community Group](https://deno.com/blog/announcing-wintercg)
  - https://wintercg.org
  - https://github.com/wintercg/proposal-common-minimum-api
  - 目测, 不会有太大的机会

- [Component Model design and specification](https://github.com/WebAssembly/component-model)
  - 期待

- [Node.js 18 is now available!](https://nodejs.org/en/blog/announcements/v18-release-announce/)
  - 2022-04-19
  - New globally available browser-compatible APIs
    - __fetch__ (experimental)
    - __Web Streams API__ (experimental)
  - **Test runner module** (experimental)

```js
import test from 'node:test'
import strictEqual from 'node:assert'

test('top level test', async (t) => {
  await t.test('sub test 1', () => {
    strictEqual(1, 1)
  })
})
```

- [WebAssembly v2](https://github.com/WebAssembly/spec/pull/1443)
  - 真正意义上的 `v1`

* [Headless UI](https://github.com/tailwindlabs/headlessui)
  - https://headlessui.dev
  - A set of completely unstyled,
    fully accessible UI components,
    designed to integrate beautifully with Tailwind CSS.
  - 哈哈哈, 我喜欢!
  - 目前仅支持: `React`, `Vue`, 看来 `Angular`, `Svelte` 几乎很难主流了.
  - 那我选择 `Vue@3`

* [Node.js Trademarks Transferred to OpenJS Foundation](https://openjsf.org/blog/2022/02/14/node-js-trademarks-transferred-to-openjs-foundation/)
  - [JSON Schema Joins OpenJS Foundation](https://openjsf.org/blog/2022/01/31/json-schema-joins-openjs-foundation/)

* [Deno: Improve Node Compat Mode](https://github.com/denoland/deno/issues/12577)
  - 不管 `Deno` 能否替代 `Node.js`,
    对于 `Server Side JavaScript` 都是一种打击
  - 本来就质量不高的社区, 近一步割裂
  - 或许 `WASI` 是一个可能性, 但那和 `JavaScript` 并无深层联系
  - 最终, `Server Side JavaScript` 就是梦幻泡影
  - 当然, **静态网站**应该是个例外

* [WebTransport](https://w3c.github.io/webtransport/)
  - [GitHub](https://github.com/w3c/webtransport)

* 春节前夕, 作为一个局外人, 选择一个 Topic,
  作为 2022 的关注点, 那就是:
  - [Svelte](https://github.com/sveltejs/svelte)

------------------

## 2021

```
什么是 Web? Web 开发的边界是什么?
算了, 不考究这些 :)

个人已经从 2019 年逐渐淡出 前端的开发了,
虽然 2020 也有 前端 (React), 微信小程序的开发,
但支持他人为主, 且个人兴趣已然不再.

2021年以来, 索性完全脱离了前端开发,
所以, 反而又希望继续了解这一块的进展.

故:
以一名 前 Web 前端码农的身份,
继续观望着...

说不定, 未来的 dApp 时代,
再次投身 新一代的 Web 开发.
```

* [Deno joins TC39](https://deno.com/blog/deno-joins-tc39)
  - We will be pushing for features and improvements to
    the language that benefit everyone, but especially
    users of **server-side JavaScript**.
  - Some of the features that we are looking
    to work on soon:
  - Better support for *non-JS assets* in
    the ES module graph
  - Better support for explicit resource management
  - More extensive standard library functions
    for *(async) iteration*
  - `2022` 年, 基本就能确定 `Deno` `可活否`

* [Web Components](https://github.com/WICG/webcomponents)
  - 很高兴 `Web Components` 还在继续发展

* [Apollo Router](https://github.com/apollographql/router)
  - The **Apollo Router** is a configurable,
    high-performance graph router for a federated graph.
  - `Apollo` 目前算作 `Node.js` 生态, 倒不能算作 `Web` 生态
  - 当年 `Golang` 刚刚火热的时候, 也有一些 `Node.js`
    的作品被用 `Golang` 重新造轮子, 但并未持续太久, 不成气候.
  - 现在轮到了 `Rust` 风生水起
  - `Rust` 目前几乎是 `WebAssembly` 第一语言, 至于对 `Node.js`
    生态的侵占, 个人其实比较*看好*, 且*期待*! 就如同 Rust 对 C++
    版图的*缓慢占领*.
  - 至于 `Deno.js`, 基本*不看好*.

* [swc](https://github.com/swc-project/swc)
  - swc is a super-fast `typescript/javascript`
    compiler written in rust.

* [Next.js 12](https://nextjs.org/blog/next-12)
  - **Rust Compiler**: `~3x` faster *Fast Refresh* and
    `~5x` faster builds
  - **AVIF** Support: Opt-in for `20%` smaller images
  - Our Rust compiler is built on **SWC**.

* [VitePress](https://github.com/vuejs/vitepress)
  - **VitePress** is `VuePress'` spiritual successor,
    built on top of **vite**.
  - 不错, 期待 `1.0`

* **Embedded scripting**
  - [**WebAssembly**](https://webassembly.org)
  - *会取代*
  - [**Lua**](https://www.lua.org)
  - 从 `Istio/Envoy` 开始

* [WebContainer](https://github.com/stackblitz/webcontainer-core)
  - *有点意思*

* 留个纪念 (2021-08)
  - **React.js**
  - **Vue.js**
> - Angular (Kubernetes, Kubeflow)
> - Svelte

* 2021-08
  - *Vue.js* has been selected as Wikimedia Foundation's
    future JavaScript framework

* [tc39/proposal-module-fragments](https://github.com/tc39/proposal-module-fragments)
  - JavaScript Module Fragments

* 期待 [ECMAScript spec proposal for Realms API](https://github.com/tc39/proposal-realms)

* [SvelteKit](https://github.com/sveltejs/kit)
  - [Using Vite](https://github.com/vitejs/vite)

* What is *SvelteKit*?

```
SvelteKit is a framework for building
extremely high-performance web apps.
You're looking at one right now!
There are two basic concepts:

1. Each page of your app is a Svelte component

2. You create pages by adding files to the
src/routes directory of your project.
These will be server-rendered so that
a user's first visit to your app is as fast as possible,
then a client-side app takes over

Building an app with all the modern best practices
- code-splitting, offline support, server-rendered views
with client-side hydration
- is fiendishly complicated.
SvelteKit does all the boring stuff for you
so that you can get on with the creative part.
```

* [Google Docs will now use canvas based rendering](https://workspaceupdates.googleblog.com/2021/05/Google-Docs-Canvas-Based-Rendering-Update.html)

```
DOM 的历史包袱

谁还记得 Google 提出的 Web components, 哈哈哈
```

* [AssemblyScript](https://github.com/AssemblyScript/assemblyscript)
  - 为啥不直接用 **Rust**?

* Second State
  - [Website](https://www.secondstate.io)
  - [Github](https://github.com/second-state)
  - [WasmEdge (formerly SSVM)](https://github.com/WasmEdge/WasmEdge)
  - 过了 2021 年, 类似的解决方案也该决出佼佼者了

* Vue v3
  - [Vite v2 - Next generation frontend tooling](https://github.com/vitejs/vite)
  - [Gridsome: The Jamstack framework for Vue.js](https://github.com/gridsome/gridsome)

```
上一次用 Vue 是什么时候?
2018年之前 :)
```

* [Tailwind CSS](https://github.com/tailwindlabs/tailwindcss)
  - https://tailwindcss.com
  - A utility-first CSS framework for rapidly building custom user interfaces

```
这么多年了, 一直没有真正的 CSS Framework

Tailwind CSS 是正确的思路

Houdini

要么 胎死腹中
要么 Game changer
```

* [Announcing the Deno Company](https://deno.com/blog/the-deno-company)
  - 定位蛮清晰的 :)

```
A Globally Distributed JavaScript VM

Deno Deploy is a distributed system that runs JavaScript, TypeScript, and WebAssembly
at the edge, worldwide. The service deeply integrates the V8 JavaScript runtime
with a high performance asynchronous web server to provide
optimal performance without unnecessary intermediate abstractions.
```

```
Deno is our attempt to breathe new life into this ecosystem.
To provide a modern, productive programming system that
adheres to browser APIs.
Deno is not a monolithic system,
but rather a set of technologies that we believe can be
repurposed to a variety of needs.
Not every use-case of server-side JavaScript needs to
access the file system;
our infrastructure makes it possible to compile out unnecessary bindings.
This allows us to create custom runtimes for different applications:
Electron-style GUIs,
Cloudflare Worker-style Serverless Functions,
embedded scripting for databases, etc.
```

> embedded scripting for databases, etc.

- 说到这个, Redis 选择 Lua 真是让人痛苦

* [Node v16.0.0 2021-04-20](https://nodejs.org/en/blog/release/v16.0.0/)
  - **Goodbye**, Node.js

------------------

## 2020

* **React** v17.0
  - October 20, 2020
  - Today, we are releasing React 17!
  - No New Features
  - This release is primarily focused on making it easier to upgrade React itself.
