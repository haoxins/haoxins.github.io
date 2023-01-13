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
  - 类别对应的分量设置为 `1`, 其他所有分量设置为 `0`.
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

* 注意在添加隐藏层之后, 模型现在需要跟踪和更新额外的参数.
  可我们能从中得到什么好处呢?
  - 你可能会惊讶地发现: 在上面定义的模型里, 我们没有好处!
  - 原因很简单: 上面的隐藏单元由输入的仿射函数给出, 而输出
    (`Softmax` 操作前) 只是隐藏单元的仿射函数.
  - 仿射函数的仿射函数本身就是仿射函数,
    但是我们之前的线性模型已经能够表示任何仿射函数.
* 为了发挥多层架构的潜力, 我们还需要一个额外的关键要素:
  - 在仿射变换之后对每个隐藏单元应用非线性的激活函数 (activation function).
  - 激活函数的输出被称为活性值 (activations).
  - 一般来说, 有了激活函数, 就不可能再将我们的多层感知机退化成线性模型.
* 而且, 虽然一个单隐层网络能学习任何函数,
  但并不意味着我们应该尝试使用单隐藏层网络来解决所有问题.
  - 事实上, 通过使用更深 (而不是更广) 的网络, 我们可以更容易地逼近许多函数.

* **激活函数** (activation function)
  - 通过计算加权和并加上偏置来确定神经元是否应该被激活,
    它们将输入信号转换为输出的可微运算.
  - 大多数激活函数都是非线性的.

* 修正线性单元 (Rectified linear unit, **ReLU**)
  - 给定元素 `x`, `ReLU` 函数被定义为该元素与`0`的最大值
* 使用 `ReLU` 的原因是, 它求导表现得特别好:
  - 要么让参数消失, 要么让参数通过.
  - 这使得优化表现得更好, 并且 `ReLU` 减轻了困扰以往神经网络的梯度消失问题.
  - `ReLU` 函数有许多变体.

* **Sigmoid** 函数
  - `sigmoid` 函数将输入变换为区间 `(0, 1)` 上的输出

* **Tanh** 函数
  - 与 `sigmoid` 函数类似, `tanh` (双曲正切)
    函数也能将其输入压缩转换到区间 `(-1, 1)` 上.

```py
net = tf.keras.models.Sequential(
  [
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation="relu"),
    tf.keras.layers.Dense(10),
  ]
)

loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
trainer = tf.keras.optimizers.SGD(learning_rate=0.1)
```

* 将模型在训练数据上拟合的比在潜在分布中更接近的现象称为**过拟合** (overfitting),
  用于对抗过拟合的技术称为**正则化** (regularization).
* 训练误差 (training error) 是指:
  - 模型在训练数据集上计算得到的误差.
* 泛化误差 (generalization error) 是指:
  - 模型应用在同样从原始样本的分布中抽取的无限多数据样本时, 模型误差的期望.
* 问题是, 我们永远不能准确地计算出泛化误差.
  - 实际中, 我们只能通过将模型应用于一个独立的测试集来估计泛化误差,
    该测试集由随机选取的, 未曾在训练集中出现的数据样本构成.
* 我们假设训练数据和测试数据都是从相同的分布中独立提取的.
  - 这通常被称为独立同分布假设 (i.i.d. assumption),
    这意味着对数据进行采样的过程没有进行"记忆".
  - 有时候我们即使轻微违背独立同分布假设, 模型仍将继续运行得非常好.
  - 有些违背独立同分布假设的行为肯定会带来麻烦.
  - 目前, 即使认为独立同分布假设是理所当然的, 理解泛化性也是一个困难的问题.
* 当我们有简单的模型和大量的数据时, 我们期望泛化误差与训练误差相近.
  当我们有更复杂的模型和更少的样本时, 我们预计训练误差会下降, 但泛化误差会增大.
* 模型复杂性由什么构成是一个复杂的问题.
  一个模型是否能很好地泛化取决于很多因素.
  - 例如, 具有更多参数的模型可能被认为更复杂,
    参数有更大取值范围的模型可能更为复杂.
  - 通常对于神经网络, 我们认为需要更多训练迭代的模型比较复杂,
    而需要"早停" (early stopping) 的模型
    (即较少训练迭代周期) 就不那么复杂.
* 就目前而言, 一条简单的经验法则相当有用:
  - 统计学家认为, 能够轻松解释任意事实的模型是复杂的,
    而表达能力有限但仍能很好地解释数据的模型可能更有现实用途.

* 几个倾向于影响模型**泛化**的因素:
  - **可调整参数的数量**:
  - 当可调整参数的数量 (有时称为自由度) 很大时, 模型往往更容易过拟合.
  - **参数采用的值**:
  - 当权重的取值范围较大时, 模型可能更容易过拟合.
  - **训练样本的数量**:
  - 即使你的模型很简单, 也很容易过拟合只包含一两个样本的数据集.
    而过拟合一个有数百万个样本的数据集则需要一个极其灵活的模型.

