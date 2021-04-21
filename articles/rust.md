---
title: Rust
description: 惟江上之清风, 与山间之明月, 耳得之而为声, 目遇之而成色, 取之无禁, 用之不竭.
date: 2021-04-10
---

### Macro (!)

### Others

* 减少内存分配和拷贝
  - zero-copy [rkyv](https://github.com/djkoloski/rkyv)

------------------

# Timeline

------------------

## 2021

* [Crust of Rust: Atomics and Memory Ordering](https://www.youtube.com/watch?v=rMGWeSjctlY)

* [Mozilla Welcomes the Rust Foundation](https://blog.mozilla.org/blog/2021/02/08/mozilla-welcomes-the-rust-foundation/)
  - [Hello World!](https://foundation.rust-lang.org/posts/2021-02-08-hello-world/)

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
  - 较之 Node.js (npm) 社区, 一开始便太多噪音

```
In Rust, the compiler plays a gatekeeper role by
refusing to compile code with these elusive bugs,
including concurrency bugs.
```

### 理念细节 (By code)

```rust
// Immutable first
let x = 666;
let mut y = 996;
```

```
An instance of `io::Result` has an `expect` method that you can call.
If this instance of `io::Result` is an `Err` value,
`expect` will cause the program to crash and display the message
that you passed as an argument to `expect`.

Like `Result`, `Ordering` is another enum,
but the variants for `Ordering` are `Less`, `Greater`, and `Equal`.

Shadowing lets us reuse the variable name rather than
forcing us to create two unique variables.

You declare constants using the `const` keyword
instead of the `let` keyword, and the type of the value
must be `annotated`.

Shadowing is different from marking a variable as `mut`,
because we'll get a compile-time error if we accidentally try to
reassign to this variable without using the `let` keyword.

The other difference between `mut` and `shadowing` is that
because we're effectively creating a new variable
when we use the `let` keyword again,
we can change the type of the value but reuse the same name.

> Cool
```

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
Statements are instructions that perform some action and
do not return a value.
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

Pushing to the stack is faster than allocating on the heap
because the allocator never has to search for a place to store new data;
that location is always at the top of the stack.

Accessing data in the heap is slower than accessing data on the stack
because you have to follow a pointer to get there.
Contemporary processors are faster if they jump around less in memory.

> restaurant 的例子不错
```

```
When a variable goes out of scope,
Rust calls a special function for us.
This function is called `drop`.

Note: In C++, this pattern of deallocating resources
at the end of an item's lifetime is sometimes called
`Resource Acquisition Is Initialization` (RAII).

This pattern has a profound impact on the way Rust code is written.
It may seem simple right now, but the behavior of code can be
unexpected in more complicated situations when we want to have
multiple variables use the data we've allocated on the heap.
```

```
If you've heard the terms shallow copy and deep copy
while working with other languages,
the concept of copying the pointer, length, and capacity
without copying the data probably sounds like making a shallow copy.
But because Rust also invalidates the first variable,
instead of being called a shallow copy, it's known as a move.
```

```
Rust will never automatically create "deep" copies of your data.
Therefore, any automatic copying can be assumed to be inexpensive
in terms of runtime performance.
```

* Here are some of the types that implement `Copy`:
  - All the `integer` types
  - The `Boolean` type
  - All the `floating point` types
  - The `character` type, `char`
  - `Tuples`, if they only contain types that also implement `Copy`
  - For example, `(i32, i32)` implements `Copy`, but `(i32, String)` does not

```
The semantics for passing a value to a function are similar to
those for assigning a value to a variable.
Passing a variable to a function will `move` or `copy`,
just as assignment does.
```

* References and Borrowing

```rust
let s1 = String::from("hello");
let len = calculate_length(&s1);
```

```
Just as variables are immutable by default, so are references.
We're not allowed to modify something we have a reference to.

But mutable references have one big restriction:
you can have only one mutable reference to
a particular piece of data in a particular scope.

We also cannot have a mutable reference while we have an immutable one.

Note that a reference's scope starts from where it is introduced
and continues through the last time that reference is used.
```

* Another data type that does not have **ownership** is the **slice**

```rust
let s = String::from("hello world");

let hello = &s[0..5];
let world = &s[6..11];
```
