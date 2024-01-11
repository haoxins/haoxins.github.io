---
title: 量子计算与量子信息 (Part 1)
description: 槛菊愁烟兰泣露, 罗幕轻寒, 燕子双飞去. 明月不谙离恨苦, 斜光到晓穿朱户.
date: 2023-01-17
---

- [量子计算与量子信息: 10 周年版](https://book.douban.com/subject/35777059/)

```
为什么量子算法的突破如此艰难?
媒体上普遍解释量子计算的加速是由于指数级的并行处理,
这种理解没有触及量子计算的本质, 因为量子计算完全不同于计算机界耳熟能详的"并行处理".
在一个量子比特的状态里, 大自然隐藏了大量的"隐含信息",
量子算法必须利用量子界独特的干涉和纠缠特性.

经典的并行性是用多个电路同时计算 f(x), 而量子并行性是利用不同量子状态的叠加,
用单个 f(x) 电路同时计算多个 x 的函数值.
"纠缠"不是简单的并行, 而是我们在宏观世界从未接触过的新的"自然资源".
人类的直觉植根于经典世界, 如果只是借助于我们已有的知识和直觉来设计算法,
就跳不出经典思维的局限. 为设计好的量子算法, 需要部分地"关闭"经典直觉,
巧妙地利用量子效应去达到期望的算法目的.

Shor 教授曾出版过诗集, 是一个具有诗人一样浪漫思维的标新立异的学者.
他采用不同寻常的思路, 将整数质因数分解重构为一个新问题:
确定一个序列的重复周期. 这本质上是一种傅里叶变换,
可以通过在量子比特的全集上使用全局运算找到这个序列.

上世纪 80 年代人们就知道量子计算机可以实现傅里叶变换,
但由于在量子计算机上, 振幅不能通过测量直接访问,
也没有有效的方法来制备傅里叶变换的初始态,
因此寻找量子傅里叶变换的应用希望渺茫.

Shor 教授找到了在不测量计算的情况下测量误差的巧妙办法,
用量子傅里叶变换解决了整数因子分解和离散对数问题.
量子计算将计算机科学推向物理学的最前沿, 如果没有对量子纠缠的深刻理解,
只在传统的并行处理上动脑筋, 就难以找到比传统算法更有效的量子算法.
```

```
学习与研究量子算法的另一个难点是, 传统算法已经研究了几十年,
各个领域都有大量成熟的算法, 如果我们设计的量子算法与已有的算法相比,
没有明显的优势, 就没有必要"杀鸡用牛刀"了.
尽管量子计算机的物理实现有较大进展, 但运行 Shor 算法破解 1024 位
RSA 的加密信息仍需要比当前量子计算机的规模扩大五个数量级,
错误率则要再降低两个数量级, 估计近十年内难以实现.

在有噪声的中尺度量子计算机上能有效运行哪些有重大科学和经济价值的量子算法,
是当前应优先考虑的研究方向. 在量子搜索, 量子组合优化, 量子机器学习,
量子游走, 变分量子算法等方向都有可能做出实用化的量子算法.
在未来的 10 到 15 年内, 量子计算机可能是与传统计算机互补的协处理器或加速器,
量子算法与传统算法的协同值得高度重视.
```

```
这种情况在 20 世纪七八十年代开始发生改变, 当时一些先驱者受到启发,
开始考虑计算机科学和信息论的一些基本问题是否可以应用于量子系统的研究.
相比将量子系统纯粹视为自然界中可以解释的现象, 他们将量子系统视为可以设计的系统.
这似乎是观念上的微小变化, 但意义是深远的.
量子世界不再仅仅是呈现出来的, 而是可以创造出来的.
其结果是一幅全新的景象, 不仅激发了人们对量子力学基本原理的兴趣,
还有融合了物理学, 计算机科学和信息论的许多新问题. 这些问题包括:
构建量子态所需的空间和时间的基本物理限制是什么?
实现给定的动态操作需要多少时间和空间?
是什么使量子系统难以通过传统的经典方法来理解和模拟?
```

- 本书的`约定`
  - __向量空间假定是有限维的__.

## 简介与概述

```
什么是量子力学?
量子力学是一个数学框架或物理理论构建的规则集.

量子力学与像量子电动力学那样的特定物理理论的关系,
更像是计算机操作系统与特定应用软件的关系 --
操作系统设置某些基本参数和操作模式,
而应用软件则完成特定任务.
```

> 与 Scott Aaronson 的观点类似, 是量子计算领域的主流观点?

### 量子比特

### 量子计算

### 量子算法

### 实验量子信息处理

### 量子信息

## 量子力学基础

### 线性代数

```
在我们看来, 认同量子力学公设的主要障碍不是公设本身,
而是为理解它们所需要的大量的线性代数概念.
再加上量子力学中被物理学家采用的不常用的狄拉克 (Dirac) 符号.
```

> 注: 原文为狄拉克`记号`, 但显然`符号`更主流.

- 向量空间中向量的标准量子力学记号为
  $$ \mid ψ \rangle $$
  - $$ ψ $$
    是向量的标签 (任意的标签都是有效的, 尽管我们喜欢用像
    $$ ψ $$
    和
    $$ φ $$
    这样的简单标签).
  - 记号
    $$ \mid \cdot \rangle $$
    用来表示其中的对象是向量.
- 常见符号
  - $$ \mid ψ \rangle $$,
    向量
  - $$ \langle ψ \mid $$,
    $$ \mid ψ \rangle $$
    的对偶向量
  - $$ \langle φ \mid ψ \rangle $$,
    向量
    $$ \mid φ \rangle $$
    和
    $$ \mid ψ \rangle $$
    的内积
  - $$ \mid φ \rangle \otimes \mid ψ \rangle $$,
    $$ \mid φ \rangle $$
    和
    $$ \mid ψ \rangle $$
    的张量积
  - $$ \mid φ \rangle \mid ψ \rangle $$,
    $$ \mid φ \rangle $$
    和
    $$ \mid ψ \rangle $$
    张量积的缩写
  - $$ \mathbf{A}^{\dagger} $$,
    矩阵 __A__ 的厄米共轭或伴随,
    $$ \mathbf{A}^{\dagger} = (\mathbf{A}^{T})^{*} $$.
    $$
      \begin{bmatrix}
        a & b \\
        c & d
      \end{bmatrix}^{\dagger}
      =
      \begin{bmatrix}
        a^{*} & c^{*} \\
        b^{*} & d^{*}
      \end{bmatrix}
    $$
  - $$ \langle φ \mid \mathbf{A} \mid ψ \rangle $$,
    $$ \mid φ \rangle $$
    和
    $$ \mathbf{A} \mid ψ \rangle $$
    的内积. 等价的,
    $$ \mathbf{A}^{\dagger} \mid φ \rangle $$
    和
    $$ \mid ψ \rangle $$
    的内积

> __注__: 符号
  $$ \mathbf{A}^{*} $$,
  在线性代数中表示:
  [共轭转置](https://en.wikipedia.org/wiki/Conjugate_transpose),
  但在量子力学中, 仅仅表示`共轭`.
> $$ \mathbf{A}^{\dagger} $$
  在量子力学中替代了
  $$ \mathbf{A}^{*} $$
  在线性代数中的含义.

- 向量空间 __V__ 和 __W__ 之间的`线性算子`定义为对输入具有线性性质的映射
  $$ \mathbf{A}: \mathbf{V} \to \mathbf{W} $$:
  - $$
      \mathbf{A} (\sum_{i} a_i \mid v_i \rangle) =
      \sum_i a_i \mathbf{A} (\mid v_i \rangle)
    $$
  - 通常将
    $$ \mathbf{A} (\mid v \rangle) $$
    写成
    $$ \mathbf{A} \mid v \rangle $$.
- 当我们说定义在线性空间 __V__ 上的线性算子 __A__ 时,
  意味着 __A__ 是一个从 __V__ 到 __V__ 的线性算子.
- 在任意向量空间 __V__ 上, 一个重要的线性算子是`恒等算子`,
  $$ I_V $$,
  定义为对任意的向量
  $$ \mid v \rangle $$,
  $$ I_V (\mid v \rangle) = \mid v \rangle $$.
  - 在不会出现混淆时, 我们丢弃下标 __V__ 仅用 __I__ 表示恒等算子.
- 另一个重要的线性算子是`零算子`, 用
  $$ \mathbf{0} $$
  表示.
  - 零算子把所有的向量都映射为零向量, 即
    $$ \mathbf{0} \mid v \rangle = \mathbf{0} $$.
- 很容易看出, 一旦线性算子在基上的行为确定, __A__ 在所有输入上的行为也就确定了.

---

- __泡利矩阵__
  - $$
      I \equiv
      \begin{bmatrix}
        1 & 0 \\
        0 & 1
      \end{bmatrix}
    $$
  - $$
      X \equiv
      \begin{bmatrix}
        0 & 1 \\
        1 & 0
      \end{bmatrix}
    $$
  - $$
      Y \equiv
      \begin{bmatrix}
        0 & -i \\
        i & 0
      \end{bmatrix}
    $$
  - $$
      Z \equiv
      \begin{bmatrix}
        1 & 0 \\
        0 & -1
      \end{bmatrix}
    $$

---

- 假设
  $$ \mathbf{A} : \mathbf{V} \to \mathbf{W} $$
  是向量空间 __V__ 和 __W__ 之间的线性算子.
  $$ \mid v_1 \rangle $$,
  ...,
  $$ \mid v_m \rangle $$
  是 __V__ 的一组基,
  $$ \mid w_1 \rangle $$,
  ...,
  $$ \mid w_n \rangle $$
  是 __W__ 的一组基. 则对
  `1`, ..., `m` 中任意的 `j` 存在复数
  $$ A_{1j} $$
  到
  $$ A_{nj} $$,
  使得
  - $$
      \mathbf{A} \mid v_j \rangle =
      \sum_{i} \mathbf{A}_{ij} \mid w_i \rangle
    $$
- 我们称这个元素为
  $$ A_{ij} $$
  的矩阵形成了算子 __A__ 的一个矩阵表示. __A__ 的矩阵表示完全等价于算子 __A__,
  因而我们将交替使用矩阵和算子的概念.
  - 需要注意的是, 为了建立矩阵和线性算子之间的联系,
    我们需要为线性算子的输入和输出向量空间各指定一组输入和输出基矢态.

---

- 内积
  $$ (\mid v \rangle, \mid w \rangle) $$
  的标准量子力学记号是
  $$ \langle v \mid w \rangle $$,
  其中
  $$ \mid v \rangle $$
  和
  $$ \mid w \rangle $$
  是内积空间的向量, 记号
  $$ \langle v \mid $$
  是向量
  $$ \mid v \rangle $$
  的对偶向量; 对偶是从内积空间 __V__ 映射到复数
  $$ \mathbb{C} $$
  的一个线性算子, 其中
  $$
    \langle v \mid (\mid w \rangle) \equiv
    \langle v \mid w \rangle \equiv
    (\mid v \rangle, \mid w \rangle)
  $$.
  - 对偶向量的矩阵表示就是一个行向量.
- 一个从
  $$ \mathbf{V} \times \mathbf{V} $$
  到复数空间
  $$ \mathbb{C} $$
  的函数
  $$ (\cdot, \cdot) $$,
  如果满足下面的要求:
  - $$ (\cdot, \cdot) $$
    对于第二个参数是线性的:
    $$
      (\mid v \rangle, \sum_{i} \lambda_{i} \mid w_i \rangle) =
      \sum_i \lambda_{i} (\mid v \rangle, \mid w_i \rangle)
    $$
  - $$
      (\mid v \rangle, \mid w \rangle) =
      (\mid w \rangle, \mid v \rangle)^{*}
    $$
  - $$ (\mid v \rangle, \mid v \rangle) \ge 0 $$,
    当且仅当
    $$ \mid v \rangle = \mathbf{0} $$
    时等式成立.
- 则称函数
  $$ (\cdot, \cdot) $$
  是一个内积.
  - 例如,
    $$ \mathbb{C}^{n} $$
    中的内积定义为
  - $$
      ((y_{1}, ..., y_{n}), (z_{1}, ..., z_{n})) \equiv
      \sum_{i} y_{i}^{*} z_{i} =
      [y_{1}^{*}, ..., y_{n}^{*}]
      \begin{bmatrix}
        z_{1} \\
        \vdots \\
        z_{n}
      \end{bmatrix}
    $$
- 我们称定义了内积的向量空间为`内积空间`.

> 注: 复向量内积的定义有差异, 参见
  [Dot product](https://en.wikipedia.org/wiki/Dot_product)
  和
  [Inner product space](https://en.wikipedia.org/wiki/Inner_product_space).
  计算结果共轭, 无实质区别~ 量子领域取本书的定义.
> 关于对偶, 参看
  [如何直观的理解对偶?](https://mp.weixin.qq.com/s/IHzQNZdhWx6ZtWjiYvcD_Q),
  [对偶空间](https://en.wikipedia.org/wiki/Dual_space),
  [从矢量到张量](math-vector-to-tensor-1.md).

```
量子力学的讨论总是关系到希尔伯特空间.
在量子计算和量子信息中出现的有限维复向量空间中,
希尔伯特空间和内积空间完全相同. 从现在开始,
我们交替使用这两个术语, 较多用希尔伯特空间这个术语.
在无限维度, 希尔伯特空间满足内积空间之上和之外的技术限制, 我们不需要担心.
```

> 再次重申, 本书只讨论`有限维`~

- 简单来说, 正规化一个向量就是用该向量除以它的范数;
  因此, 对任意的非零向量
  $$ \mid v \rangle $$,
  $$ \mid v \rangle / \| \mid v \rangle \| $$
  是
  $$ \mid v \rangle $$
  的正规化.
  - 对于一个向量集
    $$ \mid i \rangle $$,
    其中 `i` 是指标, 如果集合中的每一个向量都是单位向量,
    而且不同的向量之间是正交的, 即
    $$ \langle i \mid j \rangle = \delta_{ij} $$,
    这里 `i`, `j` 取自指标集, 那么称该向量集为`标准正交`的.

> 注:
  $$ \delta_{ij} $$
  是`克罗内克函数`. 原书并未指出~

- [格拉姆-施密特正交化](https://en.wikipedia.org/wiki/Gram-Schmidt_process)

- __下面又是本书约定__

```
从现在起, 当我们说一个线性算子的矩阵表示时,
意味着关于标准正交输入和输出基的矩阵表示.
我们还使用这样的约定:
如果线性算子的输入和输出空间相同,
那么输入和输出基相同, 除非另有说明.
```

- 根据这些约定, 希尔伯特空间的内积可以方便地用矩阵表示.
  只要向量的矩阵表示按同一组标准正交基给出,
  两个向量的内积就等于向量矩阵表示的内积.
  - 我们也看到对偶向量
    $$ \langle v \mid $$
    作为行向量有一个好的解释, 它的元素是向量
    $$ \mid v \rangle $$
    的列向量表示中对应分量的复共轭.

> 注: 下面注意区别:
  [Cross product](https://en.wikipedia.org/wiki/Cross_product),
  [Outer product](https://en.wikipedia.org/wiki/Outer_product),
  [Tensor product](https://en.wikipedia.org/wiki/Tensor_product).
  量子领域感觉译作`张量积`多一些, 而且上文刚刚出现过`张量积`.

- 有一种表示线性算子的有用方式, 充分地利用了内积, 称为外积表示. 假设
  $$ \mid v \rangle $$
  是内积空间 __V__ 的一个向量,
  $$ \mid w \rangle $$
  是内积空间 __W__ 的一个向量. 定义
  $$ \mid w \rangle \langle v \mid $$
  为从 __V__ 到 __W__ 的一个线性算子, 其作用为
  - $$
      (\mid w \rangle \langle v \mid)(\mid v' \rangle) \equiv
      \mid w \rangle \langle v \mid v' \rangle =
      \langle v \mid v' \rangle \mid w \rangle
    $$
- 这个方程与我们的记号约定完美吻合, 表达式
  $$ \mid w \rangle \langle v \mid v' \rangle $$
  可能含有以下两种含义之一:
  - 我们用它表示算子
    $$ \mid w \rangle \langle v \mid $$
    作用在
    $$ \mid v' \rangle $$
    上的结果,
  - 也可以解释为
    $$ \mid w \rangle $$
    被一个复数
    $$ \langle v \mid v' \rangle $$
    相乘.
- 我们选择的定义使得这两种潜在意思是一致的, 事实上我们通过后者定义了前者!

> [柯西-施瓦茨不等式](https://en.wikipedia.org/wiki/Cauchy-Schwarz_inequality)

- 外积记号的有用性可以从标准正交向量满足的完备性关系中看清楚. 令
  $$ \mid i \rangle $$
  为向量空间
  $$ \mathbf{V} $$
  的任意一组标准正交基, 那么任意向量
  $$ \mid v \rangle $$
  可以写为
  $$ \mid v \rangle = \sum_{i} v_i \mid i \rangle $$,
  $$ v_i $$
  是一组复数. 注意到
  $$ \langle i \mid v \rangle = v_i $$,
  因此
  - $$
      (\sum_{i} \mid i \rangle \langle i \mid) \mid v \rangle =
      \sum_{i} \mid i \rangle \langle i \mid v \rangle =
      \sum_{i} v_i \mid i \rangle =
      \mid v \rangle
    $$
- 由于最后的等式对于任意的
  $$ \mid v \rangle $$
  成立, 这等于说
  - $$ \sum_{i} \mid i \rangle \langle i \mid = \mathbf{I} $$
- 这个等式就是著名的`完备性关系`.
  完备性关系的一个应用是用外积的记号给出任意算子的表示方式. 假设
  $$ \mathbf{A}: \mathbf{V} \to \mathbf{W} $$
  是一个线性算子,
  $$ \mid v_i \rangle $$
  是
  $$ \mathbf{V} $$
  的一组标准正交基,
  $$ \mid w_i \rangle $$
  是
  $$ \mathbf{W} $$
  的一组标准正交基. 运用两次完备性关系, 可以得到
  - $$
      \begin{align}
        \mathbf{A}
          & = \mathbf{I}_{W} \mathbf{A} \mathbf{I}_{V} \\
          & = \sum_{ij}
              \mid w_j \rangle
              \langle w_j \mid A \mid v_i \rangle
              \langle v_i \mid \\
          & = \sum_{ij}
              \langle w_j \mid A \mid v_i \rangle
              \mid w_j \rangle
              \langle v_i \mid \\
      \end{align}
    $$
- 这是
  $$ \mathbf{A} $$
  的外积表示. 从这个方程我们还看到,
  $$ \mathbf{A} $$
  的第 `i` 列第 `j` 行的矩阵元素为
  $$ \langle w_j \mid \mathbf{A} \mid v_i \rangle $$,
  与输入基
  $$ \mid v_j \rangle $$
  和输出基
  $$ \mid w_j \rangle $$
  有关.

---

- [特征值和特征向量](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors)
  - [本征函数](https://en.wikipedia.org/wiki/Eigenfunction)

- 算子 __A__ 与特征值 __v__ 对应的特征空间 (本征空间) 是以 __v__ 为特征值的向量的集合.
  - 它是 __A__ 作用的向量空间的子空间.
  - 当特征空间高于一维时, 我们说它是`退化`的.

- 假设 __A__ 是希尔伯特空间 __V__ 上的任意一个线性算子. 事实上在
  __V__ 上存在一个唯一的线性算子
  $$ \mathbf{A}^{\dagger} $$,
  满足对所有的向量
  $$ \mid v \rangle, \mid w \rangle \in \mathbf{V} $$
  都有
  - $$
      (\mid v \rangle, \mathbf{A} \mid w \rangle) =
      (\mathbf{A}^{\dagger} \mid v \rangle, \mid w \rangle)
    $$
- 这个线性算子称为
  $$ \mathbf{A} $$
  算子的`伴随`或`厄米共轭`. 根据定义易知
  $$ (\mathbf{AB})^{\dagger} = \mathbf{B}^{\dagger} \mathbf{A}^{\dagger} $$.
  - 一般地, 如果
    $$ \mid v \rangle $$
    是一个向量, 那么我们定义
    $$ \mathbf{v}^{\dagger} \equiv \langle v \mid $$.
  - 根据这个定义不难看出
    $$ (\mathbf{A} \mid v \rangle)^{\dagger} = \langle v \mid \mathbf{A}^{\dagger} $$.

### 量子力学的假设

### 应用: 超密编码

### 密度算子

### 施密特分解与纯化

### EPR 和贝尔不等式

## 量子计算机: 物理实现

> 这一章比较麻烦~
  物理实现种类繁多, 工艺复杂, 对于非领域相关者, 意义不大.
  且在可预见的未来存在大量变数!
  但是, 概略性的介绍其实也是有必要的, 专注在理论框架即可~

- 实现量子计算有 `4` 项基本要求:
  1. 量子比特表示,
  2. 可控酉演化,
  3. 初始量子比特态的制备, 以及
  4. 最终量子比特态的测量.

### 指导性原则

### 量子计算的条件

### 谐振子量子计算机

### 光学光量子计算机

### 光学腔量子电动力学

### 离子阱

### 核磁共振

### 其他实现方案

## 计算机科学简介

> 标题不好, 可以改为: 计算理论简介.

### 计算模型

### 计算问题的分析

### 关于计算科学的观点

## 附录

### B. 群论

### D. 数论
