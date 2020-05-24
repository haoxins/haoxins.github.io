---
title: Rust & C++
description: The only language ~
date: 2020-02-24
---

## 概述

* Rust 蚕食 C/C++

## ...

* Pattern first, `=>`, `match`
  - `ref`, `@`
* `fn`, `->`
* Immutable default, `Shadowing`
* `Char`, `''`, single quotes
* `Tuple`, `()`, indexing `.`
* `Result`, `Ok`, `Err`
* `macros!`
* `traits`
* `loop`, `while`, `for`
* `Expression`, `(with ;)`, return value `(...)`
* `Expressions`: `if`
* `Statement`, `(no ;)`
* `Ownership`, `References`, `Borrowing`, `Lifetime`
  - `Copy` trait
  - `'a`, `'static`

```rust
// pattern
let a = 1; // immutable
let a: u32 = 2; // Shadowing
let mut b = 1;

let mut s = String::new();

xxx(& s);
xxx(&mut s);
```
