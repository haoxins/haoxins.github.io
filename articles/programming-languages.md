---
title: 编程语言
description: todo
date: 2019-04-27
---

|            | Rust | Go | JavaScript | TypeScript |
|:----------:|:----:|:--:|:----------:|:----------:|
|  elegant   |   Y  |  N |     Y      |      N     |
|            |      |    |            |            |

## Rust

### Ownership

* stack vs heap
  - `stack`: last in, first out
  - `stack`: all data stored on the stack must have a known, fixed size
* each value in Rust has a variable that’s called its owner
* there can only be one owner at a time
* when the owner goes out of scope, the value will be dropped
