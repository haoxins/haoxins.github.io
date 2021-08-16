---
title: (2021) Programming Rust - 2nd Edition
description: Fast, Safe Systems Development (Covers Rust 1.50)
date: 2021-07-12
---

* [Programming Rust, 2nd Edition](https://book.douban.com/subject/34973905/)
  - **Fast, Safe Systems Development**
  - [Code Examples for Programming Rust](https://github.com/ProgrammingRust/examples)

> 此书不断号召 *C++* 玩家转投 *Rust* 平台, 哈哈哈!

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

* References: non-owning
  - must never outlive their referents

* A *shared reference* lets you read but not modify its referent
  - *Shared references* are *Copy*
* If you have a *mutable reference* to a value,
  you may both read and modify the value
  - *Mutable references* are not *Copy*
* A *multiple readers and single writer* rule

* The **.** operator implicitly dereferences its left operand if needed.
* The **.** operator can also implicitly borrow a reference
  to its left operand if needed for a method call.

* The **.** operator follows as many references
  as it takes to find its target.

```rust
struct Point {
    x: i32,
    y: i32,
}
let p = Point { x: 1, y: 2 };
let r: &Point = &p;
let rr: &&Point = &r;
let rrr: &&&Point = &rr;
assert_eq!(rrr.x, 1);
assert_eq!(rrr.y, 2);
```

* Like the **.** operator, Rust's comparison operators
  "see-through" any number of references.

```rust
let x = 1;
let y = 1;
let rx = &x;
let ry = &y;
let rrx = &rx;
let rry = &ry;
assert!(rrx <= rry);
assert!(rrx == rry);
assert!(rrx >= rry);
```

* In Rust, a function's signature always exposes the body's behavior.

* Whenever a reference type appears inside another
  type's definition, you must write out its lifetime.

* If your function is a method on some type and
  takes its **self** parameter by reference,
  then that breaks the tie: Rust assumes that
  *self*'s lifetime is the one to give
  everything in your return value.

* Rust assumes that whatever you're borrowing,
  you're borrowing from *self*.

* Note that in both cases, the path of ownership
  leading to the referent cannot be changed for
  the reference's lifetime.
  For a shared borrow, the path is *read-only*;
  for a mutable borrow, it's completely in accessible.
  So there's no way for the program to do anything
  that will invalidate the reference.

* Most of the *control flow* tools in C are statements.
  In Rust, they are ***all expressions***.

* It's never strictly necessary to use `if let`,
  because `match` can do everything `if let` can do.
  An `if let` express on is shorthand for
  a `match` with just one pattern.

* The `..=` operator produces end-inclusive (or closed) ranges,
  which do include the end value.
  For example, the range `..= 3`
  includes the numbers `0, 1, 2,` and `3`.

* As in *C*, `a % b` computes the signed remainder,
  or modulus, of division rounding toward zero.
  The result has the same sign as the lefthand operand.
  Note that `%` can be used on
  floating-point numbers as well as integers:

```rust
let x = 1234.567 % 10.0; // approximately 4.567
```

* However, what we did earlier is generally considered
  the best style import `types`, `traits`, and `modules`
  (like `std::mem`)
  and then use relative paths to access the
  `functions`, `constants`, and other `members` within.

* Modules do not automatically inherit
  names from their parent modules.

## Traits & Generics

## Closures & Iterators

## Others
