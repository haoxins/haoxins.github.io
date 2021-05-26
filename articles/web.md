---
title: (2022) Web
description: 闲云潭影日悠悠, 物换星移几度秋.
date: 2021-04-05
---

------------------

# Timeline

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

* 争论 Svelte, Vue, React 的时代过去了
  - 争论 **SvelteKit vs Next.js** 的时代来了

* [SvelteKit](https://github.com/sveltejs/kit)
  - [Using Vite](https://github.com/vitejs/vite)

* What is SvelteKit?

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

```
为啥不直接用 Rust ?
```

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

* [Tailwind CSS: A utility-first CSS framework for rapidly building custom user interfaces](https://github.com/tailwindlabs/tailwindcss)

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
