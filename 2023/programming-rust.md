---
title: Programming Rust
description: 松风吹解带, 山月照弹琴. 君问穷通理, 渔歌入浦深.
date: 2022-12-29
---

- Rust 实用的库
  - [itertools](https://github.com/rust-itertools/itertools)
  - [snafu](https://github.com/shepmaster/snafu)
  - [anyhow](https://github.com/dtolnay/anyhow)
  - [thiserror](https://github.com/dtolnay/thiserror)
- Rust math
  - [nalgebra](https://github.com/dimforge/nalgebra)
  - nalgebra is a linear algebra library
    written for Rust targeting:
  - General-purpose linear algebra.
  - Real-time computer graphics.
  - Real-time computer physics.
  - [faer](https://github.com/sarah-ek/faer-rs)
  - faer is a collection of crates that implement
    low level linear algebra routines in pure Rust.
- Graph
  - [petgraph](https://github.com/petgraph/petgraph)
  - Graph data structure library.
  - [Arroy](https://github.com/meilisearch/arroy)
  - `Arroy` (Approximate Rearest Reighbors) is a
    Rust library with the interface of the
    [Annoy](https://github.com/spotify/annoy)
    Python library to search for vectors in
    space that are close to a given query vector.
  - It is based on `LMDB`, a memory-mapped key-value store,
    so many processes may share the same data and
    atomically modify the vectors.

---

- [All Rust string types explained](https://www.youtube.com/watch?v=CpvzeyzgQdw)

```
String -> Vec<u8>
  create/modify strings

&str -> & str -> &[u8]
  read/analyze strings
  Box<str>
  Rc<str>
  Arc<str>

&'static str

OsString & OsStr
  no need utf-8

Path & PathBuf
```

---

- [Candle](https://github.com/huggingface/candle)
  - Candle is a minimalist ML framework for Rust
    with a focus on easiness of use and on
    performance (including GPU support).
  - Hugging Face 出品!

- [Polars 开公司啦](https://www.pola.rs/posts/company-announcement/)
  - We are excited to announce the start of company
    that will build around Polars, enabling
    data processing at any scale.
  - 有意思, 期待!

```
Polars is entirely based on Arrow data types and
backed by Arrow memory arrays.
This makes data processing cache-efficient and
well-supported for Inter Process Communication.
```

- 2023-07-27, PyPI Programming Language
  - Rust: 964
  - C++: 1620
  - C: 1590
  - Cython: 1101

---

- Arrow, DataFusion 生态
  - `cargo tree --depth 1`

```
arroyo-sql v0.2
├── arrow v37
├── datafusion v23

lance v0.4
├── arrow v37
├── datafusion v23

Polars
  https://github.com/pola-rs/polars/issues/6197
```

---

> For example, in floating point numbers `NaN != NaN`,
  so floating point types implement `PartialEq`
  but not `Eq`.

- If a type `T` implements `Default`, then the
  standard library implements `Default` automatically
  for `Rc<T>`, `Arc<T>`, `Box<T>`, `Cell<T>`,
  `RefCell<T>`, `Cow<T>`, `Mutex<T>`, and `RwLock<T>`.

---

- [Decrusting the axum crate](https://www.youtube.com/watch?v=Wnb_n5YktO8)
  - [axum::extract::State](https://docs.rs/axum/latest/axum/extract/struct.State.html)

- [Crust of Rust: std::collections](https://www.youtube.com/watch?v=EF3Z4jdD1EQ)
  - https://doc.rust-lang.org/std/collections/index.html
  - 太长了, 看不完~

---

```toml
lance = { git = "https://github.com/lancedb/lance", rev = "6af670a" }
```

```
error: all dependencies must have a version specified when publishing.
Note: The published dependency will use the version from crates.io,
the `git` specification will be removed from the dependency declaration.
```

> Why not?

---

- [Stabilizing async fn in traits in 2023](https://blog.rust-lang.org/inside-rust/2023/05/03/stabilizing-async-fn-in-trait.html)
  - 期待

```
Our goal is to stabilize the MVP for Rust 1.74,
which will be released on 2023-11-16.

So, once this MVP is done, what next?
Our next immediate goals are to ship
dynamic dispatch and async closures
support in 2024.
```

- 2023-04-27, 为了 `#![feature(async_fn_in_trait)]`
  - `rustup install nightly`
  - `rustup default nightly`

- [Generic associated types to be stable in Rust 1.65](https://blog.rust-lang.org/2022/10/28/gats-stabilization.html)

```
At its core, generic associated types allow you
to have generics (type, lifetime, or const)
on associated types.
```

```rust
trait LendingIterator {
  type Item<'a> where Self: 'a;

  fn next<'a>(&'a mut self) -> Self::Item<'a>;
}
```

- Traits with GATs are not object safe
