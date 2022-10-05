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
  - **Rob Pike**

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
  in the backing array.
* Adding an element to a full slice (`length == capacity`)
  leads to creating a new backing array with a new capacity,
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
  sequence of `key/values`.
  - e.g., `key1-value1-key2-value2-key3-value3`
* Instead, all the keys are first stored
  contiguously, then all the values.
  - e.g., `key1-key2-key3-value1-value2-value3`
* Ideally, there is only one pair of `key/value`
  per bucket. If it's the case, each operation
  takes `O(1)`. However, it isn't always possible.
* Indeed, if applying the hashing function to two
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
  **copy** of the array.
* It's important to keep this behavior in mind to
  avoid common mistakes when updating the
  loop's iteration variable.

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
* Using labels, as we have seen, is the easiest
  solution to enforce breaking a
  specific statement.

* We have to recall that `defer` schedules a
  function call when the surrounding function returns.
* In this case, the `defer` calls will be executed not
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

* In Go, a **rune** is a **Unicode code point**.
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
  - its **immutability**.
* Therefore, each iteration allocates a new string that
  needs to be allocated in memory, which impacts performance.

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
    that an OS can perform.
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
  - Yet, if a thread is blocked in a system call (e.g., `I/O`),
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
  - Instead, all the goroutines rely on the same variable.
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
  - A **unbuffered** channel enables **synchronization**.
  - Indeed, we have the guarantee that two goroutines
    will be in a known state: one receiving and another
    one sending a message.
  - Yet, an **buffered** channel doesn't provide any
    strong synchronization.
  - Indeed, a producer goroutine can send a message and
    then continue its execution if the channel isn't full.
  - The only guarantee is that a goroutine won't receive
    a message before it is sent. Yet, this is only
    a guarantee because of causality.
* It's essential to keep in mind this fundamental distinction.
  - Both channel types enable communication, but only one
    provides synchronization.
  - If we need **synchronization**, we must use **unbuffered**
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

### Creating data races with append

```go
s := make([]int, 1)

go func() {
  s1 := append(s, 1)
  fmt.Println(s1)
}()

go func() {
  s2 := append(s, 1)
  fmt.Println(s2)
}()
```

* Do you believe this example has a data race?
  - The answer is `no`.
* In this example, we created a slice with
  `make([]int, 1)`.
  - This example creates a `1-length`, `1-capacity` slice.
  - Thus, as the slice is full, using append is in each
    goroutine will return a slice backed by a new array.
  - It doesn't mutate the existing array;
    hence it doesn't lead to a data race.

```go
s := make([]int, 0, 1)

go func() {
  s1 := append(s, 1)
  fmt.Println(s1)
}()

go func() {
  s2 := append(s, 1)
  fmt.Println(s2)
}()
// DATA RACE !!!
```

* Here, we created a slice with `make([]int, 0, 1)`.
  - Therefore, the array isn't full.
  - Consequently, both goroutines make an attempt to
    update the same index of the backing array
    (index `1`), which is a data race.

* How much do data races impact slices and maps?
  Having multiple goroutines:
  - Accessing the same slice index with at least one
    of them updating the value is a data race.
    Indeed, the goroutines are accessing
    the same memory location.
  - Accessing different slice indices regardless of
    the operation isn't a data race; different indices
    mean different memory locations.
  - Accessing the same map (regardless of whether it's
    the same or a different key) with at least one of
    them updating it is a data race.
  - We may be wondering why it is different from a
    slice data structure? As we mentioned in the data
    types chapter, a map is an array of buckets,
    each bucket being a pointer to an array of
    `key/value` pairs. A hashing algorithm is used to
    determine the array index of the bucket. As this
    algorithm contains some randomness during the map
    initialization, one execution may lead to the same
    array index, whereas another execution may not.
  - The race detector handles this case by raising a
    warning, regardless if an actual data race occurs or not.

### Using mutexes inaccurately with slices and maps

* Internally, a map is a `runtime.hmap` struct containing
  mostly some metadata (e.g., a counter) and a pointer
  referencing data buckets.
  - Hence, `balances := c.balances` doesn't
    copy the actual data.

