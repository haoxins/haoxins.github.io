---
title: Fluent Python, 2nd Edition
description: Clear, Concise, and Effective Programming
date: 2021-09-14
---

* [Fluent Python, 2nd Edition](https://book.douban.com/subject/34990079/)
  - https://learning.oreilly.com/library/view/fluent-python-2nd/9781492056348/

## The Python Data Model

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
