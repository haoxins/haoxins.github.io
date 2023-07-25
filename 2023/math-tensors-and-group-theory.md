---
title: 物理学家用的张量和群论导论
description: 碧云天, 黄叶地, 秋色连波, 波上寒烟翠. 山映斜阳天接水, 芳草无情, 更在斜阳外.
date: 2023-01-30
---

- [物理学家用的张量和群论导论](https://book.douban.com/subject/25934965/)

## Tensors

- To make this concrete, consider a rank `2` tensor `T`,
  whose job it is to eat two vectors `v` and `w` and produce
  a number which we will denote as `T(v, w)`.
  - For such a tensor, __multilinearity__ means
  - $$ T(v_1 + c v_2, w) = T(v_1, w) + c T(v_2, w) $$
  - $$ T(v, w_1 + c w_2) = T(v, w_1) + c T(v, w_2) $$

```
One possible objection to our approach is that matrices
and tensors are often thought of as linear operators which
take vectors into vectors, as opposed to objects which
eat vectors and spit out numbers.
```

---

- That said, an (__abstract__) __vector space__ is a set
  __V__ (whose elements are called vectors),
  together with a set of scalars __C__
  (for us, __C__ is always
  $$ \mathbb{R} $$
  or
  $$ \mathbb{C} $$
  ) and operations of addition and scalar multiplication
  that satisfy the following axioms:
  1. `v + w = w + v`
    for all `v`, `w` in `V` (__Commutativity__)
  2. `v + (w + x) = (v + w) + x`
    for all `v`, `w`, `x` in `V` (__Associativity__)
  3. There exists a vector `0` in `V` such that
    `v + 0 = v` for all `v` in `V`
  4. For all `v` in `V` there is a vector `-v`
    such that `v + (-v) = 0`
  5. `c(v + w) = cv + cw` for all `v` and `w` in
    `V` and scalars `c` (__Distributivity__)
  6. `1v = v` for all `v` in `V`
  7. $$ (c_1 + c_2)v = c_1 v + c_2 v $$
    for all scalars
    $$ c_1 $$,
    $$ c_2 $$
    and vectors `v`
  8. $$ (c_1 c_2)v = c_1(c_2 v) $$
    for all scalars
    $$ c_1 $$,
    $$ c_2 $$
    and vectors `v`

## Groups, Lie Groups, and Lie Algebras

## Basic Representation Theory

## The Wigner-Eckart Theorem and Other Applications

------------------

- [线性代数入门](https://book.douban.com/subject/36432607/)

> 支持一下`图灵数学经典`, 希望后面的翻译能快一点~

------------------

- [从矢量到张量](https://book.douban.com/subject/36000538/)
  - 副标题: 细说矢量与矢量分析, 张量与张量分析

> 非严肃数学读物, 适合随便翻翻
