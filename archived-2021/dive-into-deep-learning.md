---
title: 动手学深度学习 第二版
description: 沙上并禽池上暝, 云破月来花弄影, 重重帘幕密遮灯.
date: 2021-12-26
---

* [动手学深度学习](https://zh.d2l.ai)
  - 第二版

```py
Z = tf.Variable(tf.zeros([3, 6]))
id1 = id(Z)
Z.assign(tf.ones([3, 6]))
print(id1 == id(Z))
# True
```

```py
u = tf.constant([3.0, -4.0])
tf.norm(u).numpy()
# 5.0
```

* 矢量化

```py
import time

n = 10000
a = tf.ones(n)
b = tf.ones(n)

c = tf.Variable(tf.zeros(n))
start = time.time()
for i in range(n):
  c[i].assign(a[i] + b[i])
print(f"{(time.time() - start):.6f} sec")

start = time.time()
d = a + b
print(f"{(time.time() - start):.6f} sec")
# 4.471961 sec
# 0.000032 sec
# 矢量化代码通常会带来数量级的加速
```