### Misusing `sync.WaitGroup`

```go
wg := sync.WaitGroup{}
var v uint64

for i := 0; i < 3; i++ {
  go func() {
    wg.Add(1)
    atomic.AddUint64(&v, 1)
    wg.Done()
  }()
}

wg.Wait()
fmt.Println(v)

// non-deterministic value
// from 0 to 3
```

* The problem here is that `wg.Add(1)` is called
  within the newly created goroutine,
  not in the parent goroutine.
* Hence, there is no guarantee that we have indicated
  to the wait group that we wanted to wait for
  three goroutines before calling `wg.Wait()`.

* When dealing with goroutines, it's crucial to
  remember that the execution isn't deterministic
  without synchronization.
* The CPU has to use a so-called memory fence
  (also called a memory barrier) to ensure order.
  - Go provides different synchronization techniques
    for implementing memory fences,
    `sync.WaitGroup` being one of them.
* When using a `sync.WaitGroup`, the `Add` operation
  must be done before spinning up a goroutine in the
  parent one, whereas the `Done` operation must be
  done within the goroutine.

### Forgetting about `sync.Cond`

* The default distribution mode with multiple goroutines
  receiving from a shared channel is `round-robin`.
  - It can change if one goroutine isn't ready yet to
    receive messages (not in a waiting state on the channel);
  - in that case, Go would distribute the message to the
    next available goroutine.
* Only a channel `closure` is an event that can be
  **broadcasted** to multiple goroutines.

```
Cond implements a condition variable,
a rendezvous point for goroutines waiting for
or announcing the occurrence of an event.

-- sync package documentation
```

* A `condition` variable is a container of threads
  (here, goroutines) waiting for a
  certain condition.
* Furthermore, `sync.Cond` relies on a `sync.Locker`
  (a `*sync.Mutex` or `*sync.RWMutex`) to prevent data races.

* Let's also note one possible drawback when using `sync.Cond`.
* When we send a notification, for example, to a `chan struct`,
  even if there's no active receiver, the message will be
  buffered, which guarantees that this notification will be
  received eventually.
* Using `sync.Cond` with the `Broadcast` method wakes all
  goroutines currently waiting on the condition, and if none,
  the notification will be missed.
  - This is also an essential principle that we
    have to keep in mind.
* Signaling in Go can be achieved with channels.
  However, we should be aware that only a channel closure
  is an event multiple goroutines can catch.
  - Yet, this can happen only once.
  - Therefore, if we repeatedly send notifications to
    multiple goroutines, `sync.Cond` is a solution.
  - This primitive is based on condition variables that
    set up containers of threads waiting for
    a specific condition.
  - Using `sync.Cond`, we can broadcast signals that
    will wake all the goroutines waiting on a condition.

### Mistake - Copying a `sync` type

* The `sync` package provides basic synchronization
  primitives such as `mutexes`, condition variables,
  and wait groups.
  - For all these types, there's a hard rule to follow:
  - they **should never be copied**.

* `sync` types shouldn't be copied.
  This rule applies to the following types:
  - `sync.Cond`
  - `sync.Map`
  - `sync.Mutex`
  - `sync.RWMutex`
  - `sync.Once`
  - `sync.Pool`
  - `sync.WaitGroup`

* We can face the issue of unintentionally copying
  a `sync` field in some of the following conditions:
  - Calling a method with a value receiver
  - Calling a function with a `sync` argument
  - Calling a function with an argument
    that contains a `sync` field

* As a rule of thumb, whenever multiple goroutines have
  to access to a common `sync` element, we must ensure
  they all rely on the same instance.
  - This rule applies to all the types defined
    in the `sync` package.
  - Using `pointers` is a way to solve this problem:
  - either by having a pointer to a `sync` element
  - or a `pointer` to a struct containing a `sync` element.

## Standard Library

* Yet, `time.Duration` represents the elapsed time
  between two instants in **nanoseconds**.
* Remember always to use the `time.Duration` API and
  provide an `int64` **alongside a time unit**.

