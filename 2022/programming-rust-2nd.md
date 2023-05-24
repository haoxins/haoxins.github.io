---
title: Programming Rust - 2nd Edition
description: Fast, Safe Systems Development
date: 2022-09-16
---

> 国庆节前后, 同时看了这两本. (`Programming Rust` 是重温)

- [Programming Rust, 2nd Edition](https://book.douban.com/subject/34973905/)
  - Covers Rust `1.50`
  - 难得有一本技术书籍, 让我读第二遍
  - 第二遍读的时候 (`2022-09` ~ `2022-12`), 已经是 Rust `1.64 ~ 1.66`
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
  `&[T]` or `&str` as "slices", using the
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
    because it owns a heap-allocated buffer.
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

- From `g`'s signature alone, Rust knows it will not
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
return Vec::<i32>::with_capacity(1000); // ok, using ::<
let ramp = (0 .. n).collect::<Vec<i32>>(); // ok, using ::<
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
  specifier, to get a `Debug` view of the error.

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
    return early in the case of `None`:

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
      if let Some(mse) = err.downcast_ref::<MissingSemicolonError>() {
        insert_semicolon_in_source_code(mse.file(), mse.line())?;
        continue; // try again!
      }
      return Err(err);
    }
  }
}
```

### Dealing with Errors That "Can't Happen"

- The best choice then would be to use `.unwrap()`,
  a `Result` method that panics if the result is an `Err`,
  but simply returns the success value of an `Ok`:

```rust
let num = digits.parse::<u64>().unwrap();
```

- This is just like `?` except that if we're
  wrong about this error, if it can happen,
  then in that case we would panic.

### Ignoring Errors

```rust
writeln!(stderr(), "error: {}", err);
// warning: unused result
```

- The idiom `let _ = ...` is used to silence this warning:

```rust
let _ = writeln!(stderr(), "error: {}", err);
// ok, ignore result
```

> 相较之下, 截止 Go `1.19`, unused error 不会 warning.

### Declaring a Custom Error Type

```rust
use std::fmt;

#[derive(Debug, Clone)]
pub struct JsonError {
    pub message: String,
    pub line: usize,
    pub column: usize,
}

impl fmt::Display for JsonError {
    fn fmt(&self, f: &mut fmt::Formatter) -> Result<(), fmt::Error> {
        write!(f, "{} ({}:{})", self.message, self.line, self.column)
    }
}

impl std::error::Error for JsonError {}
```

- `thiserror`, which does all of the previous work
  for you, allowing you to write errors like this:

```rust
use thiserror::Error;

#[derive(Error, Debug)]
#[error("{message:} ({line:}, {column})")]
pub struct JsonError {
    message: String,
    line: usize,
    column: usize,
}
```

## Crates and Modules

> Go 相形见绌

- One function is marked `pub(crate)`, meaning that
  it is available anywhere inside this crate,
  but isn't exposed as part of the external interface.
  - It can't be used by other crates, and it won't
    show up in this crate's documentation.
- Anything that isn't marked `pub` is private and can
  only be used in the same module in which
  it is defined, or any child modules.
- If you want an item in a nested module to be visible
  to other crates, be sure to mark it and all
  enclosing modules as public.
- It's also possible to specify `pub(super)`,
  making an item visible to the parent module only,
  and `pub(in <path>)`, which makes it visible in
  a specific parent module and its descendants.
  - This is especially useful with deeply nested modules.

---

- A module can have its own directory.
  - When Rust sees `mod spores;`, it checks for both
    `spores.rs` and `spores/mod.rs`;
    if neither file exists, or both exist,
    that's an error.
- It's also possible to use a __file__ and
  __directory__ with the __same__ name
  to make up a module.
  - For instance, if `stems` needed to include modules
    called `xylem` and `phloem`, we could choose to keep
    `stems` in `plant_structures/stems.rs` and
    add a `stems` directory:

```
fern_sim/
  Cargo.toml
  src/
    main.rs
    spores.rs
    plant_structures/
      mod.rs
      leaves.rs
      roots.rs
      stems/
        phloem.rs
        xylem.rs
      stems.rs
```

- Then, in `stems.rs`, we declare the two new submodules:

```rust
// in plant_structures/stems.rs
pub mod xylem;
pub mod phloem;
```

### Paths and Imports

- You can use `as` to import an item but
  give it a different name locally.
- Modules __do not__ automatically inherit
  names from their parent modules.
- By default, paths are relative to
  the current module.
  - `self` is also a synonym for the current module,
    so we could write either.
- The keywords `super` and `crate` have a
  special meaning in paths:
  - `super` refers to the parent module,
  - and `crate` refers to the crate
    containing the current module.

```
Using paths relative to the crate root rather than
the current module makes it easier to move code
around the project, since all the imports won't
break if the path of the current module changes.
```

- Submodules can access private items in their
  parent modules with `use super::*`.
- Rust has a special kind of path called an
  absolute path, starting with `::`,
  which always refers to an external crate.

```rust
use ::image::Pixels; // the `image` crate's `Pixels`
```

- To refer to your own module's `Sampler` type,
  you can write:

```rust
use self::image::Sampler; // the `image` module's `Sampler`
```

### Making use Declarations pub

```rust
// in plant_structures/mod.rs
pub use self::leaves::Leaf;
pub use self::roots::Root;
```

- This means that `Leaf` and `Root` are public
  items of the `plant_structures` module.
  - They are still simple aliases for
    `plant_structures::leaves::Leaf` and
    `plant_structures::roots::Root`.

### Making Struct Fields pub

- A struct's fields, even private fields,
  are accessible throughout the module
  where the struct is declared,
  and its submodules.
  - Outside the module, __only__
    public fields are accessible.

### Statics and Constants

- A __constant__ is a bit like a C++ `#define`:
  the value is compiled into your
  code every place it's used.
- A __static__ is a variable that's set up before
  your program starts running
  and lasts until it exits.

---

- By default, `cargo build` looks at the files
  in our source directory and figures out
  what to build.
  - When it sees the file `src/lib.rs`,
    it knows to build a library.
  - The code in `src/lib.rs` forms the
    root module of the library.
  - Other crates that use our library can only
    access the public items of this root module.
- Cargo treats `.rs` files in `src/bin`
  as extra programs to build.

### Attributes

- Some attributes, like `#[cfg]` and `#[allow]`,
  can be attached to a whole module and
  apply to everything in it.
  - Others, like `#[test]` and `#[inline]`,
    must be attached to individual items.
- To attach an attribute to a whole crate,
  add it at the top of the `main.rs` or `lib.rs` file,
  before any items, and write `#!` instead of `#`,
  like this:

```rust
#![allow(non_camel_case_types)]
```

- The `#!` tells Rust to attach an attribute to the
  enclosing item rather than whatever comes next.
