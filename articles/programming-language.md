---
title: (2021) Programming language
description: 青山相待, 白云相爱, 紫罗袍共黄金带
date: 2020-12-27
---

* Rust 会单独作为一篇 文章
* 此文章 Archived
  - 才学不足, 无法诸多语言融会贯通
  - 杂放在一起只会毫无重点
* 未来数年, Rust 足矣!
* 做一个预测: TIOBE 2021 年度语言 **Rust**

## Rust

* 减少内存分配和拷贝
  - zero-copy [rkyv](https://github.com/djkoloski/rkyv)

------------------

# Timeline

------------------

## 2021

### Events

* [Rust in the Android platform (2021-04-06)](https://security.googleblog.com/2021/04/rust-in-android-platform.html)

* [My Crates Account](https://crates.io/users/haoxins)

* 正式开始把玩 **Rust**

```
编程语言同样是:
由俭入奢易, 由奢入俭难
奢俭指的是: 优秀的语言特性
最近开始把玩 Rust
无他, 喜欢, 好玩罢了

BTW: 讨厌分号!
```

* [Announcing Rust 1.50](https://blog.rust-lang.org/2021/02/11/Rust-1.50.0.html)

* [Mozilla Welcomes the Rust Foundation](https://blog.mozilla.org/blog/2021/02/08/mozilla-welcomes-the-rust-foundation/)
  - [Hello World!](https://foundation.rust-lang.org/posts/2021-02-08-hello-world/)

```
The board of directors is composed of 5 directors
from our Founding member companies,
AWS, Huawei, Google, Microsoft, and Mozilla,
as well as 5 directors from project leadership,
2 representing the Core Team,
as well as 3 project areas:
Reliability, Quality, and Collaboration.
```

* [The Go Blog - A Proposal for Adding Generics to Go](https://blog.golang.org/generics-proposal)

* `已经过时` Reddit 关于 Rust Async 的讨论
  - [Diagram of Async Architectures](https://www.reddit.com/r/rust/comments/jpcv2s/diagram_of_async_architectures/)
  - [smol vs tokio vs async-std;](https://www.reddit.com/r/rust/comments/i5hppj/smol_vs_tokio_vs_asyncstd/)

### Rust

* 分号

```
Almost everything in Rust is an expression.
An expression is something that returns a value.
A semicolon after an expression changes the type of the expression to ().
Aka turning an expression into a statement.
```

* `Option` & `Result`
  - Result, Either

* Future

```
Rust 一个 Future 只有被主动 poll（await）才会得到执行
JavaScript 一个 Promise 一旦生成, 就会放入 event loop 里等待执行
```

* Traits
  - Ord: Trait for types that form a [total order](https://en.wikipedia.org/wiki/Total_order)
  - PartialOrd: Trait for values that can be compared for a sort-order
  - Eq: Trait for equality comparisons which are [equivalence relations](https://en.wikipedia.org/wiki/Equivalence_relation)
  - PartialEq : Trait for equality comparisons which are [partial equivalence relations](https://en.wikipedia.org/wiki/Partial_equivalence_relation)

* [Crust of Rust: Atomics and Memory Ordering](https://www.youtube.com/watch?v=rMGWeSjctlY)

* Rust vs Java

```rust
let x = 5;
let mut y = 5;
```

```java
final String key = "ABC";
```

```
Immutable first

不仅仅是语法的问题
也是理念传达的问题

将良好的编程习惯融入语法设计
将诸多的语法特性融合却不显冲突

妙
```

### Kotlin

|         |  let  |  run  | apply | also | with |
| ------- |:-----:|:-----:|:-----:|:----:|:----:|
| this/it |  it   | this  |  this |  it  | this |
| return  |  yes  | yes   |  no   |  no  | yes  |

### Java

* Records

```java
record Rational(int num, int denom) {
  Rational {
    int gcd = gcd(num, denom);
    num /= gcd;
    denom /= gcd;
  }
}
```
