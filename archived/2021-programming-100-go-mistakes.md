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

```go
fmt.Println(strings.TrimRight("123xoxo", "xo"))  // 123
fmt.Println(strings.TrimSuffix("123xoxo", "xo")) // 123xo
```

```go
func concat(ids []string) string {
  s := ""
  for _, id := range ids {
    s += id
  }
  return s
}
```

* We used the `+=` operator for each string and
  assigned it to `s`. At first sight, this function
  may not look wrong. Yet, with this implementation,
  we forget one of the core characteristics of a string:
  its **immutability**. Therefore, each iteration
  allocates a new string that needs to be allocated
  in memory, which impacts performance.

```go
func concat(ids []string) string {
  sb := strings.Builder{}
  for _, id := range ids {
    _, _ = sb.WriteString(id)
  }
  return sb.String()
}
```

* Let's bear in mind that all the exported functions
  of the `strings` package also have their alternative
  in the `bytes` package.
* If we have to implement a function that consumes and
  returns a `byte[]`, be it while doing IO or else,
  we should first check whether we could implement
  the whole workflow without extra conversions.

## Functions and Methods

* In Go, we can attach to a method either
  a value or a pointer receiver. With a
  value receiver, Go makes a **copy** of the
  value and passes it to the method.
  - Any changes to the object will remain
    local to the method.
  - The original object will remain unchanged.

```go
type customer struct {
  balance float64
}

func (c customer) add(v float64) {
  c.balance += v
}

func main() {
  c := customer{balance: 100.}
  c.add(50.)
  fmt.Printf("balance: %.2f\n", c.balance)
  // balance: 100.00
}
```

* On the other side, with a pointer receiver,
  Go passes the address of an object to the method.
  Any modifications on the receiver will be done
  on the original object directly.

* A receiver **must** be a **pointer**:
  - If the method needs to *mutate* the receiver.
    This rule is also valid if the receiver is a
    `slice` and a method needs to append elements.
  - If the method receiver is a struct containing a
    `sync` field. `sync` is the Go package providing
    synchronization primitives such as `mutexes`.
* A receiver **should** be a **pointer**:
  - If the receiver is a *large object*, a pointer
    receiver should be used as doing a copy would be
    less efficient.
* A receiver **must** be a **value**:
  - If we have to enforce a receiver's
    *immutability*.
  - If the receiver is a `map`, a `function`,
    or a `channel`; otherwise, it leads to
    a compilation error.
* A receiver **should** be a **value**:
  - If the receiver is a `slice` that
    *doesn't* have to be *mutated*.
  - If the receiver is a *basic type*. As
    passing a value receiver uses on-stack copy
    instead of heap allocation, it will reduce
    GC's work.
  - If the receiver is *not a large object* and
    none of the conditions for using
    a pointer were met.

```go
type customer struct {
  data *data
}

type data struct {
  balance float64
}

func (c customer) add(operation float64) {
  c.data.balance += operation
}

func main() {
  c := customer{data: &data{
    balance: 100,
  }}
  c.add(50.)
  fmt.Printf("balance: %.2f\n", c.data.balance)
  // balance: 150.00
}
```

> - In this case, what should we use, a **pointer** or
    a **value** receiver? There's no hard rule here.

* **Never** using *named result parameters*
  - When a result parameter is named, it's
    initialized to its **zero** value when the
    `function/method` begins.
  - Also, with named result parameters, we can
    call an *empty return statement* without
    arguments.

* Unintended *side-effects* with named result parameters

```go
type Customer struct {
  Age  int
  Name string
}

type MultiError struct {
  errs []string
}

func (m *MultiError) Add(err error) {
  m.errs = append(m.errs, err.Error())
}

func (m *MultiError) Error() string {
  return strings.Join(m.errs, ";")
}

func (c Customer) Validate() error {
  var m *MultiError

  if c.Age < 0 {
    if m == nil {
      m = &MultiError{}
    }
    m.Add(errors.New("age is negative"))
  }
  if c.Name == "" {
    if m == nil {
      m = &MultiError{}
    }
    m.Add(errors.New("name is nil"))
  }

  return m
}

func main() {
  customer := Customer{Age: 33, Name: "John"}
  if err := customer.Validate(); err != nil {
    log.Fatalf("customer is invalid: %v", err)
  }
  // customer is invalid: <nil>
}
```

