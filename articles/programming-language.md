---
title: Programming language
description: 结庐在人境, 而无车马喧. 问君何能尔? 心远地自偏.
date: 2021-10-28
---

### Preference

* **Memory** intensive
  - Such as: `Apache Arrow`, `Flink`
  - **Rust**
  - Go: Heap management can be responsible for up to
    `20` to `30%` of the total CPU time consumed in
    some data-intensive applications.

## Go (1.18+)

* [ent](https://github.com/ent/ent)

* [Effective Go](https://go.dev/doc/effective_go)

```zsh
go build -gcflags "-m=2"
go tool pprof -http=:8080 ...
```

------------------

## Rust (1.59+)

* [Crossbeam](https://github.com/crossbeam-rs/crossbeam)
* [axum](https://github.com/tokio-rs/axum)
  - [Surf](https://github.com/http-rs/surf)

```zsh
cargo test -- --show-output
```

------------------

## Python (3.10+)

* [tiangolo/fastapi](https://github.com/tiangolo/fastapi)
  - [pydantic](https://github.com/samuelcolvin/pydantic)
  - [encode/httpx](https://github.com/encode/httpx)

------------------

* **华为**, 新编程语言
  - `2022-03-20`: 填写了**新语言内测**申请问卷
  - `2022-03-22`: 收到了`报名确认! 签署保密承诺函`的邮件
  - `2022-03-28`: 收到了`华为编程语言实验室生态合作-个人保密承诺函`
  - `2022-03-31`: 由于正值上海疫情隔离在家,
    只能通过编辑 PDF 完成签名, 回复邮件
  - `2022-04-13`: 通过审核, 看到了文档
  - 看见 `Cangjie` 的第一感觉: (保密期, 等 `Public` 再说)

* [An Introduction To Generics](https://go.dev/blog/intro-generics)
  - Generics adds **three** new big things to the language:
  - 1. Type parameters for function and types.
  - 2. Defining interface types as sets of types,
    including types that don't have methods.
  - 3. Type inference, which permits omitting type
    arguments in many cases when calling a function.
  - **Instantiation** happens in two steps. `First`,
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
  - In Go, **type constraints must be interfaces**.
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
  -  The expression `~string` means the set of all types
    whose underlying type is `string`. This includes the
    type `string` itself as well as all types declared with
    definitions such as `type MyString string`.
  -  In Go `1.18` an interface may contain methods and
    embedded interfaces just as before, but it may also
    embed `non-interface` types, unions, and
    sets of underlying types.
  - `[S interface{~[]E}, E interface{}]`
  - Here `S` must be a slice type whose element type can be any type.
  - `[S ~[]E, E interface{}]`
  - `[S ~[]E, E any]`
  - **Interfaces as type sets** is a powerful **new mechanism**
    and is **key to making type constraints work in Go**.
  - In many cases the compiler can **infer the type argument**
    for `T` from the ordinary arguments.
  - This kind of inference, which infers the type arguments
    from the types of the arguments to the function,
    is called *function argument type inference*.

* macOS `12.3`

```zsh
~ which python
python not found

~ which python2
python2 not found

~ /usr/bin/python3 -V
Python 3.8.2
```

* [Go 1.18 is released!](https://go.dev/blog/go1.18)
  - `15 March 2022`
  - [Go 1.18 Release Notes](https://go.dev/doc/go1.18)
  - There are three **experimental** packages using generics
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

* [runtime: make GOMAXPROCS cfs-aware on GOOS=linux](https://github.com/golang/go/issues/33803)
  - [automaxprocs](https://github.com/uber-go/automaxprocs)
  - [CFS Bandwidth Control](https://www.kernel.org/doc/Documentation/scheduler/sched-bwc.txt)

* [s2n-quic](https://github.com/aws/s2n-quic)
  - 不错

* macOS Monterey `12.3`
  - Python `2.7` was removed from macOS in this update.

* [Switch DataFusion to using arrow2](https://github.com/apache/arrow-datafusion/issues/1532)
  - https://github.com/jorgecarleitao/arrow2
  - https://github.com/jorgecarleitao/parquet2

* **Deprecated** `io/ioutil`: As of Go `1.16`,
  the same functionality is now provided by
  package `io` or package `os`.