* 原则上, 在我们确定所有的超参数之前, 我们不希望用到测试集.
  如果我们在模型选择过程中使用测试数据,
  可能会有过拟合测试数据的风险, 那就麻烦大了.
* 因此, 我们决不能依靠测试数据进行模型选择.
  然而, 我们也不能仅仅依靠训练数据来选择模型,
  因为我们无法估计训练数据的泛化误差.
* 在实际应用中, 情况变得更加复杂.
  - 虽然理想情况下我们只会使用测试数据一次,
    以评估最好的模型或比较一些模型效果,
  - 但现实是测试数据很少在使用一次后被丢弃.
    我们很少能有充足的数据来对每一轮实验采用全新测试集.
* 解决此问题的常见做法是将我们的数据分成三份,
  除了**训练**和**测试**数据集之外,
  还增加一个**验证**数据集 (validation dataset),
  也叫验证集 (validation set).
* 但现实是验证数据和测试数据之间的边界模糊得令人担忧.

* 训练误差和验证误差都很严重, 但它们之间仅有一点差距.
  - 如果模型不能降低训练误差, 这可能意味着模型过于简单 (即表达能力不足),
    无法捕获试图学习的模式.
* 此外, 由于我们的训练和验证误差之间的泛化误差很小,
  我们有理由相信可以用一个更复杂的模型降低训练误差.
  - 这种现象被称为**欠拟合** (underfitting).
* 另一方面, 当我们的训练误差明显低于验证误差时要小心,
  这表明严重的**过拟合** (overfitting).
* 另一个重要因素是数据集的大小.
  - 训练数据集中的样本越少, 我们就越有可能 (且更严重地) 过拟合.
  - 随着训练数据量的增加, 泛化误差通常会减小.
  - 对于许多任务, 深度学习只有在有数千个训练样本时才优于线性模型.

### 暂退法 (Dropout)

* 深度网络的泛化性质令人费解,
  而这种泛化性质的数学基础仍然是悬而未决的研究问题.

* 暂退法在前向传播过程中, 计算每一内部层的同时注入噪声,
  这已经成为训练神经网络的常用技术. 这种方法之所以被称为暂退法,
  因为我们从表面上看是在训练过程中丢弃 (**drop out**) 一些神经元.
  - 在整个训练过程的每一次迭代中,
    标准暂退法包括在计算下一层之前将当前层中的一些节点置零.

### 前向传播, 反向传播

* **前向传播** 指的是:
  - 按顺序 (从输入层到输出层) 计算和存储神经网络中每层的结果.
* **反向传播** 指的是计算神经网络参数梯度的方法.
  - 简言之, 该方法根据微积分中的链式规则,
    按相反的顺序从输出层到输入层遍历网络.
* 在训练神经网络时, 前向传播和反向传播相互依赖.
  - 对于前向传播, 我们沿着依赖的方向遍历计算图并计算其路径上的所有变量.
  - 然后将这些用于反向传播, 其中计算顺序与计算图的相反.

### 环境和分布偏移

* 初始化方案的选择在神经网络学习中起着举足轻重的作用,
  它对保持数值稳定性至关重要.

* 分布偏移的类型
  - **协变量偏移** (covariate shift)
  - 虽然输入的分布可能随时间而改变, 但标签函数 (即条件分布) 没有改变.
  - **标签偏移** (label shift) 描述了与协变量偏移相反的问题.
  - 这里我们假设标签边缘概率可以改变,
    但是类别条件分布在不同的领域之间保持不变.
  - **概念偏移** (concept shift)
  - 当标签的定义发生变化时, 就会出现这种问题.

### 层和块

* 事实证明, 研究讨论"比单个层大"但"比整个模型小"的组件更有价值.
* 块 (block) 可以描述单个层, 由多个层组成的组件或整个模型本身.
  - 使用块进行抽象的一个好处是可以将一些块组合成更大的组件,
    这一过程通常是递归的.
* 从编程的角度来看, 块由类 (class) 表示.
  - 它的任何子类都必须定义一个将其输入转换为输出的前向传播函数,
    并且必须存储任何必需的参数.
  - 最后, 为了计算梯度, 块必须具有反向传播函数.
    在定义我们自己的块时, 由于自动微分提供了一些后端实现,
    我们只需要考虑前向传播函数和必需的参数.

```py
class MLP(tf.keras.Model):
  def __init__(self):
    super().__init__()
    self.hidden = tf.keras.layers.Dense(units=256, activation=tf.nn.relu)
    self.out = tf.keras.layers.Dense(units=10)

  # 定义模型的前向传播, 即如何根据输入 X 返回所需的模型输出
  def call(self, X):
    return self.out(self.hidden((X)))
```