* We have to know that in Go, a
  pointer receiver **can** be `nil`.
  - Therefore, a `nil` pointer is
    a valid receiver.
* But why is a `nil` pointer valid?
  - In Go, a method is just syntactic sugar for
    a function whose first parameter would be
    the receiver.

* When we have to return an `interface`, we
  *should not* return a `nil` pointer but a
  `nil` value directly.
* In general, having a `nil` pointer is not
  a desirable state and means a probable bug.

---

* Let's see a concrete use case when receiving
  an `io.Reader` type instead of a
  *filename* is considered a best practice.
  - For each *unit test*, it will require creating
    a file within our Go project. The more complex
    the function is, the more cases we may want
    to add, and the more files we will
    have to create.
  - One may also criticize the fact that this
    function is not reusable.

---

* There's something crucial to understand
  with arguments evaluation in a `defer` function:
  - the arguments are **evaluated right away**,
    not once the surrounding function returns.
* Calling as a `defer` statement a closure.
  - As a reminder, a closure is a function value that
    references variables from outside its body.
  - The arguments passed to a `defer` function are
    evaluated right away. Yet, we must know that the
    variables referenced by a `defer` closure are
    evaluated during the closure execution.

* When we use `defer` on a method, the same logic
  related to arguments evaluation applies.
  - With a **value** receiver, the receiver
    is evaluated immediately.
  - Conversely, if the receiver is a **pointer**,
    the potential changes to the variable
    referenced by the pointer will be visible.

```go
func main() {
  s := Struct{id: "foo"}
  defer s.print()
  s.id = "bar"
}

type Struct struct {
  id string
}

func (s Struct) print() {
  fmt.Println(s.id)
  // foo
}
```

```go
func main() {
  s := &Struct{id: "foo"}
  defer s.print()
  s.id = "bar"
}

type Struct struct {
  id string
}

func (s *Struct) print() {
  fmt.Println(s.id)
  // bar
}
```

* The `s` pointer is also evaluated immediately
  while calling `defer`. However, this pointer
  references a struct that mutates before the
  surrounding function returns.
  - Hence, this example prints `bar`.
* In summary, we have to remind that calling
  `defer` on a function or method, the call's
  arguments are *evaluated immediately*.
  - For a method, the receiver is also
    *evaluated immediately*. If we want to
    delay the evaluation, it can be done
    either using *pointers* or *closures*.

## Error Management

```go
func main() {
  defer func() {
    if r := recover(); r != nil {
      fmt.Println("recover", r)
    }
  }()

  f()
}

func f() {
  fmt.Println("a")
  panic("foo")
  fmt.Println("b")
}
// a
// recover foo
```

* We should note that calling `recover()` to capture
  a goroutine panicking is only useful
  inside a `defer` function.

* `%w` allows wrapping an error that can be unwrapped
  to retrieve the initial error later.
  - For example, a caller of `GetContract` could compare
    the error to a specific error value
    using `errors.Is`:

```go
contract, err := store.GetContract(name)
if err != nil {
  if errors.Is(err, store.ErrFoo) {
    // ...
  }
}
```

> These functions unwrap the `err` error returned by
  `GetContract` to check if the source error
  was a `store.ErrFoo` value.

* `errors.As`: This function recursively unwraps an error
  and returns `true` if an error in the
  chain matches the expected type.
  - This function requires the second argument
    (the target error) to be of a pointer.
  - Otherwise, the function will compile but panic at runtime.
* In summary, if we rely on error wrapping, we must use
  `errors.As` to check whether an error is a specific type.

* **Expected errors** should be designed as error values
  (sentinel errors):
  - `var ErrFoo = errors.New("foo")`
* **Unexpected errors** should be designed as error types:
  - `type BarError struct{ … }` with `BarError`
    implementing the `error` interface

* Checking if the error is an `sql.ErrNoRows` was
  done using the `==` operator.
* If an `sql.ErrNoRows` is wrapped using `fmt.Errorf`
  and the `%w` directive, the `err == sql.ErrNoRows`
  will always be `false`.
