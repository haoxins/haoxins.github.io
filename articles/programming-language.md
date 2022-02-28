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

## Rust (1.58+)

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
