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
