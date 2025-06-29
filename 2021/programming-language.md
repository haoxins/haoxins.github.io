---
title: Programming language
description: 一曲新词酒一杯, 去年天气旧亭台. 夕阳西下几时回?
date: 2020-12-27
---

* Blockchain
  - Rust
  - Go
* Data, ML
  - Python
  - Rust
* K8s
  - Go
* Serverless
  - Python
  - Go

### Rust

* [axum](https://github.com/tokio-rs/axum)
  - axum is a web application framework that focuses on ergonomics and modularity.
  - Tokio 团队 2021 新作!

* [Rocket](https://github.com/SergioBenitez/Rocket)
  - 2022, 能否主流?
  - 嗯, 比 [Gin](https://github.com/gin-gonic/gin) 好太多
  - 比 Spring boot 差太远 :)

* [rkyv](https://github.com/djkoloski/rkyv)
  - zero-copy
  - 减少内存分配和拷贝

### Go

> * [Gin](https://github.com/gin-gonic/gin)
>   - Go 社区终于有了真正的主流 `Web Framework`
>   - 何谓主流? 即: 新人可以不纠结, 轻易地选择!
>   - 当然, 矮子里面拔将军, 还是比较简陋~
>   - 不喜欢, 不推荐

### Python

* [pydantic](https://github.com/samuelcolvin/pydantic)
  - Data parsing and validation using Python type hints

### Kotlin

* 期待 Kotlin 尽早放弃:
  - Web Frontend
  - Multiplatform Mobile
  - 更别提 Data Science
  - 踏踏实实做好 Server-side, Android
  - By haoxin, 2021-07-09

### 留个纪念, Stackoverflow survey 2021

* 2021-08

* [Most popular](https://insights.stackoverflow.com/survey/2021#section-most-popular-technologies-programming-scripting-and-markup-languages)
  - Programming, Scripting, and Markup languages
  - Remove the Shell and Markup languages
  - Merge some languages

```
1. JavaScript/TypeScript
2. Python
3. Java
4. C#
5. C/C++
6. Go
7. Kotlin
8. Rust
```

* [Most loved, dreaded, and wanted](https://insights.stackoverflow.com/survey/2021#section-most-loved-dreaded-and-wanted-programming-scripting-and-markup-languages)

* Loved vs. Dreaded

```
1. Rust
```

* Want

```
1. Python
2. TypeScript/JavaScript
3. Go
4. Rust
```

------------------

# Timeline

------------------

## 2021

### Events

* [Twelve Years of Go](https://go.dev/blog/12years)
  - https://go.dev
  - Officially proposed adding **generics** to Go (`1.18`)
  - **Generics** will be one of our focuses for `2022`.
    The initial release in Go `1.18` is only the
    beginning. We need to spend time using generics and
    learning what works and what doesn't, so that we can
    write *best practices* and decide what should be
    added to the standard library and other libraries.
  - We expect that Go `1.19` (expected in **August 2022**)
    and later releases will further refine the design
    and implementation of generics as well as
    integrating them further into the
    overall Go experience.

* [What's New In Python 3.10](https://docs.python.org/3/whatsnew/3.10.html)
  - **Structural Pattern Matching**
  - Parenthesized context managers

* [Announcing Rust 1.56.0 and Rust 2021](https://blog.rust-lang.org/2021/10/21/Rust-1.56.0/)
  - **Rust 2021**

* [Go 1.17 is released](https://blog.golang.org/go1.17)
  - [Go 1.17 Release Notes](https://golang.org/doc/go1.17)
  - *16 August 2021*
  - Pruned module graphs in go *1.17* modules
  - **`go mod tidy -go=1.17`**

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

* [Announcing Rust 1.50](https://blog.rust-lang.org/2021/02/11/Rust-1.50.0/)

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

### Go

* [Effective Go](https://golang.org/doc/effective_go)

* **new** vs **make**

```
Let's talk about new first.

It's a built-in function that allocates memory,
but unlike its namesakes in some other languages
it does not initialize the memory,
it only zeros it.

That is, new(T) allocates zeroed storage for
a new item of type T and returns its address,
a value of type *T.

In Go terminology, it returns a pointer to
a newly allocated zero value of type T.

The built-in function make(T, args) serves
a purpose different from new(T).

It creates slices, maps, and channels only,
and it returns an initialized (not zeroed)
value of type T (not *T).

The reason for the distinction is that
these three types represent, under the covers,
references to data structures that
must be initialized before use.

A slice, for example, is a three-item descriptor
containing a pointer to the data (inside an array),
the length, and the capacity,
and until those items are initialized, the slice is nil.
For slices, maps, and channels, make initializes
the internal data structure and prepares the value for use.

Remember that make applies only to maps, slices and channels
and does not return a pointer.
```

```go
// allocates slice structure; *p == nil; rarely useful
var p *[]int = new([]int)
// the slice v now refers to a new array of 100 ints
var v  []int = make([]int, 100)

// Unnecessarily complex:
var p *[]int = new([]int)
*p = make([]int, 100, 100)

// Idiomatic:
v := make([]int, 100)
```

* There are major differences between the ways **arrays** work in Go and C. In Go,
  - Arrays are values.
    Assigning one array to another copies all the elements.
  - In particular, if you pass an array to a function,
    it will receive a copy of the array, not a pointer to it.
  - The size of an array is part of its type.
    The types `[10]int` and `[20]int` are distinct.

```
Slices hold references to an underlying array,
and if you assign one slice to another,
both refer to the same array.

If a function takes a slice argument,
changes it makes to the elements of the slice will be visible to the caller,
analogous to passing a pointer to the underlying array.
A Read function can therefore accept a slice argument
rather than a pointer and a count;
the length within the slice sets an upper limit of how much data to read.
```

* **len** and **cap**

```
The length of a slice may be changed as long as
it still fits within the limits of the underlying array;
just assign it to a slice of itself.
The capacity of a slice, accessible by the built-in function cap,
reports the maximum length the slice may assume.
```

```go
// Allocate the top-level slice.
picture := make([][]uint8, YSize) // One row per unit of y.
// Loop over the rows, allocating the slice for each row.
for i := range picture {
  picture[i] = make([]uint8, XSize)
}
```

```go
// Allocate the top-level slice.
// One row per unit of y.
picture := make([][]uint8, YSize)
// Allocate one large slice to hold all the pixels.
// Has type []uint8 even though picture is [][]uint8.
pixels := make([]uint8, XSize*YSize)
// Loop over the rows,
// slicing each row from the front of the remaining pixels slice.
for i := range picture {
  picture[i], pixels = pixels[:XSize], pixels[XSize:]
}
```

```
An attempt to fetch a map value with a key that
is not present in the map will return the zero value
for the type of the entries in the map.

For instance, if the map contains integers,
looking up a non-existent key will return 0.

Sometimes you need to distinguish a missing entry from a zero value.
Is there an entry for "UTC" or is that 0
because it's not in the map at all?
You can discriminate with a form of multiple assignment.
```

```go
var seconds int
var ok bool
seconds, ok = timeZone[tz]
```

* **append**

```go
x := []int{1,2,3}
y := []int{4,5,6}
x = append(x, y...)
```

* **init function**

```
init is called after all the variable declarations
in the package have evaluated their initializers,
and those are evaluated only after
all the imported packages have been initialized.

Besides initializations that cannot be expressed as declarations,
a common use of init functions is to
verify or repair correctness of the program state
before real execution begins.
```

* **Interface checks**

```go
if _, ok := val.(json.Marshaler); ok {
  fmt.Printf("value %v of type %T implements json.Marshaler\n", val, val)
}
```

* **Embedding**

```go
type Reader interface {
  Read(p []byte) (n int, err error)
}

type Writer interface {
  Write(p []byte) (n int, err error)
}

// ReadWriter is the interface that
// combines the Reader and Writer interfaces.
type ReadWriter interface {
  Reader
  Writer
}

// ReadWriter stores pointers to a Reader and a Writer.
// It implements io.ReadWriter.
type ReadWriter struct {
  // *bufio.Reader
  *Reader
  // *bufio.Writer
  *Writer
}
```

* **Concurrency**

* **Communicating Sequential Processes (CSP)**

```
Go encourages a different approach in which shared values
are passed around on channels and, in fact,
never actively shared by separate threads of execution.

Only one goroutine has access to the value at any given time.

Data races cannot occur, by design.
To encourage this way of thinking we have reduced it to a slogan:

Do not communicate by sharing memory;
instead, share memory by communicating.
```

```
A goroutine has a simple model:
it is a function executing concurrently
with other goroutines in the same address space.
```

* **Channels**

```
If an optional integer parameter is provided,
it sets the buffer size for the channel.
The default is zero, for an unbuffered or synchronous channel.
```

```
Unbuffered channels combine communication
"the exchange of a value"
with synchronization-guaranteeing that two
calculations (goroutines) are in a known state.
```

```
If the channel is unbuffered,
the sender blocks until the receiver has received the value.

If the channel has a buffer,
the sender blocks only until the value has been copied to the buffer;

if the buffer is full,
this means waiting until some receiver has retrieved a value.
```

```go
var sem = make(chan int, MaxOutstanding)

func handle(r *Request) {
  sem <- 1    // Wait for active queue to drain.
  process(r)  // May take a long time.
  <-sem       // Done; enable next request to run.
}

// Once MaxOutstanding handlers are executing process,
// any more will block trying to send
// into the filled channel buffer,
// until one of the existing handlers
// finishes and receives from the buffer.

// v1
func Serve(queue chan *Request) {
  for req := range queue {
    sem <- 1
    go func(req *Request) {
      process(req)
      <-sem
    }(req)
  }
}

// v2
func Serve(queue chan *Request) {
  for req := range queue {
    // Create new instance of req for the goroutine.
    req := req
    sem <- 1
    go func() {
      process(req)
      <-sem
    }()
  }
}
```

* **Parallelization**

```
Although the concurrency features of Go can make
some problems easy to structure as parallel computations,
Go is a concurrent language, not a parallel one,
and not all parallelization problems fit Go's model.
```

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

```kt
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

```kt
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

```kt
GlobalScope.launch {
  // ...
}

// equals

launch(Dispatchers.Default) {
  // ...
}
```

* **Flow**

```kt
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

```kt
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

```kt
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

```kt
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

```kt
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

* **Supervisor**, **Actor**, **Select**

> **Golang** + **Elixir (Erlang)**

### Python

```
列表推导, 生成器表达式, 以及同它们很相似的
集合 (set) 推导 和 字典 (dict) 推导,
都有自己的局部作用域.

filter 和 map 合起来能做的事情, 列表推导也可以做,
而且还不需要借助难以阅读的 lambda 表达式.

生成器表达式的语法跟列表推导差不多,
只不过把方括号换成圆括号而已.
```

* **dataclass**

```py
from dataclasses import dataclass

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
```

* Global Interpreter Lock, **GIL**
  - Python 标准库中的所有*阻塞型I/O函数*都会释放 `GIL`,
    允许其他线程运行.
  - `time.sleep()` 函数也会释放 `GIL`.


* An older way of marking a function as a coroutine
  is to decorate a normal `def` function with
  `@asyncio.coroutine`. The result is a
  *generator-based* coroutine.
* Support for *generator-based* coroutines is
  **deprecated** and is scheduled for *removal* in
  Python `3.10`.
* *Generator-based coroutines* predate `async/await`
  syntax. They are Python generators that use
  `yield from` expressions to await on
  Futures and other coroutines.

* However, async IO is *not threading*,
  *nor* is it *multiprocessing*.
* In fact, async IO is a *single-threaded*,
  *single-process* design.

### Java

* `System.currentTimeMillis()` is **not monotonic**

* Text Blocks

```java
String query = """
               SELECT "EMP_ID", "LAST_NAME" FROM "EMPLOYEE_TB"
               WHERE "CITY" = 'INDIANAPOLIS'
               ORDER BY "EMP_ID", "LAST_NAME";
               """;
```

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

* Switch Expressions

```java
static void howMany(int k) {
  switch (k) {
    case 1  -> System.out.println("one");
    case 2  -> System.out.println("two");
    default -> System.out.println("many");
  }
}
```
