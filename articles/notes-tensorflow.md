---
title: TensorFlow notes
description: just notes
date: 2019-09-01
---

* Tensor
  - Scalar -> Vector -> Matrix -> 3D Tensor -> 4D Tensor

```py
c = tf.add(a, b) # Add two tensors A and B, return tensor C
with tf.Session() as sess # Lazy evaluation
  sess.run(c)
```
