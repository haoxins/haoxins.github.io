---
title: (2021) Programming Rust - 2nd Edition
description: Fast, Safe Systems Development (Covers Rust 1.50)
date: 2021-07-12
---

* [Programming Rust, 2nd Edition](https://book.douban.com/subject/34973905/)
  - **Fast, Safe Systems Development**
  - [Code Examples for Programming Rust](https://github.com/ProgrammingRust/examples)

> 看看比官方文档多了啥~

* **Rust 1.50**
  - I'm using `1.54`

> The Rust language makes you a simple **promise**:
> *if your program passes the compiler's checks,*
> *it is free of undefined behavior.*

```
Assuming that you can avoid undefined behavior in C and C++
is like assuming you can win a game of chess
simply because you know the rules.

The Rust language makes you a simple promise:
if your program passes the compiler's checks,
it is free of undefined behavior.

Further, Rust aims to be both safe and pleasant to use.
In order to make stronger guarantees about your program's behavior,
Rust imposes more restrictions on your code than C and C++ do,
and these restrictions take practice and experience to get used to.
```

## Tour

* **`assert!`**
  - Rust always checks assertions

* use **`return`** statements only for explicit early returns from the mids of a function

* **`#[test]`**
  - attribute: open-ended

* A `trait` must be in scope in order to use its methods

* Rust does not have exceptions:
  - all errors are handled using either `Result` or `panic`

* **All** Rust functions are **thread-safe**
  - Really?

* Rust lets you simply write `Complex { re, im }`.
  - This is modeled on similar notations in JavaScript.

* This kind of match statement is such a common pattern in Rust
  that the language provides the **`?`** operator
  as shorthand for the whole thing.

* [Crossbeam](https://github.com/crossbeam-rs/crossbeam)
* [Rayon](https://github.com/rayon-rs/rayon)
* [Smol](https://github.com/smol-rs/smol)

## Concepts

## Basics

## Traits & Generics

## Closures & Iterators

## Others