* The advantage of `time.After` is that it can be used
  to implement scenarios such as

```
"if I don't receive any message in this channel
for 5 seconds, then I will ...".
```

* As we said, `time.After` returns a channel.
* We may expect this channel to be closed during
  each loop iteration; yet, this isn't the case.
* The **resources** created by `time.After` (including the channel)
  will *be released once the timeout expires* and
  will **use some memory until it happens**.

* `time.NewTimer`. This function creates a
  `time.Timer` struct that exports:
  - A `C` field, which is the internal timer channel
  - A `Reset(time.Duration)` method to reset the duration
  - A `Stop()` method to stop the timer
* We should note that `time.After` also relies on
  `time.Timer`.
  - However, it only returns the `C` field.
* In general, we should be cautious when using `time.After`.
  - We have to remind ourselves that the resources created
    will only be released when the timer expires.

---

* What are the possible impacts of
  **embedded fields** with **JSON marshaling**?

```go
type Event struct {
  ID int
  time.Time
}

event := Event{
  ID:   1234,
  Time: time.Now(),
}

b, _ := json.Marshal(event)

fmt.Println(string(b))
// Expect
// {"ID": 1234, "Time": "2022-01-21T15:47:44.539103+08:00"}
// But !!!
// "2022-01-21T15:47:44.539103+08:00"
```

* **First**, if an embedded field type implements an
  interface, the struct containing the embedded field
  will also implement this interface.
  - This is about promoting a behavior.
* The **second** point to clarify is that we can change
  the default marshaling behavior by making a type
  implement `json.Marshaler` interface.
  - This interface contains a single `MarshalJSON` function

```go
type Marshaler interface {
  MarshalJSON() ([]byte, error)
}
```

* We have to know that `time.Time` implements the
  `json.Marshaler` interface. As `time.Time` is an
  embedded field of `Event`, it promotes its methods.
  - Therefore, `Event` also implement `json.Marshaler`.
* Consequently, passing an `Event` to `json.Marshal`
  will not use the default marshaling behavior
  but the one provided by `time.Time`.
  - We would also face the issue the other way around if
    we were unmarshaling an `Event` using `json.Unmarshal`.
* To fix this issue, there are **two** main possibilities.
  - First, we can make the `time.Time` field not
    embedded anymore by adding a name.
  - If we want to keep or have to keep the `time.Time`
    field embedded, the other option is to make `Event`
    implementing the `json.Marshaler` interface.

---

* An OS handles two different clock types:
  - `wall` and `monotonic`.
  - The wall clock is used to know the current time of the day.
  - This clock is subject to potential variations.
  - For example, if synchronized using NTP (Network Time Protocol),
    the clock can jump backward or forward in time.
  - The monotonic clock guarantees that the time will always move
    forward and will not be impacted by jumps in time.
  - It can be affected by potential frequency adjustments
    but never by jumps in time.

```go
type Event struct {
  Time time.Time
}

t := time.Now()
event1 := Event{
  Time: t,
}

b, _ := json.Marshal(event1)

var event2 Event
_ = json.Unmarshal(b, &event2)

fmt.Println(event1 == event2)
fmt.Println(event1.Time)
fmt.Println(event2.Time)
// false
// 2022-01-21 16:13:30.740539 +0800 CST m=+0.000086873
// 2022-01-21 16:13:30.740539 +0800 CST
```

* In Go, instead of splitting the two clocks into two
  different APIs, the `time.Time` may contain both a
  wall and monotonic time.
  - When we get the local time using `time.Now()`, it
    returns a `time.Time` with both times.
* Conversely, when we unmarshal the JSON, the `time.Time`
  field doesn't contain the monotonic time, only the wall time.
* How can we fix this problem? There are **two** main options.
  - When we used `==` operator to compare both `time.Time`,
    it compared all the struct fields, including the
    monotonic part.
  - To avoid this, we can use the `Equal` method instead.
  - The `Equal` method doesn't consider monotonic time.
  - Therefore, `areTimesEqual` will be `true`.
  - The second option is to keep the `==` to compare the
    two structs but to strip away the monotonic time using
    the `Truncate` method.
  - This method returns the result of rounding the `time.Time`
    value down to a multiple of a given duration.

