---
title: Math and Architectures of Deep Learning
description: 独坐幽篁里, 弹琴复长啸. 深林人不知, 明月来相照.
date: 2023-01-03
---

- [Math and Architectures of Deep Learning](https://book.douban.com/subject/34986154/)
  - 一开始对这本书没啥期待, 主要是想熟悉英文的数学书.
  - 不过看下来还是有一些小惊喜~

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
  - Unlike the inverse, the pseudo-inverse does not need
    the matrix to be square with linearly independent rows.

- Transforms generally map vectors (points) in one space to
  different vectors (points) in the same or a different space.
  But a typical linear transform will leave a few points in
  the space (almost) unaffected.
  - These points are called __eigenvectors__.
- These are the so called eigenvectors -
  they do not change direction when undergoing
  linear transformation by a matrix __A__.

- All rotations matrices are orthogonal matrices.
- All orthogonal matrices represent some rotation.

## Introduction to Vector Calculus from Machine Learning point of view

> It should be noted that the gradient is
  with respect to weights and not the input.

- The total change can be estimated by taking a
  weighted combination of the partial derivatives.
- This yields a physical interpretation of the gradient vector:
  its direction is the direction in parameter space along
  which the multi-dimensional function is changing fastest.
- The gradient of a function at any point is normal to the
  level surface through that point.
  - This is the direction along which the
    function value is changing fastest.
  - Moving along the gradient, one passes from
    one level surface to another.

- [Convex function](https://en.wikipedia.org/wiki/Convex_function)

## Linear Algebraic Tools in Machine Learning and Data Science

- [Quadratic form](https://en.wikipedia.org/wiki/Quadratic_form)

