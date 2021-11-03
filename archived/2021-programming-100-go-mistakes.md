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

* A `nil` and `empty` slice, then we should favor
  option one: `var s []string`.
* A `non-nil` and `empty` slice, then we should favor
  option three: `s := make([]string, 0)`.
  - Using this option, we can later update the
    slice length and/or capacity if required,
    which is impossible with option two.
* Compared to an `empty` slice that might require
  an allocation event if its capacity is *zero*,
  a `nil` slice needs no allocation.
* A `nil` slice is *marshaled* as a `null` element,
  whereas an `empty` slice is *marshaled*
  as an `empty` array.

```go
func handleOperations(id string) {
  operations := getOperations(id)
  if len(operations) != 0 {
    handle(operations)
  }
}
```

* Here we didn't check whether a slice was `nil`.
  Instead, we checked if its `length`
  was equaled to `zero`.
* With this implementation, regardless of the
  slice is `nil` or *non-nil but empty*, checking
  the length will do the job. It's the best
  practice to follow, as we can't always control
  the approach taken by a function that we call.
* Also, as the Go Wiki states, when designing
  interfaces, we **should avoid distinguishing**
  `nil` and `empty` slices as it can lead to
  subtle programming errors. Hence, when returning
  slices, we should make neither a semantic nor
  a technical difference if we return
  a `nil` or an `empty` slice.

* This principle is the same with `maps`. To
  check if a map is empty, we should check
  its length, not whether it's nil.

* In Go, a `map` is based on the *hashtable*
  data structure. Internally, a hashtable is
  an array of buckets, each bucket being a
  pointer to an array of `key/value` pairs.
* In Go, each bucket has a fixed size of
  *eight elements*. If a bucket is full
  (known as bucket overflow), Go will create
  another bucket of *eight elements* and
  link it to the previous bucket.

* **A map doesn't** keep the data
  sorted by the key
* **A map doesn't** preserve the
  order the data were added in

* Reading, updating, inserting, or deleting
  a key is done by associating a key to a
  given bucket index.
* It's achieved by a hash function that assigns
  a key to a unique bucket. This function is stable
  as we want it to return the same bucket given
  the same key consistently.
* To prevent wasting memory due to allocation
  alignment, in-memory, Go doesn't store a
  sequence of key/values.
  - e.g., `key1-value1-key2-value2-key3-value3`
* Instead, all the keys are first stored
  contiguously, then all the values.
  - e.g., `key1-key2-key3-value1-value2-value3`
* Ideally, there is only one pair of `key/value`
  per bucket. If it's the case, each operation
  takes `O(1)`. However, it isn't always possible.
  Indeed, if applying the hashing function to two
  different keys return the same bucket index,
  it leads to a collision. In that case, both
  `key/value` pairs are stored in the same bucket

* In a similar manner as `slices`, a `map`
  grows by doubling its number of buckets.
  What are the conditions to
  trigger a map to grow?
  - Either if the average number of items
    in the buckets (called load factor) is
    greater than a constant. This constant is
    currently equal to 6.5, but this may change
    in future versions as it's an internal of Go.
  - Or if there are too many buckets that are
    overflowed (containing more than eight elements).
* When a map grows, all the keys have to be
  distributed again across all the buckets.
  - It's the reason why in the *worst-case* scenario,
    inserting a key can be an `O(n)` operation.

* We can use the `make` *built-in* function to
  provide an initial size while creating a map.

```go
m := make(map[string]int, 1_000_000)
```

* With a `map`, `make` can provide only an
  initial size, **not** a `capacity`
  as with slices.
* Also, specifying a size doesn't mean making
  a map with at most one million elements.
  We can still add more than one million elements.
* Specifying a size means asking the Go runtime
  to allocate a map with room for **at least**
  `x` elements, which is helpful if we
  already know the size upfront.
* Therefore, just like with slices, if we know
  upfront the number of elements a map will contain,
  we should create it by providing an initial size.
* By doing this, we avoid potential map growth,
  which is quite heavy computation-wise as it
  requires reallocating enough space and
  rebalancing all the pairs.
* When working with maps in Go, we have to know a
  noteworthy property:
  - the size of a map in memory can
    **only increase**, **never decrease**.