---

* However, there's one **important** gotcha to remember if
  we use a `map` of `any`:
  - any numeric value, regardless if it contains a decimal,
    is converted into a `float64` type.

---

* Let's remember that `sql.Open` doesn't necessarily establish
  any connection, and the first connection can be opened lazily.
  - If we want to test our configuration and that a
    DB is reachable, we should follow `sql.Open` with a call to
    the `Ping` or `PingContext` method.

* Furthermore, it's important to remember that creating
  a pool also means four available config parameters.
  Each of these parameters is an exported method of `*sql.DB`:
  - `SetMaxOpenConns`: maximum number of open connections to
    the DB (default value: `unlimited`)
  - `SetMaxIdleConns`: maximum number of idle connections
    (default value: 2)
  - `SetConnMaxIdleTime`: maximum amount of time a connection
    can be idle before it's closed (default value: `unlimited`)
  - `SetConnMaxLifetime`: maximum amount of time a connection
    can be held open before it's closed (default value: `unlimited`)
* So, why should we tweak these config parameters?
  - Setting `SetMaxOpenConns` is important for production-grade
    applications. Indeed, as the default value is `unlimited`,
    we should rather set it to make sure it fits what
    the underlying DB can handle.
  - Setting `SetMaxIdleConns` should be increased
    (default value of `two`) if our application generates a
    significant number of concurrent requests.
  - Setting `SetConnMaxIdleTime` is important if our application
    can face a burst of requests. Indeed, when the application
    is back to a more peaceful state, we want to make sure the
    connections created are eventually released.
  - Last but not least, setting `SetConnMaxLifetime` can also be
    helpful if we connect to a load-balanced DB server, for example.

---

* If we don't eventually close an `os.File`, it will not
  lead to a leak. Indeed, the file will be closed
  automatically when `os.File` will be garbage collected.
* However, it's better to call `Close` explicitly
  and not rely on some hidden finalizers.

## Testing

* **Build tags**
  - A `build tag` is a special comment at the beginning
    of a Go file, followed by an empty line.
  - As Go `1.17`, the original syntax `// +build foo`
    got replaced by `//go:build foo`.

```go
//go:build foo

package bar
```

```go
//go:build integration

import (
  "testing"
)

func TestInsert(t *testing.T) {
}
```

* The benefit of using build tags is that we can
  select which kind of tests to execute.

```zsh
go test --tags=integration -v .
```

```go
//go:build !integration

import (
  "testing"
)

func TestContract(t *testing.T) {
}
```

* **Short mode**

```go
func TestLongRunning(t *testing.T) {
  if testing.Short() {
    t.Skip("skipping long-running test")
  }
}
```

```zsh
go test -short -v .
```

* In Go, the **race detector** isn't a static analysis tool
  that would happen during the compilation; instead, it's a
  tool to find data races that occur at runtime.
  - To enable it, we have to set the `-race` command-line
    while compiling or running a test

* First, the race detector can only be as good as our tests.
  - Thus, we should ensure that a concurrent code is
    tested thoroughly against data races.
* Furthermore, given the possible false negatives, if we do
  have a test to check data races, one option could be
  to put this logic inside a loop.
  - This way, we could increase the chances
    to catch possible data races.

* **Parallel**
  - When marking a test using `t.Parallel()`,
    it will be executed in parallel alongside
    all the other parallel tests.
  - In terms of execution, though, Go runs first all
    the sequential tests one by one. Then, once the
    sequential tests are completed,
    it executes the parallel tests.

```zsh
go test -parallel 16 .
```

* **Shuffle**
  - We should use the `-shuffle` flag to randomize tests.
  - We can either provide `on` or `off` to enable or disable
    tests shuffle (disabled by default).

```zsh
go test -shuffle=on -v .
```

* However, in some cases, we would like to run the tests
  again in the same order. To do that, instead of passing
  `on` to the `shuffle` flag, we can pass the `seed`
  used to randomize the tests.
