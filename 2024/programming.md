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



- [uv](https://github.com/astral-sh/uv)
  - 春节假期, 一经发布, 便收获了不少关注~
  - 目前在用
    [Rye](https://github.com/mitsuhiko/rye),
    体验很不错~
  - 下半年再看!

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
