---
title: 码农碎碎念
description: 寻芳不觉醉流霞, 倚树沉眠日已斜. 客散酒醒深夜后, 更持红烛赏残花.
date: 2025-02-02
---

## 2026

- [Go 1.26 is released](https://go.dev/doc/go1.26)
  - 其实, 最受益的改进是: `go fix`

```go
x := int64(300)
ptr := &x

// Can be simplified to:

ptr := new(int64(300))
```

## 2025

### Posts, Events

- 2025-12-12, Rust is now an official language in the Linux Kernel
  - https://github.com/torvalds/linux
  - 2025-12-12: C `98.0%`, Rust `0.3%`

- 做个短暂的观察, Go vs Java (Kotlin),
  选择一些新项目, 同时有 Go and Java (Kotlin) 的版本
  - [Agent Development Kit for Go](https://github.com/google/adk-go)
  - [Agent Development Kit for TypeScript](https://github.com/google/adk-js)
  - [Agent Development Kit for Java](https://github.com/google/adk-java)
  - [MCP Go SDK](https://github.com/modelcontextprotocol/go-sdk)
  - [MCP Java SDK](https://github.com/modelcontextprotocol/java-sdk)
  - [MCP Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

- [From BI to AI: A Modern Lakehouse Stack with Lance and Iceberg](https://lancedb.com/blog/from-bi-to-ai-lance-and-iceberg/)

```
Iceberg operates at two of the layers in the stack:
the table format and the catalog spec.
It typically uses Parquet as the underlying file format.

Lance spans three layers of the stack, because it's
simultaneously a file format, table format and a catalog spec.
```

```
Lance's file format makes it more convenient to maintain
multimodal data natively as blobs inside the columns,
with no external lookups (the multimodal data is co-located
with metadata and embeddings), thus simplifying governance
and management of data that's multimodal in nature.

It's also significantly more performant, because at the
table level, Lance can pack multiple smaller rows together
while storing very large rows (e.g., image or audio blobs)
in a dedicated file thanks to its fragment-based design,
thus balancing performance with storage size.
```

```
In Iceberg, data evolution comes with a non-trivial cost:
adding data to a new column requires a full table rewrite
since Parquet stores entire row groups together.
This means that for very large tables, it's common to see
multiple new feature columns being added in parallel by
multiple teams in an organization, which would require a
table lock as new columns are being added, bottlenecking
the feature engineering process.

In Lance, adding a new column is essentially a
zero-copy operation. Lance's fragment design allows
independent column files per fragment
(though multiple columns can share a data file),
meaning that adding or updating a column simply appends
new column files without touching existing data.
```

- [Arroyo is joining Cloudflare](https://www.arroyo.dev/blog/arroyo-is-joining-cloudflare/)

- [Abandonware of the web: do you know that there is an HTML tables API?](https://christianheilmann.com/2025/10/08/abandonware-of-the-web-do-you-know-that-there-is-an-html-tables-api/)

```js
let b = document.body
let t = document.createElement('table')
b.appendChild(t)
let table = [
  ['one','two','three'],
  ['four','five','six']
]
let c
let r
table.forEach((row,ri) => {
  let r = t.insertRow(ri)
  row.forEach((l,i) => {
    c = r.insertCell(i)
    c.innerText = l
  })
})
```

- [The Green Tea Garbage Collector](https://go.dev/blog/greenteagc)

- 2025-09, 从
  [Warp](https://www.warp.dev)
  迁移到了
  [Ghostty](https://ghostty.org)
  - [Ghostty code](https://github.com/ghostty-org/ghostty)

- [Rust 1.88](https://blog.rust-lang.org/2025/06/26/Rust-1.88.0/)

```rust
if let Channel::Stable(v) = release_info()
  && let Semver { major, minor, .. } = v
  && major == 1
  && minor == 88
{
  println!("`let_chains` was stabilized in this version");
}
```

- [PEP 750 - Template Strings](https://peps.python.org/pep-0750/)

```py
name = "World"
tmpl = t"Hello {name}"
assert tmpl.strings[0] == "Hello "
assert tmpl.interpolations[0].value == "World"
assert tmpl.interpolations[0].expression == "name"

tmpl = t"Hello {name!r}"
assert tmpl.interpolations[0].conversion == "r"

val = 42
tmpl = t"Value: {val:.2f}"
assert tmpl.interpolations[0].format_spec == ".2f"
```

- [Rust 1.85 and Rust 2024](https://blog.rust-lang.org/2025/02/20/Rust-1.85.0/)

```rust
let mut vec: Vec<String> = vec![];

let closure = async || {
  vec.push(ready(String::from("")).await);
};
```

---

- __数学的碎碎念__: 2025-02-10 凌晨, 洗澡的时候想出来的.
  - 如何通过一道简单的题目, 测试数学的思维水平?
    洗澡的时候编了一道.
  - 设一个矩阵 A, 输入向量 x, 输出向量 y, 则 y = Ax.
  - 问题: 1 给出一个矩阵倒数的定义; (此处可以提示: 取欧式距离)
    2 进一步, 分别定义: 全导数, 偏导数, 方向导数;
    3 再进一步, 给出积分的定义. (此处可提示: 沿某一曲线)
  - 缘起: 之所以有这个念头: 测试数学的思维水平.
    是因为看书临时去回顾了下一些群论的一些概念,
    想起几年前, 自己对于陪集, 正规子群, 商群等概念, 其实不是自然接纳的.
    但是现在, 基本也能自然的顺着思路独自给出来.
    并且过去并没有再次系统的看过群论的书籍资料, 仅仅偶尔接触到.

### 视频

- [But how do AI videos actually work? | Guest video](https://www.youtube.com/watch?v=iv-5mZ_9CPY)
  - 动画很棒~
  - CLIP (2021)
    (C: contrastive, L: language, I: image, P: pre-training);
  - DDPM (2020)
    (D: denoising, D: diffusion, P: probabilistic M: models);

- [But what is quantum computing? (Grover's Algorithm)](https://www.youtube.com/watch?v=RQWpF2Gb-gU)
  - 关于量子计算: 内容是极简的, 避开了量子的基本理论, 只做简单的数学表述.
  - 关于 Grover's Algorithm, 其实主要是形象比喻~
  - BTW, 依稀记得微信的信息流看到过一篇文章标题:
    为什么 3blue1brown 给了你在学习数学的错觉?
    (大概是类似的标题, 但是我没点击阅读那篇文章~)
  - [Where my explanation of Grover's algorithm failed](https://www.youtube.com/watch?v=Dlsa9EBKDGI)
  - 补充视频稍微细致了一点~

- [Terence Tao on how we measure the cosmos (part 1)](https://www.youtube.com/watch?v=YdOXS_9_P4U)
  - Part 1, 访谈的形式不错, 但是内容一般~
    亮点部分是开普勒如何根据大量数据得出开普勒定律!
  - [The cosmic distance ladder with Terence Tao (part 2)](https://www.youtube.com/watch?v=hFMaT9oRbs4)
  - Part 2, 一般