* We can access this `seed` value when running shuffled
  tests by enabling the verbose mode (`-v`).

```zsh
go test -shuffle=on -v .
# -test.shuffle 1636399552801504000
go test -shuffle=1636399552801504000 -v .
# -test.shuffle 1636399552801504000
```

* **Table-driven** tests
  - `Table-driven` tests rely on subtests,
    meaning the option for a single test function
    to include multiple subtests.

```go
func TestFoo(t *testing.T) {
  t.Run("subtest 1", func(t *testing.T) {
    if false {
      t.Error()
    }
  })
  t.Run("subtest 2", func(t *testing.T) {
    if 2 != 2 {
      t.Error()
    }
  })
}
```

* We can also run a single test using the `-run` flag
  and concatenating the parent test name with the subtest.
  - For example, to run only `subtest 1`:

```zsh
go test -run=TestFoo/subtest_1 -v
```

## Optimizations

```
Make it correct, make it clear,
make it concise, make it fast, in that order.

-- Wes Dyer
```

* Modern CPUs rely on caching to speed up memory access.
  In most cases, via three different caching levels:
  - `L1`, `L2`, and `L3`.

* The concept of **cache lines** is crucial to understand.
  But before presenting what it is,
  let's understand why we need it.
* When a specific memory location is accessed
  (e.g., reading a variable),
  it is likely that in the near future:
  - The same location will be referenced again
  - Nearby memory locations will be referenced
* The former refers to temporal locality,
  and the latter refers to spatial locality.
  Both are part of a principle called locality of reference.

```go
func sum(s []int64) int64 {
  var total int64
  length := len(s)
  for i := 0; i < length; i++ {
    total += s[i]
  }
  return total
}
```

* Temporal locality is part of why we need CPU caches:
  to speed up repeated accesses to the same variables.
* However, because of spatial locality, the CPU will copy
  what we call a cache line instead of copying a
  single variable from the main memory to a cache.
* A cache line is a contiguous memory segment of a
  fixed size, usually `64` bytes (eight `int64` variables).
* Whenever a CPU decides to cache a memory block from the RAM,
  it will copy it to a cache line. Then, as memory is a hierarchy,
  when a CPU wants to access a specific memory location,
  it will first check in `L1`, then in `L2`, then in `L3`,
  and finally, if not present in these caches, in the main memory.

* We have to know that different strategies exist.
  - Sometimes, caches are inclusive
  - (e.g., `L2` data are also present in `L3`),
  - and sometimes caches are exclusive
  - (e.g., `L3` is called a victim cache as it
    contains only data evicted from `L2`).
* In general, these strategies are **hidden** by
  CPU vendors and not particularly useful to know.
  - Therefore, let's not delve into these questions.

### Slice of structs vs. struct of slices

```go
type Foo struct {
  a int64
  b int64
}

func sumFoo(foos []Foo) int64 {
  var total int64
  for i := 0; i < len(foos); i++ {
    total += foos[i].a
  }
  return total
}

type Bar struct {
  a []int64
  b []int64
}

func sumBar(bar Bar) int64 {
  var total int64
  for i := 0; i < len(bar.a); i++ {
    total += bar.a[i]
  }
  return total
}
```

* In the case of `sumFoo`, we receive a slice of
  structs containing two fields, `a` and `b`.
  - Therefore, we will have a succession of
    `a` and `b` in memory.
* Conversely, in the case of `sumBar`, we receive
  a struct containing two slices, `a` and `b`.
  - Therefore, all the elements of a will be
    allocated contiguously.
* This difference doesn't lead to any memory
  compaction optimization. However, as the goal of
  both functions was to iterate over each `a`,
  in one case, it requires four cache lines and
  only two cache lines in the other case.
* `sumBar` will be faster
  - The main reason is a better spatial locality that
    makes the CPU fetch fewer cache lines from memory.

### Predictability

* Predictability refers to the ability of a
  CPU to anticipate what the application will
  do to speed up its execution.

