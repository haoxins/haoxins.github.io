---
title: 码农碎碎念~
description: 分行接绮树, 倒影入清漪. 不学御沟上, 春风伤别离.
date: 2023-01-08
---

- Rust 实用的小型库
  - [anyhow](https://github.com/dtolnay/anyhow)
  - [thiserror](https://github.com/dtolnay/thiserror)
- Rust math
  - [argmin](https://github.com/argmin-rs/argmin)

---

- [Generic associated types to be stable in Rust 1.65](https://blog.rust-lang.org/2022/10/28/gats-stabilization.html)

```
```

- https://github.com/apache/incubator-opendal
  - From [Databend](https://github.com/datafuselabs)
  - 赞!

- https://zed.dev
  - 就用它来写 Rust
  - 初体验, 还很简陋

- https://blyss.dev
  - Access data privately using homomorphic encryption.
  - Privately scan for breached credentials,
    block malicious URLs, access blockchain data, and more.
  - 先看看能活多久~

---

- [Introducing Rust-Based Ztunnel for Istio Ambient Service Mesh](https://istio.io/latest/blog/2023/rust-based-ztunnel/)
  - https://github.com/istio/ztunnel

```
This purpose-built ztunnel involved two key areas:

1. The configuration protocol between ztunnel and its Istiod
2. The runtime implementation of ztunnel

We chose to build on top of the Tokio and Hyper libraries,
two of the de-facto standards in the ecosystem that
are extensively battle-tested and easy to write
highly performant asynchronous code with.
```

> 所以, [Linkerd 2](https://github.com/linkerd/linkerd2)
  和 [Linkerd 2 Proxy](https://github.com/linkerd/linkerd2-proxy)
  彻底没戏了.
> 当然, [Istio](https://github.com/istio/istio)
  和 [Envoy](https://github.com/envoyproxy/envoy)
  也逐渐分道扬镳了~

---

- [DataFusion: Streaming execution support roadmap](https://github.com/apache/arrow-datafusion/issues/4285)
  - 暂时 (2023) 不抱太大期望~
- [Databend](https://github.com/datafuselabs/databend)
- [RisingWave](https://github.com/risingwavelabs/risingwave)
- [Materialize](https://github.com/MaterializeInc/materialize)

---

- [Service Weaver](https://serviceweaver.dev)
  - Service Weaver is a programming framework for
    writing and deploying cloud applications.
  - https://github.com/ServiceWeaver/weaver
  - 感觉现在才出, 有点晚了~
  - 看看会不会有一个活跃的社区

- ChatGPT 最近是热点话题, 与其无聊的讨论什么职位会被替代,
  我更期待何时 AI 能帮助完成那些必定无法仅靠人力解决的事情.
  - 比如: 编纂`数学史`;
  - 再比如: 评审`数学证明`;
  - 再比如: 全人类知识图谱.

- [Lance](https://github.com/eto-ai/lance)
  - Alternative to Parquet

- [Oxen](https://github.com/Oxen-AI/Oxen)
  - Library, tools, and server to manage local
    and remote Oxen repositories.
  - Includes:
  - `oxen` (command line interface)
  - `oxen-server` (remote server to sync data to)
  - `liboxen` (shared lib between cli and server)

---

- [Eclipse Zenoh](https://github.com/eclipse-zenoh/zenoh)

```
Zenoh (pronounce /zeno/) unifies data in motion,
data at rest and computations. It carefully blends
traditional pub/sub with geo-distributed storages,
queries and computations, while retaining a level of
time and space efficiency that is well beyond
any of the mainstream stacks.
```

---

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
