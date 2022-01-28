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
