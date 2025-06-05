---
title: Programming language
description: 结庐在人境, 而无车马喧. 问君何能尔? 心远地自偏.
date: 2021-10-28
---

- Rust vs Go
  - 两者都内置了 test 支持, 但是 Rust (Cargo) 区分了 unit tests `vs` integration tests.
    很多时候, 我只想在本地跑 unit tests, 而在 CI 当中跑所有的 tests.
    因为 integration tests 可能依赖数据库等额外环境, 但我本地没有.
    Rust 可以直接覆盖类似场景.

## Rust (1.64+)

- [Crossbeam](https://github.com/crossbeam-rs/crossbeam)
- [axum](https://github.com/tokio-rs/axum)

```zsh
cargo test -- --show-output
```

- [RFC-0048 Traits](https://github.com/rust-lang/rfcs/blob/master/text/0048-traits.md)

- __Pin__

- __trait object__
  - `&dyn Trait`
  - `&mut dyn`
  - `Box<dyn Trait>`

- `String`
- `Box<T>`
- `Rc<T>`
  - 非线程安全
- `Arc<T>`
  - 线程安全
- `Cell<T>`
- `RefCell<T>`
- `Cow<T>`
- `Vec<T>`
- `RawVec<T>`
- `Unique<T>`
- `Shared<T>`
- Raw Pointer
  - `*mut T`
  - `*const T`

------------------

## Go (1.18+)

```zsh
go build -gcflags "-m=2"
go tool pprof -http=:8080 ...
GODEBUG=gctrace=1 go test -bench=. -v
```

- Returning `structs` instead of `interfaces`.
  Meanwhile, it also means
  accepting `interfaces` whenever possible.
- When designing `interfaces`,
  we should __avoid__ distinguishing
  `nil` and `empty` slices
  - This principle is the same with `maps`.
  - To check if a `map` is empty,
    we should check its `length`,
    not whether it's `nil`.
  - `if len(ops) != 0`
- When working with `maps` in Go, we have to know a
  noteworthy property:
  - the size of a `map` in memory can
    __only increase__, __never decrease__.
- In Go, everything we assign is a __copy__.
  - The expression passed to `range` is
    evaluated __only once__, before the
    beginning of the loop.
- __Never__ using named result parameters
- The arguments passed to a `defer` function
  are evaluated right away.
  - Yet, the variables referenced by a `defer` closure
    are evaluated during the closure execution.
- The expression `~string` means the set of all types
  whose underlying type is `string`. This includes the
  type `string` itself as well as all types declared with
  definitions such as `type MyString string`.
- We can face the issue of unintentionally copying
  a `sync` field in some of the following conditions:
  - Calling a method with a value receiver
  - Calling a function with a `sync` argument
  - Calling a function with an argument
    that contains a `sync` field
- we should rather need
  __mutexes__ for __parallel__ goroutines and
  __channels__ for __concurrent__ ones.
- A `send` on a channel `happens before`
  the corresponding `receive`
  from that channel completes.
- A `receive` from an `unbuffered` channel
  `happens before` the `send` on that
  channel completes.
- Let's keep this idea in mind:
  `nil` channels (set closed channel to `nil`)
  are truly useful in some conditions.
- Both channel types enable communication, but only one
  provides synchronization.
  - If we need synchronization, we must use unbuffered channels.
- When using a `sync.WaitGroup`, the `Add` operation
  must be done before spinning up a goroutine in the
  parent one.

------------------

- 选择一个语言, 最重要的其实是生态, 而非语法特性.
- 一些 Rust 领先其他语言的生态~
  - [Serde](https://github.com/serde-rs/serde)
  - Serde is a framework for serializing and deserializing
    Rust data structures efficiently and generically.
  - [Rayon](https://github.com/rayon-rs/rayon)
  - A data parallelism library for Rust
- ML Ecosystem
  - [Polars](https://github.com/pola-rs/polars)
  - Blazingly fast DataFrames in Rust, and Python.
  - [rust-gpu](https://github.com/EmbarkStudios/rust-gpu)
  - Rust as a first-class language and ecosystem
    for GPU graphics & compute shaders
  - [BastionLab](https://github.com/mithril-security/bastionlab)
  - A simple privacy framework for data science collaboration.
- 一些常见需求
  - [rust-rdkafka](https://github.com/fede1024/rust-rdkafka)
  - [Anyhow](https://github.com/dtolnay/anyhow)
  - [derive(Error)](https://github.com/dtolnay/thiserror)

---

- [Rust in 2023](https://www.ncameron.org/blog/rust-in-2023/)

```
Async. Work on async programming is progressing nicely
and I hope that things start coming together and producing
tangible results in 2023. I'm kind of frustrated with my
own slow progress here, and unfortunately most of the async
WG are busy with many other things, but things are moving
and I think 2023 will be an exciting year for async.
It should remain a high priority for the project.
```

```
Kind of a wildcard to finish off: I'm really excited to
see how data analysis/numeric computing with Rust is
going to go next year. This is an entirely community-led
effort and there is some really exciting stuff happening
(Polars in particular is very cool).

I think it's a really good fit for Rust, it seems to be
reaching an inflection point in terms of maturity,
and I'm genuinely curious to see if it will
take off and where it goes.
```

---

- [JEP 434: Foreign Function & Memory API](https://openjdk.org/jeps/434)

```
This JEP proposes to incorporate refinements
based on feedback, and to re-preview the
API in JDK 20. In this version:

The MemorySegment and MemoryAddress abstractions are
unified (memory addresses are now modeled by
zero-length memory segments);
The sealed MemoryLayout hierarchy is enhanced to
facilitate usage with pattern matching in
switch expressions and statements (JEP 433), and
MemorySession has been split into Arena and
SegmentScope to facilitate sharing segments
across maintenance boundaries.
```

> 期待 Flink call Rust

---

- Memory Safe Languages in Android `13`
  - `Dec 1, 2022`

```
We're implementing userspace HALs in Rust.
We're adding support for Rust in Trusted Applications.
We've migrated VM firmware in the Android Virtualization Framework to Rust.
With support for Rust landing in Linux 6.1 we're excited to
bring memory-safety to the kernel, starting with kernel drivers.

As Android migrates away from C/C++ to Java/Kotlin/Rust,
we expect the number of memory safety vulnerabilities to continue to fall.
```

- [The Initial Rust Infrastructure Has Been Merged Into Linux 6.1](https://www.phoronix.com/news/Rust-Is-Merged-Linux-6.1)
  - `2022-10`

---

- 2022 国庆节, 数落 Go 的几个问题
  - `Enum` 迟迟不考虑
  - Go `1.18` 带来的 `interface` 的语义变化 (这个, 倒也还好)
  - Go `1.18` 带来的 `Generics` 导致的后续的 std APIs 变更
  - `Error` 处理的改进可能带来的 broken
  - 对 `map`, `filter` 等系列 func 的一味拒绝
  - Rust Attributes 之类的语法, 对于在开发 K8s operator 时的
    CRD by code 类似场景还是很便利的. Struct Tags 丑陋且呆板!
  - Rust Option 解决了 Primitive Types, 到底是 `0`, `false`, `""`,
    还是 `nil`. 这绝对是一个设计缺失!
  - 最关键的, 语言发展缓慢!
  - 2022: Rust > Go > Java

- 2022 年国庆节前后, 同时看两本编程语言的书籍
  - 重温
    [Programming Rust, 2nd Edition](https://book.douban.com/subject/34973905/)
    和
    [On Java 进阶卷](https://book.douban.com/subject/35751623/)
  - Rust 是我接下来项目中, 唯一主动选择的语言
  - Go, Java, Kotlin, Python 都会是被动选择项
  - Rust 也是目前唯一值得认真把玩的语言

- 纯粹从语言角度而言, 2022 以及接下来的 `2~3` 年,
  Java 都会比 Go 迭代的更加迅速.
  - Web service 本来就是 Java (Spring) 的优势
  - 而原本 Go 的地盘, K8s operator, 搞不好都会被 Java 瓜分.
    当然, 也会被 Rust 和 Python 瓜分.
  - 但是由于内存效率的原因, 一些所谓的云原生应用, 不会被 Java 占领.
    但是, 可能且个人也期待 Rust 的表现.
- 个人的偏好或者期待:
  - Python 做 prototype
  - Rust ~
- 有一点必须强调, 所谓的合适的语言做合适的事情,
  和开发者的水平是有很大关系的.
  (准确说是开发者关于某一语言的水平)
  - 如果足够熟练, Rust 也可以做 prototype
- 一言以蔽之: Go core team 有自己的坚持;
  但开源社区同样有自己的发展趋势与选择!

- __Python__ 的正确使用姿势, `call` __Rust__

- 除非是 K8s 密切相关的场景, 比如 K8s operator 开发,
  否则, __都不应该选择__ Go 语言
  - 好吧, 我有点后悔了,
    其实 K8s operator 开发也不应该用 Go

---

- `2022-09` 开始正式评估在团队项目中引入 Rust
  - 参照一些手头上的项目, 看看 Rust 生态还缺点啥
  - 由于公司使用 GCP (很垃圾的云平台)
  - https://github.com/googleapis/google-cloud-rust
  - 这玩意还打算继续开发么?
  - https://github.com/kafka-rust/kafka-rust
  - 功能还很贫乏! 看样子也不打算维护了
  - 鉴于
    [confluent-kafka-go](https://github.com/confluentinc/confluent-kafka-go)
    基于
    [librdkafka](https://github.com/edenhill/librdkafka),
    所以还是选择基于 librdkafka 的
    [rust-rdkafka](https://github.com/fede1024/rust-rdkafka)
  - https://github.com/tokio-rs/axum
  - https://github.com/hyperium/tonic
  - https://github.com/diesel-rs/diesel
  - https://github.com/SeaQL/sea-orm
  - 以上 gRPC, API, ORM 皆胜过 Go 社区!
  - Diesel vs SeaORM, 还是用 SeaORM,
    因为不想再需要一个 https://github.com/weiznich/diesel_async
  - VS Code + `rust-analyzer` 插件, 体验还是有待改善~

---

- [Diesel 2.0.0](https://github.com/diesel-rs/diesel/releases/tag/v2.0.0)
  - [SeaORM](https://github.com/SeaQL/sea-orm)

- [Ent](https://github.com/ent/ent)
  搭配
  [Atlas](https://github.com/ariga/atlas)
  - 体验不错~
  - declarative and versioned migrations
  - 从稳妥角度来讲, 显然 versioned 靠谱
  - 但是从维护成本来看, 显然 declarative 更轻松

```
As part of the Atlas project we advocate for a third
combined approach that we call "Versioned Migration Authoring".
Versioned Migration Authoring is an attempt to combine
the simplicity and expressiveness of the declarative approach
with the control and explicitness of versioned migrations.

With versioned migration authoring, users still declare
their desired state and use the Atlas engine to plan a safe
migration from the existing to the new state. However,
instead of coupling planning and execution, plans are
instead written into normal migration files which can be
checked into source control, fine-tuned manually and
reviewed in regular code review processes.
```

```
Partitions:
Atlas currently only supports PostgreSQL.
```

> 哈哈, 运气不错~

- [The Go Memory Model](https://tip.golang.org/ref/mem)
  - If a package `p` imports package `q`,
    the completion of `q`'s `init` functions
    happens before the start of any of `p`'s.
  - The completion of all `init` functions is
    synchronized before the start of
    the function `main.main`.
  - If the effects of a goroutine must be observed by
    another goroutine, use a synchronization mechanism
    such as a lock or channel communication
    to establish a relative ordering.
  - The closing of a channel is synchronized before a
    receive that returns a zero value
    because the channel is closed.
  - A receive from an `unbuffered` channel is
    synchronized before the completion of the
    corresponding send on that channel.
  - The `k`th receive on a channel with capacity `C` is
    synchronized before the completion of the `k+C`th
    send from that channel completes.
  - For any `sync.Mutex` or `sync.RWMutex` variable `l`
    and `n < m`, call `n` of `l.Unlock()` is synchronized
    before call `m` of `l.Lock()` returns.
  - For any call to `l.RLock` on a `sync.RWMutex` variable `l`,
    there is an `n` such that the `n`th call to `l.Unlock` is
    synchronized before the return from `l.RLock`, and the
    matching call to `l.RUnlock` is synchronized before the
    return from call `n+1` to `l.Lock`.
  - A successful call to `l.TryLock` (or `l.TryRLock`) is
    equivalent to a call to `l.Lock` (or `l.RLock`).
  - An unsuccessful call has no synchronizing effect at all.
  - As far as the memory model is concerned, `l.TryLock`
    (or `l.TryRLock`) may be considered to be able to return
    `false` even when the mutex `l` is unlocked.
  - The completion of a single call of `f()` from `once.Do(f)`
    is synchronized before the return of any call of `once.Do(f)`.
  - All the atomic operations executed in a program behave
    as though executed in some sequentially consistent order.
  - A call to `SetFinalizer(x, f)` is synchronized before
    the finalization call `f(x)`.
  - Programs with races are incorrect and can
    exhibit __non-sequentially consistent executions__.
    In particular, note that a read `r` may observe the
    value written by any write `w` that executes
    concurrently with `r`. Even if this occurs,
    it does not imply that reads happening after `r` will
    observe writes that happened before `w`.
  - The Go memory model restricts compiler optimizations as much
    as it does Go programs. Some compiler optimizations that
    would be valid in single-threaded programs
    are not valid in all Go programs.
  - In particular, a compiler __must not__ introduce writes that
    do not exist in the original program, it __must not__ allow
    a single read to observe multiple values, and it __must not__
    allow a single write to write multiple values.

```go
var a, b int

func f() {
  a = 1
  b = 2
}

func g() {
  print(b)
  print(a)
}

func main() {
  go f()
  g()
}
// it can happen that g prints 2 and then 0.
```

- [JEP 425: Virtual Threads (Preview)](https://openjdk.org/jeps/425)
  - 这个才能真正吸引大家升级
  - 有那么一点点期待`2024`年的 LTS JDK `23` 了

- `2022-06`, 公司有团队在推 [Quarkus](https://github.com/quarkusio/quarkus)
  - 其实, 只要不是 Spring boot, 都不错

- `2022-05`, 有一个新的 Service 项目, 较简单, 所以上了 `Go 1.18`
  - Go 用来开发 Web Service, 说实话, 体验还是较差
  - 优势在于资源占用低, 相较于目前公司内部主流的 Spring + Kotlin
  - [Gin Web Framework](https://github.com/gin-gonic/gin)
  - [Sarama: Go client library for Kafka](https://github.com/Shopify/sarama)
  - [Goavro: encodes and decodes Avro data](https://github.com/linkedin/goavro)

---

- [Robyn](https://github.com/sansyrox/robyn)
  - __Robyn__ is an `async` Python backend server
    with a runtime written in __Rust__.
  - 该来的, 终究还是来了, __FastAPI__ 其实也可以这么做, 期待后者
    (主要是 __FastAPI__ 文档写得很好)
  - __SQLAlchemy__ 其实更应该如此, 但是估计会是一个新的替代者

- [pydantic-core](https://github.com/samuelcolvin/pydantic-core)
  - __pydantic__ 作者打造
  - The plan is for `pydantic` to adopt `pydantic-core` in `v2`
    and to generate the schema definition from type hints in
    `pydantic`, then create a `SchemaValidator`
    upon model creation.
  - `pydantic-core` will be a separate package,
    required by `pydantic`.
  - `Pydantic-core` is currently around `17x` faster
    than `pydantic` standard.
  - The aim is to remain `10x` faster than current
    `pydantic` for common use cases.

- `2022-04`: 把一个 __Model Serving Framework__ 从
  - [Flask](https://github.com/pallets/flask) `v2`
  - [Gunicorn](https://github.com/benoitc/gunicorn)
  - __迁移到了__
  - [FastAPI](https://github.com/tiangolo/fastapi)
  - [Uvicorn](https://github.com/encode/uvicorn)

- 时至今日 (2022-04), 觉得 `go mod` 是最好的包管理方式
  - 核心点: __版本控制__ 和 __包管理__ 本就应该 __合二为一__

---

- __华为__, 新编程语言
  - 2022-03-20: 填写了 __新语言内测__ 申请问卷
  - 2022-03-22: 收到了`报名确认! 签署保密承诺函`的邮件
  - 2022-03-28: 收到了`华为编程语言实验室生态合作-个人保密承诺函`
  - 2022-03-31: 由于正值上海疫情隔离在家,
    只能通过编辑 PDF 完成签名, 回复邮件
  - 2022-04-13: 通过审核, 看到了文档
  - 看见 Cangjie 的第一感觉: (保密期, 等 `Public` 再说)
    Kotlin 为主, 参杂 Rust, Go 的影子, __没有惊喜__
  - Cangjie AI: 不看好, Python + Rust
    的生态已经初具规模, 且发展的很快
  - 2022-05-18, Gitee 仓库开源须审核,
    已开源仓库暂时关闭, 审核通过后再次公开.
    很好, 正好告别 Gitee, 也不再关注 Cangjie

---

- [An Introduction To Generics](https://go.dev/blog/intro-generics)
  - Generics adds three new big things to the language:
  - (1) Type parameters for function and types.
  - (2) Defining interface types as sets of types,
    including types that don't have methods.
  - (3) Type inference, which permits omitting type
    arguments in many cases when calling a function.
  - __Instantiation__ happens in two steps. `First`,
    the compiler substitutes all type arguments for
    their respective type parameters throughout the
    generic function or type. `Second`, the compiler
    verifies that each type argument satisfies
    the respective constraint.
  - Similarly, type parameter lists have a type for
    each type parameter. Because a type parameter is
    itself a type, the types of type parameters define
    sets of types. This `meta-type` is called
    a type constraint.
  - In Go, __type constraints must be interfaces__.
    That is, an interface type can be used as a value
    type, and it can also be used as a `meta-type`.
    Interfaces define methods, so obviously we can
    express type constraints that require certain
    methods to be present. But `constraints.Ordered`
    is an interface type too, and the `<`
    operator is not a method.
  - Until recently, the Go spec said that an interface
    defines a method set, which is roughly the set of methods
    enumerated in the interface. Any type that implements
    all those methods implements that interface.
  - But another way of looking at this is to say that
    the interface defines a set of types, namely the
    types that implement those methods.
    From this perspective, any type that is an element
    of the interface's type set implements the interface.
  - The two views lead to the same outcome: For each set
    of methods we can imagine the corresponding set of
    types that implement those methods, and that is the
    set of types defined by the interface.
  - For our purposes, though, the type set view has an
    advantage over the method set view: we can explicitly
    add types to the set, and thus control
    the type set in new ways.
  - The expression `~string` means the set of all types
    whose underlying type is `string`. This includes the
    type `string` itself as well as all types declared with
    definitions such as `type MyString string`.
  - In Go `1.18` an interface may contain methods and
    embedded interfaces just as before, but it may also
    embed `non-interface` types, unions, and
    sets of underlying types.
  - `[S interface{~[]E}, E interface{}]`
  - Here `S` must be a slice type whose element type can be any type.
  - `[S ~[]E, E interface{}]`
  - `[S ~[]E, E any]`
  - __Interfaces as type sets__ is a powerful new mechanism
    and is key to making type constraints work in Go.
  - In many cases the compiler can __infer the type argument__
    for `T` from the ordinary arguments.
  - This kind of inference, which infers the type arguments
    from the types of the arguments to the function,
    is called __function argument type inference__.

---

- macOS `12.3`

```zsh
~ which python
python not found

~ which python2
python2 not found

~ /usr/bin/python3 -V
Python 3.8.2
```

- [Go 1.18 is released!](https://go.dev/blog/go1.18)
  - `15 March 2022`
  - [Go 1.18 Release Notes](https://go.dev/doc/go1.18)
  - There are three __experimental__ packages using generics
    that may be useful. These packages are in `x/exp` repository.
  - `golang.org/x/exp/constraints`
  - Constraints that are useful for generic code,
    such as `constraints.Ordered`.
  - `golang.org/x/exp/slices`
  - A collection of generic functions that operate on
    `slices` of any element type.
  - `golang.org/x/exp/maps`
  - A collection of generic functions that operate on
    `maps` of any key or element type.

- [runtime: make GOMAXPROCS cfs-aware on GOOS=linux](https://github.com/golang/go/issues/33803)
  - [automaxprocs](https://github.com/uber-go/automaxprocs)
  - [CFS Bandwidth Control](https://www.kernel.org/doc/Documentation/scheduler/sched-bwc.txt)

- [s2n-quic](https://github.com/aws/s2n-quic)
  - 不错

- macOS Monterey `12.3`
  - Python `2.7` was removed from macOS in this update.

- __Deprecated__ `io/ioutil`: As of Go `1.16`,
  the same functionality is now provided by
  package `io` or package `os`.
