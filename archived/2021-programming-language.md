---
title: (2021) Programming language
description: 青山相待, 白云相爱, 紫罗袍共黄金带
date: 2020-12-27
---

* **Rust** 会单独作为一篇文章
* 此文章 **归档**
  - 才学不足, 无法诸多语言融会贯通
  - 多个语言放在一起只会杂乱无章
* 未来数年, **Rust** 足矣!
* 做一个预测: `TIOBE 2021 年度语言` **Rust**

## Rust

* 减少内存分配和拷贝
  - zero-copy [rkyv](https://github.com/djkoloski/rkyv)

### Kotlin

* 期待 Kotlin 尽早放弃:
  - Web Frontend
  - Multiplatform Mobile
  - 更别提 Data Science
  - 踏踏实实做好 Server-side, Android
  - By haoxin, 2021-07-09

------------------

# Timeline

------------------

## 2021

### Events

* [PEP 621: Storing project metadata in pyproject.toml](https://www.python.org/dev/peps/pep-0621/)
  - `pyproject.toml`

* Kotlin 逐渐废弃了一些子项目, 好事!
  - 还需要更加 `Focus`, 缩小 `Scope`

* [Kotlin Coroutines 1.5: GlobalScope Marked as Delicate, Refined Channels API, and More](https://blog.jetbrains.com/kotlin/2021/05/kotlin-coroutines-1-5-0-released/)

```
While the use of GlobalScope isn't recommended for most cases

In many cases, the use of GlobalScope should be avoided and the
containing operation should be marked with suspend

Version 1.5 of Kotlin Coroutines promotes most of the functions
responsible for integrations with reactive frameworks to stable API.
```

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
Rust 一个 Future 只有被主动 poll (await) 才会得到执行
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

* Coroutine

```kotlin
fun main() = runBlocking {
  launch {
    delay(200L)
    println("Task from runBlocking")
  }

  coroutineScope {
    launch {
      delay(500L)
      println("Task from nested launch")
    }

    delay(100L)
    println("Task from coroutine scope")
  }

  println("Coroutine scope is over")
}

// Task from coroutine scope
// Task from runBlocking
// Task from nested launch
// Coroutine scope is over
```

```kotlin
val job = launch {
  try {
    repeat(1000) { i ->
      println("job: I'm sleeping $i ...")
      delay(500L)
    }
  } finally {
    withContext(NonCancellable) {
      println("job: I'm running finally")
      delay(1000L)
      println("job: And I've just delayed for 1 sec because I'm non-cancellable")
    }
  }
}
delay(1300L)
println("main: I'm tired of waiting!")
job.cancelAndJoin()
println("main: Now I can quit.")

// job: I'm sleeping 0 ...
// job: I'm sleeping 1 ...
// job: I'm sleeping 2 ...
// main: I'm tired of waiting!
// job: I'm running finally
// job: And I've just delayed for 1 sec because I'm non-cancellable
// main: Now I can quit.
```

```kotlin
GlobalScope.launch {
  // ...
}

// equals

launch(Dispatchers.Default) {
  // ...
}
```

* **Flow**

```kotlin
fun simple(): Flow<Int> = flow {
  emit(1)
  throw RuntimeException()
}

fun main() = runBlocking<Unit> {
  simple()
    .onCompletion { cause -> if (cause != null) println("Flow completed exceptionally") }
    .catch { cause -> println("Caught exception") }
    .collect { value -> println(value) }
}

// 1
// Flow completed exceptionally
// Caught exception
```

```kotlin
fun simple(): Flow<Int> = (1..3).asFlow()

fun main() = runBlocking<Unit> {
  simple()
    .onCompletion { cause -> println("Flow completed with $cause") }
    .collect { value ->
      check(value <= 1) { "Collected $value" }
      println(value)
    }
}

// 1
// Flow completed with java.lang.IllegalStateException: Collected 2
// Exception in thread "main" java.lang.IllegalStateException: Collected 2
```

```kotlin
fun events(): Flow<Int> = (1..3).asFlow().onEach { delay(100) }

fun main() = runBlocking<Unit> {
  events()
    .onEach { event -> println("Event: $event") }
    .collect()
  println("Done")
}

// Event: 1
// Event: 2
// Event: 3
// Done

fun main() = runBlocking<Unit> {
  events()
    .onEach { event -> println("Event: $event") }
    .launchIn(this)
  println("Done")
}

// Done
// Event: 1
// Event: 2
// Event: 3
```

* **Channel**

```kotlin
val channel = Channel<Int>()
launch {
  for (x in 1..5) channel.send(x * x)
}
repeat(5) { println(channel.receive()) }
println("Done!")

// 1
// 4
// 9
// 16
// 25
// Done!

launch {
  for (x in 1..5) channel.send(x * x)
  channel.close()
}
for (y in channel) println(y)
println("Done!")
```

```kotlin
fun CoroutineScope.produceNumbers() = produce<Int> {
  var x = 1
  while (true) send(x++)
}

fun CoroutineScope.square(numbers: ReceiveChannel<Int>): ReceiveChannel<Int> = produce {
  for (x in numbers) send(x * x)
}

val numbers = produceNumbers()
val squares = square(numbers)
repeat(5) {
  println(squares.receive())
}
println("Done!")
coroutineContext.cancelChildren()

// 1
// 4
// 9
// 16
// 25
// Done!
```

* **Supervisor**

* **Actor**

* **Select**

> **Golang** + **Elixir (Erlang)**

### Python

* Global Interpreter Lock, GIL

```
An older way of marking a function as a coroutine
is to decorate a normal def function with
@asyncio.coroutine.

The result is a generator-based coroutine.

Support for generator-based coroutines is deprecated
and is scheduled for removal in Python 3.10.

Generator-based coroutines predate async/await syntax.
They are Python generators that use yield from expressions
to await on Futures and other coroutines.

However, async IO is not threading,
nor is it multiprocessing.

In fact, async IO is a single-threaded,
single-process design.
```

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