* We have seen how `errors.As` is used to check an
  **error** against a **type**.
* With **error values**, we should use its
  counterpart: `errors.Is`.
* Using `errors.Is` instead of the `==` makes the
  comparison working even if the error was
  **wrapped** using `%w`.

## Concurrency

```
Concurrency is about dealing with lots of things at once.
Parallelism is about doing lots of things at once.

-- Rob Pike
```

* Concurrency **isn't always faster**
  - If the workload that we want to parallelize is
    **too small**, meaning we're going to compute it
    too fast, the benefit of distributing a job
    across cores will be destroyed.

> - A **thread** is the **smallest unit** of processing
    that an **OS** can **perform**.
> - Context switching is considered an expensive operation
    as the OS needs to save the current execution state of
    a thread before the switch (e.g., the current register values).

* Context switching a goroutine `vs.` a thread is about
  `80%` to `90%` faster depending on the architecture.

* Internally, the Go scheduler uses the following terminology:
  - **G**: goroutine
  - **M**: OS thread (stands for machine)
  - **P**: CPU core (stands for processor)
* The `GOMAXPROCS` variable defines the limit of `OS threads (M)`
  in charge of executing user-level code simultaneously.
  - Yet, if a thread is blocked in a system call (e.g., I/O),
    the scheduler can spin up more OS threads (M).
  - As of Go 1.5, `GOMAXPROCS` is by default equal to the
    number of available CPU cores.
* A goroutine has a simpler lifecycle than an OS thread.
  It can be either:
  - **Executing**: the goroutine is scheduled on an **M**
    and executing its instructions
  - **Runnable**: waiting for being in an executing state
  - **Waiting**: stopped and pending for something to
    complete, such as a system call or a
    synchronization operation (e.g., mutex)
* Indeed, the Go runtime handles two kinds of queues:
  - one local queue per **P**
  - and a global queue shared among all the **P**s.

* Every `1/61` execution, the Go scheduler will check
  whether goroutines from the global queue are available.
  - If not, it will check its local queue.
  - Meanwhile, if both the global and the local queues
    are empty, it can pick up goroutines from other local queues.
  - This principle in scheduling is called `work-stealing`,
    and it allows an underutilized processor to actively
    look for other processor's goroutine and **steal** some.
* Since Go `1.14`, the Go scheduler is now preemptive.
  - It means that when a goroutine is running for a specific
    amount of time (`10 ms`), it will be marked preemptible
    and can be context-switched off to be replaced by
    another goroutine.
  - It allows a long-running job to be forced to share CPU time.

* If we're not sure that a parallel version will be faster,
  perhaps the right approach is first to start with a simple
  and sequential one and build from here thanks to profiling
  and benchmarks.

* **Mutexes** and **channels** have different semantics.
  - Whenever we want to share a state or access a
    shared resource, **mutexes** ensure exclusive
    access to this resource.
  - Conversely, **channels** are a mechanic for signaling
    with or without data (`chan struct{}` or not).
  - Coordination or ownership transfer should be achieved
    via **channels**.
  - It's important to know whether goroutines are parallel
    or concurrent as in general, we should rather need
    **mutexes** for **parallel** goroutines and
    **channels** for **concurrent** ones.

* Data races `vs.` race conditions
  - A **data race** occurs when two or more goroutines
    simultaneously access the same memory location,
    and at least one is writing.
  - A **race condition** occurs when the behavior depends
    on the sequence or the timing of events that can't
    be controlled.
* So how should we prevent a data race from happening?
  - **Atomic** operations can be done in Go
    using the `atomic` package.
  - In Go, the `sync` package provides a **Mutex** type.
* We have also seen how to prevent data race with three
  synchronization approaches:
  - Using **atomic** operations
  - Protecting a critical section with a **mutex**
  - Using communication and **channels** to ensure
    a variable is updated only by a single goroutine
* Ensuring a specific sequence of execution among
  goroutines is a question of coordination and orchestration.
  - If we want to ensure that we first go from `state 0`
    to `state 1`, then from `state 1` to `state 2`, we
    should find a way to guarantee that goroutines are
    executed in order.
  - **Channels** can be a way to solve this problem.

