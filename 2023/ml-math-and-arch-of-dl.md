---
title: Math and Architectures of Deep Learning
description: 独坐幽篁里, 弹琴复长啸. 深林人不知, 明月来相照.
date: 2023-01-03
---

- [Math and Architectures of Deep Learning](https://book.douban.com/subject/34986154/)

- If one wants the agreement score to be neutral to
  the vector length, one can use a normalized dot product -
  between unit length vectors along same directions.
- Geometrically speaking, given a plane (in any dimension),
  we will be able to find a direction,
  called __normal direction__.
- __Closure__: A set of vectors is said to be closed under
  linear combination if and only if the linear combination
  of any pair of vectors in the set
  also belongs to the same set.
  - The set of points on the surface of a sphere is not
    closed under linear combination, because,
    the line joining an arbitrary pair of of points
    on this set will not wholly lie on
    the surface of that sphere.
- A transform is __linear__ if and only if the transform of
  the linear combination of two vectors is same as the
  linear combination (with same weights) of the
  transforms of individual vectors.
  - linear transform means transforms of linear combinations
    are same as linear combinations of transforms.
- In __finite__ dimensions, multiplication with a matrix and
  linear transformation are one and the same thing.

- Sometimes, the determinant is not exactly zero,
  but close to zero. Such systems, although solvable is theory,
  are numerically unstable.
  - Small changes in input causes the result to change drastically.

- The __pseudo-inverse__ of matrix __A__, denoted
  $$ \mathbf{A}^{+} = (\mathbf{A}^{T} \mathbf{A})^{−1} \mathbf{A}^{T} $$.