- `#!` can also be used inside functions, structs,
  and so on, but it's only typically used at the
  beginning of a file, to attach an attribute
  to the whole module or crate.

### Tests and Documentation

- To test error cases, add the
  `#[should_panic]` attribute to your test:

```rust
#[test]
#[allow(unconditional_panic, unused_must_use)]
#[should_panic(expected = "divide by zero")]
fn test_divide_by_zero_error() {
    // ...
}
```

- So the convention, when your tests get substantial
  enough to require support code, is to put them in
  a tests module and declare the whole module to be
  testing-only using the `#[cfg]` attribute:

```rust
#[cfg(test)] // include this module only when testing
mod tests {
  fn roughly_equal(a: f64, b: f64) -> bool {
    // ...
  }

  #[test]
  fn trig_works() {
    use std::f64::consts::PI;
    assert!(roughly_equal(PI.sin(), 0.0));
  }
}
```

- Integration tests are `.rs` files that live in a
  `tests` directory alongside your
  project's `src` directory.
- `cargo test` runs both unit tests and integration tests.

---

- But when Rust sees comments that start with `three slashes`,
  it treats them as a `#[doc]` attribute instead.
- Likewise, comments starting with `//!` are treated as
  `#![doc]` attributes and are attached to the
  enclosing feature, typically a module or crate.
- When you run tests in a Rust library crate, Rust checks
  that all the code that appears in your documentation
  actually runs and works.

## Structs

- The struct expression `GrayscaleMap { pixels, size }` is
  short for `GrayscaleMap { pixels: pixels, size: size }`.
- Like all other items, structs are private by default,
  visible only in the module where they're
  declared and its submodules.
- That is, creating a struct value requires all the
  struct's fields to be visible.
  - This is why you can't write a struct expression
    to create a new `String` or `Vec`.
- In a struct expression, if the named fields are
  followed by `.. EXPR`, then any fields not mentioned
  take their values from `EXPR`, which must be another
  value of the same struct type.

---

- Individual elements of a tuple-like struct may be
  public or not:

```rust
pub struct Bounds(pub usize, pub usize);
```

- The expression `Bounds(1024, 768)` looks like a
  function call, and in fact it is:
  - defining the type also implicitly
    defines a function:

```rust
fn Bounds(elem0: usize, elem1: usize) -> Bounds { ... }
```

---

- The third kind of struct is a little obscure:
  - it declares a struct type with
    no elements at all:

```rust
struct Onesuch;
```

- A value of such a type occupies no memory,
  much like the unit type `()`.

### Defining Methods with impl

- Rust passes a method the value it's being
  called on as its first argument, which
  __must__ have the special name `self`.

### Passing Self as a Box, Rc, or Arc

- A method's `self` argument can also be a
  `Box<Self>`, `Rc<Self>`, or `Arc<Self>`.
  - Such a method can only be called on a
    value of the given pointer type.
  - Calling the method passes ownership
    of the pointer to it.
- For most methods, `&self`, `&mut self`, and
  `self` (by value) are all you need.
  - But if a method's purpose is to affect the
    ownership of the value, using other pointer
    types for `self` can be just the right thing.

### Type-Associated Functions

- An `impl` block for a given type can also define
  functions that don't take `self` as an argument at all.

### Associated Consts

- As the name implies, associated consts are constant values.
  - They're often used to specify commonly
    used values of a type.

### Generic Structs

```rust
pub struct Queue<T> {
  older: Vec<T>,
  younger: Vec<T>
}
```

```rust
impl<T> Queue<T> {
  pub fn new() -> Queue<T> {
    // ...
  }
  pub fn push(&mut self, t: T) {
    // ...
  }
  pub fn is_empty(&self) -> bool {
    // ...
  }
  // ...
}
```

- However, you'll __always__ need to supply
  type parameters in function signatures
  and type definitions.
  - Rust __doesn't__ infer those; instead,
    it uses those explicit types as the
    basis from which it infers types
    within function bodies.
- `Self` can also be used in this way;
  we could have written `Self { ... }` instead.
- For associated function calls, you can supply
  the type parameter explicitly using the
  `::<>` (turbofish) notation:

```rust
let mut q = Queue::<char>::new();
```

> But in practice, you can usually just let
  Rust figure it out for you.

### Structs with Lifetime Parameters

- Because it's so common for the return type
  to use the same lifetime as an argument,
  Rust lets us omit the lifetimes when
  there's one obvious candidate.

### Deriving Common Traits for Struct Types

```rust
#[derive(Copy, Clone, Debug, PartialEq)]
struct Point {
  x: f64,
  y: f64
}
```

> We can ask Rust to derive `PartialEq` for `Point`
  because its two fields are both of type `f64`,
  which already implements `PartialEq`.

### Interior Mutability

- What we need is a little bit of mutable data
  inside an otherwise immutable value.
  - This is called __interior mutability__.
- Rust offers several flavors of it; in this section,
  we'll discuss the two most straightforward types:
  - `Cell<T>` and `RefCell<T>`,
    both in the `std::cell` module.
- A `Cell<T>` is a struct that contains a single
  private value of type `T`. The only special thing
  about a `Cell` is that you can get and set the
  field even if you don't have `mut`
  access to the `Cell` itself:
  - `Cell::new(value)` Creates a new `Cell`,
    moving the given value into it.
  - `cell.get()` Returns a copy of the value in the cell.
  - `cell.set(value)` Stores the given value in the cell,
    dropping the previously stored value.
  - This method takes `self` as a non-mut reference:
  - `fn set(&self, value: T)`
  - note: __not__ `&mut self`
- Like `Cell<T>`, `RefCell<T>` is a generic type that
  contains a single value of type `T`.
  - Unlike `Cell`, `RefCell` supports borrowing
    references to its `T` value:
  - `RefCell::new(value)` Creates a new `RefCell`,
    moving value into it.
  - `ref_cell.borrow()` Returns a `Ref<T>`,
    which is essentially just a shared reference to
    the value stored in `ref_cell`.
  - This method panics if the value is already mutably borrowed.
  - `ref_cell.borrow_mut()` Returns a `RefMut<T>`, essentially a
    mutable reference to the value in `ref_cell`.
  - This method panics if the value is already borrowed.
  - `ref_cell.try_borrow(), ref_cell.try_borrow_mut()`
  - Work just like `borrow()` and `borrow_mut()`,
    but return a `Result`.
  - Instead of panicking if the value is already mutably borrowed,
    they return an `Err` value.

> cells, and any types that contain them, are __not__ thread-safe.

## Enums

- In memory, values of C-style enums are stored as integers.
  - Occasionally it's useful to tell
    Rust which integers to use:

```rust
enum HttpStatus {
  Ok = 200,
  NotModified = 304,
  NotFound = 404,
  // ...
}
```

