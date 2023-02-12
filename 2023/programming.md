---
title: 码农碎碎念~
description: 分行接绮树, 倒影入清漪. 不学御沟上, 春风伤别离.
date: 2023-01-08
---

- Rust 实用的小型库
  - [Anyhow](https://github.com/dtolnay/anyhow)
  - [derive(Error)](https://github.com/dtolnay/thiserror)
- Rust math
  - [argmin](https://www.argmin-rs.org)

---

- [Generic associated types to be stable in Rust 1.65](https://blog.rust-lang.org/2022/10/28/gats-stabilization.html)

```
```

---

- [Enso](https://github.com/enso-org/enso)
  - An award-winning interactive programming language
    with dual visual and textual representations.
  - 年底再看看~

- ChatGPT 最近是热点话题, 与其无聊的讨论什么职位会被替代,
  我更期待何时 AI 能帮助完成那些必定无法仅靠人力解决的事情.
  - 比如: 编纂`数学史`;
  - 再比如: 评审`数学证明`;
  - 再比如: 全人类知识图谱.

- [RustPython](https://github.com/RustPython/RustPython)
  - A Python-3 (CPython >= `3.10`) Interpreter written in Rust.
  - 有点意思, 哈哈哈~

- Go `1.20` is released!
  - `1 Feb 2023`

```go
package errors

// Join returns an error that wraps the given errors.
// Any nil error values are discarded.
// Join returns nil if errs contains no non-nil values.
// The error formats as the concatenation of the strings obtained
// by calling the Error method of each element of errs, with a newline
// between each string.
func Join(errs ...error) error {
  // ...
}
```

- The `math/rand` package now automatically seeds
  the global random number generator
  (used by top-level functions like `Float64` and `Int`)
  with a random value, and the top-level
  `Seed` function has been __deprecated__.

- The top-level `Read` function has been __deprecated__.
  - In almost all cases, `crypto/rand.Read` is more appropriate.

> 前进一小步, 真的是一小步, 无聊~

---

- `2023-01`, 列几个值得关注的`早期项目`
  - [Polars](https://github.com/pola-rs/polars)
  - Blazingly fast DataFrames in Rust, Python
  - [DataFusion](https://github.com/apache/arrow-datafusion)
  - DataFusion is an extensible query planning, optimization,
    and execution framework, written in Rust, that uses
    Apache Arrow as its in-memory format.
  - [BlindAI](https://github.com/mithril-security/blindai)
  - BlindAI is a confidential AI inference server.
  - 关注原因: 早期探索者
  - [BastionLab](https://github.com/mithril-security/bastionlab)
  - BastionLab is a simple privacy framework for
    data science collaboration,
    covering data exploration and AI traning.
  - 关注原因: 早期探索者
  - [Engula](https://github.com/engula/engula)
  - A highly scalable, low latency key-value store
  - 关注原因: Redis 有点贵

---

- [sqld](https://github.com/libsql/sqld)
  - 蛮适合用在测试环境的
