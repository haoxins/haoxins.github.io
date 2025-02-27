---
title: Math and Architectures of Deep Learning
description: 独坐幽篁里, 弹琴复长啸. 深林人不知, 明月来相照.
date: 2023-01-03
---

- [Math and Architectures of Deep Learning](https://book.douban.com/subject/34986154/)
  - 一开始对这本书没啥期待, 主要是想熟悉英文的数学书.
  - 不过看下来还是有一些小惊喜~
  - 整体上, 还是不推荐~

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
    the line joining an arbitrary pair of points
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

- Thus, the quadratic form
  $$ Q = x^{T} A x $$
  attains its maximum when `x` is along the eigenvector
  corresponding to the largest eigenvalue of `A`.
  - The corresponding maximum `Q` is equal to the
    largest eigenvalue of `A`.
  - Similarly, the minimum of the quadratic form occurs
    when `x` is along the eigenvector corresponding to
    the smallest eigenvalue.
- As stated above, many machine learning problems
  boil down to minimizing a quadratic form.

```
The variation along the direction perpendicular to
the true pattern is caused by measurement errors.
PCA finds the underlying straight line pattern as
first principal axis.
Rotating the coordinate system so that this becomes
the X axis and then replacing every point by its projection
on the new X axis converts the data from 2D to 1D.
The projected data is less noisy.
And it captures the true distribution.
```

```
The cosine similarity between document vectors is often
used to measure similarity between two documents.
It is a principled way of measuring the degree of
term sharing between the two documents.
```

## Probability Distributions for Machine Learning and Data Science

```
Thus, the total area under a univariate
probability density curve is always one.
In higher dimensions, the volume under the
hyper-surface for a multivariate probability
density function is always one.
```

- We will show that the expected value of a function
  of a random variable can be viewed as a dot product
  between a vector representing the probability and
  the another vector representing the function itself.

```
Covariance of a multidimensional point distribution is a
matrix that allows us to easily measure the spread or
packing density along any desired direction.
It also allows us to easily figure out the direction along
which maximum spread occurs and what that spread is.
```

## Bayesian Tools for Machine Learning and Data Science

- Entropy then is a measure which becomes high if
  everything is more or less equally probable,
  and becomes low if a few of the items have much
  higher probability than others.

> In Maximum Likelihood Estimation of parameters (abbreviated MLE),
> we ask the question:
> "what parameter values will maximize the joint likelihood
> of the training data instances"?

------------------

- [动手学深度学习](https://book.douban.com/subject/36142067/)
  - 支持一下`李沐`

```
简而言之, 我们可以从两方面来考虑交叉熵分类目标:
(1) 最大化观测数据的似然;
(2) 最小化传达标签所需的惊异.
```

> 如果微妙的边界条件很重要, 那么我们很可能是在研究数学而非工程.

```
常见的技巧是在靠近输入层的地方设置较低的暂退概率.
```

- 一般来说, `k` 个 GPU 并行训练过程如下:
  - 在任何一次训练迭代中, 给定的随机小批量样本都将被分成 `k` 个部分,
    并均匀地分配到 GPU 上;
  - 每个 GPU 根据分配给它的小批量子集, 计算模型参数的损失和梯度;
  - 将 `k` 个 GPU 中的局部梯度聚合, 以获得当前小批量的随机梯度;
  - 聚合梯度被重新分发到每个 GPU 中;
  - 每个 GPU 使用这个小批量随机梯度, 来更新它所维护的完整的模型参数集.
- 分布式并行训练大致如下:
  - (1) 在每台机器上读取一组 (不同的) 批量数据,
    在多个 GPU 之间分割数据并传输到 GPU 的显存中.
    基于每个 GPU 上的批量数据分别计算预测和梯度.
  - (2) 来自一台机器上的所有本地 GPU 的梯度聚合在一个 GPU 上
    (或者在不同的 GPU 上聚合梯度的某些部分).
  - (3) 每台机器的梯度被发送到其本地 CPU 中.
  - (4) 所有 CPU 将梯度发送到中央参数服务器中, 由该服务器聚合所有梯度.
  - (5) 使用聚合后的梯度来更新参数, 并将更新后的参数广播回各个 CPU 中.
  - (6) 更新后的参数信息发送到本地一个 (或多个) GPU 中.
  - (7) 所有 GPU 上的参数更新完成.

## 卷积神经网络

- 在实践中, 我们很少使用不一致的步幅或填充.

```
注意, 在应用批量规范化时, 批量大小的选择可能比未批量规范化时更重要.
```

```
事实证明, 这是深度学习中一个反复出现的主题.
优化中的各种噪声源通常会导致更快的训练和较少的过拟合,
虽然目前尚未在理论上明确证明, 这种变化似乎是正则化的一种形式.
```

### ResNet (残差网络)

- 残差网络的核心思想是: 每个附加层都应该更容易地包含原始函数作为其元素之一.
  - 于是, `残差块`便诞生了.

## 循环神经网络

- 我们可以从随机偏移量开始拆分序列, 以同时获得`覆盖性`和`随机性`.
  - 下面, 我们将描述如何实现`随机抽样`和`顺序分区`策略.

```
在随机抽样中, 每个样本都是在原始的长序列上任意捕获的子序列.
在迭代过程中, 来自两个相邻的, 随机的, 小批量中的子序列不一定在原始序列中相邻.
对于语言建模, 目标是基于到目前为止我们看到的词元来预测下一个词元,
因此标签是移位了一个词元的原始序列.
```

```
在迭代过程中, 除了可以对原始序列随机抽样,
我们还可以保证两个相邻的小批量中的子序列在原始序列中也是相邻的.
这种策略在基于小批量的迭代过程中保留了拆分的子序列的顺序,
因此称为顺序分区.
```

- 遗憾的是, 虽然随机截断在理论上具有吸引力,
  但由于多种因素很可能在实践中并不比常规截断效果好,
  原因有 `3` 个方面:
  - 第一, 在对过去若干时间步经过反向传播后,
    观测结果足以捕获实际的依赖关系;
  - 第二, 增加的方差抵消了时间步数越多梯度越精确的效果;
  - 第三, 我们真正想要的是只在小范围交互的模型. 因此,
    模型需要的正是截断的通过时间反向传播方法所具备的轻度正则化效果.

- 门控循环单元与普通的循环神经网络之间的关键区别在于:
  前者支持隐状态的门控. 这意味着模型有专门的机制来确定应该何时更新隐状态,
  以及应该何时重置隐状态.

- 总之, 门控循环单元具有以下两个显著特征.
  - `重置门`有助于捕获序列中的短期依赖关系.
  - `更新门`有助于捕获序列中的长期依赖关系.

## 注意力机制

- 因此, "是否包含自主性提示"将注意力机制与全连接层或汇聚层区别开来.
  - 在注意力机制的背景下, 自主性提示被称为`查询`.
  - 给定任何查询, 注意力机制通过`注意力汇聚`将选择引导至`感官输入`,
    例如中间特征表示.
  - 在注意力机制中, 这些感官输入被称为`值`. 更通俗地解释,
    每个值都与一个`键`匹配, 这可以想象为感官输入的非自主性提示.

## 自然语言处理

```
虽然独热向量很容易构建, 但它通常不是一个好的选择,
其中一个主要原因是独热向量不能准确表达不同词之间的相似度,
如我们经常使用的"余弦相似度".
```
