---
title: 码农碎碎念~
description: 薄雾浓云愁永昼, 瑞脑销金兽. 佳节又重阳, 玉枕纱厨, 半夜凉初透.
date: 2023-07-17
---

- 自己在用的一些 Go 的官方命令行工具:

```sh
go install golang.org/x/vuln/cmd/govulncheck@latest
go install golang.org/x/tools/cmd/deadcode@latest
```

- Rust 的一些容易犯的小错误 (Coding 的时候)
  - 忘记引入相应的 `trait`

---

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