- Otherwise Rust will assign the numbers for you,
  starting at `0`.
- By default, Rust stores C-style enums using the
  smallest built-in integer type that
  can accommodate them.
  - __Most__ fit in a single byte.
- Casting a C-style enum to an integer is allowed:
  - `assert_eq!(HttpStatus::Ok as i32, 200);`
- However, casting in the other direction,
  from the integer to the enum, is not.

### Enums with Data

> In all, Rust has three kinds of enum variant,
  echoing the three kinds of struct
  we showed in the previous chapter.

- Variants with no data correspond to unit-like structs.
- Tuple variants look and function just like tuple structs.
- Struct variants have curly braces and named fields.

- All constructors and fields of an enum share the
  __same__ visibility as the enum itself.

### Enums in Memory

- In memory, enums with data are stored as a
  small integer tag, plus enough memory to
  hold all the fields of the largest variant.
  - The tag field is for Rust's internal use.
  - It tells which constructor created the value
    and therefore which fields it has.

### Generic Enums

```rust
enum Option<T> {
  None,
  Some(T),
}

enum Result<T, E> {
  Ok(T),
  Err(E),
}
```

- One unobvious detail is that Rust can eliminate
  the tag field of `Option<T>` when the type `T` is
  a reference, `Box`, or other smart pointer type.
  - Since none of those pointer types is allowed
    to be zero, Rust can represent `Option<Box<i32>>`,
    say, as a single machine word: `0` for `None` and
    nonzero for `Some` pointer.

## Patterns

> Expressions produce values; patterns consume values.
  The two use a lot of the same syntax.

### Literals, Variables, and Wildcards in Patterns

```rust
match meadow.count_rabbits() {
  0 => {}
  1 => println!("..."),
  n => println!("There are {} ...", n),
}
```

### Tuple and Struct Patterns

```rust
fn describe_point(x: i32, y: i32) -> &'static str {
  use std::cmp::Ordering::*;
  match (x.cmp(&0), y.cmp(&0)) {
    (Equal, Equal) => "at the origin",
    (_, Equal) => "on the x axis",
    (Equal, _) => "on the y axis",
    (Greater, Greater) => "in the first quadrant",
    (Less, Greater) => "in the second quadrant",
    _ => "somewhere else",
  }
}
```

```rust
match balloon.location {
  Point { x: 0, y: height } => println!("straight up {} meters", height),
  Point { x: x, y: y } => println!("at ({}m, {}m)", x, y),
}
```

- Patterns like `Point { x: x, y: y }` are common when
  matching structs, and the redundant names are
  visual clutter, so Rust has a shorthand
  for this:
  - `Point {x, y}`.

### Array and Slice Patterns

```rust
fn hsl_to_rgb(hsl: [u8; 3]) -> [u8; 3] {
  match hsl {
    [_, _, 0] => [0, 0, 0],
    [_, _, 255] => [255, 255, 255],
    // ...
  }
}
```

```rust
fn greet_people(names: &[&str]) {
  match names {
    [] => {
      println!("Hello, nobody.")
    }
    [a] => {
      println!("Hello, {}.", a)
    }
    [a, b] => {
      println!("Hello, {} and {}.", a, b)
    }
    [a, .., b] => {
      println!(
        "Hello, everyone from {} to {}.",
        a, b
      )
    }
  }
}
```

### Reference Patterns

- Rust patterns support two features for
  working with references.
  - `ref` patterns borrow parts of a matched value.
  - `&` patterns match references.
- Matching a noncopyable value moves the value.
- You can use `ref mut` to borrow mut references.

---

- The opposite kind of reference pattern is the `&` pattern.
  - A pattern starting with `&` matches a reference.
- This is a bit tricky because Rust is following a
  pointer here, an action we usually associate
  with the `*` operator, not the `&` operator.
- The thing to remember is that patterns and
  expressions are natural opposites.
  - The expression `(x, y)` makes two values into a new tuple,
  - but the pattern `(x, y)` does the opposite:
  - it matches a tuple and breaks out the two values.
- It's the same with `&`.
  - In an expression, `&` creates a reference.
  - In a pattern, `&` matches a reference.

### Match Guards

```rust
match point_to_hex(click) {
  None => Err("That's not a game space."),
  Some(hex) if hex == current_hex => Err("You must click somewhere else!"),
  Some(hex) => Ok(hex),
}
```

- If the pattern matches, but the condition is false,
  matching continues with the next arm.

### Matching Multiple Possibilities

- The vertical bar (`|`) can be used to combine
  several patterns in a single match arm:

```rust
let at_end = match chars.peek() {
  Some(&'\r') | Some(&'\n') | None => true,
  _ => false,
};
```

- Use `..=` to match a whole range of values.

```rust
match next_char {
  '0'..='9' => self.read_number(),
  'a'..='z' | 'A'..='Z' => self.read_word(),
  ' ' | '\t' | '\n' => self.skip_whitespace(),
  _ => self.handle_punctuation(),
}
```

- Rust does not (yet) permit the use of
  end-exclusive ranges like `0..100` in patterns.

### Binding with @ Patterns

- Finally, `x @` pattern matches exactly like the
  given pattern, but on success, instead of
  creating variables for parts of the matched value,
  it creates a single variable `x` and
  moves or copies the whole value into it.

### Where Patterns Are Allowed

- Patterns that always match are special in Rust.
- They're called __irrefutable patterns__,
  and they're the only patterns allowed
  in the four places shown here
  (after `let`, in function arguments,
  after `for`, and in closure arguments).

## Traits and Generics

> The type of `out` is `&mut dyn Write`, meaning
  "a mutable reference to any value that implements the `Write` trait."

- Generics and traits are closely related:
  - generic functions use traits in bounds to spell out
    what types of arguments they can be applied to.
  - So we'll also talk about how `&mut dyn Write` and
    `<T: Write>` are similar, how they're different,
    and how to choose between these
    two ways of using traits.

### Using Traits

- There is one unusual rule about trait methods:
  __the trait itself must be in scope__.
  - Otherwise, all its methods are hidden.
- Rust has this rule because, you can use traits to add
  new methods to any type, even standard library types
  like `u32` and `str`.
  - Third-party crates can do the same thing.
  - Clearly, this could lead to naming conflicts!
  - But since Rust makes you import the traits you
    plan to use, crates are free to take advantage
    of this superpower.

### Trait Objects

- A reference to a trait type, is called a trait object.
  - Like any other reference, a trait object points
    to some value, it has a lifetime, and it can
    be either `mut` or `shared`.
- What makes a trait object different is that Rust
  usually doesn't know the type of the
  referent at compile time.
  - So a trait object includes a little extra
    information about the referent's type.
