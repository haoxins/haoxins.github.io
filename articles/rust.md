---
title: Rust
description: 惟江上之清风, 与山间之明月, 耳得之而为声, 目遇之而成色, 取之无禁, 用之不竭.
date: 2021-04-10
---

### 美妙之处

* **反复强调** 从 Docs, eBook, 编译器, 工具链 全方位的强调设计理念
* **暴露细节** 指引大家去了解, 而非屏蔽细节
* **提供便利** 友好详尽的 Warning Error 信息
* **兼容并蓄** 纯粹的 FP 难以流行, OO 的糟粕不宜提倡
  - 单纯把所谓的 Modern language 的语法整合在一起并不难
  - 取舍 融合 融洽 不突兀 是高手
* **社区氛围** 这一点后期很难改变
  - 所幸 Rust 诞生之初, 社区并未蓬勃, 得以聚集优良的信念
  - 后来也会有噪音, 但好在优良的基因已经种下
  - 较之 Node.js (npm) 社区, 一开始便太多噪音

```
In Rust, the compiler plays a gatekeeper role by
refusing to compile code with these elusive bugs,
including concurrency bugs.
```

### 理念细节 (By code)

```rust
// Immutable first
let x = 666;
let mut y = 996;
```

* 减少内存分配和拷贝
  - zero-copy [rkyv](https://github.com/djkoloski/rkyv)

------------------

# Timeline

------------------

## 2021

* [Crust of Rust: Atomics and Memory Ordering](https://www.youtube.com/watch?v=rMGWeSjctlY)

* [Mozilla Welcomes the Rust Foundation](https://blog.mozilla.org/blog/2021/02/08/mozilla-welcomes-the-rust-foundation/)
  - [Hello World!](https://foundation.rust-lang.org/posts/2021-02-08-hello-world/)
