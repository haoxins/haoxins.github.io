---
title: rust.go
description: The only languages ~
date: 2020-02-24
---

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

## Modules

### Go

* [ORM - facebook/ent](https://github.com/facebook/ent)
* [HTTP Client - go-resty/resty](https://github.com/go-resty/resty)

### Rust

* [ORM - diesel-rs/diesel](https://github.com/diesel-rs/diesel)
* [HTTP Client - seanmonstar/reqwest](https://github.com/seanmonstar/reqwest)