* **Striding** relates to how CPUs work through our data.
  There are `three` different types of strides:
  - A **unit stride** is when all the values we want to
    access are allocated contiguously; for example,
    a slice of `int64` elements.
  - This stride is predictable for a CPU and the most
    efficient as it requires a minimum number of
    cache lines to walk through the elements.
  - A **constant stride** is still predictable for the CPU;
    for example, a slice that iterates over every two elements.
  - However, it requires more cache lines to walk through data,
    so it's less efficient than a unit stride.
  - A **non-unit stride** is a stride the CPU can't predict to
    walk through data; for example, a linked list of a slice of
    pointers.
  - As the CPU doesn't know whether data are allocated
    contiguously or not, it won't fetch any cache line.

### Cache placement policy

* When a CPU decides to copy a memory block and place
  it into the cache, it must follow a particular strategy.
  Assuming an `L1D` cache of `32KB` and a cache line of
  `64` bytes, if a block was placed randomly into `L1D`,
  the CPU would have to iterate over `512` cache lines in
  the worst case to read a variable.
  - This kind of cache is called fully associative.
* To improve how fast an address can be accessed from a
  CPU cache, designers work on different policies regarding
  cache placement.
  - Let's skip the history and discuss today's most widely used option:
    `set-associative cache`, which relies on cache partitioning.
* With the `set-associate cache` policy,
  a cache is partitioned into sets. We will assume the cache is
  `2-way` set associative, meaning each set contains two lines.
* A memory block can belong to only one set, and the placement
  is determined by its memory address. To understand it,
  we have to dissect the memory block address into three parts,
  *block offset*, *set index*, and *tag bits*:
  - The *block offset* is based on the block size.
    Here a block size is `512` bytes, and `512` equals `2^9`.
    Therefore the first `9` bits of the address represent
    the *block offset* (`bo`).
  - The *set index* indicates to which set an address belongs.
    As the cache is `2-way` set associative and contains
    eight lines, we have `8 / 2 = 4` sets. Furthermore,
    `4` equals `2^2`; therefore, the two next bits
    represent the *set index* (`si`).
  - The rest of the address are the *tag bits* (`tb`).
    In the previous figure, we represented an address using
    `13` bits for simplicity. To compute `tb`, we do
    `13 - bo - si`. Here, it means the two remaining bits
    represent the *tag bits*.

* The cache replacement policy depends on the CPU,
  but usually, it's a pseudo-LRU policy
  (a real LRU would be too complex to handle).

### Not taking into account instruction-level parallelism

* ILP (`instruction-level parallelism`), which allows
  parallelizing the execution of a sequence of instructions.
  - A processor that implements ILP within a single
    virtual core is called a superscalar processor.

### Not understanding stack vs. heap

* The stack is the default memory, it's a LIFO
  data structure storing all the local variables
  for a specific goroutine.
* When a goroutine starts, it gets `2KB` of
  contiguous memory forming its stack space
  - this size has evolved in the past and could change again.
* However, this size isn't fixed at runtime and can
  grow and shrink as necessary
  - but it will always remain contiguous in memory,
    preserving data locality.

* A memory heap is a pool of memory
  shared for all the goroutines.

* Indeed, if the compiler cannot prove that a
  variable isn't referenced after the function returns,
  the variable is allocated on the heap.

* As we said, a `stack` is self-cleaning and is accessed
  by a single goroutine. Conversely, the `heap` has to
  be cleaned by an external system: the GC.
* Therefore, the more heap allocations are made, the more
  we pressure the GC. When the GC runs, it will use `25%`
  of the available CPU capacity and potentially create
  milliseconds of "stop the world" latency.

> Using pointers to avoid a copy isn't necessarily faster;
  it depends on the context.

* Escape analysis
  - First of all, when an allocation cannot be done
    on the stack, it will be done on the heap.
  - Global variables as multiple goroutines can access them.
  - A pointer sent to a channel.
  - A variable referenced by a value sent to a channel.
  - If a local variable is too large to fit on the stack.
  - If the size of a local variable is unknown.
  - The backing array of a slice reallocated using `append`.

> It's not exhaustive and can also change
  in future Go versions.

