---
title: Programming Rust - 2nd Edition
description: Fast, Safe Systems Development
date: 2022-09-16
---

> 国庆节前后, 同时看了这两本. (`Programming Rust` 是重温)

- [Programming Rust, 2nd Edition](https://book.douban.com/subject/34973905/)
  - Covers Rust `1.50`
  - 难得有一本技术书籍, 让我读第二遍
  - 第二遍读的时候 (`2022-09` ~), 已经是 Rust `1.64`
  - 第一遍读的时候 (`2021-07` ~ `2022-01`), 貌似是 Rust `1.54+`

---

- It's common to initialize a struct's fields with
  variables of the __same name__, so rather than
  forcing you to write `Complex { re: re, im: im }`,
  Rust lets you simply write `Complex { re, im }`.

- The unit type, written `()`, is akin to `void` in C++.

```
It's a common beginner's mistake to attempt to
use ? in the main function.
However, since main itself doesn't return a value,
this won't work; instead, you need to use a match statement,
or one of the shorthand methods like unwrap and expect.
There's also the option of simply changing main to
return a Result.
```

- When an integer arithmetic operation overflows,
  Rust panics, in a `debug` build.
- In a `release` build, the operation wraps around:
  - it produces the value equivalent to the
    mathematically correct result modulo
    the range of the value.

---

- Rust uses the `char` type for single characters in isolation,
  but uses the UTF-8 encoding for strings and streams of text.
  - So, a `String` represents its text as a sequence of
    UTF-8 bytes, __not__ as an array of characters.

- Further, tuples allow only constants as indices, like `t.4`.
  - You __can't__ write `t.i` or `t[i]` to get the `ith` element.
- The other commonly used tuple type is the zero-tuple `()`.
  - This is traditionally called the unit type because
    it has only one value, also written `()`.

### References

- The expression `&x` produces a reference to `x`;
  in Rust terminology, we say that it borrows
  a reference to `x`.
  - Given a reference `r`, the expression `*r`
    refers to the value `r` points to.
- Rust references come in two flavors:
  - `&T`
  - An immutable, shared reference.
  - `&mut T`
  - A mutable, exclusive reference.

### Boxes

- The simplest way to allocate a value
  in the heap is to use `Box::new`.

### Raw Pointers

```
Using a raw pointer is unsafe, because Rust
makes no effort to track what it points to.
```

### Arrays, Vectors, and Slices

- The type `[T; N]` represents an array of `N` values,
  each of type `T`.
  - An array's size is a constant determined at
    compile time and is part of the type; you
    can't append new elements or shrink an array.
- The type `Vec<T>`, called a vector of `T`s, is a
  dynamically allocated, growable sequence
  of values of type `T`.
- The types `&[T]` and `&mut [T]`, called a __shared slice__
  of `T`s and __mutable slice__ of `T`s, are references to
  a series of elements that are a part of some other value,
  like an array or vector.
  - A __mutable slice__ `&mut [T]` lets you read and modify
    elements, but can't be shared;
  - a __shared slice__ `&[T]` lets you share access among
    several readers, but doesn't let you modify elements.

```
Rust has no notation for an uninitialized array.

An array's length is part of its type
and fixed at compile time.
```

- A `Vec<T>` consists of three values:
  - a pointer to the heap-allocated
    buffer for the elements, which is
    created and owned by the `Vec<T>`;
  - the number of elements that buffer
    has the capacity to store;
  - and the number it actually contains now
    (in other words, its length).
- When the buffer has reached its capacity,
  adding another element to the vector
  entails allocating a larger buffer,
  copying the present contents into it,
  updating the vector's pointer and capacity
  to describe the new buffer,
  and finally freeing the old one.

---

- A slice, written `[T]` without specifying the length,
  is a region of an array or vector.
  - Slices are __always__ passed by reference.
  - A reference to a slice is a fat pointer:
  - a two-word value comprising a pointer to
    the slice's first element, and
    the number of elements in the slice.
- Since slices __almost always__ appear behind
  references, we often just refer to types like
  `&[T]` or `&str` as "slices," using the
  shorter name for the more common concept.

### String

- Rust offers __raw strings__. A raw string is
  tagged with the lowercase letter `r`.
  - All backslashes and whitespace characters inside
    a raw string are included verbatim in the string.
  - The start and end of a raw string can be
    marked with pound signs:
  - You can add as few or as many pound signs as needed
    to make it clear where the raw string ends.
- A string literal with the `b` prefix is a __byte string__.
  - Such a string is a slice of `u8` values, that is,
    bytes, rather than Unicode text.

---

- You can think of a `String` as a `Vec<u8>` that is
  guaranteed to hold well-formed UTF-8;
  - in fact, this is how `String` is implemented.
- A `&str` is a reference to a run of UTF-8 text
  owned by someone else: it "borrows" the text.
  - A `&str` is a fat pointer, containing both
    the address of the actual data and its length.
  - You can think of a `&str` as being nothing
    more than a `&[u8]` that is guaranteed to
    hold well-formed UTF-8.
- A `String` or `&str`'s `.len()` method returns its length.
  - The length is measured in bytes, __not__ characters.
- It is impossible to modify a `&str`.
- The type `&mut str` does exist,
  but it is not very useful.

## Ownership and Moves

### Moves

- Returning values from a function
- Constructing new values
- Passing values to a function

---

- There are two things to keep in mind.
  - First, the moves always apply to the value proper,
    __not__ the heap storage they own.
  - For vectors and strings, the value proper is the
    three-word header alone; the potentially large
    element arrays and text buffers sit
    where they are in the heap.
  - Second, the Rust compiler's code generation is
    good at "seeing through" all these moves;
    in practice, the machine code often stores
    the value directly where it belongs.

---

- Assigning a value of a `Copy` type copies the value,
  rather than moving it.
  - Passing `Copy` types to functions and
    constructors behaves similarly.
  - A tuple or fixed-size array of
    `Copy` types is itself a `Copy` type.
  - Only types for which a simple
    bit-for-bit copy suffices
    can be `Copy`.
  - `String` is __not__ a `Copy` type,
    because it owns a
    heap-allocated buffer.
  - `Box<T>` is __not__ `Copy`; it owns
    its heap-allocated referent.
- As a rule of thumb, any type that needs to
  do something special when a value is
  dropped __cannot__ be `Copy`:
  - a `Vec` needs to free its elements,
    a `File` needs to close its file handle,
    a `MutexGuard` needs to unlock its mutex,
    and so on.
  - Bit-for-bit duplication of such types would
    leave it unclear which value was now
    responsible for the original's resources.
- If all the fields of your struct are themselves `Copy`,
  then you can make the type `Copy` as well by placing
  the attribute `#[derive(Copy, Clone)]`
  above the definition.

### Rc and Arc: Shared Ownership

- The `Rc` and `Arc` types are very similar;
  the only difference between them is that an
  `Arc` is safe to share between threads directly.
  - The name `Arc` is short for __atomic reference count__.
- Cloning an `Rc<T>` value __does not__ copy the `T`;
  instead, it simply creates another pointer to it
  and increments the reference count.
- A value owned by an `Rc` pointer is __immutable__.

## References

> Rust also has non-owning pointer types called __references__,
  which have no effect on their referents' lifetimes.

```
In fact, it's rather the opposite:
references must never outlive their referents.
You must make it apparent in your code that no
reference can possibly outlive the value it points to.
To emphasize this, Rust refers to creating a reference
to some value as borrowing the value:
what you have borrowed,
you must eventually return to its owner.
```

- Shared references are `Copy`.
- Mutable references are __not__ `Copy`.

### Working with References

- In Rust, references are created explicitly
  with the `&` operator, and dereferenced explicitly
  with the `*` operator.
  - To create a mutable reference,
    use the `&mut` operator.
- Since references are so widely used in Rust,
  the `.` operator implicitly __dereferences__
  its __left__ operand, if needed.
- The `.` operator can also implicitly __borrow__ a
  reference to its __left__ operand,
  if needed for a method call.

```rust
let mut v = vec![1973, 1968];
v.sort(); // implicitly borrows a mutable reference to v
(&mut v).sort(); // equivalent, but more verbose
```

### References to References

- The `.` operator follows as many references
  as it takes to find its target

### Comparing References

- Like the `.` operator, Rust's comparison operators
  "see through" any number of references

```rust
let x = 10;
let y = 10;
let rx = &x;
let ry = &y;
let rrx = &rx;
let rry = &ry;

assert!(rrx <= rry);
assert!(rrx == rry);
```

- If you actually want to know whether two references
  point to the same memory, you can use `std::ptr::eq`,
  which compares them as addresses.
  - Note that the operands of a comparison must have
    exactly the same type, including the references.

### Receiving References as Function Arguments

- Rust's equivalent of a global variable is called a `static`:
  it's a value that's created when the program starts
  and lasts until it terminates.
  - Like any other declaration, Rust's module system controls
    where statics are visible, so they're only "global" in
    their lifetime, not their visibility.
- Every static __must__ be initialized.
- Mutable statics are inherently __not__ thread-safe,
  and even in single-threaded programs,
  they can fall prey to other sorts of reentrancy problems.
  - For these reasons, you may access a mutable static
    only within an `unsafe` block.

> In Rust, a function's signature always
  exposes the body's behavior.

### Passing References to Functions

```rust
fn g<'a>(p: &'a i32) { ... }
let x = 10;
g(&x);
```

- From `g's` signature alone, Rust knows it will not
  save `p` anywhere that might outlive the call:
  - any lifetime that encloses the call must work for `'a`.
- So Rust chooses the smallest possible lifetime for `&x`:
  - that of the call to `g`.
- This meets all constraints:
  - it doesn't outlive `x`,
  - and it encloses the entire call to `g`.

### Returning References

- When a function takes a single reference as
  an argument and returns a single reference,
  Rust assumes that the two __must__
  have the same lifetime.

### Structs Containing References

- Whenever a reference type appears inside another
  type's definition, you must write out its lifetime.

- Every type in Rust has a lifetime, including
  `i32` and `String`.
  - Most are simply `'static`, meaning that values
    of those types can live for as long as you like;
  - for example, a `Vec<i32>` is self-contained and
    needn't be dropped before any particular variable
    goes out of scope.
- But a type like `Vec<&'a i32>` has a lifetime that
  must be enclosed by `'a`:
  - it must be dropped while its referents are still alive.

### Omitting Lifetime Parameters

- If there are multiple lifetimes among your parameters,
  then there's no natural reason to prefer one over
  the other for the return value, and Rust makes you
  spell out what's going on.
- If your function is a method on some type and takes
  its `self` parameter by reference, then that
  __breaks__ the tie:
  - Rust assumes that `self`'s lifetime is the one to
    give everything in your return value.
  - Rust assumes that whatever you're borrowing,
    you're borrowing from `self`.

### Sharing Versus Mutation

- Shared access is read-only access.

```
Values borrowed by shared references are read-only.
Across the lifetime of a shared reference,
neither its referent,
nor anything reachable from that referent,
can be changed by anything.
There exist no live mutable references to anything
in that structure, its owner is held read-only,
and so on. It's really frozen.
```

- Mutable access is exclusive access.

```
A value borrowed by a mutable reference is
reachable exclusively via that reference.
Across the lifetime of a mutable reference,
there is no other usable path to its referent
or to any value reachable from there.
The only references whose lifetimes may overlap
with a mutable reference are those you borrow
from the mutable reference itself.
```

## Expressions

- Blocks are the most general kind of expression.
  - A block produces a value and can be
    used anywhere a value is needed.
  - When you leave the semicolon off the last line
    of a block, that makes the value of the block
    the value of its final expression,
    rather than the usual `()`.

- There is one more `if` form, the `if let` expression:

```rust
if let pattern = expr {
  block1
} else {
  block2
}
```

> Sometimes this is a nice way to get
  data out of an `Option` or `Result`.

- It's never strictly necessary to use `if let`,
  because `match` can do everything `if let` can do.
  - An `if let` expression is shorthand for a
    `match` with just one pattern:

```rust
match expr {
  pattern => { block1 }
  _ => { block2 }
}
```

- Loops are expressions in Rust, but the value of a
  `while` or `for` loop is always `()`,
  so their value isn't very useful.
  - A `loop` expression can produce a value
    if you specify one.
- Iterating over a `mut` reference provides a
  `mut` reference to each element.

---

- Within the body of a `loop`, you can give `break`
  an expression, whose value becomes
  that of the `loop`:

```rust
let answer = loop {
  if let Some(line) = next_line() {
    if line.starts_with("answer: ") {
      break line;
    }
  } else {
    break "answer: nothing";
  }
};
```

- A `break` can have both a `label`
  and a `value` expression:

```rust
let sqrt = 'outer: loop {
  let n = next_number();
  for i in 1.. {
    let square = i * i;
    if square == n {
      break 'outer i;
    }
    if square > n {
      break;
    }
  }
};
```

- Labels can also be used with `continue`.

- `return` without a value is shorthand for `return ()`.

### Why Rust Has loop?

```
Rust went for simplicity. Its flow-sensitive analyses
do not examine loop conditions at all, instead simply
assuming that any condition in a program
can be either true or false.
```

- Expressions that don't finish normally are assigned
  the special type `!`, and they're exempt from the
  rules about types having to match.

---

- One quirk of Rust syntax is that in a function call
  or method call, the usual syntax for generic types,
  `Vec<T>`, does not work:

```rust
return Vec<i32>::with_capacity(1000); // error
let ramp = (0 .. n).collect<Vec<i32>>(); // same error
```

- The problem is that in expressions,
  `<` is the less-than operator.
  - The Rust compiler helpfully suggests writing
    `::<T>` instead of `<T>` in this case,
    and that solves the problem:

```rust
return Vec::<i32>::with_capacity(1000); // ok, using ::< let ramp = (0 .. n)
collect::<Vec<i32>>(); // ok, using ::<
```

- The symbol `::<...>` is affectionately known
  in the Rust community as the turbofish.
- Alternatively, it is often possible to drop the
  type parameters and let Rust infer them:

```rust
return Vec::with_capacity(10); // ok, if the fn return type is Vec<i32>
let ramp: Vec<i32> = (0 .. n).collect(); // ok, variable's type is given
```

- The `..` operator allows either operand to be omitted;
  it produces up to four different types of object
  depending on which operands are present:

```rust
.. // RangeFull
a .. // RangeFrom { start: a }
.. b // RangeTo { end: b }
a .. b // Range { start: a, end: b }
```

- The latter two forms are end-exclusive (or half-open):
  - the end value is __not included__
    in the range represented.
- The `..=` operator produces end-inclusive (or closed)
  ranges, which do include the end value:

```rust
..= b // RangeToInclusive { end: b }
a ..= b // RangeInclusive::new(a, b)
```

- Only ranges that include a start value are iterable,
  since a loop must have somewhere to start.
  - But in array slicing, all six forms are useful.
  - If the start or end of the range is omitted,
    it defaults to the start or end of
    the data being sliced.

### Type Casts

- Numbers may be cast from any of the
  built-in numeric types to any other.
  - Converting from a floating-point type to
    an integer type rounds toward zero:
    the value of `-1.99` as `i32` is `-1`.
  - If the value is too large to fit in the
    integer type, the cast produces the closest
    value that the integer type can represent:
    the value of `1e6` as `u8` is `255`.
- Several more significant automatic conversions
  can happen, though:
  - Values of type `&String` auto-convert to
    type `&str` without a cast.
  - Values of type `&Vec<i32>` auto-convert to `&[i32]`.
  - Values of type `&Box<Chessboard>`
    auto-convert to `&Chessboard`.

> These are called `deref coercions`, because they apply
  to types that implement the `Deref` built-in trait.

## Error Handling

- Rust can either `unwind` the stack when a panic
  happens or `abort` the process.
  - `Unwinding` is the __default__.
- Panic is __safe__. It doesn't violate any of Rust's safety rules.
  - It would be unsafe to proceed, so Rust unwinds the stack.
  - But the rest of the process can continue running.
- Panic is __per thread__. One thread can be panicking while
  other threads are going on about their normal business.
- Stack unwinding is the default panic behavior,
  but there are two circumstances in which Rust
  does __not__ try to unwind the stack.
  - If a `.drop()` method triggers a second panic while
    Rust is still trying to clean up after the first,
    this is considered fatal. Rust stops unwinding
    and aborts the whole process.
- Also, Rust's panic behavior is customizable.
  If you compile with `-C panic=abort`,
  the first panic in your program
  immediately aborts the process.

### Result Type Aliases

- Sometimes you'll see Rust documentation that
  seems to omit the error type of a `Result`:

```rust
fn remove_file(path: &Path) -> Result<()>
```

- This means that a `Result` type alias is being used.
- Modules often define a `Result` type alias to avoid
  having to repeat an error type that's used
  consistently by almost every
  function in the module.

### Printing Errors

- Printing an error with the `{}` format specifier
  typically displays only a brief error message.
- Alternatively, you can print with the `{:?}` format
  specifier, to get a Debug view of the error.

### Propagating Errors

- You can add a `?` to any expression that produces
  a `Result`, such as the result of a function call:

```rust
let weather = get_weather(hometown)?;
```

- The behavior of `?` depends on whether this
  function returns a success result
  or an error result:
  - On success, it unwraps the `Result` to
    get the success value inside.
  - On error, it immediately returns from the
    enclosing function, passing the error
    result up the call chain.
  - To ensure that this works, `?` can only be
    used on a `Result` in functions that
    have a `Result` return type.

- `?` also works similarly with the `Option` type.
  - In a function that returns `Option`,
    you can use `?` to unwrap a value and
    return early in the case of None:

```rust
let weather = get_weather(hometown).ok()?;
```

### Working with Multiple Error Types

- If you're calling a function that returns a
  `GenericResult` and you want to handle one
  particular kind of error but let all
  others propagate out, use the generic method
  `error.downcast_ref::<ErrorType>()`.
  - It borrows a reference to the error,
    if it happens to be the particular
    type of error you're looking for:

```rust
loop {
  match compile_project() {
    Ok(()) => return Ok(()),
    Err(err) => {
      if let Some(mse) = err.downcast_ref:: <MissingSemicolonError>() {
        insert_semicolon_in_source_code(mse.file(), mse.line())?;
        continue; // try again!
      }
      return Err(err); }
  }
}
```

### Dealing with Errors That "Can't Happen"

------------------

- [On Java 中文版 进阶卷](https://book.douban.com/subject/35751623/)
  - `2022-09`: 最近有一些思考, 我觉得 Go 会比 Java 先被淘汰
  - 淘汰不是指消失, 而是不再是主流
  - 何为主流: `2022`年, C++ 可以勉强算主流, 但 C 肯定不算了
  - 说白了就是平时用到的开源项目, 你需要偶尔去看代码 Debug 的

```java
import java.util.List;

sealed interface Transport {};

record Bicycle(String id) implements Transport {};

record Glider(int size) implements Transport {};

record Surfboard(double weight) implements Transport {};

public class SealedPatternMatch {
    static String exhaustive(Transport t) {
        return switch (t) {
            case Bicycle b -> "Bicycle " + b.id();
            case Glider g -> "Glider " + g.size();
            case Surfboard s -> "Surfboard " + s.weight();
        };
    }

    public static void main(String[] args) {
        List.of(new Bicycle("Bob"), new Glider(65), new Surfboard(6.4)).forEach(t -> System.out.println(exhaustive(t)));
        try {
            exhaustive(null);
        } catch (NullPointerException e) {
            System.out.println("Not exhaustive: " + e);
        }
    }
}
```
