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

* Rust uses the `u8` type for byte values

* Rust's `character` type `char` represents
  a single `Unicode` character, as a `32-bit` value.

* Rust uses the `char` type for single characters in isolation,
  but uses the `UTF-8` encoding for `strings` and `streams` of text.
  So, a String represents its text as a sequence of `UTF-8` bytes,
  not as an array of characters.

* To a certain extent, tuples resemble arrays:
  - both types represent an ordered sequence of values.
  - each element of a tuple can have a different type,
    whereas an array's elements must be all the same type.
  - tuples allow only constants as indices,
    like `t.4`. You can't write `t.i` or `t[i]`.

* Pointer types
  - References
  - Boxes (heap)
  - Unsafe pointers/Raw pointers

* Rust references are never null
  - `&T`
  - `&mut T`

* Array: `[T; N]`
* Vector: `Vec<T>`
  - `vec![1, 2, 3]`
* Shared slice: `&[T]`
* Mutable slice: `&mut [T]`

> Share or Modify

* Strings (**`str`**)
  - String literals
  - Raw strings
  - Byte stings

## Basics

* Ownership tree
  - **Copy types**: excused from the ownership rules
  - You can move values from one owner to another
  - **Rc, Arc** reference-counted pointer types
  - Borrow a reference, references are non-owning pointers

> In Rust, for most types, Rust doesn't copy the value but moves it.

* The standard Copy types include all the machine integer
  and floating-point numeric types, the char and bool types,
  and a few others. A tuple or fixed-size array of
  Copy types is itself a Copy type.

* A value owned by an `Rc` pointer is immutable.

## Traits & Generics

## Closures & Iterators

## Others
