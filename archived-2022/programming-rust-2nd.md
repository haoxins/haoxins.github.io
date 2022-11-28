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
