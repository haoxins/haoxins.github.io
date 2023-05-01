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

## Asynchronous Programming

## Strings and Text

## Input and Output

## Iterators

## Collections

------------------

- [Modern Polars](https://github.com/kevinheavey/modern-polars)
