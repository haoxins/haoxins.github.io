---
title: Fluent Python, 2nd Edition
description: Clear, Concise, and Effective Programming
date: 2021-09-14
---

* [Fluent Python, 2nd Edition](https://book.douban.com/subject/34990079/)
  - https://learning.oreilly.com/library/view/fluent-python-2nd/9781492056348/

* [From Protocols to ABCs in Python](https://jarombek.com/blog/dec-15-2018-python-protocols-abcs)

### The Python Data Model

* `__len__`, `__getitem__`
* `reversed`, `sorted`, `random.choice`
* If a collection has no `__contains__` method,
  the `in` operator does a sequential scan.
  - `__iter__` vs `__getitem__`

* Normally, your code should **not** have many
  direct calls to special methods.
* Unless you are doing a lot of metaprogramming,
  you should be *implementing* special methods
  more often than *invoking* them explicitly.
  - If you need to invoke a special method,
    it is usually better to call the related
    *built-in* function.
  - e.g., `len`, `iter`, `str`, etc.

* `__repr__`, `__abs__`, `__add__` and `__mul__`.
* The `__repr__` special method is called by
  the repr built-in to get the string
  representation of the object for inspection.
* In contrast, `__str__` is called by the `str()`
  built-in and implicitly used by the print function.
  It should return a string suitable for
  *display to end users*.
* Sometimes same string returned by `__repr__` is
  user-friendly, and you don't need to code
  `__str__` because the implementation inherited
  from the object class calls `__repr__` as a fallback.
* If you only implement one of these special
  methods in Python, choose **`__repr__`**.
* Basically, `bool(x)` calls `x.__bool__()` and
  uses the result. If `__bool__` is not implemented,
  Python tries to invoke `x.__len__()`, and if that
  returns *zero*, bool returns `False`.
  Otherwise bool returns `True`.

* The `Collection` *ABC* unifies the three
  essential interfaces that every
  collection should implement:
  - `Iterable` to support `for`, unpacking,
    and other forms of iteration;
  - `Sized` to support the `len` built-in function;
  - `Container` to support the `in` operator.
* Three very important specializations
  of `Collection` are:
  - `Sequence`, formalizing the interface of
    built-ins like `list` and `str`;
  - `Mapping`, implemented by `dict`,
    `collections.defaultdict`, etc.;
  - `Set`: the interface of the `set` and
    `frozenset` built-in types.

### An Array of Sequences

* **Container** sequences
  - Can hold items of different types, including
    *nested containers*. Some examples:
    `list`, `tuple`, and `collections.deque`.
* **Flat** sequences
  - Hold items of one simple type. Some examples:
    `str`, `bytes`, and `array.array`.

* A *container sequence* holds *references* to the
  objects it contains, which may be of any type,
  while a *flat sequence* stores the *value* of
  its contents in its own memory space, and not
  as distinct Python objects.

* Another way of grouping sequence types
  is by *mutability*:
  - *Mutable* sequences
  - E.g. `list`, `bytearray`, `array.array`,
    and `collections.deque`.
  - *Immutable* sequences
  - E.g. `tuple`, `str`, and `bytes`.

* The built-in concrete sequence types
  do not actually *subclass* the `Sequence`
  and `MutableSequence` *abstract base classes*
  (ABCs), but they are *virtual subclasses*
  registered with those ABCs

```py
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
```

```py
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)
```

* Pattern Matching with Sequences

```py
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
```

### Dictionaries and Sets

```py
def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')
```

### Unicode Text versus Bytes

### Data Class Builders

### Object References, Mutability, and Recycling

### Functions as First-Class Objects

### Type Hints in Functions

### Decorators and Closures

### Special Methods for Sequences

### Interfaces, Protocols, and ABCs

```py
import abc

class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable."""

    @abc.abstractmethod
    def pick(self):
        """Remove item at random, returning it.

        This method should raise `LookupError` when the instance is empty.
        """

    def loaded(self):
        """Return `True` if there's at least 1 item, `False` otherwise."""
        return bool(self.inspect())

    def inspect(self):
        """Return a sorted tuple with the items currently inside."""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(items)
```

> The standard way to declare an `ABC` is to
  subclass `abc.ABC` or any other `ABC`.

### More About Type Hints

### Operator Overloading

### Iterators, Generators, and Classic Coroutines

### With, match, and else blocks

### Concurrency Models in Python

* Let's make sure we are on the same page
  regarding some core concepts.

* **concurrency**
  - The ability to handle multiple pending tasks,
    making progress one at a time or in parallel
    (if possible) so that each of them eventually
    succeeds or fails.
  - A *single-core* CPU is capable of concurrency
    if it runs an OS scheduler that interleaves
    the execution of the pending tasks.
    Also known as *multitasking*.

* **parallelism**
  - The ability to execute multiple computations
    at the same time. This requires a *multi-core*
    CPU, a GPU, or multiple computers in cluster.

* **process**
  - An instance of a computer program while
    it is running, using memory and a slice of
    the CPU time.
  - Modern operating systems are able to manage
    many processes concurrently, with each process
    isolated in its own private memory space.
  - Processes communicate via pipes, sockets, or
    memory mapped files all of which can only
    carry raw bytes, not live Python objects.
  - A process can spawn *sub-processes*, each
    called a child process. These are also isolated
    from each other and from the parent.

* **thread**
  - An execution path within a single process.
  - When a process starts, it uses a single thread:
    the main thread. Using operating system APIs,
    a process can create more threads that operate
    concurrently thanks to the operating system scheduler.
  - Threads share the memory space of the process,
    which holds live Python objects. This allows easy
    communication between threads, but can also lead to
    corrupted data when more than one thread updates
    the same object concurrently.

* **contention**
  - Dispute over a limited asset. Resource contention
    happens when multiple processes or threads try
    to access a shared resource such as
    a lock or storage.
  - There's also CPU contention, when compute-intensive
    processes or threads must wait for
    their share of CPU time.

* **lock**
  - An object that threads can use to coordinate
    and synchronize their actions and
    avoid corrupting data. While updating a shared
    data structure, a thread should hold
    an associated lock.
  - This makes other well behaved threads wait
    until the lock is released before accessing
    the same data structure. The simplest type of
    lock is also known as a *mutex*
    (for mutual exclusion).

* Here is how the concepts we just saw apply
  to Python programming, in **ten points**.
  - Each instance of the Python interpreter
    is a process. You can start additional
    Python processes using the `multiprocessing` or
    `concurrent.futures` libraries. Python's
    *subprocess* library is designed to launch
    processes to run external programs, regardless
    of the languages used to write them.
  - The Python *interpreter* uses a single thread
    to run the user's program and the memory
    garbage collector. You can start additional
    Python threads using the `threading` or
    `concurrent.futures` libraries.
  - Access to object reference counts and
    other internal interpreter state is controlled
    by a lock, the *Global Interpreter Lock*
    (**GIL**). Only one Python thread can hold the
    GIL at any time. This means that only one thread
    can execute Python code at any time, regardless
    of the number of CPU cores.
  - To prevent a Python thread from holding the
    *GIL* indefinitely, Python's bytecode interpreter
    pauses the current Python thread every `5ms` by
    `default`, releasing the GIL. The thread can
    then try to reacquire the GIL, but if there are
    other threads waiting for it, the OS scheduler
    may pick one of them to proceed.
  - When we write Python code, we have no control
    over the GIL. But a built-in function or an
    extension written in `C` or any language that
    interfaces at the *Python/C* API level can
    release the GIL while running time-consuming tasks.
  - Every Python standard library function that
    makes a syscall releases the GIL. This includes all
    functions that perform disk I/O, network I/O, and
    `time.sleep()`. Many CPU-intensive functions in
    the `NumPy/SciPy` libraries, as well as the
    *compressing/decompressing* functions from the
    `zlib` and `bz2` modules also release the GIL.
  - Extensions that integrate at the *Python/C* level
    can also launch other non-Python threads that
    are not affected by the GIL. Such GIL-free
    threads generally cannot change Python objects,
    but they can read from and write to the memory
    underlying objects that support the buffer protocol,
    such as `bytearray`, `array.array`, and NumPy arrays.
  - The effect of the GIL on network programming with
    Python threads is relatively small, because the I/O
    functions release the GIL, and reading or writing
    to the network always implies high latency compared
    to reading and writing to memory. Consequently,
    each individual thread spends a lot of time
    waiting anyway, so their execution can be interleaved
    without major impact on the overall throughput.
    That's why David Beazley says:
    "Python threads are great at doing nothing."
  - Contention over the GIL slows down compute-intensive
    Python threads. Sequential, single-threaded code is
    simpler and faster for such tasks.
  - To run CPU-intensive Python code on multiple cores,
    you must use multiple Python processes.

### Concurrency with Futures

* Since Python 3.4, there are two classes named
  *Future* in the standard library:
  `concurrent.futures.Future` and `asyncio.Future`.
* They serve the same purpose: an instance of
  either `Future` class represents a deferred
  computation that may or may not have completed.

### Asynchronous Programming

* Python 3.5 and later offer three kinds of coroutines:
  - **native coroutines**
  - A coroutine defined with `async def`. You can delegate
    from a native coroutine to another native coroutine
    using the `await` keyword, similar to how classic
    coroutines use `yield from`. The `async def` statement
    always defines a native coroutine, even if the `await`
    keyword is not used in its body. The `await` keyword
    cannot be used outside of a native coroutine.
  - **classic coroutines**
  - A generator function that consumes data sent to it
    via `my_coro.send(data)` calls, and reads that data
    by using `yield` in an expression. Classic coroutines
    can delegate to other classic coroutines using
    `yield from`. Classic coroutines cannot be driven
    by `await`, and are *no longer supported* by `asyncio`.
  - **generator-based coroutines**
  - A generator function decorated with `@types.coroutine`
    introduced in Python 3.5. That decorator makes the
    generator compatible with the new `await` keyword.

### Dynamic Attributes and Properties

* Most updates to this chapter were motivated by
  a discussion of `@functools.cached_property`
  (introduced in Python 3.8), as well as the
  combined use `@property` with
  `@functools.cache` (new in 3.9).

### Attribute Descriptors

### Class Metaprogramming

* `@dataclass` decorator and `typing.NamedTuple`.
