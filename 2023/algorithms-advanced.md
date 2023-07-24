---
title: Advanced Algorithms and Data Structures
description: 江涵秋影雁初飞, 与客携壶上翠微. 尘世难逢开口笑, 菊花须插满头归.
date: 2021-09-12
---

- [Advanced Algorithms and Data Structures](https://www.manning.com/books/advanced-algorithms-and-data-structures)

## Introducing data structures

- An abstract data type (`ADT`) specifies the
  operations that can be performed on some data and
  the computational complexity of those operations.
  - No details are provided on how data is stored
    or how physical memory is used.
- A data structure (`DS`) is a concrete
  implementation of the specification
  provided by an `ADT`.
- A more formal definition would describe an `ADT` as
  a set of types, a designated type from that type set,
  a set of functions, and a set of axioms.
- In contrast, a data structure, which is a concrete
  representation of data, is described from
  the point of view of an implementer, not a user.

```
NP-complete problems are a set of problems for which
any given solution can be verified quickly (in polynomial time),
but there is no known efficient way to
locate a solution in the first place.

NP-complete problems, by definition, can't currently be
solved in polynomial time
on a classical deterministic machine.
```

## Improving priority queues: d-way heaps
