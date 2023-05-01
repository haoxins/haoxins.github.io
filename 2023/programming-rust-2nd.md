---
title: Programming Rust
description: 松风吹解带, 山月照弹琴. 君问穷通理, 渔歌入浦深.
date: 2022-12-29
---

- Rust 实用的库
  - [rayon](https://github.com/rayon-rs/rayon)
  - [itertools](https://github.com/rust-itertools/itertools)
  - [thiserror](https://github.com/dtolnay/thiserror)
  - [anyhow](https://github.com/dtolnay/anyhow)
  - [snafu](https://github.com/shepmaster/snafu)
- Rust math
  - [argmin](https://github.com/argmin-rs/argmin)

---

- [Generic associated types to be stable in Rust 1.65](https://blog.rust-lang.org/2022/10/28/gats-stabilization.html)

```rust
```

- 2023-04-27, 为了 `#![feature(async_fn_in_trait)]`,

```zsh
$ rustup install nightly
$ rustup default nightly
```

------------------

- [Asynchronous Programming in Rust](https://rust-lang.github.io/async-book/)

------------------

- [Programming Rust, 2nd Edition](https://book.douban.com/subject/34973905/)
  - 部分 2022 没有看完的章节

## Asynchronous Programming

## Iterators

- An iterator is any value that implements the
  `std::iter::Iterator` trait:

```rust
trait Iterator {
  type Item;

  fn next(&mut self) -> Option<Self::Item>;

  // ...
  // many default methods
}
```

- If there's a natural way to iterate over some type,
  that type can implement `std::iter::IntoIterator`,
  whose `into_iter` method takes a value and
  returns an iterator over it:

```rust
trait IntoIterator where Self::IntoIter: Iterator<Item=Self::Item> {
  type Item;
  type IntoIter: Iterator;
  fn into_iter(self) -> Self::IntoIter;
}
```

- `IntoIter` is the type of the iterator value itself,
  and `Item` is the type of value it produces.

## Concurrency

- `Sender<T>` implements the `Clone` trait.
  To get a channel with multiple senders,
  simply create a regular channel and clone
  the sender as many times as you like.
  - You can move each `Sender` value
    to a different thread.
- A `Receiver<T>` can't be cloned, so if you
  need to have multiple threads receiving values
  from the same channel, you need a `Mutex`.

- A synchronous channel is exactly like a
  regular channel except that when you create it,
  you specify how many values it can hold.
  - For a synchronous channel, `sender.send(value)`
    is potentially a blocking operation.
  - After all, the idea is that
    blocking is not always bad.

### Thread Safety: Send and Sync

- Rust's full thread safety story hinges on
  two built-in traits, `std::marker::Send`
  and `std::marker::Sync`.
  - Types that implement `Send` are safe to pass
    by value to another thread.
  - Types that implement `Sync` are safe to pass
    by non-mut reference to another thread.
- When you spawn a thread, the closure you pass
  __must__ be `Send`, which means all the values
  it contains must be `Send`.
- Similarly, if you want to send values through a
  channel to another thread,
  the values __must__ be `Send`.

---

- Creating a new `Mutex` looks like creating a new
  `Box` or `Arc`, but while `Box` and `Arc` signify
  heap allocation, `Mutex` is solely about locking.
- `Arc` is handy for sharing things across threads,
  and `Mutex` is handy for mutable data
  that's shared across threads.

```
In fact, a mutex is little more than a way to
do exactly this, to provide exclusive (mut) access
to the data inside, even though many threads may
have shared (non-mut) access to the Mutex itself.
```

> Rust's borrow system can't protect you from deadlock.
> It's also possible to get deadlock with channels.

- If a thread panics while holding a `Mutex`,
  Rust marks the `Mutex` as __poisoned__.
  - Any subsequent attempt to lock the poisoned
    `Mutex` will get an error result.

### Condition Variables (Condvar)

- In Rust, the `std::sync::Condvar` type implements
  condition variables.
  - A `Condvar` has methods `.wait()` and `.notify_all()`;
  - `.wait()` blocks until some other
    thread calls `.notify_all()`.

## Input and Output

- Rust's standard library features for input and output
  are organized around three traits,
  `Read`, `BufRead`, and `Write`:
  - Values that implement `Read` have methods for
    byte-oriented input. They're called __readers__.
  - Values that implement `BufRead` are buffered readers.
    They support all the methods of `Read`,
    plus methods for reading lines of text and so forth.
  - Values that implement `Write` support both
    byte-oriented and UTF-8 text output.
    They're called __writers__.

## Strings and Text

- The char type implements `Copy` and `Clone`,
  along with all the usual traits for
  comparison, hashing, and formatting.
  - A string slice can produce an iterator over its
    characters with `slice.chars()`.

### String and str

- Rust places text-handling methods on either `str`
  or `String` depending on whether the method needs
  a resizable buffer or is content just
  to use the text in place.
- Since `String` dereferences to `&str`, every method
  defined on `str` is directly available
  on `String` as well.
  - These methods index text by byte offsets and
    measure its length in bytes,
    rather than characters.
- A `String` is implemented as a wrapper around a
  `Vec<u8>` that ensures the vector's contents are
  always well-formed UTF-8.
  - Rust will never change `String` to use a more
    complicated representation,
  - so you can assume that `String` shares
    `Vec`'s performance characteristics.

------------------

- [Modern Polars](https://github.com/kevinheavey/modern-polars)
