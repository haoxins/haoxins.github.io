---
title: Fluent Python, 2nd Edition
description: Clear, Concise, and Effective Programming
date: 2021-09-14
---

* [Fluent Python, 2nd Edition](https://book.douban.com/subject/34990079/)
  - https://learning.oreilly.com/library/view/fluent-python-2nd/9781492056348/

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


### Dictionaries and Sets


### Unicode Text versus Bytes

### Data Class Builders

### Object References, Mutability, and Recycling

### Functions as First-Class Objects

### Type Hints in Functions

### Decorators and Closures

### Special Methods for Sequences

### Interfaces, Protocols, and ABCs


### More About Type Hints

### Operator Overloading

### Iterators, Generators, and Classic Coroutines

### With, match, and else blocks

### Concurrency Models in Python


### Asynchronous Programming


### Dynamic Attributes and Properties


### Attribute Descriptors

### Class Metaprogramming

