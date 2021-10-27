---
title: Programming Rust - 2nd Edition (下)
description: Fast, Safe Systems Development (Covers Rust 1.50)
date: 2021-09-08
---

* [Programming Rust, 2nd Edition](https://book.douban.com/subject/34973905/)
  - **Fast, Safe Systems Development**
  - [Code Examples for Programming Rust](https://github.com/ProgrammingRust/examples)

## Closures

* The only thing we've changed is to add the
  `move` keyword before each of the two closures.
  The `move` keyword tells Rust that a closure
  doesn't *borrow* the variables it uses:
  - it *steals* them.
* Rust thus offers two ways for closures to get
  data from enclosing scopes:
  - **moves** and **borrowing**.
* Really there is nothing more to say than that;
  closures follow the same rules about
  moves and borrowing that we already covered.
  A few cases in point:
  - Just as everywhere else in the language, if
    a closure would `move` a value of a
    *copyable* type, like `i32`, it copies the
    value instead.
  - Values of *noncopyable* types, like `Vec<City>`,
    really are *moved*. Rust would not let us access
    `cities` by name after creating the closure.

* Well, a closure is callable, but its not a `fn`.
  The closure `|city| city.monster_attack_risk > limit`
  has its own type that's not a `fn` type,
* In fact, every closure you write has its own type,
  because a closure may contain data: values either
  `borrowed` or `stolen` from enclosing scopes.
* This could be any number of variables, in any
  combination of types. So every closure has an
  `ad hoc` type created by the compiler, large
  enough to hold that data. *No two closures* have
  exactly *the same type*. But every closure implements
  an `Fn` *trait*; the closure in our example implements
  `Fn(&City) -> i64`.
* Since every closure has its own type, code that
  works with closures usually needs to be generic,
  like `count_selected_cities`. Its a little clunky
  to spell out the generic types each time, but to
  see the advantages of this design, just read on.

## Iterators

## Collections

## Strings and Text

## Concurrency

## Asynchronous Programming

## Macros

## Unsafe Code
