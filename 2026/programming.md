---
title: 码农碎碎念
description: 又闻子规啼夜月, 愁空山. 蜀道之难, 难于上青天! 使人听此凋朱颜.
date: 2026-02-25
---


#### Daft and Lance

- [Daft](https://github.com/eventual-inc/daft)
  - [Lance](https://github.com/lance-format/lance)
  - [Ray](https://github.com/ray-project/ray)

> 何时可以不再依赖 Ray?

> 2026 年初, 开始使用 Databricks, 体验不好!

#### 温州 苍南 168 黄金海岸线

- 五一假期之后, 高铁到温州南站, 办好租车手续, 已经是下午两点多;
  沿途小雨, 先抵达岩家岙, 168 起始点,
  然后到龙台背, MOJ 咖啡喝了一杯咖啡;
  途经炎亭镇, 下车走了百米路, 就离开了.
  - 到霞关镇住宿, 透过窗户就看到停泊着一排船的码头;
    夜里顺着海岸边驱车行驶了一小段, 看见灯火通明的三澳核电站.

- 第二天早上十一点出发, 很快就经过渔寮, 月亮湾沙滩;
  无尽蓝咖啡, 视野很好, 咖啡店很有设计感~ 值得驻足!
  - 棕榈湾黑沙滩, 依稀几人, 浪起浪落, 颇有意境!
    景色视野也确实不错, 几乎是独享这一片鹅卵石沙滩!
  - 原计划是还去油罐咖啡和云台山的, 不去了,
    就静静的在这里看海, 听潮~
  - 什么是旅程的惬意收尾, 就是有个值得提前结束的地方!
    随着雨点渐起, 意犹未尽的离开~

#### Go: Type Construction and Cycle Detection

- [Type Construction and Cycle Detection](https://go.dev/blog/type-construction-and-cycle-detection)

```
The type checker constructs an internal representation
for each type it encounters while traversing the AST:
a process informally called type construction.
```

```
Type construction is naturally a depth-first process,
since completing a type requires its dependencies
to be completed first.
```

- Go's type system also allows us to express recursive types.

```go
type T []U
type U *T
```

```
Recall that type completeness is a prerequisite
for deconstructing a type. In this case,
type construction never deconstructs a type,
it merely refers to types. In other words,
type completeness does not block type construction here.

Because type construction isn't blocked, the type checker
can simply delay such checks until the end of type checking,
when all types are complete (note that the checks
themselves also do not block type construction).
If a type were to reveal a type error,
it makes no difference when that error is reported
during type checking, only that it is reported eventually.
```

- Now, how does cycle detection work for type
  `T [unsafe.Sizeof(T{})]int`? To answer this,
  let's look at the inner `T{}`. Because `T{}`
  is a composite literal expression, the type
  checker knows that its resulting value is of
  type `T`. Because `T` is incomplete, we call
  the value `T{}` an incomplete value.
  - We must be cautious: operating on an incomplete
    value is only sound if it doesn't deconstruct
    the value's type.
  - For example, type `T [unsafe.Sizeof(new(T))]int`
    is sound, since the value `new(T)` (of type `*T`)
    is never deconstructed, all pointers have the
    same size. To reiterate, it is sound to size
    an incomplete value of type `*T`,
    but not one of type `T`.
  - This is because the "pointerness" of `*T` provides
    enough type information for `unsafe.Sizeof`,
    whereas just `T` does not. In fact, it's never
    sound to operate on an incomplete value whose
    type is a defined type, because a mere type name
    conveys no (underlying) type information at all.

```
Instead of returning an incomplete value,
we return a special invalid operand, which signals
that the call expression could not be evaluated.
The rest of the type checker has special
handling for invalid operands.
```

#### IBM completed its acquisition of Confluent

> 2026 年 3 月, 官宣

- 看来, 下面两个终于可以只留一个了
  - [IBM/sarama](https://github.com/IBM/sarama)
  - [confluentinc/confluent-kafka-go](https://github.com/confluentinc/confluent-kafka-go)

#### Go: Allocating on the Stack

- [Allocating on the Stack](https://go.dev/blog/allocation-optimizations)

```
We generally double the size of the allocation
each time it fills up, so we can eventually append
most new tasks to the slice without allocation.
But there is a fair amount of overhead in the
"startup" phase when the slice is small.
During this startup phase we spend a lot of time
in the allocator, and produce a bunch of garbage,
which seems pretty wasteful.
```

```go
func process4(c chan task, lengthGuess int) {
    var tasks []task
    if lengthGuess <= 10 {
        tasks = make([]task, 0, 10)
    } else {
        tasks = make([]task, 0, lengthGuess)
    }
    for t := range c {
        tasks = append(tasks, t)
    }
    processAll(tasks)
}
```

- Kind of ugly, but it would work. When the guess is small,
  you use a constant size make and thus a `stack-allocated`
  backing store, and when the guess is larger you use a variable
  size make and allocate the backing store from the heap.
  - But in Go 1.25, you don't need to head down this ugly road.
    The Go 1.25 compiler does this transformation for you!

- Ok, but you still don't want to have to change your API
  to add this weird length guess. Anything else you could do?
  - Upgrade to Go 1.26!

```go
func process(c chan task) {
    var tasks []task
    for t := range c {
        tasks = append(tasks, t)
    }
    processAll(tasks)
}
```

- In Go 1.26, we allocate the same kind of small,
  speculative backing store on the stack,
  __but now we can use it directly at the append site__.

- For escaping slices, the compiler will transform
  the original `extract` code to something like this:

```go
func extract3(c chan task) []task {
    var tasks []task
    for t := range c {
        tasks = append(tasks, t)
    }
    tasks = runtime.move2heap(tasks)
    return tasks
}
```

- `runtime.move2heap` is a special `compiler+runtime`
  function that is the identity function for slices
  that are already allocated in the heap.
  - For slices that are on the stack,
    it allocates a new slice on the heap,
    copies the `stack-allocated` slice to the heap copy,
    and returns the heap copy.