- In memory, a trait object is a fat pointer consisting
  of a pointer to the value, plus a pointer to a table
  representing that value's type.
  - Again, these aren't fields and data structures
    that you can access directly.
  - Instead, the language automatically uses the
    `vtable` when you call a method of a trait object,
    to determine which implementation to call.

> Rust automatically converts ordinary references
  into trait objects when needed.

- Likewise, Rust will happily convert a
  `Box<File>` to a `Box<dyn Write>`,
  a value that owns a writer in the heap:

```rust
let w: Box<dyn Write> = Box::new(local_file);
```

- `Box<dyn Write>`, like `&mut dyn Write`,
  is a fat pointer: it contains the address of the
  writer itself and the address of the vtable.
  - The same goes for other pointer types,
    like `Rc<dyn Write>`.

### Generic Functions and Type Parameters

```rust
fn say_hello(out: &mut dyn Write) // plain function
fn say_hello<W: Write>(out: &mut W) // generic function
```

- If the generic function you're calling doesn't
  have any arguments that provide useful clues,
  you may have to spell it out:

```rust
let v1 = (0..1000).collect(); // error: type annotations needed
let v2 = (0..1000).collect::<Vec<i32>>();
```

```
It's also possible for a type parameter to have
no bounds at all, but you can't do much with a
value if you haven't specified any bounds for it.
You can move it. You can put it into a box or vector.
That's about it.
```

- Generic functions can have multiple type parameters:

```rust
fn run_query<M: Mapper + Serialize, R: Reducer + Serialize>(
  data: &DataSet,
  map: M,
  reduce: R,
) -> Results {
  unimplemented!()
}
```

- Rust provides an alternative syntax using the keyword `where`:

```rust
fn run_query<M, R>(data: &DataSet, map: M, reduce: R) -> Results
where
  M: Mapper + Serialize,
  R: Reducer + Serialize,
{
  unimplemented!()
}
```

```
This kind of where clause is also allowed on
generic structs, enums, type aliases, and methods
-- anywhere bounds are permitted.
```

- A generic function can have both lifetime parameters
  and type parameters.
  - Lifetime parameters come first.

```rust
fn nearest<'t, 'c, P>(target: &'t P, candidates: &'c [P]) -> &'c P
where
  P: MeasureDistance,
{
  unimplemented!()
}
```

- Lifetimes never have any impact on machine code.
  - Two calls to `nearest()` using the same type `P`,
    but different lifetimes, will call the
    same compiled function.
  - Only differing types cause Rust to compile
    multiple copies of a generic function.

```
All the features introduced in this section -- bounds,
where clauses, lifetime parameters, and so forth -- can
be used on all generic items, not just functions.
```

### Default Methods

```rust
trait Write {
  fn write(&mut self, buf: &[u8]) -> Result<usize>;

  fn flush(&mut self) -> Result<()>;

  fn write_all(&mut self, buf: &[u8]) -> Result<()> {
    let mut bytes_written = 0;
    while bytes_written < buf.len() {
      bytes_written += self.write(&buf[bytes_written..])?;
    }
    Ok(())
  }
  // ...
}
```

```
Your own traits can include default implementations
using the same syntax.

The most dramatic use of default methods in the
standard library is the Iterator trait,
which has one required method (.next())
and dozens of default methods.
```

### Traits and Other People's Types

- Rust lets you implement any trait on any type,
  as long as either the trait or the type
  is introduced in the current crate.
  - This means that any time you want to add a
    method to any type, you can use
    a trait to do it:

```rust
trait IsEmoji {
  fn is_emoji(&self) -> bool;
}

impl IsEmoji for char {
  fn is_emoji(&self) -> bool {
    unimplemented!()
  }
}
```

> Like any other trait method, this new `is_emoji` method
  is only visible when `IsEmoji` is in scope.

- The sole purpose of this particular trait is to
  add a method to an existing type, `char`.
  - This is called an __extension trait__.
- You can even use a generic impl block to add an
  extension trait to a whole family of types at once.
  - This trait could be implemented on any type:

```rust
use std::io::{self, Write};

trait WriteHtml {
  fn write_html(&mut self, html: &HtmlDocument) -> io::Result<()>;
}

impl<W: Write> WriteHtml for W {
  fn write_html(&mut self, html: &HtmlDocument) -> io::Result<()> {
    unimplemented!()
  }
}
```

- The line `impl<W: Write> WriteHtml for W` means
  "for every type `W` that implements `Write`,
  here's an implementation of `WriteHtml` for `W`."

### Self in Traits

- A trait can use the keyword `Self` as a type.

```rust
pub trait Spliceable {
  fn splice(&self, other: &Self) -> Self;
}
```

- A trait that uses the `Self` type is
  incompatible with trait objects:

```rust
// error: the trait `Spliceable` cannot be made into an object
fn splice_anything(left: &dyn Spliceable, right: &dyn Spliceable) {
  let combo = left.splice(right);
  // ...
}
```

- Rust rejects this code because it has no way to
  type-check the call `left.splice(right)`.
- The whole point of trait objects is that the
  type isn't known until run time.

---

- Now, had we wanted genetically improbable splicing,
  we could have designed a trait-object-friendly trait:

```rust
pub trait MegaSpliceable {
  fn splice(&self, other: &dyn MegaSpliceable) -> Box<dyn MegaSpliceable>;
}
```

- This trait is compatible with trait objects.
- There's no problem type-checking calls to this
  `.splice()` method because the type of the argument
  `other` is not required to match the type of `self`,
  as long as both types are `MegaSpliceable`.

### Subtraits

```rust
trait Creature: Visible {
  // ...
}
```

- In Rust, a subtrait does not inherit the associated
  items of its supertrait; each trait still needs to be
  in scope if you want to call its methods.
- In fact, Rust's subtraits are really just a shorthand
  for a bound on `Self`.
  - A definition of `Creature` like this is exactly
    equivalent to the one shown earlier:

```rust
trait Creature where Self: Visible {
  // ...
}
```

### Fully Qualified Method Calls

- First of all, it helps to know that a method is
  just a special kind of function.
  - These two calls are equivalent:

```rust
"hello".to_string()
str::to_string("hello")
```

- Since `to_string` is a method of the standard
  `ToString` trait, there are two more
  forms you can use:

```rust
ToString::to_string("hello")
<str as ToString>::to_string("hello")
```

- All four of these method calls do exactly the same thing.
  - Most often, you'll just write `value.method()`.
  - The other forms are qualified method calls.
  - They specify the type or trait that a
    method is associated with.
  - The last form, with the angle brackets,
    specifies both: a fully qualified method call.

### Associated Types (or How Iterators Work)

- Rust has a standard `Iterator` trait,
  defined like this:

```rust
pub trait Iterator {
  type Item;
  fn next(&mut self) -> Option<Self::Item>;
  // ...
}
```

