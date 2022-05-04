---
title: Programming language
description: 结庐在人境, 而无车马喧. 问君何能尔? 心远地自偏.
date: 2021-10-28
---

## Rust (1.60+) and Python (3.10+)

> __Python__ 的正确使用姿势, `call` __Rust__

- [Crossbeam](https://github.com/crossbeam-rs/crossbeam)
- [axum](https://github.com/tokio-rs/axum)

```zsh
cargo test -- --show-output
```

- [RFC-0048 Traits](https://github.com/rust-lang/rfcs/blob/master/text/0048-traits.md)

- __Pin__

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
  - 迁移到了
  - [FastAPI](https://github.com/tiangolo/fastapi)
  - [Uvicorn](https://github.com/encode/uvicorn)

- 时至今日 (2022-04), 觉得 `go mod` 是最好的包管理方式
  - 核心点: __版本控制__ 和 __包管理__ 本就应该 __合二为一__

- __华为__, 新编程语言
  - `2022-03-20`: 填写了 __新语言内测__ 申请问卷
  - `2022-03-22`: 收到了`报名确认! 签署保密承诺函`的邮件
  - `2022-03-28`: 收到了`华为编程语言实验室生态合作-个人保密承诺函`
  - `2022-03-31`: 由于正值上海疫情隔离在家,
    只能通过编辑 PDF 完成签名, 回复邮件
  - `2022-04-13`: 通过审核, 看到了文档
  - 看见 `Cangjie` 的第一感觉: (保密期, 等 `Public` 再说)
    `Kotlin` 为主, 参杂 `Rust`, `Go` 的影子, __没有惊喜__
  - `Cangjie AI`: 不看好, `Python + Rust`
    的生态已经初具规模, 且发展的很快

- [An Introduction To Generics](https://go.dev/blog/intro-generics)
  - Generics adds three new big things to the language:
  - 1) Type parameters for function and types.
  - 2) Defining interface types as sets of types,
    including types that don't have methods.
  - 3) Type inference, which permits omitting type
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

- [Switch DataFusion to using arrow2](https://github.com/apache/arrow-datafusion/issues/1532)
  - https://github.com/jorgecarleitao/arrow2
  - https://github.com/jorgecarleitao/parquet2

- __Deprecated__ `io/ioutil`: As of Go `1.16`,
  the same functionality is now provided by
  package `io` or package `os`.
