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