* In summary, when we work in concurrent applications,
  it's essential to understand that a **data race**
  is different from a **race condition**.
* A **data race** occurs when multiple goroutines
  simultaneously access the same memory location,
  and at least one of them is writing.
* A **data race** means an `unexpected behavior`.
* However, a `data race-free` application doesn't
  necessarily mean **deterministic** results. Indeed,
  an application can be free of data races but can
  still have its behavior depending on uncontrolled events
  - e.g., goroutines execution, how fast will a message
    be published to a channel, how long will last a call to a DB;
  - this is a **race condition**.

* Creating a goroutine `happens before`
  the goroutine's execution begins.
* **Closing** a channel `happens before`
  a **receive** of this closure.
* A **send** on a channel `happens before`
  the corresponding **receive**
  from that channel completes.
* A **receive** from an **unbuffered** channel
  `happens before` the **send** on that
  channel completes.

* If the workload executed by the workers is `IO-bound`,
  the value mainly depends on the external system.
* Conversely, if the workload is `CPU-bound`, the most
  optimal number of goroutines is close to the number
  of available threads.
  - It's why knowing the workload type
    (either `I/O` or the `CPU`) is crucial when
    designing concurrent applications.

### Context

> A **Context** carries a `deadline`,
  a `cancellation` signal, and
  other values across API boundaries.

* A **deadline** is either:
  - A `time.Duration` (e.g., `250 ms`)
  - A `time.Time` (e.g., `1999-02-07 00:00:00 UTC`)
* The semantic of a `deadline` conveys that an ongoing
  activity should be stopped if this deadline is met.
  - An activity is, for example, an `I/O` request, or a
    goroutine waiting to receive a message from a `channel`.

* A context conveying values can be created this way:

```go
ctx := context.WithValue(parentCtx, "key", "value")
```

* Just like `context.WithTimeout`, `context.WithDeadline`,
  and `context.WithCancel`, `context.WithValue` is created
  from a parent context.

* Consequently, a best practice while handling `context keys`
  is to create an unexported custom type.
* Hence, there's no risk that another package using
  the `same context` could override the value already set.

* Catching a context **cancellation**
  - The `context.Context` type exports a `Done` method
    that returns a `receive-only` notification channel:
    `<- chan struct{}`.
  - This channel is closed when the work associated
    to the context should be canceled.
* For example, the `Done` channel related to a context created with:
  - `context.WithCancel` is closed when the
    cancel function is called
  - `context.WithDeadline` is closed when the
    deadline has expired
* One thing to mention, why should the internal channel
  be closed when a context is canceled or has met
  a deadline instead of receiving a specific value?
  - Because the closure of a channel is the
    only channel action that all the consumer goroutines
    will receive.
  - This way, all the consumers will be notified once
    a context is canceled or a deadline is reached.
* Furthermore, `context.Context` exports an `Err` method
  that returns `nil` if the `Done` channel isn't yet closed;
  otherwise, it returns a `non-nil` error explaining why
  the `Done` channel was closed, for example:
  - A `context.Canceled` error if the channel was cancelled
  - A `context.DeadlineExceeded` error if the
    context's deadline passed

```go
func handler(ctx context.Context, ch chan Message) error {
  for {
    select {
    case msg := <-ch:
      // Do something with msg
    case <-ctx.Done():
      return ctx.Err()
    }
  }
}
```

* In summary, propagating a context should be done cautiously.
  - We illustrated this section with an example of handling
    an asynchronous action based on a context associated
    with an HTTP request. As the context is canceled once we
    return the response, the asynchronous action can also
    get stopped unexpectedly.
  - Let's bear in mind the impacts of propagating a given
    context and if necessary, let's also keep in mind that
    it would always be possible to create our custom
    context for a specific action.

### Mistake - Starting a goroutine without knowing when to stop it

* Not knowing when to stop a goroutine is a
  design issue and a common
  concurrency mistake in Go.

* In summary, let's be mindful that a goroutine is a
  resource like any other which have to be eventually closed,
  be it to free memory or other resources.
  - Starting a goroutine without knowing when to
    stop it is a design issue.
* Whenever a goroutine is started, we should have a clear
  plan about when it will stop.