* It's essential to understand how to use
  `==` and `!=` to make comparisons effectively.
  We can use them on operands that are comparable:
  - *Booleans*: Compare whether two
    booleans are equals.
  - *Numerics* (`int`, `float`, and `complex` types):
    Compare whether two numerics are equals.
    It compiles if both values have the same
    type or can be converted to be of the same type
    (e.g., comparing a `float32` with a `float64` is
    accepted but not a `int64` with an `int`).
  - *Strings*: Compare whether two strings are equals.
  - *Channels*: Compare whether two channels were
    created by the same call to make or
    if both are `nil`.
  - *Interfaces*: Compare whether two interfaces
    have identical dynamic types and equal
    dynamic values or if both have value `nil`.
  - *Pointers*: Compare whether two pointers
    point to the same value in memory or
    if both are `nil`.
  - Structs and arrays if they are
    composed of *comparable types*

* The `reflect.DeepEqual` has specific behavior
  with the different types it accepts.
* However, there are **two things** to keep in
  mind while using `reflect.DeepEqual`.
  - The first one is that it makes the distinction
    between an `empty` and a `nil` collection.
  - The other catch is something pretty standard
    in most of the languages. As this function uses
    *reflection*, which will introspect at runtime
    the values to discover how they are formed,
    it has a performance penalty.

## Control Structures

* A `range` loop allows iterating over
  different data structures:
  - `String`
  - `Array`
  - `Pointer` to an array
  - `Slice`
  - `Map`
  - Receiving channel

* In general, `range` produces two values for
  each data structure except for a
  `receiving channel` that produces
  a single element.

```go
type account struct {
  balance float32
}

accounts := []account{
  {balance: 100.},
  {balance: 200.},
  {balance: 300.},
}

for _, a := range accounts {
  a.balance += 1000
}

fmt.Println(accounts) // [{100} {200} {300}]
```

* In Go, everything we *assign* is a **copy**.
  For example, if we assign the result
  of a function returning:
  - A `struct`, we will perform a
    *copy* of this struct
  - A `pointer`, we will perform a *copy*
    of this pointer (though both pointers
    reference the same object,
    it remains a pointer *copy*)
* Indeed, when a `range` loop iterates over
  a data structure, it performs a *copy* of
  each element to the value variable
  (the second item).

```go
type account struct {
  balance float32
}

accounts := []*account{
  {balance: 100.},
  {balance: 200.},
  {balance: 300.},
}

for _, a := range accounts {
  a.balance += 1000
}

for _, a := range accounts {
  fmt.Println(a)
}
// &{1100}
// &{1200}
// &{1300}
```

```go
s := []int{0, 1, 2}
for range s {
  s = append(s, 10)
}
fmt.Println(s) // [0 1 2 10 10 10]
```

* The expression passed to `range` is
  evaluated **only once**, before the
  beginning of the loop.
* In this context, evaluated means that
  the provided expression is copied to a
  temporary variable, and then the `range`
  operator will iterate over this variable,
  not the original one.

```go
s := []int{0, 1, 2}
for i := 0; i < len(s); i++ {
  s = append(s, 10)
}
fmt.Println("Never ends!!!")
```

```go
ch1 := make(chan int, 3)
go func() {
  ch1 <- 0
  ch1 <- 1
  ch1 <- 2
  close(ch1)
}()

ch2 := make(chan int, 3)
go func() {
  ch2 <- 10
  ch2 <- 11
  ch2 <- 12
  close(ch2)
}()

ch := ch1
for v := range ch {
  fmt.Println(v)
  ch = ch2
}
```

* What's the impact of using a `range` loop with
  an `array`? As the range expression is evaluated
  before the beginning of the loop, what is
  assigned to the temporary loop variable is a
  **copy** of the array. It's important to keep
  this behavior in mind to avoid common mistakes
  when updating the loop's iteration variable.

```go
a := [3]int{0, 1, 2}
for i, v := range a {
  a[2] = 10
  if i == 2 {
    fmt.Println(v) // 2
  }
}
```

```go
a := [3]int{0, 1, 2}
for i := range a {
  a[2] = 10
  if i == 2 {
    fmt.Println(a[2]) // 10
  }
}
```

```go
a := [3]int{0, 1, 2}
for i, v := range &a {
  a[2] = 10
  if i == 2 {
    fmt.Println(v) // 10
  }
}
```

* When we have to iterate over a data structure
  using a `range` loop, we have to recall that all
  the values are assigned to a unique variable with
  a unique address.
* Therefore, if we store this **pointer** variable
  during each iteration, we will end up in a situation
  where we have stored the same pointer that references
  the *same* element: the *latest* one.
* We can overcome this issue by forcing the creation
  of a local variable in the loop's scope or accessing
  the value via its index. Both solutions are perfectly
  fine.

* In Go, the *iteration order* over a map is
  **not specified**. Also, there is no guarantee that
  the order will be the same from
  one iteration to the next.

```
If a map entry is created during iteration,
it may be produced during the iteration or skipped.
The choice may vary for each entry created and
from one iteration to the next.
  - Go spec
```

