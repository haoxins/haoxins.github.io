---
title: 动手学深度学习 第二版
description: 沙上并禽池上暝, 云破月来花弄影, 重重帘幕密遮灯.
date: 2021-12-26
---

* [动手学深度学习](https://zh.d2l.ai)
  - 第二版
  - 除了免费, 没啥特色
  - **不推荐**

---

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

### 线性回归

* 在每次迭代中, 我们读取一小批量训练样本, 并通过我们的模型来获得一组预测.
  计算完损失后, 我们开始反向传播, 存储每个参数的梯度.
  - 最后, 我们调用优化算法 `sgd` 来更新模型参数.

* 即使是在复杂的优化问题上, `随机梯度下降`通常也能找到非常好的解.
  其中一个原因是, 在深度网络中存在许多参数组合能够实现高度精确的预测.

* 在 `Keras` 中, 全连接层在 `Dense` 类中定义.
  - `Keras` 不要求我们为每个层指定输入形状.
  - `Keras` 会自动推断每个层输入的形状.
* `TensorFlow` 中的 `initializers` 模块提供了多种模型参数初始化方法.
  - 在 `Keras` 中最简单的指定初始化方法是在创建层时指定 `kernel_initializer`.
* `Keras` 在后端执行时, 初始化实际上是推迟 (`deferred`) 执行的.
  - 只有在我们第一次尝试通过网络传递数据时才会进行真正的初始化.
* 小批量随机梯度下降算法是一种优化神经网络的标准工具,
  `Keras` 在 `optimizers` 模块中实现了该算法的许多变种.
  - 小批量随机梯度下降只需要设置 `learning_rate` 值.

```py
initializer = tf.initializers.RandomNormal(stddev=0.01)

net = tf.keras.Sequential()
net.add(tf.keras.layers.Dense(1, kernel_initializer=initializer))
loss = tf.keras.losses.MeanSquaredError()

trainer = tf.keras.optimizers.SGD(learning_rate=0.03)

num_epochs = 3
for _ in range(num_epochs):
  for X, y in data_iter:
    with tf.GradientTape() as tape:
        l = loss(net(X, training=True), y)
    grads = tape.gradient(l, net.trainable_variables)
    trainer.apply_gradients(zip(grads, net.trainable_variables))
```

* 在每个迭代周期里, 我们将完整遍历一次数据集 (`train_data`),
  不停地从中获取一个小批量的输入和相应的标签.
  对于每一个小批量, 我们会进行以下步骤:
  - 通过调用 `net(X)` 生成预测并计算损失 `l` (前向传播).
  - 通过进行反向传播来计算梯度.
  - 通过调用优化器来更新模型参数.

### Softmax 回归

* 独热编码 (one-hot encoding).
  - 独热编码是一个向量, 它的分量和类别一样多.
  - 类别对应的分量设置为 `1`, 其他所有分量设置为0.
  - 在 `(猫, 鸡, 狗)` 分类例子中, 标签将是一个三维向量,
    其中 `(1, 0, 0)` 对应于`猫`,
    `(0, 1, 0)` 对应于`鸡`,
    `(0, 0, 1)` 对应于`狗`.

* 为了估计所有可能类别的条件概率, 我们需要一个有多个输出的模型,
  每个类别对应一个输出.
* 为了解决线性模型的分类问题, 我们需要和输出一样多的仿射函数
  (affine function).
  - 每个输出对应于它自己的仿射函数.
* `Softmax` 函数将未规范化的预测变换为非负并且总和为`1`,
  同时要求模型保持可导.
  - `Softmax` 运算不会改变未规范化的预测之间的顺序, 只会确定分配给每个类别的概率.
  - 尽管 `Softmax` 是一个非线性函数, 但 `Softmax`
    回归的输出仍然由输入特征的仿射变换决定.
    因此, `Softmax` 回归是一个线性模型 (linear model).

```py
net = tf.keras.models.Sequential()

net.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
weight_initializer = tf.keras.initializers.RandomNormal(mean=0.0, stddev=0.01)
net.add(tf.keras.layers.Dense(10, kernel_initializer=weight_initializer))

loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
trainer = tf.keras.optimizers.SGD(learning_rate=0.1)

for _ in range(10):
  for X, y in train_iter:
    with tf.GradientTape() as tape:
      l = loss(y, net(X))
      params = net.trainable_variables
      grads = tape.gradient(l, params)
      trainer.apply_gradients(zip(grads, params))
```

### 多层感知机
