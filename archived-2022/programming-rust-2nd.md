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
