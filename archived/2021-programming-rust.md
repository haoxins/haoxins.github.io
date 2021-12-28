---
title: Rust
description: 惟江上之清风, 与山间之明月, 耳得之而为声, 目遇之而成色, 取之无禁, 用之不竭.
date: 2021-04-10
---

### Ecosystems

* [SeaORM](https://github.com/SeaQL/sea-orm)

* [axum](https://github.com/tokio-rs/axum)

* [rkyv](https://github.com/djkoloski/rkyv)
  - zero-copy

------------------

# Timeline

------------------

## 2021

* [SeaORM](https://github.com/SeaQL/sea-orm)
  - 期待 `v1.0`

* [An update on Memory Safety in Chrome](https://security.googleblog.com/2021/09/an-update-on-memory-safety-in-chrome.html)
  - September 21, 2021

```
We've started to land limited, non-user-facing
Rust experiments in the Chromium source code tree,
but we're not yet using it in production versions
of Chrome - we remain in an experimental phase.
```

* [Diesel 2.0](https://github.com/diesel-rs/diesel/milestone/16)
  - 期待 2021 发布
  - BTW: `1.0.0`, `2018-01`

* [axum](https://github.com/tokio-rs/axum)
  - axum is a web application framework that focuses on ergonomics and modularity.
  - Tokio 团队 2021 新作! 目前尚且简陋, 但值得期待!

* [Launching Rust Cloud Native](https://nickgerace.dev/post/launching-rust-cloud-native)
  - https://github.com/rust-cloud-native
  - https://rust-cloud-native.github.io

* Arti: reimplementing Tor in Rust
  - https://www.torproject.org

* [Rocket](https://github.com/SergioBenitez/Rocket)
  - Version 0.5.0-rc.1 (Jun 09, 2021)
  - 期待 `v1.0`

* [Crust of Rust: Dispatch and Fat Pointers](https://www.youtube.com/watch?v=xcygqF5LVmM)
  - name is hard (hahahaha)

* [Crust of Rust: Atomics and Memory Ordering](https://www.youtube.com/watch?v=rMGWeSjctlY)

* [程序君的 Rust 培训 (1)](https://www.bilibili.com/video/BV19b4y1o7Lt)

* 2021-05-11: The Plan for the **Rust 2021** Edition

```
We are happy to announce that the third edition
of the Rust language, Rust 2021,
is scheduled for release in October.
Rust 2021 contains a number of small changes that are
nonetheless expected to make a significant improvement
to how Rust feels in practice.
```

* [Mozilla Welcomes the Rust Foundation](https://blog.mozilla.org/blog/2021/02/08/mozilla-welcomes-the-rust-foundation/)
  - [Hello World!](https://foundation.rust-lang.org/posts/2021-02-08-hello-world/)
  - Facebook Joins the Rust Foundation (2021-04-29)

* [Models of Generics and Metaprogramming: Go, Rust, Swift, D and More](https://thume.ca/2019/07/14/a-tour-of-metaprogramming-models-for-generics/)

### Advanced

* [Smart Pointers](https://doc.rust-lang.org/book/ch15-00-smart-pointers.html)

* [Fearless Concurrency](https://doc.rust-lang.org/book/ch16-00-concurrency.html)

* [Advanced Features](https://doc.rust-lang.org/book/ch19-00-advanced-features.html)

### 美妙之处

* **反复强调** 从 Docs, eBook, 编译器, 工具链 全方位的强调设计理念
* **暴露细节** 指引大家去了解, 而非屏蔽细节
* **提供便利** 友好详尽的 Warning Error 信息
* **兼容并蓄** 纯粹的 FP 难以流行, OO 的糟粕不宜提倡
  - 单纯把所谓的 Modern language 的语法整合在一起并不难
  - 取舍 融合 融洽 不突兀 是高手
* **社区氛围** 这一点后期很难改变
  - 所幸 Rust 诞生之初, 社区并未蓬勃, 得以聚集优良的信念
  - 后来也会有噪音, 但好在优良的基因已经种下
  - 较之 **Node.js (npm)** 社区, 一开始便太多噪音

```
In Rust, the compiler plays a gatekeeper role by
refusing to compile code with these elusive bugs,
including concurrency bugs.
```

* `2015-05-15` **Rust 1.0**

```
Every two or three years, the Rust team produces
a new Rust edition. Each edition brings together
the features that have landed into a clear package
with fully updated documentation and tooling.

New editions ship as part of the
usual six-week release process.
```

### Basic

```rust
// Immutable first
let x = 666;
let mut y = 996;
```

```
An instance of `io::Result` has an `expect`
method that you can call.
If this instance of `io::Result` is an `Err` value,
`expect` will cause the program to crash and
display the message that you passed as
an argument to `expect`.

Like `Result`, `Ordering` is another enum,
but the variants for `Ordering` are
`Less`, `Greater`, and `Equal`.

Shadowing lets us reuse the variable name
rather than forcing us to create
two unique variables.

You declare constants using the `const` keyword
instead of the `let` keyword, and the type
of the value must be `annotated`.

Shadowing is different from marking a
variable as `mut`, because we'll get a
compile-time error if we accidentally try
to reassign to this variable without
using the `let` keyword.

The other difference between `mut` and `shadowing`
is that because we're effectively creating a new
variable when we use the `let` keyword again,
we can change the type of the value
but reuse the same name.
```

> Cool

* Shadowing

```rust
// 虽说不是很特别的特性, 但在项目中确实能增加美感
let mut guess = String::new();

io::stdin()
  .read_line(&mut guess)
  .expect("Failed to read line");

let guess: u32 = guess.trim().parse()
  .expect("Please type a number!");
```

```
Rust's char type is four bytes in size
and represents a Unicode Scalar Value.
```

```rust
// Tuple
let tup = (500, 6.4, 1);
let (x, y, z) = tup;

let x: (i32, f64, u8) = (500, 6.4, 1);
let five_hundred = x.0;
let six_point_four = x.1;
```

```
Arrays in Rust are different from arrays
in some other languages because
arrays in Rust have a fixed length, like tuples.
```

```
Statements are instructions that perform some
action and do not return a value.
Expressions evaluate to a resulting value.
```

```rust
let x = 5; // statement

let y = { // expression
  let x = 3;
  x + 1
};

// Expressions do not include ending semicolons.
// If you add a semicolon to the end of an expression,
// you turn it into a statement,
// which will then not return a value.

fn plus_one(x: i32) -> i32 {
  x + 1
}
```

```rust
// Returning Values from Loops
let mut counter = 0;

let result = loop {
  counter += 1;

  if counter == 10 {
    break counter * 2;
  }
};

// Looping Through a Collection with for
let a = [10, 20, 30, 40, 50];
let mut index = 0;

while index < 5 {
  println!("the value is: {}", a[index]);
  index += 1;
}

for number in (1..4).rev() {
  println!("{}!", number);
}
```

* Ownership
  - Each value in Rust has a variable that's called its owner.
  - There can only be **one owner at a time**.
  - When the owner goes out of scope, the value will be dropped.
  - **Drop**, **Move**

```
All data stored on the stack must have a known, fixed size.

Pushing to the stack is faster than allocating
on the heap because the allocator never has to
search for a place to store new data;
that location is always at the top of the stack.

Accessing data in the heap is slower than accessing
data on the stack because you have to follow
a pointer to get there.

Contemporary processors are faster if they
jump around less in memory.
```

```
When a variable goes out of scope,
Rust calls a special function for us.
This function is called `drop`.

Note: In C++, this pattern of deallocating resources
at the end of an item's lifetime is sometimes called
`Resource Acquisition Is Initialization` (RAII).

This pattern has a profound impact on the way Rust
code is written. It may seem simple right now, but
the behavior of code can be unexpected in more
complicated situations when we want to have multiple
variables use the data we've allocated on the heap.
```

```
If you've heard the terms shallow copy and deep copy
while working with other languages,
the concept of copying the pointer, length, and capacity
without copying the data probably sounds like
making a shallow copy. But because Rust also invalidates
the first variable, instead of being called a
shallow copy, it's known as a move.
```

```
Rust will never automatically create "deep" copies
of your data. Therefore, any automatic copying can
be assumed to be inexpensive in terms of
runtime performance.
```

* Here are some of the types that implement `Copy`:
  - All the `integer` types
  - The `Boolean` type
  - All the `floating point` types
  - The `character` type, `char`
  - `Tuples`, if they only contain types
    that also implement `Copy`
  - For example, `(i32, i32)` implements `Copy`,
    but `(i32, String)` does not

```
The semantics for passing a value to a function
are similar to those for assigning a value
to a variable.
Passing a variable to a function will `move` or `copy`,
just as assignment does.
```

* References and Borrowing

```rust
let s1 = String::from("hello");
let len = calculate_length(&s1);
```

```
Just as variables are immutable by default,
so are references. We're not allowed to modify
something we have a reference to.

But mutable references have one big restriction:
you can have only one mutable reference to
a particular piece of data in a particular scope.

We also cannot have a mutable reference
while we have an immutable one.

Note that a reference's scope starts from
where it is introduced and continues through
the last time that reference is used.
```

* Another data type that does not have
  **ownership** is the **slice**

```rust
let s = String::from("hello world");

let hello = &s[0..5];
let world = &s[6..11];
```

* Structs vs Tuples

```rust
// Tuples
fn main() {
  let rect1 = (30, 50);

  println!(
    "The area of the rectangle is {} square pixels.",
    area(rect1)
  );
}

fn area(dimensions: (u32, u32)) -> u32 {
  dimensions.0 * dimensions.1
}
```

```rust
// Structs
struct Rectangle {
  width: u32,
  height: u32,
}

impl Rectangle {
  fn area(&self) -> u32 {
    self.width * self.height
  }
}

fn main() {
  let rect1 = Rectangle {
    width: 30,
    height: 50,
  };

  println!(
    "The area of the rectangle is {} square pixels.",
    rect1.area()
  );
}
```

```rust
// Associated functions are often used for constructors
// that will return a new instance of the struct.

impl Rectangle {
  fn square(size: u32) -> Rectangle {
    Rectangle {
      width: size,
      height: size,
    }
  }
}

let sq = Rectangle::square(3);
```

* Enums and Pattern Matching

```rust
// v1
enum IpAddrKind {
  V4,
  V6,
}

let six = IpAddrKind::V6;

// v2
enum IpAddr {
  V4(String),
  V6(String),
}

let loopback = IpAddr::V6(String::from("::1"));

// v3
enum IpAddr {
  V4(u8, u8, u8, u8),
  V6(String),
}

let home = IpAddr::V4(127, 0, 0, 1);
let loopback = IpAddr::V6(String::from("::1"));

// v4
struct Ipv4Addr {
  // ...
}

struct Ipv6Addr {
  // ...
}

enum IpAddr {
  V4(Ipv4Addr),
  V6(Ipv6Addr),
}
```

```
There is one more similarity between enums and structs:
just as we're able to define methods on structs using impl,
we're also able to define methods on enums.
```

```
Rust does not have nulls, but it does have an enum that
can encode the concept of a value being present or absent.
This enum is `Option<T>`
```

```rust
let coin = Coin::Penny;
let mut count = 0;

// match
match coin {
  Coin::Quarter(state) => println!("State quarter from {:?}!", state),
  _ => count += 1,
}

// if let
if let Coin::Quarter(state) = coin {
  println!("State quarter from {:?}!", state);
} else {
  count += 1;
}
```

```
In other words, you can think of `if let`
as syntax sugar for a match that runs code
when the value matches one pattern
and then ignores all other values.
```

* The module system
  - **Packages**: A **Cargo** feature that
    lets you build, test, and share crates
  - Crates: A tree of modules that produces
    a library or executable
  - **Modules**: Let you control the organization,
    scope, and privacy of paths
  - Paths: A way of naming an item, such as a
    `struct`, `function`, or `module`

* Packages and Crates

```
The way privacy works in Rust is that all items
(functions, methods, structs, enums,
modules, and constants)
are private by default.

Items in a parent module can't use the private
items inside child modules, but items in child
modules can use the items in their ancestor modules.
```

```
Enums aren't very useful unless their variants
are public; it would be annoying to have to
annotate all enum variants with pub in every case,
so the default for enum variants is to be `public`.

Structs are often useful without their fields
being public, so struct fields follow the general
rule of everything being private by default
unless annotated with pub.
```

```rust
use std::{cmp::Ordering, io};

use std::collections::*;

// v1
use std::io;
use std::io::Write;

// v2
use std::io::{self, Write};
```

* Storing Lists of Values with Vectors

```rust
let v: Vec<i32> = Vec::new();
// macro
let v = vec![1, 2, 3];
```

```
When we run this code, the first [] method will
cause the program to panic because it
references a nonexistent element.
This method is best used when you want your
program to crash if there's an attempt to access
an element past the end of the vector.

When the get method is passed an index that
is outside the vector, it returns
None without panicking.
You would use this method if accessing an
element beyond the range of the vector happens
occasionally under normal circumstances.
```

```
adding a new element onto the end of the
vector might require allocating new memory
and copying the old elements to the new space,
if there isn't enough room to put all the
elements next to each other where
the vector currently is.

In that case, the reference to the first element
would be pointing to deallocated memory.
The borrowing rules prevent programs from
ending up in that situation.
```

```rust
let v = vec![100, 32, 57];
for i in &v {
  println!("{}", i);
}
```

```rust
let mut v = vec![100, 32, 57];
for i in &mut v {
  *i += 50;
}
```

> when we need to store elements of a
  different type in a `vector`,
  we can define and use an `enum`!

* Rust strings don't support indexing
  - A `String` is a wrapper over a `Vec<u8>`

```rust
for c in "नमस्ते".chars() {
  println!("{}", c);
}

for b in "नमस्ते".bytes() {
  println!("{}", b);
}
```

* Hash Maps

```rust
let teams = vec![String::from("Blue"), String::from("Yellow")];
let initial_scores = vec![10, 50];

let mut scores: HashMap<_, _> =
  teams.into_iter().zip(initial_scores.into_iter()).collect();
```

```
If we insert references to values into the hash map,
the values won't be moved into the hash map.
The values that the references point to
must be valid for at least as long as
the hash map is valid.
```

```rust
let mut scores = HashMap::new();
scores.insert(String::from("Blue"), 10);

scores.entry(String::from("Yellow")).or_insert(50);
scores.entry(String::from("Blue")).or_insert(50);
```

* Updating a Value Based on the Old Value

```rust
let text = "hello world wonderful world";

let mut map = HashMap::new();

for word in text.split_whitespace() {
  let count = map.entry(word).or_insert(0);
  *count += 1;
}
```

* Error Handling

```
Rust groups errors into two major categories:
recoverable and unrecoverable errors.

Most languages don't distinguish between these
two kinds of errors and handle both in the
same way, using mechanisms such as exceptions.

Rust doesn't have exceptions.
Instead, it has the type `Result<T, E>` for
recoverable errors and the `panic!` macro that
stops execution when the program encounters
an unrecoverable error.
```

```toml
[profile.release]
panic = 'abort'
```

> Let's try getting a backtrace by setting
  the `RUST_BACKTRACE` environment variable
  to any value except `0`.

```rust
// v1
let f = File::open("hello.txt");

let f = match f {
  Ok(file) => file,
  Err(error) => match error.kind() {
    ErrorKind::NotFound => match File::create("hello.txt") {
      Ok(fc) => fc,
      Err(e) => panic!("Problem creating the file: {:?}", e),
    },
    other_error => {
      panic!("Problem opening the file: {:?}", other_error)
    }
  },
};

// v2
let f = File::open("hello.txt").unwrap_or_else(|error| {
  if error.kind() == ErrorKind::NotFound {
    File::create("hello.txt").unwrap_or_else(|error| {
      panic!("Problem creating the file: {:?}", error);
    })
  } else {
    panic!("Problem opening the file: {:?}", error);
  }
});
```

```
The ? placed after a `Result` value is defined to
work in almost the same way as the match expressions
we defined to handle the `Result` values.

If the value of the `Result` is an `Ok`, the value
inside the `Ok` will get returned from this
expression, and the program will continue.

If the value is an `Err`, the `Err` will be returned
from the whole function as if we had used the
return keyword so the error value gets
propagated to the calling code.
```

```rust
// v1
fn read_username_from_file() -> Result<String, io::Error> {
  let mut f = File::open("hello.txt")?;
  let mut s = String::new();
  f.read_to_string(&mut s)?;
  Ok(s)
}

// v2
fn read_username_from_file() -> Result<String, io::Error> {
  let mut s = String::new();

  File::open("hello.txt")?.read_to_string(&mut s)?;

  Ok(s)
}

// v3
fn read_username_from_file() -> Result<String, io::Error> {
  fs::read_to_string("hello.txt")
}
```

* The **?** Operator Can Be Used in
  **Functions That Return Result**

```
The ? operator can be used in functions
that have a return type of `Result`,
because it is defined to work in the
same way as the match expression.
The part of the match that requires a
return type of `Result` is return `Err(e)`,
so the return type of the function has
to be a `Result` to be compatible
with this return.
```

```rust
fn main() -> Result<(), Box<dyn Error>> {
  let f = File::open("hello.txt")?;

  Ok(())
}
```

* Generic Types, Traits, and Lifetimes

```rust
struct Point<T> {
  x: T,
  y: T,
}

impl<T> Point<T> {
  fn x(&self) -> &T {
    &self.x
  }
}

// mixup

struct Point<T, U> {
  x: T,
  y: U,
}

impl<T, U> Point<T, U> {
  fn mixup<V, W>(self, other: Point<V, W>) -> Point<T, W> {
    Point {
      x: self.x,
      y: other.y,
    }
  }
}

let p1 = Point { x: 5, y: 10.4 };
let p2 = Point { x: "Hello", y: 'c' };
let p3 = p1.mixup(p2);
```

```
Rust accomplishes this by performing
monomorphization of the code that is
using generics at compile time.
Monomorphization is the process of
turning generic code into specific code
by filling in the concrete types
that are used when compiled.
```

* Trait Bound Syntax

```rust
// v1
pub fn notify(item1: &impl Summary, item2: &impl Summary)
// v2
pub fn notify<T: Summary>(item1: &T, item2: &T)

// +

// v1
pub fn notify(item: &(impl Summary + Display))
// v2
pub fn notify<T: Summary + Display>(item: &T)
```

* Lifetimes `'`

```rust
fn longest_with_an_announcement<'a, T>(
  x: &'a str,
  y: &'a str,
  ann: T,
) -> &'a str
where
  T: Display,
{
  println!("Announcement! {}", ann);
  if x.len() > y.len() {
    x
  } else {
    y
  }
}
```

* Closures

```
To define a closure, we start with
a pair of vertical pipes (|),
inside which we specify the parameters
to the closure; this syntax was chosen
because of its similarity to closure
definitions in Smalltalk and Ruby.
```

* Making Useful Documentation Comments

```rust
/// Documentation
///
/// # Examples
///
/// ```
/// code here!
/// ```
```
