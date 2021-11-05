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

## Strings and Text

* `String` and `str`

* Rust's `string` and `str` types are guaranteed
  to hold only well-formed UTF-8. The library ensures
  this by restricting the ways you can create `String`
  and `str` values and the operations you can perform
  on them, such that the values are well-formed when
  introduced and remain so as you work with them.
* All their methods protect this guarantee: no safe
  operation on them can introduce ill-formed UTF-8.
  This simplifies code that works with the text.

* Rust places text-handling methods on either
  `str` or `String` depending on whether the method
  needs a resizable buffer or is content just to
  use the text in place.
* Since String dereferences to `&str`, every method
  defined on `str` is directly available on `String`
  as well.

* These methods index text by *byte offsets* and
  measure its length in bytes, rather than characters.
* In practice, given the nature of *Unicode*, indexing
  by character is not as useful as it may seem, and
  *byte offsets* are faster and simpler. If you try to
  use a *byte offset* that lands in the midst of some
  character's UTF-8 encoding, the method panics, so
  you can't introduce ill-formed UTF-8 this way.

* A `String` is implemented as a wrapper around a
  `Vec<u8>` that ensures the vector's contents are
  always well-formed UTF-8. Rust will never change
  `String` to use a more complicated representation,
  so you can assume that `String` shares `Vec's`
  performance characteristics.

## Concurrency


## Asynchronous Programming


## Unsafe Code

* An `unsafe` block unlocks five
  additional options for you:
  - You can call `unsafe` functions. Each `unsafe`
    function must specify its own *contract*,
    depending on its purpose.
  - You can dereference raw pointers. Safe code can
    pass raw pointers around, compare them, and
    create them by conversion from references
    (or even from integers), but only `unsafe` code
    can actually use them to access memory.
  - You can access the fields of `unions`, which the
    compiler can't be sure contain valid bit patterns
    for their respective types.
  - You can access *mutable static variables*. Rust
    can't be sure when threads are using
    *mutable static variables*, so their contract
    requires you to ensure all access is
    properly synchronized.
  - You can access functions and variables declared
    through Rust's foreign function interface. These
    are considered `unsafe` even when *immutable*, since
    they are visible to code written in other languages
    that may not respect Rust's safety rules.

* Restricting `unsafe` features to `unsafe` blocks
  doesn't really prevent you from doing whatever you want.
  Its perfectly possible to just stick an `unsafe` block
  into your code and move on. The benefit of the rule
  lies mainly in *drawing human attention* to code whose
  safety Rust can't guarantee:
  - You won't accidentally use `unsafe` features and
    then discover you were responsible for contracts
    you didn't even know existed.
  - An `unsafe` block attracts *more attention* from
    *reviewers*. Some projects even have automation
    to ensure this, flagging code changes that affect
    `unsafe` blocks for special attention.
  - When you're considering writing an `unsafe` block,
    you can take a moment to ask yourself whether your
    task really requires such measures. If it's for
    performance. do you have measurements to show that
    this is actually a bottleneck? Perhaps there is a
    good way to accomplish the same thing in safe Rust.

* Two critical facts about bugs and `unsafe` code:
  - Bugs that occur before the `unsafe` block can
    break contracts. Whether an `unsafe` block causes
    undefined behavior can depend not just on the code
    in the block itself, but also on the code that
    supplies the values it operates on. Everything that
    your `unsafe` code relies on to satisfy contracts
    is safety-critical. The conversion from `Ascii` to
    `String` based on `String::from_utf8_unchecked`
    is well-defined only if the rest of the module
    properly maintains Ascii's invariants.
  - The consequences of breaking a contract may appear
    after you leave the `unsafe` block. The undefined
    behavior courted by failing to comply with an
    `unsafe` feature's contract often does not occur
    within the `unsafe` block itself. Constructing a
    bogus `String` as shown before may not cause
    problems until much later in the
    program's execution.

* Essentially. Rust's *type checker*, *borrow checker*,
  and other *static checks* are inspecting your program
  and trying to construct proof that it cannot exhibit
  undefined behavior.
* When Rust compiles your program successfully, that
  means it succeeded in proving your code sound. An
  `unsafe` block is a gap in this proof:
  - "This code," you are saying to Rust, "is fine, trust me."
* Whether your claim is true could depend on any part
  of the program that influences what happens in the
  `unsafe` block, and the consequences of being wrong
  could appear anywhere influenced by the `unsafe` block.
* Writing the `unsafe` keyword amounts to a reminder
  that you are not getting the full benefit of the
  language's safety checks.

* Given the choice, you should naturally prefer to
  create safe interfaces, without contracts. These are
  much easier to work with, since users can count
  on Rust's safety checks to ensure their code is free
  of undefined behavior. Even if your implementation
  uses `unsafe` features, it's best to use Rust's
  `types`, `lifetimes`, and module system to meet
  their contracts while using only what you can
  guarantee yourself, rather than passing
  responsibilities on to your callers.

* Unfortunately, it's not unusual to come across
  *unsafe functions* in the wild whose documentation
  does not bother to explain their contracts. You
  are expected to infer the rules yourself, based on
  your experience and knowledge of how the code
  behaves. If you've ever uneasily wondered whether
  what you're doing with a `C` or `C++` API is OK,
  then you know what that's like.

* **Unsafe Block** or **Unsafe Function**?

* You may find yourself wondering whether to
  use an `unsafe block` or just mark the whole
  `function unsafe`. The approach we recommend is
  to first make a decision about the function:
  - If it's possible to misuse the function in a
    way that compiles fine but still causes
    undefined behavior, you must mark it as `unsafe`.
    The rules for using the function correctly are
    its contract; the existence of a contract is
    what makes the function `unsafe`.
  - Otherwise, the function is **safe**: no
    well-typed call to it can cause undefined
    behavior. It should not be marked `unsafe`.

* Whether the function uses `unsafe` features in
  its body is irrelevant; what matters is the
  presence of a contract. Before, we showed an
  `unsafe` function that uses no `unsafe` features,
  and a safe function that does use `unsafe` features.
* Don't mark a *safe* function `unsafe` just because
  you use `unsafe` features in its body. This makes
  the function harder to use and confuses readers
  who will (correctly) expect to find a contract
  explained somewhere. Instead, use an `unsafe` block,
  *even if it's the function's entire body*.
