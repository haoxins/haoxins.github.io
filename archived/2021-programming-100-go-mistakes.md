---
title: 100 Go Mistakes, How to Avoid Them
description: 但将酩酊酬佳节, 不用登临恨落晖. 古往今来只如此, 牛山何必独沾衣.
date: 2021-09-12
---

* [100 Go Mistakes: How to Avoid Them](https://www.manning.com/books/100-go-mistakes-and-how-to-avoid-them)

## Go: Simple to Learn but Hard to Master

* Go implements the **CSP model** with
  two primitives: the **goroutine**
  and the **channel**.

* When to use `interfaces`?
* When to use `value` or `pointer` receivers?
* How to deal efficiently with `slices`?
* How to handle `error` management
  cleanly and expressively?
* How to avoid `memory leaks`?

## Code and Project Organization

* In the following example, we will see
  an unintended side effect because of
  a **shadowed variable**.

```go
var client *http.Client

if tracing {
  client, err := createClientWithTracing()
  if err != nil {
    return err
  }
  log.Println(client)
} else {
  client, err := createDefaultClient()
  if err != nil {
    return err
  }
  log.Println(client)
}
// Use client

// This code compiles because the
// inner client variables are used
// in the logging calls.
```

* As a result, following this example,
  the HTTP client will always be `nil`.

* An `init function` is a function taking
  *no arguments* and returning *no result*
  (a `func()` function).
* When a package is *initialized*, all the
  constants and variables declarations in the
  package are evaluated. Then, the `init`
  functions are executed.
* In this case, the execution order of the
  `init function` inside *a package* is based
  on the source files' alphabetical order.
* We **shouldn't** rely on the ordering of
  `init` functions within a package. Indeed,
  it can be dangerous as source files can be
  renamed, potentially impacting
  the execution order.
* Another aspect of an `init` function is
  that it *can't be invoked directly*.

* When to use init functions?
  - First, *error management* in an `init`
    function is somewhat limited.
  - Another important downside is related
    to `testing`. If we add tests to this file,
    the `init` function will be executed *before*
    running the test cases, which isn't
    necessarily what we want.

* **Interface pollution** is about overwhelming
  our code with unnecessary abstractions making
  it harder to understand and evolve.
* What makes Go interfaces so different is that
  they are satisfied implicitly. There is no
  explicit keyword like `implements` for example,
  to mark that an `object X implements interface Y`.
* **The bigger the interface**,
  **the weaker the abstraction**.
* An *interface name* should *describe a behavior*,
  *not a state*. Hence, in general, it should be
  a **verb**, **not** a **noun**.
* The interfaces allow us to create abstractions,
  and **abstractions should be discovered**,
  **not created**.

* **Don't design with interfaces, discover them.**
  - ***Rob Pike***

* Be conservative in what you do, be liberal
  in what you accept from others.
* If we apply this idiom to Go, it means
  **returning structs** instead of interfaces.
  Meanwhile, it also means **accepting interfaces**
  whenever possible.
  - Of course, there are some exceptions.
* `interface{}` says nothing

* [Standard Go Project Layout](https://github.com/golang-standards/project-layout)

## Data Types

* In Go, we must know that an integer
  *starting with* `0` is considered an
  *octal integer* (`base 8`).

* If we want to match the Linux permissions,
  we can pass an octal number for readability
  instead of a base 10 number:
  - Using `0o` instead of only `0`
    doesn't change anything.

```go
file, err := os.OpenFile("foo", os.O_RDONLY, 0644)
```

* **Binary**: `0b` or `0B` prefix.
  - For example, `0b100` is equal to `4` in base `10`.
* **Hexadecimal**: `0x` or `0X` prefix.
  - For example, `0xF` is equal to `15` in base `10`.
* **Imaginary**: `i` suffix.
  - For example, `3i`.

* We can also use an *underscore* character
  as a separator. For example, we can write
  `1 billion` this way: `1_000_000_000`.

* A `slice` is backed by an `array` in Go,
  meaning the slice's data are stored in an array.
  A slice structure also handles the logic of
  adding an element if the backing array is
  full or how to shrink the backing array
  if it's almost empty.
* Furthermore, a `slice` holds a `pointer` towards
  the backing array plus a *length* and a *capacity*.
  - The `length` is the number of elements the
    slice contains,
  - whereas the `capacity` is the number of
    elements in the backing array.
* In Go, a `slice` grows by *doubling* until
  it contains `1024` elements, after which it
  grows by `25%` each time.
* To summarize, the slice length is the number of
  available elements in the slice, whereas the
  slice capacity is the number of elements
  in the backing array. Adding an element to a
  full slice (`length == capacity`) leads to
  creating a new backing array with a new capacity,
  copying all the elements from the previous array,
  and updating the slice pointer to the new array.

* We have also seen that slicing an existing slice
  will create another slice, and the
  same array will back both.
* Therefore, updating an element on one slice
  using an index (e.g., `s1[1] = 10`) will also
  be visible on the other slice if this index is
  within the length range of both slices.

```go
s1 := []int{1, 2, 3}
s2 := s1[1:2]
s3 := append(s2, 10)
// s1: [1 2 10]
// s2: [2]
// s3: [2 10]
```

* `s1` is a `3-length`, `3-capacity` slice,
  while `s2` is a `1-length`, `2-capacity` slice,
  both backed by the **same array**.
* Adding an element using `append` checks whether
  the slice is full:
  - the slice length is equal to the slice capacity.
* If `not`, the `append` function will add
  the element by updating the backing array and
  returning a slice having a length
  incremented by one.

* **full slice expression**: `s[low:high:max]`
  - it creates a similar slice to one created with
    `s[low:high]` except that the resulting slice's
    `capacity` will *be equal to* `max - low`.

* We have to keep in mind that we can have
  conflicts between two slices if one was created
  from slicing the other.
* Conflicts can occur while modifying an element
  directly or even when using `append`.
* If we want to restrict the range of potential
  *side-effects* of a caller, we can use the
  **full slice expression**.
  - It's the most efficient solution as it
    doesn't require any additional `copy` step.

```go
src := []int{0, 1, 2}
var dst []int
copy(dst, src)
fmt.Println(dst) // []
```

* To use `copy` effectively, it's important to
  understand that the *number of elements copied*
  to the *destination* slice corresponds to the
  `minimum` between the *source slice's length*
  and the *destination slice's length*.
* In the previous example, `src` is a `3-length`
  slice but `dst` is a `0-length-slice`. Therefore,
  `copy` will *copy* the `minimum` between `3` and `0`:
  - `0` element. It's the reason why
    the slice was **empty**.
* If we want to perform a **complete copy**, the
  destination slice must have a length
  greater or equal to the source slice's length:

```go
src := []int{0, 1, 2}
dst := make([]int, len(src))
copy(dst, src)
fmt.Println(dst) // [0 1 2]
```

```go
src := []int{0, 1, 2}
dst := append([]int(nil), src...)
fmt.Println(dst) // [0 1 2]
```

* As a rule of thumb, we have to bear in mind
  that *slicing an existing slice or array*
  may potentially create a slice with a large
  backing array leading to a potential high
  memory consumption in our applications.
* Using **slice copy** allows us to restrict
  the memory consumed by slices.

```go
var s []string
fmt.Printf("1: nil = %t, len = %d, cap = %d\n", s == nil, len(s), cap(s))
s = []string{}
fmt.Printf("2: nil = %t, len = %d, cap = %d\n", s == nil, len(s), cap(s))
s = make([]string, 0)
fmt.Printf("3: nil = %t, len = %d, cap = %d\n", s == nil, len(s), cap(s))
// 1: nil = true, len = 0, cap = 0
// 2: nil = false, len = 0, cap = 0
// 3: nil = false, len = 0, cap = 0
```

