---
title: Programming Rust
description: 松风吹解带, 山月照弹琴. 君问穷通理, 渔歌入浦深.
date: 2022-12-29
---

```toml
lance = { git = "https://github.com/eto-ai/lance.git", rev = "bdbd5ba" }
```

------------------

- [Programming Rust, 2nd Edition](https://book.douban.com/subject/34973905/)
  - 部分 2022 没有看完的章节

## Concurrency

- `Sender<T>` implements the Clone trait.
  To get a channel with multiple senders,
  simply create a regular channel and clone
  the sender as many times as you like.
  - You can move each Sender value
    to a different thread.
- A `Receiver<T>` can't be cloned, so if you
  need to have multiple threads receiving values
  from the same channel, you need a Mutex.

- A synchronous channel is exactly like a
  regular channel except that when you create it,
  you specify how many values it can hold.
  - For a synchronous channel, `sender.send(value)`
    is potentially a blocking operation.
  - After all, the idea is that
    blocking is not always bad.

### Thread Safety: Send and Sync

## Asynchronous Programming

## Strings and Text

## Input and Output

## Iterators

## Collections

------------------

- [Asynchronous Programming in Rust](https://rust-lang.github.io/async-book/)

------------------

- [Modern Polars](https://github.com/kevinheavey/modern-polars)
