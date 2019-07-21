---
title: Linear algebra
description: with Octave examples
date: 2019-07-16
---

* `向量` -> `有向线段`
* `矩阵` -> 空间到空间的 `映射`
* `行列式` -> `映射` 对应的 体积阔大率

## Octave

* 矩阵:

```matlab
A = [1, 2, 0; 0, 5, 6; 7, 0, 9]
A_trans = A'
A_inv = inv(A)
inv(A) * A
```