- The type is written as `Self::Item`,
  not just plain `Item`, because `Item`
  is a feature of each type of iterator,
  not a standalone type.

---

- Here's what it looks like to implement
  `Iterator` for a type:

```rust
impl Iterator for Args {
  type Item = String;
  fn next(&mut self) -> Option<String> {
    unimplemented!()
  }
  // ...
}
```

### Generic Traits (or How Operator Overloading Works)

- Multiplication in Rust uses this trait:

```rust
pub trait Mul<RHS> {
  type Output;
  fn mul(self, rhs: RHS) -> Self::Output;
}
```

> `Mul` is a generic trait. The type parameter,
  `RHS`, is short for righthand side.

```
Generic traits get a special dispensation when it
comes to the orphan rule: you can implement a
foreign trait for a foreign type, so long as
one of the trait's type parameters is a
type defined in the current crate.
```

- The trait shown earlier is missing one minor detail.
  - The real `Mul` trait looks like this:

```rust
pub trait Mul<RHS=Self> {
  // ...
}
```

- The syntax `RHS=Self` means that `RHS` defaults to `Self`.
  - If I write `impl Mul for Complex`, without specifying
    `Mul`'s type parameter, it means `impl Mul<Complex> for Complex`.
  - In a bound, if I write `where T: Mul`, it means `where T: Mul<T>`.
- In Rust, the expression `lhs * rhs` is shorthand for
  `Mul::mul(lhs, rhs)`.
  - So overloading the `*` operator in Rust is as simple as
    implementing the `Mul` trait.

### impl Trait

- `impl Trait` allows us to "erase" the type of a return value,
  specifying only the trait or traits it implements,
  without dynamic dispatch or a heap allocation:

```rust
fn cyclical_zip(v: Vec<u8>, u: Vec<u8>) -> impl Iterator<Item = u8> {
  v.into_iter().chain(u.into_iter()).cycle()
}
```

- It might be tempting to use `impl Trait` to approximate a
  statically dispatched version of the factory pattern
  that's commonly used in object-oriented languages.
  - For example, you might define a trait like this:

```rust
trait Shape {
  fn new() -> Self;
  fn area(&self) -> f64;
}
```

- It's important to note that Rust doesn't allow
  trait methods to use `impl Trait` return values.

---

- `impl Trait` can also be used in functions
  that take generic arguments.
  - For instance, consider this simple generic function:

```rust
fn print<T: Display>(val: T) {
  println!("{}", val);
}
```

- It is identical to this version using `impl Trait`:

```rust
fn print(val: impl Display) {
  println!("{}", val);
}
```

- There is one important exception. Using generics allows
  callers of the function to specify the type of the
  generic arguments, like `print::<i32>(42)`,
  while using `impl Trait` does not.
- Each `impl Trait` argument is assigned its own
  anonymous type parameter, so `impl Trait` for arguments
  is limited to only the simplest generic functions,
  with no relationships between the types of arguments.

### Associated Consts

- You can declare a trait with an associated constant
  using the same syntax as for a struct or enum:

```rust
trait Greet {
  const GREETING: &'static str = "Hello";
  fn greet(&self) -> String;
}
```

- Like associated types and functions,
  you can declare them but not give them a value:

```rust
trait Float {
  const ZERO: Self;
  const ONE: Self;
}
```

- Then, implementors of the trait can define these values:

```rust
impl Float for f64 {
  const ZERO: f64 = 0.0;
  const ONE: f64 = 1.0;
}
```

- This allows you to write generic code that uses these values:

```rust
fn add_one<T: Float + Add<Output = T>>(value: T) -> T {
  value + T::ONE
}
```

## Operator Overloading

- In Rust, the expression `a + b` is actually shorthand for
  `a.add(b)`, a call to the `add` method of the
  standard library's `std::ops::Add` trait.
  - Similar traits cover the other operators:
    `a * b` is shorthand for `a.mul(b)`,
    a method from the `std::ops::Mul` trait,
    `std::ops::Neg` covers the prefix `-`
    negation operator, and so on.

> Here's the definition of `std::ops::Add`:

```rust
trait Add<Rhs = Self> {
  type Output;
  fn add(self, rhs: Rhs) -> Self::Output;
}
```

> The trait's type parameter `Rhs` defaults to `Self`.

```rust
use std::ops::Add;
impl<T> Add for Complex<T>
where
  T: Add<Output = T>,
{
  type Output = Self;
  fn add(self, rhs: Self) -> Self {
    Complex {
      re: self.re + rhs.re,
      im: self.im + rhs.im,
    }
  }
}
```

- Rust's built-in traits for arithmetic and bitwise
  operators come in three groups:
  - unary operators,
  - binary operators,
  - and compound assignment operators.

### Unary Operators

```rust
trait Neg {
  type Output;
  fn neg(self) -> Self::Output;
}
trait Not {
  type Output;
  fn not(self) -> Self::Output;
}
```

### Binary Operators

- The definition of `std::ops::BitXor`,
  for the `^` operator, looks like this:

```rust
trait BitXor<Rhs = Self> {
  type Output;
  fn bitxor(self, rhs: Rhs) -> Self::Output;
}
```

### Compound Assignment Operators

> In Rust, the value of a compound assignment expression
  is always `()`, never the value stored.

- Instead, `x += y` is shorthand for the method call
  `x.add_assign(y)`, where `add_assign` is the sole method
  of the `std::ops::AddAssign` trait:

```rust
trait AddAssign<Rhs = Self> {
  fn add_assign(&mut self, rhs: Rhs);
}
```

- The built-in trait for a compound assignment operator
  is completely independent of the built-in trait for the
  corresponding binary operator.
  - Implementing `std::ops::Add` does __not__ automatically
    implement `std::ops::AddAssign`;
  - if you want Rust to permit your type as the lefthand
    operand of a `+=` operator, you must
    implement `AddAssign` yourself.

### Equivalence Comparisons

- These get tedious to write, and equality is a common
  operation to support, so if you ask, Rust will generate
  an implementation of `PartialEq` for you automatically.
  - Simply add `PartialEq` to the type definition's
    derive attribute like so:

```rust
#[derive(Clone, Copy, Debug, PartialEq)]
struct Complex<T> {
  // ...
}
```

- Since `str` implements `PartialEq<str>`, the
  following assertions are equivalent:

```rust
assert!("ungula" != "ungulate");
assert!("ungula".ne("ungulate"));
```

- So while Rust's `==` operator meets the first two
  requirements for equivalence relations, it clearly
  doesn't meet the third when used on
  IEEE floating-point values.
  - This is called a partial equivalence relation, so
    Rust uses the name `PartialEq` for the `==`
    operator's built-in trait.
  - If you write generic code with type parameters
    known only to be `PartialEq`, you may assume the
    first two requirements hold, but you should not
    assume that values always equal themselves.