* In general, *sharing down* stays on the stack,
  whereas *sharing up* escapes to the heap.
* This should prevent common mistakes such as
  premature optimizations where we may want to
  return pointers, for example, because "it avoids a copy".
* Let's **focus on readability and semantics first**
  and then **optimize** allocations **if needed**.

### Not knowing how to reduce allocations

* Therefore, sometimes even a slight change on an
  API can positively impact allocations. When designing
  an API, let's remain aware of the escape analysis
  rules described in the previous section and use,
  if needed, `gcflags` to understand compiler's decisions.

* In summary, if we frequently allocate many objects
  of the same type, we can consider using `sync.Pool`.
* Indeed, `sync.Pool` is a set of temporary objects
  that can help us prevent reallocating the same kind
  of data repeatedly.
* Also, `sync.Pool` is safe for use by multiple
  goroutines simultaneously.

### Not relying on inlining

* However, inlining only works for functions with
  a certain complexity, also known as inlining budget.
* Inlining has two main benefits.
  - First, it removes the overhead of a function call.
  - Second, it allows the compiler to proceed to
    further optimizations.
  - For example, following inlining a function, the
    compiler can decide that a variable supposed to
    escape initially on the heap may stay on the stack.

* *Mid stack inlining* is about inlining functions
  that call other functions.
* Thanks to *mid-stack inlining*, as Go developers,
  we can now optimize an application using the concept
  of fast path inlining to distinguish between a fast
  and a slow path.

### Not using Go diagnostics tooling

* **Profiling**
  - `CPU`: determines where an application spends its time
  - `Goroutines`: reports the stack traces of the
    ongoing goroutines
  - `Heap`: reports heap memory allocation to monitor current
    memory usage and check for possible memory leaks
  - `Mutex`: reports lock contentions to see the behaviors
    of the mutexes used in our code and whether an application
    spend too much time in locking calls
  - `Block`: shows where goroutines block waiting on
    synchronization primitives

* **Execution tracer**

```zsh
go test -bench=. -v -trace=trace.out
go tool trace trace.out
```

### Not understanding how the GC works

* A GC keeps a tree of the object references.
  The Go GC is based on the `mark-and-sweep` algorithm,
  which relies on two stages:
  - **Mark stage**: traverse all the objects of the heap
    and mark them whether they are still in use
  - **Sweep stage**: traverse the tree of references from
    the root and deallocate blocks of objects
    no longer referenced
* The Go GC is called concurrent `mark-and-sweep` as it
  aims to reduce the amount of stop-the-world operations
  per GC cycle to mostly run concurrently
  alongside our application.

* The Go GC also includes a way to free memory after
  a peak of consumption. Imagine our application is
  based on two phases:
  - An init phase that would lead to frequent
    allocations and a large heap
  - A runtime phase with moderate allocations
    and a small heap
* How will Go tackle the fact that the large heap was
  only helpful when the application started but not after?
  - It's handled as part of the GC with a so-called
    periodic scavenger. After a certain time, the GC
    will detect that such a large heap
    isn't necessary anymore.
  - Hence, it will free some memory and return it to the OS.

* `GOGC`. This variable defines the percentage of the heap
  since the last GC before triggering another GC,
  - by default: `100%`.

* One concrete example to make sure we understand it.
  Let's assume the current heap size is `128 MB`.
* If `GOGC=100`, the next GC will be triggered when the
  heap size reaches `256 MB`.
* Hence, a GC is triggered by default every time the
  heap size doubles.
* Also, if a GC hasn't been executed during the last
  two minutes, Go will force running one.

```zsh
GODEBUG=gctrace=1 go test -bench=. -v
```

* To conclude with GC, it's essential to understand how
  it behaves to optimize it. As Go developers, we can use
  `GOGC` to configure when the next GC cycle is triggered.
* In most cases, keeping it to `100` should be enough.
  However, if our application can face some peak of requests
  leading to frequent GC and latency impacts,
  we can increase this value.
* Last but not least, in the event of an exceptional
  peak of requests, using the trick to keep the virtual
  heap size to a minimum can be something to consider.
