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

## Iterators

## Collections

## Strings and Text

## Concurrency

## Asynchronous Programming

## Macros

## Unsafe Code