* To summarize, when we work with a map,
  we **shouldn't** rely on:
  - The ordering of the data by keys
  - The preservation of the insertion order
  - A deterministic iteration order
  - The fact that an element added during
    an iteration will be produced
    during this iteration

* One important rule to keep in mind:
  a `break` statement terminates the execution
  of the innermost `for`, `switch`, or
  `select` statement.

```go
loop:
  for i := 0; i < 5; i++ {
    fmt.Println(i)
    switch i {
    default:
    case 2:
      break loop
    }
  }
  // 0
  // 1
  // 2
```

* We can also use `continue` with a label to
  go to the next iteration of the labeled loop.
* We should remain cautious while using a
  `switch` or `select` statement inside a loop.
* When using `break`, we should always make sure
  to know which statement it will affect.
  Using labels, as we have seen, is the easiest
  solution to enforce breaking a
  specific statement.

* We have to recall that `defer` schedules a
  function call when the surrounding function returns.
  In this case, the `defer` calls will be executed not
  during each iteration of the loop but when the
  `readFiles` function `return`. If `readFiles` doesn't
  `return`, the file descriptors will be kept open
  forever, causing leaks.

* The first way to do it is to extract the logic
  inside of the loop in another function
  and refactor `readFiles`:

```go
func readFiles(ch <-chan string) error {
  for path := range ch {
    if err := readFile(path); err != nil {
      return err
    }
  }
  return nil
}

func readFile(path string) error {
  file, err := os.Open(path)
  if err != nil {
    return err
  }
  defer file.Close()
  // Do something with file
  return nil
}
```

* In this implementation, the `defer` function
  is called when `readFile` returns, meaning at
  the end of each iteration. Therefore, we will
  not keep file descriptors opened until the
  parent `readFiles` function returns.
* The other way to create a surrounding function
  so that `defer` can be executed during each
  iteration is to use a closure (as a reminder,
  a function value that references variables
  from outside its body):

```go
func readFiles(ch <-chan string) error {
  for path := range ch {
    err := func() error {
      file, err := os.Open(path)
      if err != nil {
        return err
      }
      defer file.Close()
      // Do something with file
      return nil
    }()
    if err != nil {
      return err
    }
  }
  return nil
}
```

## Strings

* In Go, a **string** is an **immutable** data
  structure representing:
  - A *pointer* to a backing array of bytes
  - The total number of bytes in this array

* We should understand the distinction between
  `charset` and `encoding`.
  - A `charset`, as the name suggests, is a set of
    characters. For example, ASCII contains `128`
    characters from the null char character
    (`0` in decimal) to the delete character
    (`127` in decimal). It includes all the
    uppercase letters from `A` to `Z` and
    lowercase letters from `a` to `z`.
  - On the other side, `encoding` is the
    translation of a character's list in binary.
  - Unicode is an extension of ASCII and
    contains `2^21` characters.

* In Go, a ***rune*** is a **Unicode code point**.
* Some people believe that Go strings are
  always `UTF-8`, yet this is **not always true**.

* A charset is a set of characters, whereas an
  encoding describes how to translate
  a charset into binary.
* In Go, a string references a
  *slice of arbitrary bytes*.
* A Go source code is encoded using `UTF-8`. Hence,
  all string literals are `UTF-8` strings. Yet,
  as a string can contain arbitrary bytes,
  it's not necessarily based on `UTF-8`.
* A `rune` corresponds to a *Unicode code point*
  concept, meaning an item represented
  by a single value.

```go
s := "hêllo"
for i := range s {
  fmt.Printf("position %d: %c\n", i, s[i])
}
fmt.Printf("len=%d\n", len(s))
// position 0: h
// position 1: Ã
// position 3: l
// position 4: l
// position 5: o
// len=6
```

* We have to know that `len(s)` doesn't return
  the *number of runes* in a string
  but its *number of bytes*.
* Printing `s[i]` didn't print the `i'th` *rune*;
  it printed the UTF-8 representation of
  the byte at index `i`.

```go
s := "hêllo"
for i, r := range s {
  fmt.Printf("position %d: %c\n", i, r)
}
// position 0: h
// position 1: ê
// position 3: l
// position 4: l
// position 5: o
```

* Indeed, using a `range` loop on a string
  returns two variables: the starting index
  of a rune and the **rune** itself.

```go
s := "hêllo"
runes := []rune(s)
for i, r := range runes {
  fmt.Printf("position %d: %c\n", i, r)
}
// position 0: h
// position 1: ê
// position 2: l
// position 3: l
// position 4: o
```

* `TrimRight` vs `TrimSuffix`