* Last but not least, if a goroutine creates resources
  and its lifetime is bound to the lifetime of the application,
  it's probably **safer** to **wait for it to be closed**
  **instead of notifying it**.
  - This way, we can ensure the resources are
    **freed before exiting** the application.

### Mistake - Not being careful with goroutines and loop variables

```go
s := []int{1, 2, 3}

for _, i := range s {
  go func() {
    fmt.Print(i)
  }()
}
```

* One may expect this code to print `123` in
  no particular order.
  - as there is no guarantee that a goroutine
    created first will complete first
* **However**, the output of this code isn't
  deterministic.
  - For example, sometimes it can print `233`,
    sometimes `333`.
* What's the reason?
* We have to know that when a **closure goroutine**
  is executed, it **doesn't** capture the values when
  the goroutine is **created**.
* Instead, all the goroutines rely on the same variable.
* When a goroutine runs, it prints the value of `i` at
  the time `fmt.Print` is **executed**.
  - Hence, `i` may have been modified since
    the goroutine was launched.

```go
s := []int{1, 2, 3}

for _, i := range s {
  v := i
  go func() {
    fmt.Print(v)
  }()
}
```

```go
s := []int{1, 2, 3}

for _, i := range s {
  go func(i int) {
    fmt.Print(i)
  }(i)
}
```

* We have to be **cautious** with `goroutines` and `loop` variables.
* If the goroutine is a `closure` that accesses an iteration
  variable from outside its body, it's a problem.
  - We can fix it either by creating a local variable
  - for example, as we have seen using `i := i` before
    executing the goroutine
  - or by making the function no longer a closure.

### Mistake - Expecting a deterministic behavior using select and channels

```
If one or more of the communications can proceed,
a single one that can proceed is chosen via a
uniform pseudo-random selection.

-- Programming Language Specification
```

* Unlike a `switch` statement where the first case
  with a match wins, the `select` statement will
  select one **randomly** if multiple
  options are possible.
* This behavior might look odd at first, but there's
  a good reason for that:
  - to prevent possible **starvation**.
* Indeed, suppose the first possible communication
  chosen is based on the source order. In that case,
  we may fall into the situation where we would solely
  receive from one single channel because of a
  fast sender, for example.
  - To prevent this, the language designers have
    decided to use a random selection.
* Using `default` in a `select` statement is chosen
  only if none of the other cases match.

* When using `select` with multiple channels, we have to
  remember that if multiple options are possible,
  it's not the first case in the source order that will win.
* Instead, Go will **select** it **randomly**, so there's
  no guarantee about which one will be chosen.
  - To overcome this behavior, we can either change the
    producer and receiver (if possible) to use a single
    channel or use inner selects and `default` case to
    handle prioritizations.

### Not using notification channels

* In Go, an **empty** `struct` is a `struct`
  without any fields. Regardless of the architecture,
  it occupies **zero** `bytes` of storage as we can
  verify using `unsafe.Sizeof`:

```go
var s struct{}
fmt.Println(unsafe.Sizeof(s))
// 0
```

* We may wonder why not using an empty `interface`.
  - `var i interface{}`
* Yet, an empty `interface` isn't free;
  - it occupies `8` bytes on `32-bit` architecture
  - and `16` bytes on `64-bit` architecture.

* Applied to channels, if we want to create a channel
  to send notification without data, the appropriate
  manner of doing it in Go is a `chan struct{}`.

### Mistake - Not using nil channels

* Receiving a message on a `nil` channel is
  a valid operation. The goroutine won't panic;
  however, it will **block forever**.

```go
func merge(ch1, ch2 <-chan int) <-chan int {
  ch := make(chan int, 1)
  ch1Closed := false
  ch2Closed := false

  go func() {
    for {
      select {
      case v, open := <-ch1:
        if !open {
          ch1Closed = true
          break
        }
        ch <- v
      case v, open := <-ch2:
        if !open {
          ch2Closed = true
          break
        }
        ch <- v
      }

      if ch1Closed && ch2Closed {
        close(ch)
        return
      }
    }
  }()

  return ch
}
```

