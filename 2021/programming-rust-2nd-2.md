---
title: Programming Rust - 2nd Edition (下)
description: Fast, Safe Systems Development (Covers Rust 1.50)
date: 2021-09-08
---

* [Programming Rust, 2nd Edition](https://book.douban.com/subject/34973905/)
  - **Fast, Safe Systems Development**
  - [Code Examples for Programming Rust](https://github.com/ProgrammingRust/examples)

## Closures

* The only thing we've changed is to add the
  `move` keyword before each of the two closures.
  The `move` keyword tells Rust that a closure
  doesn't *borrow* the variables it uses:
  - it *steals* them.
* Rust thus offers two ways for closures to get
  data from enclosing scopes:
  - **moves** and **borrowing**.
* Really there is nothing more to say than that;
  closures follow the same rules about
  moves and borrowing that we already covered.
  A few cases in point:
  - Just as everywhere else in the language, if
    a closure would `move` a value of a
    *copyable* type, like `i32`, it copies the
    value instead.
  - Values of *noncopyable* types, like `Vec<City>`,
    really are *moved*. Rust would not let us access
    `cities` by name after creating the closure.

* Well, a closure is callable, but its not a `fn`.
  The closure `|city| city.monster_attack_risk > limit`
  has its own type that's not a `fn` type,
* In fact, every closure you write has its own type,
  because a closure may contain data: values either
  `borrowed` or `stolen` from enclosing scopes.
* This could be any number of variables, in any
  combination of types. So every closure has an
  `ad hoc` type created by the compiler, large
  enough to hold that data. *No two closures* have
  exactly *the same type*. But every closure implements
  an `Fn` *trait*; the closure in our example implements
  `Fn(&City) -> i64`.
* Since every closure has its own type, code that
  works with closures usually needs to be generic,
  like `count_selected_cities`. Its a little clunky
  to spell out the generic types each time, but to
  see the advantages of this design, just read on.

* **Pseudocode** for `Fn`, `FnMut`,
  and `FnOnce` traits.

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

* Any closure that requires `mut` access to
  a value, but doesn't `drop` any values,
  is an `FnMut` closure.
* The three categories of Rust closures.
  - `Fn` is the family of closures and functions
    that you can call multiple times without
    restriction. This **highest** category also
    includes all `fn` functions.
  - `FnMut` is the family of closures that can be
    called multiple times if the
    closure itself is declared `mut`.
  - `FnOnce` is the family of closures that can
    be called **once**, if the caller
    owns the closure.
* Every `Fn` meets the requirements for `FnMut`, and
  every `FnMut` meets the requirements for `FnOnce`.
* Instead, `Fn()` is a *subtrait* of `FnMut()`,
  which is a *subtrait* of `FnOnce( )`.
* This makes `Fn` the most exclusive and most powerful
  category. `FnMut` and `FnOnce` are broader
  categories that include closures
  with usage restrictions.

* On the other hand, a `non-move` closure that *does*
  `mutate` values has `mutable` references within
  its internal representation. `Mutable` references
  are neither `Clone` nor `Copy`, so neither is
  a closure that uses them.

* For a `move` closure, the rules are even simpler.
  If everything a `move` closure captures ís `Copy`,
  it's `Copy`. If everything it captures is `Clone`,
  it's `Clone`.

* Closures have unique types because each one
  captures different variables, so among other things,
  they're each a different size.
* If they don't capture anything, though, there's
  nothing to store. By using `fn` pointers in functions
  that take callbacks, you can restrict a caller to
  use only these noncapturing closures, gaining some
  perfomance and flexibility within the code using
  callbacks at the cost of flexibility
  for the users of your APl.

## Iterators

* Here, `filter` returns a new iterator that
  produces only those items from the `map` iterator
  for which the closure returns `true`.
* A chain of iterator adapters is like a pipeline
  in the `Unix` shell: each adapter has a single
  purpose, and it's clear how the sequence is
  being transformed as one reads from left to right.
  These adapters' signatures are as follows:

```rust
fn map<B, F>(self, f: F) -> impl Iterator<Item=B>
  where Self: Sized, F: FnMut(Self::Item) -> B;

fn filter<P>(self, predicate: P) -> impl Iterator<Item=Self::Item>
  where Self: Sized, P: FnMut(&Self::Item) -> bool;
```

* In the standard library, `map` and `filter` actually
  return specific opaque `struct` types named
  `std::iter::Map` and `std::iter::Filter`. However,
  just seeing their names is not very informative,
  so in this book, were just going to write
  `-> impl Iterator<Item=...>` instead, since that
  tells us what we really want to know:
  - the method returns an `Iterator` that produces
    items of the given type.
* Since most adapters take `self` by value, they require
  `Self` to be `Sized` (which all common iterators are).
  - A `map` iterator passes each item to its closure
    by `value` and, in turn, passes along *ownership* of the
    closure's result to it's consumer.
  - A `filter` iterator passes each item to its closure
    by *shared reference*, retaining *ownership* in case
    the item is selected to be passed on to it's consumer.

* There are **two** important points to notice about
  iterator adapters
* **First**, simply calling an adapter on an iterator
  doesn't consume any items; it just returns a
  new iterator, ready to produce its own items by
  drawing from the first iterator as `needed`.
* In a chain of adapters, the only way to make any work
  actually get done is to call `next`
  on the **final** iterator.
  - **No** work takes place until `collect` starts
    calling `next` on the `filter` iterator.
  - This point is especially important if you use
    adapters that have *side effects*.
  - For example, this code prints **nothing** at all:

```rust
["earth", "water", "air", "fire"]
  .iter().map(|elt| println!("{}", elt));
```

* The `iter` call returns an iterator over the array's
  elements, and the `map` call returns a second
  iterator that applies the closure to each value the
  first produces. But there is nothing here that ever
  actually demands a value from the whole chain, so no
  `next` method ever runs.
* The term `"lazy"` in the error message is not a
  disparaging term; it's just jargon for any mechanism
  that puts off a computation until its value is needed.
  It is Rust's convention that iterators should do the
  minimum work necessary to satisfy each call to `next`;
  in the example, there are no such calls at all,
  so no work takes place.
* The **second** important point is that iterator
  adapters are a `zero-overhead` abstraction. Since
  `map`, `filter`, and their companions are `generic`,
  applying them to an iterator specializes their code
  for the specific iterator type involved.
* This means that Rust has enough information to inline
  each iterator's next method into its consumer and
  then translate the entire arrangement into
  machine code as a unit، So the `lines/map/filter` chain
  of iterators we showed before is as efficient as the
  code you would probably write by hand.

## Strings and Text

* `String` and `str`

* Rust's `String` and `str` types are guaranteed
  to hold only well-formed UTF-8. The library ensures
  this by restricting the ways you can create `String`
  and `str` values and the operations you can perform
  on them, such that the values are well-formed when
  introduced and remain so as you work with them.
* All their methods protect this guarantee: no safe
  operation on them can introduce ill-formed UTF-8.
  This simplifies code that works with the text.

* Rust places text-handling methods on either
  `str` or `String` depending on whether the method
  needs a resizable buffer or is content just to
  use the text in place.
* Since `String` dereferences to `&str`, every method
  defined on `str` is directly available on `String`
  as well.

* These methods index text by *byte offsets* and
  measure its length in bytes, rather than characters.
* In practice, given the nature of *Unicode*, indexing
  by character is not as useful as it may seem, and
  *byte offsets* are faster and simpler. If you try to
  use a *byte offset* that lands in the midst of some
  character's UTF-8 encoding, the method panics, so
  you can't introduce ill-formed UTF-8 this way.

* A `String` is implemented as a wrapper around a
  `Vec<u8>` that ensures the vector's contents are
  always well-formed UTF-8. Rust will never change
  `String` to use a more complicated representation,
  so you can assume that `String` shares `Vec's`
  performance characteristics.

## Concurrency

* Thread Safety: **`Send`** and **`Sync`**

* So far we've been acting as though all values can
  be freely moved and shared across threads. This is
  mostly true, but Rust's full thread safety story
  hinges on two built-in traits, `std::marker::Send`
  and `std::marker::Sync`.
  - Types that implement `Send` are safe to pass
    by value to another thread. They can be
    *moved across threads*.
  - Types that implement `Sync` are safe to pass
    by *non-mut reference to another thread*. They
    can be shared across threads.
* By safe here, we mean the same thing we always
  mean: free from *data races* and other
  undefined behavior.

* **Mutexes** are helpful for several reasons:
  - They prevent *data races*, situations where racing
    threads concurrently read and write the same memory.
    *Data races* are undefined behavior in `C++` and `Go`.
    Managed languages like `Java` and `C#` promise
    not to crash, but the results of *data races* are
    still (to summarize) nonsense.
  - Even if data races didn't exist, even if all reads
    and writes happened one by one in program order,
    without a `mutex` the actions of different threads
    could interleave in arbitrary ways. Imagine trying
    to write code that works even if other threads
    modify its data while it's running. Imagine trying
    to debug it. It would be like your
    program was haunted.
  - *Mutexes* support programming with invariants, rules
    about the protected data that are true by
    construction when you set it up and maintained
    by every critical section.
* Of course, all of these are really the same reason:
  *uncontrolled race conditions* make
  programming intractable. *Mutexes* bring some order
  to the *chaos*.
  - though not as much order as channels or fork-join

## Asynchronous Programming

* Rust's use of *polling*, however, is **unusual**.
  In `JavaScript`, an asynchronous function begins
  running as soon as it is called, and there is a
  global event loop built into the system library
  that resumes suspended async function calls
  when the values they were awaiting become available.
* In Rust, however, an `async` call does **nothing**
  until you pass it to a function like `block_on`,
  `spawn`, or `spawn_local` that will poll it and
  drive the work to completion. These functions,
  called **executors**, play the role that other
  languages cover with *a global event loop*.
* Because Rust makes you, the programmer, choose
  an executor to poll your futures. Rust has
  **no need** for a global event loop built into
  the system. The `async-std` crate offers the
  executor functions we've used in this chapter
  so far, but the `tokio` crate. which we'll
  use later in this chapter, defines its own set
  of similar executor functions.

* Rust's solution to this problem rests on the
  insight that futures are always safe to move
  when they are first created, and only become
  `unsafe` to move when they are *polled*. A
  future that has just been created by calling an
  asynchronous function simply holds a resumption
  point and the argument values. These are only
  in scope for the asynchronous function's body,
  which has not yet begun execution. Only polling
  a future can *borrow* its contents.

* From this, we can see that every **future** has
  **two life stages**:
  - The first stage begins when the future is
    created. Because the function's body hasn't
    begun execution, no part of it could possibly
    be *borrowed* yet. At this point, it's as safe
    to move as any other Rust value.
  - The second stage begins the first time the
    future is *polled*. Once the function's body has
    begun execution, it could borrow references to
    variables stored in the future and then await,
    leaving that part of the future borrowed.
    Starting after its first poll, we must assume
    the future may not be safe to move.

* The flexibility of the first life stage is what
  lets us pass futures to `block_on` and `spawn`
  and call adapter methods like `race` and `fuse`,
  all of which take futures by value. In fact,
  even the asynchronous function call that created
  the future in the first place had to return it
  to the caller; that was a `move` as well.
* To enter its second life stage, the future must
  be *polled*. The `poll` method requires the future
  be passed as a `Pin<&mut Self>` value. `Pin` is a
  wrapper for *pointer types* (like `&mut Self`) that
  restricts how the pointers can be used, ensuring
  that their referents (like `Self`) cannot ever be
  moved again. So you must produce a `Pin-wrapped`
  pointer to the future before you can poll it.

* This, then, is Rust's strategy for keeping
  futures *safe*: a future can't become dangerous
  to move until it's *polled*; you can't poll a
  future until you've constructed a `Pin-wrapped`
  pointer to it; and once you've done that,
  the future can't be moved.
* **"A value you can't move"** sounds impossible:
  moves are everywhere in Rust.

* Although this section has discussed asynchronous
  *functions*, everything here applies to asynchronous
  *blocks* as well.
* A freshly created future of an *asynchronous block*
  simply captures the variables it will use from the
  surrounding code, like a closure.
* Only polling the future can create references to
  its contents, rendering it `unsafe` to `move`.

* Keep in mind that this `move` fragility is limited
  to futures of asynchronous functions and blocks,
  with their special compiler-generated `Future`
  implementations. If you implement Future by hand
  for your own types, such futures are perfectly safe
  to move both before and after they've been *polled*.
* In any handwritten poll implementation, the borrow
  checker ensures that whatever references you had
  borrowed to parts of self are gone by the time
  poll returns. It is only because asynchronous
  *functions and blocks* have the power to suspend
  execution in the midst of a function call, with
  borrows in progress, that we must handle
  their futures with care.

* **Pinned Pointers**

* The `Pin` type is a wrapper for pointers to
  futures that restricts how the pointers may be
  used to make sure that futures can't be moved
  once they've been polled. These restrictions
  can be lifted for futures that don't mind being
  moved, but they are essential to safely polling
  futures of asynchronous functions and blocks.
* By *pointer*, we mean any type that implements
  `Deref`, and possibly `DerefMut`. A `Pin`
  wrapped around a pointer is called a
  *pinned pointer*. `Pin<&mut T>` and `Pin<Box<T>>`
  are typical.

* The definition of `Pin` in the standard library
  is simple:

```rust
pub struct Pin<P> {
  pointer: P,
}
```

* Note that the pointer field is *not* `pub`.
  This means that the only way to construct or
  use a `Pin` is through the carefully chosen
  methods the type provides.
* Given a future of an asynchronous function or
  block, there are only a few ways to get a
  pinned pointer to it:
  - The `pin!` macro, from the `futures-lite` crate,
    shadows a variable of type `T` with a new one of
    type `Pin<&mut T>`. The new variable points to
    the original's value, which has been moved to an
    anonymous temporary location on the stack. When
    the variable goes out of scope,
    the value is dropped.
    We used `pin!` in our `block_on` implementation
    to `pin` the future we wanted to *poll*.
  - The standard library's `Box::pin` constructor
    takes ownership of a value of any type `T`,
    moves it into the heap, and returns a
    `Pin<Box<T>>`.
  - `Pin<Box<T>>` implements `From<Box<T>>`, so
    `Pin::from(boxed)` takes ownership of boxed
    and gives you back a pinned box pointing
    at the same `T` on the heap.

* Every way to obtain a *pinned pointer* to these
  futures entails giving up ownership of the future,
  and there is no way to get it back out. The
  *pinned pointer* itself can be moved in any way
  you please, of course, but moving a pointer doesn't
  move its *referent*. So possession of a *pinned pointer*
  to a future serves as proof that you have permanently
  given up the ability to move that future. This is
  all we need to know that it can be polled safely.
* Once you've pinned a future, if you'd like to poll it,
  all `Pin<pointer to T>` types have an `as_mut` method
  that dereferences the pointer and returns the
  `Pin<&mut T>` that poll requires.
* The `as_mut` method can also help you poll a future
  without giving up ownership. Our `block_on`
  implementation used it in this role:

```rust
pin!(future);

loop {
  match future.as_mut().poll(&mut context) {
    Poll::Ready(value) => return value,
    Poll::Pending => parker.park(),
  }
}
```

* Here, the `pin!` macro has redeclared future as
  a `Pin<&mut F>`, so we could just pass that to poll.
  But *mutable* references are not `Copy`, so
  `Pin<&mut F>` cannot be `Copy` either, meaning that
  calling `future.poll()` directly would take
  ownership of future, leaving the next iteration of
  the loop with an uninitialized variable.
* To avoid this, we call `future.as_mut()` to reborrow
  a fresh `Pin<&mut F>` for each loop iteration.

* There is no way to get a `&mut` reference to a
  pinned future: if you could, you could use
  `std::mem::replace` or `std::mem::swap` to move
  it out and put a different future in its place.
* The reason we don't have to worry about
  *pinning futures* in ordinary asynchronous code
  is that the most common ways to obtain a future's
  *value-awaiting* it or passing to an executor.
  - all take ownership of the future and manage
    the pinning internally.
* For example, our `block_on` implementation
  takes ownership of the future and uses the
  `pin!` macro to produce the `Pin<&mut F>`
  needed to poll. An *await expression* also
  takes ownership of the future and uses an
  approach similar to the `pin!` macro internally.

### The Unpin Trait

* However, not all futures require this kind of
  careful handling.
* Such durable types implement the
  `Unpin` marker trait:

```rust
trait Unpin { }
```

* Almost all types in Rust automatically implement
  `Unpin`, using special support in the compiler.
  Asynchronous function and block futures are the
  exceptions to this rule.
* For `Unpin` types, `Pin` imposes no restrictions
  whatsoever. You can make a *pinned pointer* from an
  ordinary pointer with `Pin::new` and get the pointer
  back out with `Pin::into_inner`. The `Pin` itself
  passes along the pointer's own `Deref` and
  `DerefMut` implementations.
* For example, `String` implements `Unpin`,
  so we can write:

```rust
let mut string = "Pinned?".to_string();
let mut pinned: Pin<&mut String> = Pin::new(&mut string);

pinned.push_str(" Not");
Pin::into_inner(pinned).push_str(" so much.");

let new_home = string;
assert_eq!(new_home, "Pinned? Not so much.");
```

* Even after making a `Pin<&mut String>`, we have
  full **mutable** access to the string and can
  move it to a new variable once the `Pin` has been
  consumed by `into_inner` and the *mutable reference*
  is gone. So for types that are `Unpin`
  - which is almost all of them - `Pin` is a boring
    wrapper around pointers to that type.
* This means that when you implement `Future` for your
  own `Unpin` types, your poll implementation can treat
  *self* as if it were `&mut Self`, not `Pin<&mut Self>`.
  - Pinning becomes something you can mostly ignore.
* It may be surprising to learn that `Pin<&mut F>` and
  `Pin<Box<F>>` implement `Unpin`, even if `F` does not.
  This doesn't read well - how can a `Pin` be `Unpin`?
  - But if you think carefully about what each term
    means, it does make sense.
    Even if `F` is not safe to move once it has been
    polled, a pointer to it is always safe to move,
    *polled or not*. Only the pointer moves; its
    fragile referent says put.
* This is useful to know when you would like to
  pass the future of an asynchronous function or
  block to a function that only
  accepts `Unpin` futures.
  - Such functions are rare in `async_std`, but
    less so elsewhere in the async ecosystem.
* `Pin<Box<F>>` is `Unpin` even if `F` is not, so
  applying `Box::pin` to an asynchronous function
  or block future gives you a future you can use
  anywhere, at the cost of a heap allocation.

* There are various unsafe methods for working
  with `Pin` that let you do whatever you like
  with the pointer and its target, even for
  target types that are not `Unpin`. But Rust
  cannot check that these methods are being
  used correctly; you become responsible for
  ensuring the safety of the code that uses them.

### When Is Asynchronous Code Helpful?

* Asynchronous code is trickier to write than
  *multithreaded* code. You have to use the
  right `I/O` and synchronization primitives,
  break up long-running computations by hand
  or spin them off on other threads, and manage
  other details like pinning that don't arise
  in threaded code. So what specific advantages
  does asynchronous code offer?

* Two claims you'll often hear don't stand up
  to careful inspection:
* **"Async code is great for I/O"**: This is
  **not quite correct**. If your application is
  spending its time waiting for `I/O`, making
  it async will not make that `I/O` run faster.
* There is nothing about the asynchronous `I/O`
  interfaces generally used today that makes
  them more efficient than their synchronous
  counterparts. The operating system has the
  same work to do either way.
  - In fact, an asynchronous `I/O` operation that
    isn't ready must be tried again later, so it
    takes two system calls to complete instead of one.
* **"Async code is easier to write than multithreaded code"**:
  In languages like `JavaScript` and `Python`, this may
  well be true. In those languages, programmers use
  `async/await` as well-behaved form of concurrency:
  - there's a single thread of execution, and interruptions
    only occur at *await expressions*, so there's often no
    need for a `mutex` to keep data consistent:
  - just dont await while you're in the midst of using it!
    It's much easier to understand your code when task
    switches occur only with your explicit permission.
* But this argument doesn't carry over to Rust, where
  threads aren't nearly as troublesome. Once your
  program compiles, it is free of data races.
  - Nondeterministic behavior is confined to
    synchronization features like
    `mutexes`, `channels`,`atomics`, and so on,
    which were designed to cope with it.
  - So asynchronous code has no unique advantage at
    helping you see when other threads might impact you;
    that's clear in all safe Rust code.
  - And of course, Rust's asynchronous support really
    shines when used in combination with threads.
    It would be a pity to give that up.

### So, what are the real advantages of asynchronous code?

* Asynchronous tasks can use **less memory**.
* On Linux, a thread's memory use starts at `20 KiB`,
  counting both user and kernel space.
  - Futures can be much smaller.
* Asynchronous tasks are **faster to create**.
* On Linux, creating a thread takes around `15us`.
  Spawning an asynchronous task takes around `300 ns`.
* **Context switches are faster** between asynchronous
  tasks than between operating system threads,
  `0.2 us` versus `1.7 us` on Linux. However,
  these are best-case numbers for each:
  if the switch is due to `I/O` readiness,
  both costs rise to `1.7 us`.
  - Whether the switch is between threads or
    tasks on different processor cores also
    makes a big difference:
  - communication between cores is very slow.

* This gives us a hint as to what sorts of problems
  asynchronous code can solve. For example, an
  asynchronous server might use less memory per task
  and thus be able to handle more
  simultaneous connections.
  - This is probably where asynchronous code gets
    its reputation for being "good for I/O."
* Or, if your design is naturally organized as many
  independent tasks communicating with each other,
  then *low per-task costs*, *short creation times*,
  and *quick context switches* are all important
  advantages.
  - This is why chat servers are the classic example
    for asynchronous programming, but multi
    player games and network routers would
    probably be good uses too.
* In other situations, the case for using async is
  less clear. If your program has a pool of threads
  doing heavy computations or sitting idle waiting
  for `I/O` to finish. The advantages listed earlier
  are probably not a big influence on its performance.
  You'll have to optimize your computation, find a
  faster net connection, or do something else that
  actually affects the limiting factor.

* In practice, every account of implementing high-volume
  servers that we could find emphasized the importance
  of measurement, tuning, and a relentless campaign to
  identify and remove sources of contention between tasks.
* An asynchronous architecture **won't** let you skip any of
  this work. In fact, while there are plenty of
  `off-the-shelf` tools for assessing the behavior of
  `multithreaded` programs, Rust asynchronous tasks are
  invisible to those tools and thus require tooling of
  their own.
* Even if you don't use asynchronous code now, it's
  nice to know that the option is there if you ever
  have the good fortune to be vastly
  busier than you are now.

## Unsafe Code

* An `unsafe` block unlocks five
  additional options for you:
  - You can call `unsafe` functions. Each `unsafe`
    function must specify its own *contract*,
    depending on its purpose.
  - You can dereference raw pointers. Safe code can
    pass raw pointers around, compare them, and
    create them by conversion from references
    (or even from integers), but only `unsafe` code
    can actually use them to access memory.
  - You can access the fields of `unions`, which the
    compiler can't be sure contain valid bit patterns
    for their respective types.
  - You can access *mutable static variables*. Rust
    can't be sure when threads are using
    *mutable static variables*, so their contract
    requires you to ensure all access is
    properly synchronized.
  - You can access functions and variables declared
    through Rust's foreign function interface. These
    are considered `unsafe` even when *immutable*, since
    they are visible to code written in other languages
    that may not respect Rust's safety rules.

* Restricting `unsafe` features to `unsafe` blocks
  doesn't really prevent you from doing whatever you want.
  Its perfectly possible to just stick an `unsafe` block
  into your code and move on. The benefit of the rule
  lies mainly in *drawing human attention* to code whose
  safety Rust can't guarantee:
  - You won't accidentally use `unsafe` features and
    then discover you were responsible for contracts
    you didn't even know existed.
  - An `unsafe` block attracts *more attention* from
    *reviewers*. Some projects even have automation
    to ensure this, flagging code changes that affect
    `unsafe` blocks for special attention.
  - When you're considering writing an `unsafe` block,
    you can take a moment to ask yourself whether your
    task really requires such measures. If it's for
    performance. do you have measurements to show that
    this is actually a bottleneck? Perhaps there is a
    good way to accomplish the same thing in safe Rust.

* Two critical facts about bugs and `unsafe` code:
  - Bugs that occur before the `unsafe` block can
    break contracts. Whether an `unsafe` block causes
    undefined behavior can depend not just on the code
    in the block itself, but also on the code that
    supplies the values it operates on. Everything that
    your `unsafe` code relies on to satisfy contracts
    is safety-critical. The conversion from `Ascii` to
    `String` based on `String::from_utf8_unchecked`
    is well-defined only if the rest of the module
    properly maintains Ascii's invariants.
  - The consequences of breaking a contract may appear
    after you leave the `unsafe` block. The undefined
    behavior courted by failing to comply with an
    `unsafe` feature's contract often does not occur
    within the `unsafe` block itself. Constructing a
    bogus `String` as shown before may not cause
    problems until much later in the
    program's execution.

* Essentially. Rust's *type checker*, *borrow checker*,
  and other *static checks* are inspecting your program
  and trying to construct proof that it cannot exhibit
  undefined behavior.
* When Rust compiles your program successfully, that
  means it succeeded in proving your code sound. An
  `unsafe` block is a gap in this proof:
  - "This code," you are saying to Rust, "is fine, trust me."
* Whether your claim is true could depend on any part
  of the program that influences what happens in the
  `unsafe` block, and the consequences of being wrong
  could appear anywhere influenced by the `unsafe` block.
* Writing the `unsafe` keyword amounts to a reminder
  that you are not getting the full benefit of the
  language's safety checks.

* Given the choice, you should naturally prefer to
  create safe interfaces, without contracts. These are
  much easier to work with, since users can count
  on Rust's safety checks to ensure their code is free
  of undefined behavior.
* Even if your implementation uses `unsafe` features,
  it's best to use Rust's `types`, `lifetimes`,
  and module system to meet their contracts while
  using only what you can guarantee yourself,
  rather than passing responsibilities on to your callers.

* Unfortunately, it's not unusual to come across
  *unsafe functions* in the wild whose documentation
  does not bother to explain their contracts. You
  are expected to infer the rules yourself, based on
  your experience and knowledge of how the code
  behaves. If you've ever uneasily wondered whether
  what you're doing with a `C` or `C++` API is OK,
  then you know what that's like.

* **Unsafe Block** or **Unsafe Function**?

* You may find yourself wondering whether to
  use an `unsafe block` or just mark the whole
  `function unsafe`. The approach we recommend is
  to first make a decision about the function:
  - If it's possible to misuse the function in a
    way that compiles fine but still causes
    undefined behavior, you must mark it as `unsafe`.
    The rules for using the function correctly are
    its contract; the **existence of a contract** is
    what makes the function `unsafe`.
  - Otherwise, the function is **safe**: no
    well-typed call to it can cause undefined
    behavior. It should not be marked `unsafe`.

* Whether the function uses `unsafe` features in
  its body is irrelevant; what matters is the
  presence of a contract. Before, we showed an
  `unsafe` function that uses no `unsafe` features,
  and a safe function that does use `unsafe` features.
* Don't mark a *safe* function `unsafe` just because
  you use `unsafe` features in its body. This makes
  the function harder to use and confuses readers
  who will (correctly) expect to find a contract
  explained somewhere.
  - Instead, use an `unsafe` block,
    *even if it's the function's entire body*.
