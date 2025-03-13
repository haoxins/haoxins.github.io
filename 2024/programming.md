---
title: 码农碎碎念~
description: 薄雾浓云愁永昼, 瑞脑销金兽. 佳节又重阳, 玉枕纱厨, 半夜凉初透.
date: 2023-07-17
---

- [Faster Go maps with Swiss Tables](https://go.dev/blog/swisstable)

```
In an open-addressed hash table, all items are
stored in a single backing array. We'll call
each location in the array a slot.
The slot to which a key belongs is primarily
determined by the hash function, hash(key).
The hash function maps each key to an integer,
where the same key always maps to the same integer,
and different keys ideally follow a uniform random
distribution of integers.
The defining feature of open-addressed hash tables
is that they resolve collisions by storing the key
elsewhere in the backing array.
So, if the slot is already full (a collision),
then a probe sequence is used to consider other
slots until an empty slot is found.

The proportion of used slots is called the load factor,
and most hash tables define a maximum load factor
(typically 70-90%) at which point they will grow to avoid
the extremely long probe sequences of very full hash tables.
```

```
The Swiss Table design is also a form of open-addressed hash table.
We still have a single backing array for storage,
but we will break the array into logical groups of 8 slots each.
```

```
In addition, each group has a 64-bit control word for metadata.
Each of the 8 bytes in the control word corresponds to one of
the slots in the group.
The value of each byte denotes whether that slot is empty,
deleted, or in use. If it is in use, the byte contains the
lower 7 bits of the hash for that slot's key (called h2).
```

```
Insertion works as follows:

1. Compute hash(key) and break the hash into two parts:
   the upper 57-bits (called h1) and
   the lower 7 bits (called h2).
2. The upper bits (h1) are used to select
   the first group to consider.
3. Within a group, all slots are equally eligible to
   hold the key. We must first determine whether
   any slot already contains this key, in which case
   this is an update rather than a new insertion.
4. If no slot contains the key, then we look for
   an empty slot to place this key.
5. If no slot is empty, then we continue the
   probe sequence by searching the next group.
```

```
Step 3 is where the Swiss Table magic happens.
We need to check whether any slot in a group
contains the desired key. Naively, we could just
do a linear scan and compare all 8 keys.

However, the control word lets us do this more efficiently.
Each byte contains the lower 7 bits of the hash (h2)
for that slot. If we determine which bytes of the
control word contain the h2 we are looking for,
we'll have a set of candidate matches.
```

> __SIMD__

- [Go 1.24 Release Notes](https://go.dev/doc/go1.24)
  - [Swiss Tables](https://abseil.io/about/design/swisstables)
  - When marshaling, a struct field with the new
    `omitzero` option in the struct field tag will
    be omitted if its value is zero. If the field
    type has an `IsZero()` bool method, that will be
    used to determine whether the value is zero.
  - Otherwise, the value is zero if it is the zero
    value for its type. The `omitzero` field tag is
    clearer and less error-prone than `omitempty`
    when the intent is to omit zero values.
  - In particular, unlike `omitempty`, `omitzero`
    omits zero-valued `time.Time` values,
    which is a common source of friction.
  - If both `omitempty` and `omitzero` are specified,
    the field will be omitted if the value is either
    empty or zero (or both).
  - 总体上, Always `omitzero` only.

```
2025-02-11 发布, 这次正好可以借助
Go Telemetry 看看一个月之后,
Go 1.23 有多大比例迁移至 Go 1.24!

2025-03-13
v1.24 / (v1.23 + v1.24) > 0.33
```

- [Go: reduce error handling boilerplate using ?](https://github.com/golang/go/discussions/71460)
  - 我还是偏支持的, 语法糖有意义吗? 有! 如果使用频率高的话~
  - 多年前, 已经有过类似的提案, Go 官方的独断是个事实~
    不过, 社区治理的事情很难评价, 未见不良行为.
  - 我个人还是希望下一个版本 (1.25) 能用上~

- 自己在用的一些 Go 的官方命令行工具:
  - [Go Telemetry](https://telemetry.go.dev)

```sh
go install golang.org/x/vuln/cmd/govulncheck@latest
go install golang.org/x/tools/cmd/deadcode@latest
```

---

- [A Gentle Introduction to Graph Neural Networks](https://distill.pub/2021/gnn-intro/)
  - 配图 (动图) 是个亮点~

```
GNNs adopt a "graph-in, graph-out" architecture.
```

```
We need a way to collect information from edges
and give them to nodes for prediction.
We can do this by pooling.
Pooling proceeds in two steps:
1. For each item to be pooled, gather each of their
   embeddings and concatenate them into a matrix.
2. The gathered embeddings are then aggregated,
   usually via a sum operation.
```

```
If we only have node-level features and need to predict
a binary global property, we need to gather all available
node information together and aggregate them.
This is similar to Global Average Pooling layers in CNNs.
The same can be done for edges.
```

```
Note that in this simplest GNN formulation,
we're not using the connectivity of the graph
at all inside the GNN layer.
We only use connectivity when
pooling information for prediction.
```

```
We could make more sophisticated predictions by
using pooling within the GNN layer, to make our
learned embeddings aware of graph connectivity.
We can do this using message passing, where
neighboring nodes or edges exchange information
and influence each other's updated embeddings.
```

```
Message passing works in three steps:
1. For each node in the graph, gather all the
   neighboring node embeddings (or messages).
2. Aggregate all messages via an aggregate function (like sum).
3. All pooled messages are passed through an update function,
   usually a learned neural network.
```

```
By stacking messages passing GNN layers together,
a node can eventually incorporate information from
across the entire graph:
after three layers, a node has information
about the nodes three steps away from it.
```

```
One solution to this problem is by using the global
representation of a graph (U), which is sometimes
called a master node or context vector.
This global context vector is connected to all other
nodes and edges in the network and can act as a bridge
between them to pass information, building up a
representation for the graph as a whole.
```

```
A common practice for training neural networks is to
update network parameters with gradients calculated
on randomized constant size (batch size) subsets of
the training data (mini-batches).
This practice presents a challenge for graphs due to the
variability in the number of nodes and edges adjacent to
each other, meaning that we cannot have a constant batch size.
The main idea for batching with graphs is to create subgraphs
that preserve essential properties of the larger graph.
```

> 全文偏概述, 也值得一阅.

---

- [Quickwit joins Datadog](https://quickwit.io/blog/quickwit-joins-datadog)
  - [Quickwit](https://github.com/quickwit-oss/quickwit)
  - Quickwit is the fastest search engine on cloud storage.
    It's the perfect fit for observability use cases
  - 印象中, 这是缩小了当初的愿景? 聚焦了?
  - 看看后面
    [Meilisearch](https://github.com/meilisearch/meilisearch)
    花落谁家?

---

- [Temporal](https://github.com/temporalio/temporal)

```
By default, Temporal SDKs set a Worker Identity to
${process.pid}@${os.hostname}, which combines the
Worker's process ID (process.pid) and the hostname of
the machine is running the Worker (os.hostname).

When running Workers inside Docker containers, the
process ID is always 1, as each container typically
runs a single process. This makes the process
identifier meaningless for identification purposes.

Include relevant context: Incorporate information that
helps establish the context of the Worker, such as the
deployment environment (staging or production), region,
or any other relevant details.

Ensure uniqueness: Make sure that the Worker Identity is unique
within your system to avoid ambiguity when debugging issues.

Keep it concise: While including relevant information is important,
try to keep the Worker Identity concise and easily readable to
facilitate quick identification and troubleshooting.
```

```
The Temporal Service (including the Temporal Cloud) doesn't execute
any of your code (Workflow and Activity Definitions) on Temporal Service
machines. The Temporal Service is solely responsible for orchestrating
State Transitions and providing Tasks to the next available Worker Entity.

A Worker Process can be both a Workflow Worker Process and an
Activity Worker Process. Many SDKs support the ability to have
multiple Worker Entities in a single Worker Process.
(Worker Entity creation and management differ between SDKs.)

A single Worker Entity can listen to only a single Task Queue.
But if a Worker Process has multiple Worker Entities, the
Worker Process could be listening to multiple Task Queues.

There are two types of Task Queues,
Activity Task Queues and Workflow Task Queues.

Task Queues do not require explicit registration but instead
are created on demand when a Workflow Execution or Activity
spawns or when a Worker Process subscribes to it.

When a Task Queue is created, both a Workflow Task Queue and
an Activity Task Queue are created under the same name.
```

```
A Sticky Execution is when a Worker Entity caches the Workflow
in memory and creates a dedicated Task Queue to listen on.
A Sticky Execution occurs after a Worker Entity completes the
first Workflow Task in the chain of Workflow Tasks
for the Workflow Execution.

Some SDKs provide a Session API that provides a straightforward
way to ensure that Activity Tasks are executed with the same
Worker without requiring you to manually specify Task Queue names.
```

---

```
2024-12-02: 想到一个好玩的问题

给出一个具体的数学定理 (或者大一点, 主题),
你觉得它最大程度上桥接了不同的数学, 物理, 计算科学.
```

---

- [Delta Lake](https://github.com/delta-io)

```
其实我想说的是:
有不少项目一开始 Scala/Java 开发, 后来也开发 Rust 版本.
但这个项目是极少数 Rust 版本活跃度赶超 Scala/Java 的.

对比:
https://github.com/apache/iceberg-rust
https://github.com/apache/iceberg

https://github.com/apache/hudi
https://github.com/apache/hudi-rs
```

> 2024-12, 看来 Hudi 最先出局了~
  然后 Databricks 自己放弃 Delta Lake, all in Iceberg~

---

- [Kubernetes in Action, Second Edition](https://book.douban.com/subject/34986745/)
  - https://www.manning.com/books/kubernetes-in-action-second-edition

> 不得不吐槽, 作者在 manning.com 几乎停更了 2023 & 2024 两年整!
  很多读者 (包括本人) 在论坛催更无效~

> 后续就算更新也不会再阅读了~ 差评!

---

> Move 生态, 半死不活~

- [Sui (SUI)](https://github.com/MystenLabs/sui)
- [Movement](https://github.com/movementlabsxyz/movement)
  - 不过, 感觉 Ethereum 将在 2025 迎来下坡, 最终消亡~
- [Aptos (APT)](https://github.com/aptos-labs/aptos-core)
  - [Aptos Keyless ZK proofs](https://github.com/aptos-labs/keyless-zk-proofs)

---

- [Announcing Arroyo 0.12](https://www.arroyo.dev/blog/arroyo-0-12-0)
  - [v0.12.0](https://github.com/ArroyoSystems/arroyo/releases/tag/v0.12.0)

---

- [Programming ZKPs: From Zero to Hero](https://zkintro.com/articles/programming-zkps-from-zero-to-hero)
  - [Circom](https://github.com/iden3/circom)

```
The prover key embeds all the information necessary to
generate proof in a zero-knowledge-preserving fashion
for that specific circuit. Similarly, the verifier key
embeds all the required information to verify that the
proof is indeed correct. These aren't private keys but
information that can and should be publicly distributed.
Any party that needs to generate or verify proof
should have access to them.
```

> 既没有 From Zero, 也没有 to Hero; 文章水了一些~

---

- [bon](https://github.com/elastio/bon)
  - `bon` is a Rust crate for generating
    compile-time-checked builders for
    functions and structs.
  - 我想说的是: Go 做不到! 哈哈~

- Rust 的一些容易犯的小错误 (Coding 的时候)
  - 忘记引入相应的 `trait`

---

- [NIST Releases First 3 Finalized Post-Quantum Encryption Standards](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)
  - [Cryspen: High Assurance Cryptography](https://github.com/cryspen)
  - [libcrux - the formally verified crypto library](https://github.com/cryspen/libcrux)

---

- [Go: Range Over Function Types](https://go.dev/blog/range-functions)

```
We've now seen two different approaches (Push/Pull)
to looping over all the elements of a set.
Different Go packages use these approaches and several others.
That means that when you start using a new Go container package
you may have to learn a new looping mechanism.
It also means that we can't write one function that
works with several different types of containers,
as the container types will handle looping differently.

We want to improve the Go ecosystem by developing
standard approaches for looping over containers.
```

```
As of Go 1.23 it now supports ranging over functions that
take a single argument. The single argument must itself be a
function that takes zero to two arguments and returns a bool;
by convention, we call it the yield function.
```

```go
func(yield func() bool)

func(yield func(V) bool)

func(yield func(K, V) bool)
```

```
When we speak of an iterator in Go, we mean a function
with one of these three types. As we'll discuss below,
there is another kind of iterator in the
standard library: a pull iterator.
When it is necessary to distinguish between
standard iterators and pull iterators,
we call the standard iterators push iterators.
```

```
As a matter of convention, we encourage all container types
to provide an All method that returns an iterator,
so that programmers don't have to remember whether to range
over All directly or whether to call All
to get a value they can range over.
```

```
A pull iterator works the other way around:
it is a function that is written such that each time
you call it, it returns the next value in the sequence.

We'll repeat the difference between the two types
of iterators to help you remember:

A push iterator pushes each value in a sequence to
a yield function. Push iterators are standard iterators
in the Go standard library, and are supported
directly by the for/range statement.

A pull iterator works the other way around. Each time you
call a pull iterator, it pulls another value from a sequence
and returns it. Pull iterators are not supported directly by
the for/range statement; however, it's straightforward to write
an ordinary for statement that loops through a pull iterator.
```

```
The first function returned by iter.Pull, the pull iterator,
returns a value and a boolean that reports
whether that value is valid.
The boolean will be false at the end of the sequence.
```

```
iter.Pull returns a stop function in case we don't read
through the sequence to the end. In the general case the
push iterator, the argument to iter.Pull, may
start goroutines, or build new data structures that need
to be cleaned up when iteration is complete.

The push iterator will do any cleanup when the yield
function returns false, meaning that no more values
are required. When used with a for/range statement,
the for/range statement will ensure that if the loop
exits early, through a break statement or for any
other reason, then the yield function will return false.

With a pull iterator, on the other hand, there is no way
to force the yield function to return false,
so the stop function is needed.
```

```go
// EqSeq reports whether two iterators contain the same
// elements in the same order.
func EqSeq[E comparable](s1, s2 iter.Seq[E]) bool {
  next1, stop1 := iter.Pull(s1)
  defer stop1()
  next2, stop2 := iter.Pull(s2)
  defer stop2()
  for {
    v1, ok1 := next1()
    v2, ok2 := next2()
    if !ok1 {
      return !ok2
    }
    if ok1 != ok2 || v1 != v2 {
      return false
    }
  }
}
```

---

```
自 GitOps 理念以来, 至少在长驻的任务上, 带来的便利是毋庸置疑的~
之前也实施过一个项目, 基于:

https://github.com/apache/flink-kubernetes-operator

开发了公司内部的 Flink Job 的调度, 也颇有收益~
但是, 对于 Batch Job (not scheduled), GitOps 还合适么? 比如:

https://github.com/kubeflow/spark-operator
https://github.com/apache/spark-kubernetes-operator

我不觉得! (至少, 对于 no schedule 的)

从一个十分粗暴的角度而言, GitOps 就是声明了长驻资源~
一切皆 GitOps 显然不合适. 或许, 简单的原则是:
GitOps 适用于手动 (包括通过一些: 工具/CI/CD) 提交的资源定义.
而这些资源定义, 一般而言是相对不容易变更的.
此处不容易变更, 是相对的, 大体上不会超过 (微) 服务发布的频率.
```

---

- [SeaORM](https://github.com/SeaQL/sea-orm/releases/tag/1.0.0)
  已经发布 `v1.0` 了, 然而
  [ent](https://github.com/ent/ent)
  还是迟迟未至~ 感觉以目前作者的重心来看,
  [Atlas](https://github.com/ariga/atlas)
  会更早发布 `v1.0`.
  - [Announcing SeaORM 1.0](https://www.sea-ql.org/blog/2024-08-04-sea-orm-1.0/)

- [Announcing Swift Homomorphic Encryption](https://www.swift.org/blog/announcing-swift-homomorphic-encryption/)
  - 文章本身没啥信息量~
  - [Swift Homomorphic Encryption](https://github.com/apple/swift-homomorphic-encryption)
  - [TFHE-rs](https://github.com/zama-ai/tfhe-rs)
  - 个人不觉得 Apple 能真正改变啥, 但是, 多少会推进一丢丢吧?
  - 不看好
    [Swift Crypto](https://github.com/apple/swift-crypto),
    貌似只有 Apple 自己在用~

---

```
7 月末, 体验了一下 Axum (Rust) 的 Web 开发.
说实话, 纯粹个人的角度, 比 Hertz (Go) 要好得多!

但是, 很快发现意义不大, 因为, Rust 的生态优势目前有三处:
1. 区块链/密码学/同态加密 (隐私计算)
2. 围绕着 Arrow(-rs) 与 DataFusion 的数据生态
3. Rust powered 的 Python 生态

其实绝大多数纯 Web 开发者很大概率不会接受 Rust 的学习曲线.
所以, 除非是个人开发者或者 (独立) 开源项目,
否则, Rust 的纯 Web 开发意义不大~
(包括用 Rust 写 K8s operator 等.)

嗯, 如果团队成员大多数是 Rust 掌握者呢? 比如: Data, ML 团队~
再熟练的 Rust 玩家在 Web 开发领域得到的优势也抵不过消耗.
(比如: 编译时间, 编译报错的处理等.)

打一个不恰当的比喻: Rust 大多处于 Data Plane (数据处理, 计算密集).
(Data Plane 对立面是 Control Plane)

有一个特殊情况, 很多 Rust 编写的数据计算组件,
K8s operator 也就用 Rust 写了, 单一代码库, 同一种语言, 也合理.
否则, 其实我不觉得 Rust 写 K8s operator 有任何好处~
```

---

- [Pin](https://without.boats/blog/pin/)
  - [Pinned places](https://without.boats/blog/pinned-places/)

```rs
// The problem was that those references might be
// self-references, meaning they point to
// other fields of the same object.
async fn foo<'a>(z: &'a mut i32) {
  // ...
}

async fn bar(x: i32, y: i32) -> i32 {
  let mut z = x + y;
  foo(&mut z).await;
  z
}
```

```rs
// Let's ask ourselves, what would the internal
// states of `Bar` be? Something like this:

enum Bar {
  // When it starts, it contains only its arguments
  Start { x: i32, y: i32 },

  // At the first await, it must contain `z` and
  // the `Foo` future that references `z`
  FirstAwait { z: i32, foo: Foo<'?> }

  // When its finished it needs no data
  Complete,
}
// The `Foo` object instead borrows the `z` field of `Bar`,
// which is stored along side it in the same struct.
// This is why these future types are said to be
// "self-referential:" they contain fields which
// reference other fields in themselves.
```

---

- 特别喜欢
  [Dependi](https://github.com/filllabs/dependi)
  这个 VSCode 插件
  - 原本的插件
    [Crates](https://github.com/serayuzgur/crates)
    只支持 Rust (archived)
  - Now: Rust, Go, JavaScript, Python

---

- [BLAKE3](https://github.com/BLAKE3-team/BLAKE3)
  - __Much faster__ than MD5, SHA-1, SHA-2, SHA-3, and BLAKE2.
  - Secure, unlike MD5 and SHA-1.
    And secure against length extension, unlike SHA-2.
  - Highly parallelizable across any number of threads and
    SIMD lanes, because it's a Merkle tree on the inside.
  - [Go lukechampine/blake3](https://github.com/lukechampine/blake3)

```
简单 bench 了下

(1_000_000 次):
sha2 (256): 6666.56 ms
md5:        1252.75 ms
blake3:     417.502 ms

(10_000_000 次):
sha2 (256)  66.40 s
md5         12.74 s
blake3      3.47  s
```

- [How to build a plugin system in Rust](https://www.arroyo.dev/blog/rust-plugin-systems)

> 为啥不 WASM 的那一段很务实.

```
But there is a workaround: use the C ABI.
Unlike Rust, C does have a stable ABI on
every major OS and processor architecture.
So if we can constrain our plugin interface
to only use C-compatible data structures and
functions we can safely link against plugins
compiled by any Rust compiler.

Even better: as the C ABI is the lingua franca
in the systems world, many other languages are
able to emit it, opening the door to supporting
UDFs in a variety of compiled languages.
```

- 时至今日, 个人承认
  [Hertz](https://github.com/cloudwego/hertz/pull/1119)
  算是一个可用的 Go Web 框架吧~
  - 首先, Go 的语言特性限制, 导致不可能出现功能丰富的 Web 框架;
    所以, Go 的 Web 框架基本属于大同小异.
  - 但是 Hertz 属于在大同小异之中做到了细节完善度较高~
    比如: binding & validation.

- [Introducing Istio v1 APIs](https://preliminary.istio.io/latest/blog/2024/v1-apis/)
  - Reflecting the stability of Istio's features, our networking,
    security and telemetry APIs are promoted to v1 in 1.22.
  - 嗯, 我也远离了 Istio 了, 哈哈哈~

---

- 2024-05, 正好手头有个场景, 简单 benchmark 了一下
  [NetworkX](https://github.com/networkx/networkx)
  vs
  [Raphtory](https://github.com/Pometry/Raphtory)
  vs
  [rustworkx](https://github.com/Qiskit/rustworkx)
  - rustworkx 这个名字起的不好~
  - __Python 3.12__
  - rustworkx 可以添加 object 作为 node,
    但是会导致 `.neighbors(node_id)` 显著变慢;
    也有可能是 `.get_node_data(node_id)` 导致的.
    没有细究~
  - 同样的使用模式下, 不包含构图过程, 最简单的 `neighbors()`, 粗略估计:
    NetworkX (6.864 s) 耗时是 rustworkx (0.728 s) ~9.4 倍;
    Raphtory (0.748 s) 耗时与 rustworkx (0.728 s) 基本持平.
  - 但是, 查询结果上, Raphtory 与 NetworkX 相对接近;
    rustworkx 则有一定的差异, 想来准确性有待提升.

- [云风的 Blog: 重新启程](https://blog.codingnow.com/2024/05/farewell.html)

```
2018 年开始, 我决定安心做一点想做而擅长的事.
人生短暂, 学习如何管理很多人做事并非我期望的发展方向.
尤其当我逐步融入开源社区后, 我发现,
这个世界上许多软件基础设施往往都是由一两个人支撑.
早在 2011 年时, 我就怀疑过, 软件项目需要很多人一起完成可能是一个骗局,
那么, 当处于一个稳定的环境而自己又有能力时,
这种机遇并不多见, 就应该尝试做点什么.
```

---

- [Compiling fast GPU kernels](https://luminalai.com/blog/gpu)

```
The typical approach in Luminal for supporting new backends would be:

1. Swap out each primitive operation with a backend-specific operation.
2. Add in operations to copy to device and copy from device
   before and after Function operations.
3. Pattern-match to swap out chunks of
   operations with specialized variants.
4. All other optimizations.
```

```
One more note: The core of Luminal has no idea about any of this!
GPUs are a foreign concept to it, which is nessecary since we
want to add backends to TPUs, Groq chips, and whatever else
may come in the future without changing anything in the core.
```

> 拭目以待!

---

- [Secure Randomness in Go 1.22](https://go.dev/blog/chacha8rand)
  - 值得一读!

```
Our new generator, which we unimaginatively named ChaCha8Rand
for specification purposes and implemented as
math/rand/v2's rand.ChaCha8,
is a lightly modified version of ChaCha stream cipher.
ChaCha is widely used in a 20-round form called ChaCha20,
including in TLS and SSH.
We used ChaCha8 as the core of ChaCha8Rand.
```

```
Most stream ciphers, including ChaCha8, work by defining a
function that is given a key and a block number and produces a
fixed-size block of apparently random data.
The cryptographic standard these aim for (and usually meet) is
for this output to be indistinguishable from actual random data in
the absence of some kind of exponentially costly brute-force search.
A message is encrypted or decrypted by XOR'ing successive blocks of
input data with successive randomly generated blocks.
To use ChaCha8 as a rand.Source, we use the generated blocks directly
instead of XOR'ing them with input data
(this is equivalent to encrypting or decrypting all zeros).
We changed a few details to make ChaCha8Rand more
suitable for generating random numbers.
```

```
The Go runtime now maintains a per-core ChaCha8Rand state
(300 bytes), seeded with operating system-supplied
cryptographic randomness, so that random numbers can be
generated quickly without any lock contention.
Dedicating 300 bytes per core may sound expensive,
but on a 16-core system, it is about the same as storing
a single shared Go 1 generator state (4,872 bytes).
The speed is worth the memory.
```

```
Overall, ChaCha8Rand is slower than the Go 1 generator,
but it is never more than twice as slow,
and on typical servers, the difference is never more than 3ns.
Very few programs will be bottlenecked by this difference,
and many programs will enjoy the improved security.
```

---

- [GQL Database Language](https://jtc1info.org/slug/gql-database-language/)
  - ISO/IEC 39075 Database Language GQL
  - 其实也带来了命名规范:
  - `label`, __not__ `tag`
  - `property`: pairs of `names` and `values`
  - `node`, __not__ `vertex`
  - `edge`, __not__ `relationship`

```
The GQL standard does not specify how the
returned data is displayed to the user.
```

```sql
MATCH ((a)-[r]->(b)){1, 5}
RETURN a, r, b

-- This example will find paths where one node
-- knows another node, up to five hops long.
```

```
Nodes are enclosed in parenthesis while
edges are enclosed in square brackets.
```

```sql
INSERT (:Person {
  firstname: 'Avery',
  lastname: 'Stare',
  joined: date("2022-08-23")
})
- [:LivesIn {
  since: date("2022-07-15")
}]
-> (:City {
  name: 'Granville',
  state: 'OH',
  country: 'USA'
})
```

```sql
MATCH (a {
  firstname: 'Avery'
}), (d {
  name: 'Unique'
})
INSERT (a) - [:HasPet] -> (d)
```

```sql
-- GQL data is deleted by identifying nodes,
-- detaching them to delete relationships,
-- then deleting the nodes.
MATCH (a {firstname: 'Avery'}) - [b] -> (c)
DETACH DELETE a, c
```

```
A schema-free graph will accept any data that is inserted.
This allows for quick startup but leaves the control of
the data with the application developer(s) and/or users.
```

---

- [Fluence](https://github.com/fluencelabs)
  - Fluence is a decentralized serverless computing platform.
  - 2024-04-15, 因 Fluence Developer Reward Airdrop 结缘~ 祝好!

- [Loco](https://github.com/loco-rs/loco)
  - Loco is "Rust on Rails".
  - 基于
    [axum](https://github.com/tokio-rs/axum),
    [sea-orm](https://github.com/SeaQL/sea-orm),
    [tracing](https://github.com/tokio-rs/tracing).

---

- [Ethereum has blobs. Where do we go from here?](https://vitalik.eth.limo/general/2024/03/28/blobs.html)

```
This milestone represents a key transition in
Ethereum's long-term roadmap:

blobs are the moment where Ethereum scaling ceased to be
a "zero-to-one" problem, and became a "one-to-N" problem.
```

```
The next stage is likely to be a simplified version of
DAS called PeerDAS. In PeerDAS, each node stores a significant
fraction (eg. 1/8) of all blob data, and nodes maintain
connections to many peers in the p2p network.
When a node needs to sample for a particular piece of data,
it asks one of the peers that it knows is
responsible for storing that piece.
```

- [Changes to u128/i128 layout in 1.77 and 1.78](https://blog.rust-lang.org/2024/03/30/i128-layout-update.html)
  - 嗯, 没直接用过 `u128` 和 `i128`

```rust
// rustc 1.77.0
alignment of i128: 16
```

- [Nebula: 恭喜郝鑫成为 2024 年度首位 Committer](https://mp.weixin.qq.com/s/JvnW-M9MdbiYqxircLxz8w)
  - 哈哈哈~
  - 同一天, 3 月 28 日, 雷军发布小米 SU7~

- 记一个开发 K8s Operator 的时候容易忽略的点:
  - [Multiple Reconcile() invocations on single object creation](https://github.com/kubernetes-sigs/kubebuilder/issues/980)

```go
func (r *TheController) SetupWithManager(mgr ctrl.Manager) error {
  return ctrl.NewControllerManagedBy(mgr).
    For(&TheObject{}).
    // This is useful because we don't want to
    // reconcile again when the generation is not changed.
    // The generation is changed when the spec is updated.
    // The generation is not changed when the status is updated.
    WithEventFilter(predicate.GenerationChangedPredicate{}).
    Complete(r)
}
```

- [Beyond Self-Attention: How a Small Language Model Predicts the Next Token](https://shyam.blog/posts/beyond-self-attention/)

```
For those readers familiar with transformers
and eager for the punchline, here it is:

Each transformer block (containing a multi-head self-attention
layer and feed-forward network) learns weights that associate a
given prompt with a class of strings found in the training corpus.
The distribution of tokens that follow those strings in the
training corpus is, approximately, what the block outputs as
its predictions for the next token.

Each block may associate the same prompt with a different
class of training corpus strings, resulting in a different
distribution of the next tokens and thus different predictions.
The final transformer output is a linear combination of
each block's predictions.
```

```
The takeaway is that simplifying the transformation performed
by the blocks to just the contributions of the feed-forward
networks results in a shorter output vector (has a smaller norm)
than the original output but points in roughly the same direction.

And the difference in norms would have no impact on the
transformer's final output, because of the LayerNorm operation
after the stack of blocks. That LayerNorm step will adjust the
norm of any input vector to a similar value regardless of its
initial magnitude; the final linear layer that follows it will
always see inputs of approximately the same norm.
```

```
I think the model has learned a complex, non-linear embedding
subspace corresponding to each token. Any embedding within that
subspace results in an output distribution that assigns the
token near a certain probability.
Each embedding I was able to learn is probably a point in
the embedding subspace for the corresponding token.
```

```
Within a block, adding the feed-forward network output
vector to the input produces an output embedding that
better aligns with the embedding subspaces of specific tokens.

And those tokens are the same ones predicted in the approximation:
they're the tokens that follow the strings in the training
corpus that yield similar feed-forward network
outputs to the current prompt.
```

> 哈哈, 作者蛮逗的~ 结论一般, 过程值得尊敬~

- [Flink Kubernetes Operator 1.8 Release](https://flink.apache.org/2024/03/21/apache-flink-kubernetes-operator-1.8.0-release-announcement/)

```
Resource savings are nice to have, but the real power of
Flink Autotuning is the reduced time to production.

With Flink Autoscaling and Flink Autotuning, all users
need to do is set a max memory size for the TaskManagers,
just like they would normally configure TaskManager memory.
Flink Autotuning then automatically adjusts the various
memory pools and brings down the total container memory size.
It does that by observing the actual max memory usage on
the TaskMangers or by calculating the exact number of
network buffers required for the job topology.
The adjustments are made together with Flink Autoscaling,
so there is no extra downtime involved.
```

> 很实用的功能, 实际效果有待检验!

- [The magic of Rust's type system](https://www.youtube.com/watch?v=NDIU1GSBrVI&t=11s)

- [Burn](https://github.com/tracel-ai/burn)
  - 自从
    [Candle](https://github.com/huggingface/candle)
    发布以来, Burn 似乎就打了鸡血~ 哈哈哈!
  - 2024, 但愿胜负揭晓~

- [We built a new SQL Engine on Arrow and DataFusion](https://www.arroyo.dev/blog/why-arrow-and-datafusion)
  - 难得的务实好文!

```
Arroyo 0.10 ships as a single, compact binary that
can be deployed in a variety of ways.
```

```
Our first decision was to adopt Apache Arrow as our in-memory
data representation, replacing the static Struct types.
Arrow is a columnar, in-memory format designed for
analytical computations. The coolest thing about Arrow is that
it's a cross-language standard; it supports sharing data
directly between engines and even different languages without
copying or serialization overhead.
For example, Pandas programs written in Python could
operate directly on data generated by Arroyo.
```

```
The takeaway: we only have to pay high overhead of small
batch sizes when our data volume is very low.
But if we're only handling 10 or 100 events per second,
the overall cost of processing will be very small in any case.
And at high data volumes (tens of thousands to millions of
events per second) we can have our cake and eat it too-achieve
high throughput with batching and columnar data while
still maintaining low absolute latency.
```

```
Now that Arroyo compiles down to a single binary,
we're working to remove the other external dependencies,
including Postgres and Prometheus;
future releases of Arroyo will have the option of running
their control plane on an embedded sqlite database.
```

- [River](https://github.com/memorysafety/river)
  - Reverse Proxy Application, based on the
    [Pingora](https://github.com/cloudflare/pingora)
    library from Cloudflare.
  - 嗯, 期待下一步, API Gateway!

- [Blixt](https://github.com/kubernetes-sigs/blixt)
  - An experimental layer 4 load-balancer for Kubernetes.
  - The __control-plane__ is built using Gateway API and
    written in Golang with `Operator SDK/Controller Runtime`.
  - The __data-plane__ is built using eBPF and is
    written in Rust using Aya.

- [Robust generic functions on slices](https://go.dev/blog/generic-slice-functions)
  - `Delete` need not allocate a new array,
    as it shifts the elements in place.
    Like `append`, it returns a new slice.
  - Many other functions in the `slices` package
    follow this pattern, including
    `Compact`, `CompactFunc`, `DeleteFunc`,
    `Grow`, `Insert`, and `Replace`.
  - When calling these functions we must consider
    the original slice invalid, because the
    underlying array has been modified.
  - `go vet` 应该检测这些~
  - Out of pragmatism, we chose to modify the implementation
    of the five functions `Compact`, `CompactFunc`, `Delete`,
    `DeleteFunc`, `Replace` to "clear the tail".
  - The code changed in the five functions uses the new
    built-in function `clear` (Go 1.21) to set the obsolete
    elements to the zero value of the element type.

```go
first, second, third, fourth := 11, 22, 33, 44
s := []*int{&first, &second, &third, &fourth}

if len(s) >= 4 {
  s = slices.Delete(s, 2, 3)
  fmt.Println("New length is", len(s))
}

for _, v := range s {
  fmt.Println(*v)
}

// New length is 3
// 11
// 22
// 44
```

```go
first, second, third, fourth := 11, 22, 33, 44
s := []*int{&first, &second, &third, &fourth}

if len(s) >= 4 {
  s := slices.Delete(s, 2, 3)
  fmt.Println("New length is", len(s))
}

for _, v := range s {
  fmt.Println(*v)
}

// New length is 3
// 11
// 22
// 44
// panic: runtime error: invalid memory address or nil pointer dereference
```

- [Warp](https://www.warp.dev)
  - Warp is the terminal reimagined with AI and
    collaborative tools for better productivity.
  - [GitHub](https://github.com/warpdotdev)
  - 体验很棒! Bye Bye, iTerm2~

- [uv](https://github.com/astral-sh/uv)
  - 春节假期, 一经发布, 便收获了不少关注~
  - 目前在用
    [Rye](https://github.com/astral-sh/rye),
    体验很不错~
  - [Rye: Better uv integration](https://github.com/astral-sh/rye/issues/668)
  - [Rye: Hi Astral, Hi uv!](https://github.com/astral-sh/rye/discussions/659)
  - [uv: Python packaging in Rust](https://astral.sh/blog/uv)

- [UI = f(statesⁿ)](https://daverupert.com/2024/02/ui-states/)
  - 多年前有一些类似的思考, 不过这篇文章无疑要细致一些.
  - 由于已经不做前端了, 所以没有细看~

- [Post-Quantum Cryptography Alliance](https://github.com/pqca)
  - https://github.com/pq-code-package
  - 目前啥都没有~

---

- [Go 1.22 Release Notes](https://go.dev/doc/go1.22)
  - 春节前~
  - Functions that shrink the size of a slice
    (`Delete`, `DeleteFunc`, `Compact`, `CompactFunc`, and `Replace`)
    now zero the elements between the new length and the old length.

```go
type Item struct {
  Name   string
  Amount int
}

items := []*Item{
  {Name: "Car", Amount: 1},
  {Name: "Car", Amount: 1},
}

l1 := len(slices.CompactFunc(items, func(a *Item, b *Item) bool {
  return a.Name == b.Name
}))

l2 := len(slices.CompactFunc(items, func(a *Item, b *Item) bool {
  return a.Amount == b.Amount
}))

fmt.Println(l1, l2)

// Go 1.21:
// 1 1
// Go 1.22:
// panic: runtime error: invalid memory address or nil pointer dereference
```

> 这个 Case 因为我使用
  [ent](https://github.com/ent/ent),
  比较容易出现 `[]*ent.Entity`.
> 所以我切换到了
  [lo.UniqBy](https://github.com/samber/lo).
  一方面是 `slices` 目前无法替代 `lo`;
  另一方面是 `lo` 使用体验更加.

---

- [Arroyo: What is stateful stream processing?](https://www.arroyo.dev/blog/stateful-stream-processing)
  - In stream processing, statelessness also goes hand-in-hand with a
    property that I'll call __map-only__. This means that there are no
    operations that require reorganizing ("shuffling") or sorting data;
    only operators that are like "map" or "filter" (in SQL terms,
    `SELECT` and `WHERE`) are supported. In particular,
    `GROUP BY`, `JOIN`, and `ORDER BY` can't be implemented.
  - [10x faster sliding windows: how our Rust streaming engine beats Flink](https://www.arroyo.dev/blog/how-arroyo-beats-flink-at-sliding-windows)
  - Early stateful systems like Flink and ksqlDB were designed at a
    time when memory was expensive and networks were slow.
    They relied on embedded key-value stores like RocksDB
    in order to provide large, relatively fast storage.
    __However, in practice__ many users rely on the in-memory backend
    due to the complexity of tuning RocksDB.
  - `... due to the complexity of tuning RocksDB.`
    哈哈哈, 蛮现实的~
  - While Flink supports storing TBs of state in RocksDB,
    in practice this proves operationally difficult because of
    the need to load all of the state onto the processing nodes.
  - Newer systems like Rising Wave and Arroyo have adopted
    remote state backends that allow only live data to be
    loaded onto the processing nodes which enables much faster
    operations at large state sizes.

- [Arroyo 0.9](https://github.com/ArroyoSystems/arroyo/releases/tag/v0.9.0)
  - User-defined functions (UDFs) and user-defined aggregate functions
    (UDAFs) allow you to extend Arroyo with custom logic.
    New in Arroyo `0.9` is support for what we call async UDFs.

```rust
pub async fn get_city(ip: String) -> Option<String> {
  let body: serde_json::Value =
    reqwest::get(format!("http://geoip-service:8000/{ip}"))
      .await
      .ok()?
      .json()
      .await
      .ok()?;

  body.pointer("/names/en")
    .and_then(|t| t.as_str())
    .map(|t| t.to_string())
}
```

```sql
create view cities as
select get_city(logs.ip) as city
from logs;

SELECT * FROM (
  SELECT *, ROW_NUMBER() OVER (
    PARTITION BY window
    ORDER BY count DESC
  ) as row_num
  FROM (SELECT count(*) as count,
    city,
    hop(interval '5 seconds', interval '15 minutes') as window
      FROM cities
      WHERE city IS NOT NULL
      group by city, window)
) WHERE row_num <= 5;
```

- [Announcing Rust 1.75](https://blog.rust-lang.org/2023/12/28/Rust-1.75.0.html)
  - [Announcing `async fn` and return-position `impl Trait` in traits](https://blog.rust-lang.org/2023/12/21/async-fn-rpit-in-traits.html)
  - 终于可以切换回 `stable` 了!

---

- [Go Wiki: Rangefunc Experiment](https://go.dev/wiki/RangefuncExperiment)
  - `GOEXPERIMENT=rangefunc`

- Previously, the variables declared by a `for` loop were created once
  and updated by each iteration.
  - In Go `1.22`, each iteration of the loop creates new variables,
    to avoid accidental sharing bugs.

```go
values := []int{1, 2, 3, 4, 5}
for _, v := range values {
  go func() {
    // go <= 1.21
    // vet: loop variable val captured by func literal
    // 5 5 5 5 5
    // go >= 1.22
    // 2 1 4 5 3 (randomly)
    fmt.Printf("%d ", v)
  }()
}
```