- If you'd prefer your generic code to require a
  full equivalence relation, you can instead use the
  `std::cmp::Eq` trait as a bound, which represents a
  full equivalence relation:
  - if a type implements `Eq`, then `x == x` must be
    `true` for every value `x` of that type.
- In practice, almost every type that implements
  `PartialEq` should implement `Eq` as well;
  `f32` and `f64` are the __only__ types in the
  standard library that are `PartialEq` but __not__ `Eq`.

---

- The standard library defines `Eq` as an
  extension of `PartialEq`, adding no new methods:

```rust
trait Eq: PartialEq<Self> {}
```

- If your type is `PartialEq` and you would like
  it to be `Eq` as well, you __must__ explicitly
  implement `Eq`, even though you need not actually
  define any new functions or types to do so.
  - So implementing `Eq` for our `Complex` type is quick:

```rust
impl<T: Eq> Eq for Complex<T> {}
```

- We could implement it even more succinctly by just
  including `Eq` in the derive attribute
  on the `Complex` type definition:

```rust
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Complex<T> {
  // ...
}
```

- Derived implementations on a generic type may
  depend on the type parameters.
  - With the derive attribute, `Complex<i32>`
    would implement `Eq`, because `i32` does,
  - but `Complex<f32>` would only implement `PartialEq`,
    since `f32` doesn't implement `Eq`.
- When you implement `std::cmp::PartialEq` yourself,
  Rust can't check that your definitions for the
  `eq` and `ne` methods actually behave as required
  for partial or full equivalence.

### Ordered Comparisons

- Rust specifies the behavior of the
  ordered comparison operators
  `<`, `>`, `<=`, and `>=` all in
  terms of a single trait,
  `std::cmp::PartialOrd`:

```rust
trait PartialOrd<Rhs = Self>: PartialEq<Rhs>
where
  Rhs: ?Sized,
{
  fn partial_cmp(&self, other: &Rhs) -> Option<Ordering>;
  fn lt(&self, other: &Rhs) -> bool {
    todo!()
  }
  fn le(&self, other: &Rhs) -> bool {
    todo!()
  }
  fn gt(&self, other: &Rhs) -> bool {
    todo!()
  }
  fn ge(&self, other: &Rhs) -> bool {
    todo!()
  }
}
```

- The only method of `PartialOrd` you must implement
  yourself is `partial_cmp`.
  - When `partial_cmp` returns `Some(o)`, then `o`
    indicates self's relationship to other:

```rust
enum Ordering {
  Less, // self < other
  Equal, // self == other
  Greater, // self > other
}
```

- But if `partial_cmp` returns `None`, that means `self` and
  other are unordered with respect to each other:
  - neither is greater than the other,
  - nor are they equal.
- Among all of Rust's primitive types, only comparisons between
  floating-point values ever return `None`:
  - specifically, comparing a `NaN` (not-a-number) value
    with anything else returns `None`.

> If you know that values of two types are always ordered
  with respect to each other, then you can implement the
  stricter `std::cmp::Ord` trait.

- Almost all types that implement `PartialOrd` should
  also implement `Ord`.
  - In the standard library, `f32` and `f64` are
    the only exceptions to this rule.

### Index and IndexMut

- You can specify how an indexing expression like
  `a[i]` works on your type by implementing the
  `std::ops::Index` and `std::ops::IndexMut` traits.
  - Arrays support the `[]` operator directly,
    but on any other type, the expression `a[i]` is
    normally shorthand for `*a.index(i)`, where index
    is a method of the `std::ops::Index` trait.
  - However, if the expression is being assigned to
    or borrowed mutably, it's instead shorthand for
    `*a.index_mut(i)`, a call to the method of the
    `std::ops::IndexMut` trait.

```rust
trait Index<Idx> {
  type Output: ?Sized;
  fn index(&self, index: Idx) -> &Self::Output;
}
trait IndexMut<Idx>: Index<Idx> {
  fn index_mut(&mut self, index: Idx) -> &mut Self::Output;
}
```

## Utility Traits

### Drop

```
Drops occur under a variety of circumstances:
when a variable goes out of scope;
at the end of an expression statement;
when you truncate a vector,
removing elements from its end; and so on.
```

- When a value is dropped, if it implements
  `std::ops::Drop`, Rust calls its `drop` method,
  before proceeding to drop whatever values its
  fields or elements own, as it normally would.

```
If a variable's value gets moved elsewhere,
so that the variable is uninitialized when
it goes out of scope, then Rust
will not try to drop that variable:
there is no value in it to drop.
```

> Although a value may be moved from place to place,
  Rust drops it only once.

- If a type implements `Drop`,
  it cannot implement the `Copy` trait.
  - If a type is `Copy`, that means that simple
    byte-for-byte duplication is sufficient to
    produce an independent copy of the value.
  - But it is typically a mistake to call the same
    drop method more than once on the same data.

### Sized

- A sized type is one whose values all have
  the same size in memory.
  - Almost all types in Rust are sized:
  - every `u64` takes eight bytes,
  - every `(f32, f32, f32)` tuple twelve.
- Even enums are sized:
  - no matter which variant is actually present,
  - an enum always occupies enough space
    to hold its __largest__ variant.
- And although a `Vec<T>` owns a heap-allocated buffer
  whose size can vary, the `Vec` value itself is a
  pointer to the buffer, its capacity, and its length,
  so `Vec<T>` is a sized type.
- All sized types implement the `std::marker::Sized` trait,
  which has no methods or associated types.
  - Rust implements it automatically for all types to
    which it applies; you can't implement it yourself.
  - The only use for `Sized` is as a bound for type variables:
  - a bound like `T: Sized` requires `T` to be a type whose
    size is known at compile time.
  - Traits of this sort are called marker traits,
    because the Rust language itself uses them to mark
    certain types as having characteristics of interest.

---

- Rust can't store unsized values in variables or
  pass them as arguments. You can only deal with
  them through pointers like `&str` or `Box<dyn Write>`,
  which themselves are sized.
- Since unsized types are so limited, most generic type
  variables should be restricted to `Sized` types.
  - In fact, this is necessary so often that it is the
    implicit default in Rust:
  - if you write struct `S<T> { ... }`, Rust understands
    you to mean struct `S<T: Sized> { ... }`.
  - If you do not want to constrain `T` this way, you must
    explicitly opt out, writing struct `S<T: ?Sized> { ... }`.
  - The `?Sized` syntax is specific to this case and means
    "not necessarily Sized."
  - For example, if you write struct `S<T: ?Sized> { b: Box<T> }`,
    then Rust will allow you to write `S<str>` and `S<dyn Write>`,
    where the box becomes a fat pointer, as well as
    `S<i32>` and `S<String>`, where the box is an ordinary pointer.
