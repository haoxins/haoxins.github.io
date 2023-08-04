---
title: 线性代数
description: 小径红稀, 芳郊绿遍. 高台树色阴阴见. 春风不解禁杨花, 濛濛乱扑行人面.
date: 2022-11-24
---

- [线性代数 第5版](https://book.douban.com/subject/34820335/)

> 需要开始习惯英文的数学, 物理书籍了.

```
2023年5月, Gilbert Strang 大师, 正式退休.
致敬!
```

- [Graphic notes on Gilbert Strang's "Linear Algebra for Everyone"](https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra)

```
Gilbert Strang, an MIT mathematics professor,
received a standing ovation after giving his
last linear algebra lecture on Monday.

After 63 years teaching and over 10 million
views on his online lectures, MIT professor
Gilbert Strang received a standing ovation
from his students Monday once he completed
his last linear algebra lecture.

The mathematics professor graduated from MIT
in 1955 and has since published several books
on linear algebra and differential equations.
He was one of the first professors to publish
his lectures on the institute's online
open learning library OpenCourseWare, or OCW,
and continues to fall within the top 10
most viewed lecturers at MIT.
```

## Solving Linear Equations

> 首先, 强调`线性变换`的概念.

- You may like the row picture better,
  but only for one day.
  - 哈哈哈

---

- If `A` and `B` are `n` by `n`, so is `AB`. It contains
  $$ n^2 $$
  dot products, row of `A` times column of `B`.
  Each dot product needs `n` multiplications,
  so the computation of `AB` uses
  $$ n^3 $$
  separate multiplications.
  - For `n = 100` we multiply a million times.
  - For `n = 2` we have
    $$ n^3 = 8 $$.
- Mathematicians thought until recently that `AB`
  absolutely needed
  $$ 2^3 = 8 $$
  multiplications. Then somebody found a way to do it with `7`
  (and extra additions). By breaking `n` by `n` matrices into
  `2` by `2` blocks, this idea also reduced the count
  to multiply large matrices.
  - Instead of
    $$ n^3 $$
    multiplications the count has now dropped to
    $$ n^{2.376} $$.
  - Maybe
    $$ n^2 $$
    is possible?
  - But the algorithms are so awkward that scientific
    computing is done the regular
    $$ n^3 $$
    way.

## Vector Spaces and Subspaces

## Orthogonality

## Determinants

## Eigenvalues and Eigenvectors

## The Singular Value Decomposition (SVD)

## Linear Transformations

## Complex Vectorsand Matrices

## Applications

## Numerical Linear Algebra

## Linear Algebrain Probability & Statistics
