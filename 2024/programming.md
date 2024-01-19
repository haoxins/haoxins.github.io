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

---

- [Arroyo 0.9](https://github.com/ArroyoSystems/arroyo/releases/tag/v0.9.0)
  - User-defined functions (UDFs) and user-defined aggregate functions
    (UDAFs) allow you to extend Arroyo with custom logic.
    New in Arroyo 0.9 is support for what we call async UDFs.

```rust
pub async fn get_city(ip: String) -> Option<String> {
  let body: serde_json::Value =
    reqwest::get(
      format!("http://geoip-service:8000/{ip}"))
        .await
        .ok()?
        .json()
        .await
        .ok()?;

  body.pointer("/names/en").and_then(|t|
    t.as_str()
  ).map(|t| t.to_string())
}
```

```sql
create view cities as
select get_city(logs.ip) as city
from logs;

SELECT * FROM (
  SELECT *, ROW_NUMBER() OVER (
    PARTITION BY window
    ORDER BY count DESC) as row_num
  FROM (SELECT count(*) as count,
    city,
    hop(interval '5 seconds', interval '15 minutes') as window
      FROM cities
      WHERE city IS NOT NULL
      group by city, window)) WHERE row_num <= 5;
```

- [Announcing Rust 1.75](https://blog.rust-lang.org/2023/12/28/Rust-1.75.0.html)
  - [Announcing `async fn` and return-position `impl Trait` in traits](https://blog.rust-lang.org/2023/12/21/async-fn-rpit-in-traits.html)
  - 终于可以切换回 `stable` 了!

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