- When a type variable has the `?Sized` bound, people often
  say it is questionably sized:
  - it might be `Sized`, or it might not.

---

- Aside from slices and trait objects,
  there is one more kind of unsized type.
  - A struct type's last field (but only its last)
    may be unsized, and such a struct is itself unsized.
  - For example, an `Rc<T>` reference-counted pointer is
    implemented internally as a pointer to the private
    type `RcBox<T>`, which stores the reference count
    alongside the `T`.
- Here's a simplified definition of `RcBox`:

```rust
struct RcBox<T: ?Sized> {
  ref_count: usize,
  value: T,
}
```

- The value field is the `T` to which `Rc<T>` is counting references;
  `Rc<T>` dereferences to a pointer to this field.
  - The `ref_count` field holds the reference count.

### Clone

- Cloning a value usually entails allocating copies of
  anything it owns, as well, so a clone can be expensive,
  in both time and memory.
- The reference-counted pointer types like `Rc<T>` and
  `Arc<T>` are exceptions:
  - cloning one of these simply increments the
    reference count and hands you a new pointer.

### Copy

- But because `Copy` is a marker trait with special
  meaning to the language, Rust permits a type to
  implement `Copy` only if a shallow byte-for-byte
  copy is all it needs.
  - Types that own any other resources, like
    heap buffers or operating system handles,
    cannot implement `Copy`.
- Any type that implements the `Drop` trait cannot be `Copy`.

### Deref and DerefMut

- You can specify how dereferencing operators like
  `*` and `.` behave on your types by implementing
  the `std::ops::Deref` and `std::ops::DerefMut` traits.
  - Pointer types like `Box<T>` and `Rc<T>` implement
    these traits so that they can behave as
    Rust's built-in pointer types do.

---

- Although the deref coercions aren't anything you
  couldn't write out explicitly yourself,
  they're convenient:
  - If you have some `Rc<String>` value `r` and want to
    apply `String::find` to it, you can simply write
    `r.find('?')`, instead of `(*r).find('?')`:
  - the method call implicitly borrows `r`, and
    `&Rc<String>` coerces to `&String`, because
    `Rc<T>` implements `Deref<Target=T>`.
  - You can use methods like `split_at` on `String` values,
    even though `split_at` is a method of the `str` slice type,
    because `String` implements `Deref<Target=str>`.
  - There's no need for `String` to reimplement
    all of `str`'s methods, since you can
    coerce a `&str` from a `&String`.
  - If you have a vector of bytes `v` and you want to pass
    it to a function that expects a byte slice `&[u8]`,
    you can simply pass `&v` as the argument,
    since `Vec<T>` implements `Deref<Target=[T]>`.
- Rust will apply several deref coercions in succession if necessary.
  - For example, using the coercions mentioned before,
    you can apply `split_at` directly to an `Rc<String>`, since
    `&Rc<String>` dereferences to `&String`,
    which dereferences to `&str`,
    which has the `split_at` method.

### Default

- All of Rust's collection types: `Vec`, `HashMap`,
  `BinaryHeap`, and so on, implement `Default`,
  with default methods that return an empty collection.
- Another common use of `Default` is to produce default
  values for structs that represent a large collection
  of parameters, most of which you won't
  usually need to change.
- If a type `T` implements `Default`, then the
  standard library implements `Default` automatically
  for `Rc<T>`, `Arc<T>`, `Box<T>`, `Cell<T>`,
  `RefCell<T>`, `Cow<T>`, `Mutex<T>`, and `RwLock<T>`.
- If all the element types of a tuple type implement
  `Default`, then the tuple type does too,
  defaulting to a tuple holding each
  element's default value.
- Rust does not implicitly implement `Default` for
  struct types, but if all of a struct's fields
  implement `Default`, you can implement `Default` for
  the struct automatically using `#[derive(Default)]`.

### AsRef and AsMut

- When a type implements `AsRef<T>`, that means you can
  borrow a `&T` from it efficiently.
  - `AsMut` is the analogue for mutable references.
- So, for example, `Vec<T>` implements `AsRef<[T]>`, and
  `String` implements `AsRef<str>`.
  - You can also borrow a `String`'s contents as an
    array of bytes, so `String`
    implements `AsRef<[u8]>` as well.
- Although `AsRef` and `AsMut` are pretty simple,
  providing standard, generic traits for reference
  conversion avoids the proliferation of more
  specific conversion traits.
  - You should avoid defining your own `AsFoo` traits
    when you could just implement `AsRef<Foo>`.

### Borrow and BorrowMut

- The `std::borrow::Borrow` trait is similar to `AsRef`:
  - if a type implements `Borrow<T>`, then its borrow method
    efficiently borrows a `&T` from it.
- But `Borrow` imposes more restrictions:
  - a type should implement `Borrow<T>` only when a `&T`
    hashes and compares the same way as the
    value it's borrowed from.
  - (Rust doesn't enforce this; it's just the
    documented intent of the trait.)
  - This makes `Borrow` valuable in dealing with keys
    in hash tables and trees or when dealing with
    values that will be hashed or
    compared for some other reason.
- `Borrow` is designed to address a specific situation
  with generic hash tables and
  other associative collection types.

### From and Into

- `From` and `Into` take ownership of their argument,
  transform it, and then return ownership
  of the result back to the caller.
- Given an appropriate `From` implementation,
  the standard library automatically implements
  the corresponding `Into` trait.
- The `?` operator uses `From` and `Into` to help
  clean up code in functions that could fail in
  multiple ways by automatically converting from
  specific error types to general ones when needed.

### TryFrom and TryInto

- Where `From` and `Into` relate types with simple
  conversions, `TryFrom` and `TryInto` extend the
  simplicity of `From` and `Into` conversions with
  the expressive error handling afforded by Result.

### ToOwned

- Unlike `clone`, which must return exactly `Self`,
  `to_owned` can return anything you could borrow a
  `&Self` from:
  - the `Owned` type must implement `Borrow<Self>`.
  - You can borrow a `&[T]` from a `Vec<T>`, so
    `[T]` can implement `ToOwned<Owned=Vec<T>>`,
    as long as `T` implements `Clone`,
  - so that we can copy the slice's elements into the vector.
  - Similarly, `str` implements `ToOwned<Owned=String>`,
    `Path` implements `ToOwned<Owned=PathBuf>`, and so on.

## Closures

- Rust thus offers two ways for closures to
  get data from enclosing scopes:
  - moves and borrowing.
- Just as everywhere else in the language,
  if a closure would move a value of a copyable type,
  like `i32`, it copies the value instead.
- Values of noncopyable types,
  like `Vec<City>`, really are moved.

---