* There is one major **issue**: when one of the two
  channels is closed, the for loop will act as a
  busy-waiting one, meaning it will keep looping
  even though there's no new message received in
  the other channel.
* Indeed, we have to keep in mind the behavior of
  the select statement in our example.
  - Let's say `ch1` was closed
    (so we won't receive any new message in here);
  - once we reach select again, it will wait for
    one of these three conditions to happen:
  - `ch1` is closed
  - `ch2` has a new message
  - `ch2` is closed

```go
func merge(ch1, ch2 <-chan int) <-chan int {
  ch := make(chan int, 1)

  go func() {
    for ch1 != nil || ch2 != nil {
      select {
      case v, open := <-ch1:
        if !open {
          ch1 = nil
          break
        }
        ch <- v
      case v, open := <-ch2:
        if !open {
          ch2 = nil
          break
        }
        ch <- v
      }
    }
    close(ch)
  }()

  return ch
}
```

* First, we loop as long as at least one channel
  is still opened. Then, for example, if `ch1` is
  closed, we assign `ch1` to `nil`.
* Hence, during the next loop iteration, the `select`
  statement will now only wait for two conditions:
  - `ch2` has a new message
  - `ch2` is closed
* This is the implementation we've been waiting for.
  We cover all the different cases, and it doesn't
  require a busy loop that will waste CPU cycles.

* In summary, we have seen that waiting or sending to
  a `nil` channel is a blocking action, and this behavior
  isn't useless at all.
* As we have seen throughout the example of merging
  two channels, we can use `nil` channels to implement
  an elegant state machine that would remove one case
  from a `select` statement.
* Let's keep this idea in mind: `nil` channels are truly
  useful in some conditions and should be part of the
  Go developer toolset when it comes to
  dealing with concurrent code.

### Being puzzled about a channel size

* An **unbuffered** channel is a channel without
  any capacity.
  - It can be created by either omitting the size
    or providing a zero size:
* Using an **unbuffered** channel
  (also sometimes called **synchronous** channels),
  the sender will *block until* the
  *receiver receives* data from the channel.

```go
ch1 := make(chan int)
ch2 := make(chan int, 0)
```

* With a **buffered** channel, a sender can send
  messages while the channel isn't full.
* Once the channel is full, it will block until
  a receiver goroutine receives a message.

* Regarding channels:
  - A **buffered** channel enables **synchronization**.
    Indeed, we have the guarantee that two goroutines
    will be in a known state: one receiving and another
    one sending a message.
  - Yet, an **unbuffered** channel doesn't provide any
    strong synchronization. Indeed, a producer goroutine
    can send a message and then continue its execution
    if the channel isn't full. The only guarantee is that
    a goroutine won't receive a message before it is sent.
    Yet, this is only a guarantee because of causality.
* It's essential to keep in mind this fundamental distinction.
  - Both channel types enable communication, but only one
    provides synchronization.
  - If we need synchronization, we must use unbuffered
    channels. Also, unbuffered channels might be easier
    to reason about.
  - Indeed, buffered channels can lead to obscure
    deadlocks that would have been immediately
    apparent with unbuffered channels.

```
Queues are typically always close to full
or close to empty due to the differences in
pace between consumers and producers.

They very rarely operate in a balanced middle
ground where the rate of production and
consumption is evenly matched.

-- LMAX Disruptor
```

### Forgetting about possible side-effects with string formatting

* Can you see what the problem is in this code?

```go
type Customer struct {
  mutex sync.RWMutex
  id    string
  age   int
}

func (c *Customer) UpdateAge(age int) error {
  c.mutex.Lock()
  defer c.mutex.Unlock()

  if age < 0 {
    return errors.New("age should be positive")
  }

  c.age = age
  return nil
}

func (c *Customer) String() string {
  c.mutex.RLock()
  defer c.mutex.RUnlock()
  return fmt.Sprintf("id %s, age %d", c.id, c.age)
}
```

* The problem here might not be that straightforward.
  - If the provided `age` is negative, we return an error.
  - As the error is formatted, using the `%s` directive
    on the receiver, it will call the `String` method
    to format `Customer`.
  - Yet, as `UpdateAge` already acquires the `mutex` lock,
    the `String` method won't be able to acquire it.
