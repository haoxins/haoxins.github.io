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

* **Pseudocode** for `Fn`, `FnMut`,
  and `FnOnce` traits.

```rust
trait Fn() -> R {
  fn call(&self) -> R;
}

trait FnMut() -> R {
  fn call_mut(&mut self) -> R;
}

trait FnOnce() -> R {
  fn call_once(self) -> R;
}
```

* Any closure that requires `mut` access to
  a value, but doesn't `drop` any values,
  is an `FnMut` closure.
* The three categories of Rust closures.
  - `Fn` is the family of closures and functions
    that you can call multiple times without
    restriction. This **highest** category also
    includes all `fn` functions.
  - `FnMut` is the family of closures that can be
    called multiple times if the
    closure itself is declared `mut`.
  - `FnOnce` is the family of closures that can
    be called **once**, if the caller
    owns the closure.
* Every `Fn` meets the requirements for `FnMut`, and
  every `FnMut` meets the requirements for `FnOnce`.
* Instead, `Fn()` is a *subtrait* of `FnMut()`,
  which is a *subtrait* of `FnOnce( )`.
* This makes `Fn` the most exclusive and most powerful
  category. `FnMut` and `FnOnce` are broader
  categories that include closures
  with usage restrictions.

* On the other hand, a `non-move` closure that *does*
  `mutate` values has `mutable` references within
  its internal representation. `Mutable` references
  are neither `Clone` nor `Copy`, so neither is
  a closure that uses them.

* For a `move` closure, the rules are even simpler.
  If everything a `move` closure captures ís `Copy`,
  it's `Copy`. If everything it captures is `Clone`,
  it's `Clone`.

* Closures have unique types because each one
  captures different variables, so among other things,
  they're each a different size.
* If they don't capture anything, though, there's
  nothing to store. By using `fn` pointers in functions
  that take callbacks, you can restrict a caller to
  use only these noncapturing closures, gaining some
  perfomance and flexibility within the code using
  callbacks at the cost of flexibility
  for the users of your APl.

## Iterators

* Here, `filter` returns a new iterator that
  produces only those items from the `map` iterator
  for which the closure returns `true`.
* A chain of iterator adapters is like a pipeline
  in the `Unix` shell: each adapter has a single
  purpose, and it's clear how the sequence is
  being transformed as one reads from left to right.
  These adapters' signatures are as follows:

```rust
fn map<B, F>(self, f: F) -> impl Iterator<Item=B>
  where Self: Sized, F: FnMut(Self::Item) -> B;

fn filter<P>(self, predicate: P) -> impl Iterator<Item=Self::Item>
  where Self: Sized, P: FnMut(&Self::Item) -> bool;
```

* In the standard library, `map` and `filter` actually
  return specific opaque `struct` types named
  `std::iter::Map` and `std::iter::Filter`. However,
  just seeing their names is not very informative,
  so in this book, were just going to write
  `-> impl Iterator<Item=...>` instead, since that
  tells us what we really want to know:
  - the method returns an `Iterator` that produces
    items of the given type.
* Since most adapters take `self` by value, they require
  `Self` to be `Sized` (which all common iterators are).
  - A `map` iterator passes each item to its closure
    by `value` and, in turn, passes along *ownership* of the
    closure's result to it's consumer.
  - A `filter` iterator passes each item to its closure
    by *shared reference*, retaining *ownership* in case
    the item is selected to be passed on to it's consumer.

* There are **two** important points to notice about
  iterator adapters
* **First**, simply calling an adapter on an iterator
  doesn't consume any items; it just returns a
  new iterator, ready to produce its own items by
  drawing from the first iterator as `needed`. In a
  chain of adapters, the only way to make any work
  actually get done is to call `next`
  on the **final** iterator.
  - **No** work takes place until `collect` starts
    calling `next` on the `filter` iterator.
  - This point is especially important if you use
    adapters that have *side effects*. For example,
    this code prints **nothing** at all:

```rust
["earth", "water", "air", "fire"]
  .iter().map(|elt| println!("{}", elt));
```

* The `iter` call returns an iterator over the array's
  elements, and the `map` call returns a second
  iterator that applies the closure to each value the
  first produces. But there is nothing here that ever
  actually demands a value from the whole chain, so no
  `next` method ever runs.
* The term `"lazy"` in the error message is not a
  disparaging term; it's just jargon for any mechanism
  that puts off a computation until its value is needed.
  It is Rust's convention that iterators should do the
  minimum work necessary to satisfy each call to `next`;
  in the example, there are no such calls at all,
  so no work takes place.
* The **second** important point is that iterator
  adapters are a `zero-overhead` abstraction. Since
  `map`, `filter`, and their companions are `generic`,
  applying them to an iterator specializes their code
  for the specific iterator type involved.
* This means that Rust has enough information to inline
  each iterator's next method into its consumer and
  then translate the entire arrangement into
  machine code as a unit، So the `lines/map/filter` chain
  of iterators we showed before is as efficient as the
  code you would probably write by hand.

## Collections

## Strings and Text

## Concurrency

## Asynchronous Programming

## Macros

## Unsafe Code
