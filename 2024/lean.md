---
title: 关于 Lean 4
description: 而今识得愁滋味, 欲说还休, 欲说还休, 却道天凉好个秋.
date: 2024-10-13
---

官网的各种文档很丰富!

首先是安装
[elan: Lean version manager](https://github.com/leanprover/elan),
熟悉 Rust 的自然了然于胸, 类似于 rustup.
elan 是 Rust 编写的 (嗯, 会不会未来 Lean 的 C++ 也会切换到 Rust? 哈哈)

```sh
# source $HOME/.elan/env
elan self update
elan default leanprover/lean4:stable
```

然后, lake 类比于 Cargo

```sh
lake new lean-snippet
cd lean-snippet
lake build
./.lake/build/bin/lean-snippet
```

> 顺便提一下本人的第一个 Lean4 PR
  [5789](https://github.com/leanprover/lean4/pull/5789),
  哈哈~


### Functional Programming in Lean

- [Functional Programming in Lean](https://lean-lang.org/functional_programming_in_lean/)

### Theorem Proving in Lean 4

- [Theorem Proving in Lean 4](https://lean-lang.org/theorem_proving_in_lean4/)