- Well, a closure is callable, but it's not a `fn`.
- In fact, every closure you write has its own type,
  because a closure may contain data:
  - values either borrowed or stolen from enclosing scopes.
  - This could be any number of variables,
    in any combination of types.
  - So every closure has an ad hoc type created
    by the compiler, large enough to hold that data.
- No two closures have exactly the same type.
  - But every closure implements an `Fn` trait;
    the closure in our example implements
    `Fn(&City) -> i64`.

### FnOnce

> As with functions, the return type can be omitted
  if it's `()`; `Fn()` is shorthand for `Fn() -> ()`.

```rust
trait Fn() -> R {
  fn call(&self) -> R;
}

trait FnOnce() -> R {
  fn call_once(self) -> R;
}
```

- Just as an arithmetic expression like `a + b` is
  shorthand for a method call, `Add::add(a, b)`,
  Rust treats `closure()` as shorthand for one
  of the two trait methods shown in the preceding example.
  - For an `Fn` closure, `closure()` expands to `closure.call()`.
  - This method takes `self` by reference,
    so the closure is not moved.
  - But if the closure is only safe to call once, then
    `closure()` expands to `closure.call_once()`.
  - That method takes `self` by value, so the closure is used up.

### FnMut

```rust
trait Fn() -> R {
  fn call(&self) -> R;
}

trait FnMut() -> R {
  fn call_mut(&mut self) -> R;
}

trait FnOnce() -> R {
  fn call_once(self) -> R;
}
```

- Any closure that requires `mut` access to a value,
  but doesn't drop any values, is an `FnMut` closure.

---

- `Fn` is the family of closures and functions that
  you can call multiple times without restriction.
  - This highest category also includes all `fn` functions.
- `FnMut` is the family of closures that can be called
  multiple times if the closure itself is declared `mut`.
- `FnOnce` is the family of closures that can be
  called once, if the caller owns the closure.

---

- Every `Fn` meets the requirements for `FnMut`,
  and every `FnMut` meets the requirements for `FnOnce`.
  - Instead, `Fn()` is a subtrait of `FnMut()`,
    which is a subtrait of `FnOnce()`.
  - This makes `Fn` the most exclusive and
    most powerful category.
  - `FnMut` and `FnOnce` are broader categories that
    include closures with usage restrictions.

### Copy and Clone for Closures

- Just as Rust automatically figures out which closures
  can be called only once, it can figure out which
  closures can implement `Copy` and `Clone`, and which cannot.
- As we explained earlier, closures are represented as
  structs that contain either the values
  (for move closures) or references to the values
  (for non-move closures) of the variables they capture.
  - The rules for `Copy` and `Clone` on closures are just
    like the `Copy` and `Clone` rules for regular structs.

### Callbacks

- In fact, closures that don't capture anything from
  their environment are identical to function pointers,
  since they don't need to hold any extra
  information about captured variables.

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

## Iterators

- An iterator is any value that implements the
  `std::iter::Iterator` trait:

```rust
trait Iterator {
  type Item;

  fn next(&mut self) -> Option<Self::Item>;

  // ...
  // many default methods
}
```

- If there's a natural way to iterate over some type,
  that type can implement `std::iter::IntoIterator`,
  whose `into_iter` method takes a value and
  returns an iterator over it:

```rust
trait IntoIterator where Self::IntoIter: Iterator<Item=Self::Item> {
  type Item;
  type IntoIter: Iterator;
  fn into_iter(self) -> Self::IntoIter;
}
```

- `IntoIter` is the type of the iterator value itself,
  and `Item` is the type of value it produces.

## Concurrency

- `Sender<T>` implements the `Clone` trait.
  To get a channel with multiple senders,
  simply create a regular channel and clone
  the sender as many times as you like.
  - You can move each `Sender` value
    to a different thread.
- A `Receiver<T>` can't be cloned, so if you
  need to have multiple threads receiving values
  from the same channel, you need a `Mutex`.

- A synchronous channel is exactly like a
  regular channel except that when you create it,
  you specify how many values it can hold.
  - For a synchronous channel, `sender.send(value)`
    is potentially a blocking operation.
  - After all, the idea is that
    blocking is not always bad.

### Thread Safety: Send and Sync

- Rust's full thread safety story hinges on
  two built-in traits, `std::marker::Send`
  and `std::marker::Sync`.
  - Types that implement `Send` are safe to pass
    by value to another thread.
  - Types that implement `Sync` are safe to pass
    by non-mut reference to another thread.
- When you spawn a thread, the closure you pass
  __must__ be `Send`, which means all the values
  it contains must be `Send`.
- Similarly, if you want to send values through a
  channel to another thread,
  the values __must__ be `Send`.

---

- Creating a new `Mutex` looks like creating a new
  `Box` or `Arc`, but while `Box` and `Arc` signify
  heap allocation, `Mutex` is solely about locking.
- `Arc` is handy for sharing things across threads,
  and `Mutex` is handy for mutable data
  that's shared across threads.

```
In fact, a mutex is little more than a way to
do exactly this, to provide exclusive (mut) access
to the data inside, even though many threads may
have shared (non-mut) access to the Mutex itself.
```

> Rust's borrow system can't protect you from deadlock.
> It's also possible to get deadlock with channels.

- If a thread panics while holding a `Mutex`,
  Rust marks the `Mutex` as __poisoned__.
  - Any subsequent attempt to lock the poisoned
    `Mutex` will get an error result.

### Condition Variables (Condvar)

- In Rust, the `std::sync::Condvar` type implements
  condition variables.
  - A `Condvar` has methods `.wait()` and `.notify_all()`;
  - `.wait()` blocks until some other
    thread calls `.notify_all()`.

## Input and Output

- Rust's standard library features for input and output
  are organized around three traits,
  `Read`, `BufRead`, and `Write`:
  - Values that implement `Read` have methods for
    byte-oriented input. They're called __readers__.
  - Values that implement `BufRead` are buffered readers.
    They support all the methods of `Read`,
    plus methods for reading lines of text and so forth.
  - Values that implement `Write` support both
    byte-oriented and UTF-8 text output.
    They're called __writers__.

## Strings and Text

- The char type implements `Copy` and `Clone`,
  along with all the usual traits for
  comparison, hashing, and formatting.
  - A string slice can produce an iterator over its
    characters with `slice.chars()`.

### String and str

- Rust places text-handling methods on either `str`
  or `String` depending on whether the method needs
  a resizable buffer or is content just
  to use the text in place.
- Since `String` dereferences to `&str`, every method
  defined on `str` is directly available
  on `String` as well.
  - These methods index text by byte offsets and
    measure its length in bytes,
    rather than characters.
- A `String` is implemented as a wrapper around a
  `Vec<u8>` that ensures the vector's contents are
  always well-formed UTF-8.
  - Rust will never change `String` to use a more
    complicated representation,
  - so you can assume that `String` shares
    `Vec`'s performance characteristics.
