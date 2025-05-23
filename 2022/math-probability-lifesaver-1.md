---
title: 普林斯顿概率论读本
description: 翠叶藏莺, 珠帘隔燕. 炉香静逐游丝转. 一场愁梦酒醒时, 斜阳却照深深院.
date: 2022-11-24
---

- [普林斯顿概率论读本](https://book.douban.com/subject/35193606/)

> 注意, 本书中用
  $$ \log x $$
  表示以 `e` 为底 `x` 的对数, 而不是用
  $$ \ln x $$.

- 当 `x` 取值较小时, `log(1 - x)` 近似于 `-x`.
  - 在讨论中心极限定理的证明时, 我们还会遇到这种展开式.

```
关于和与积分之间的相互转化, 我们有一套庞大的理论.
你可能还记得像黎曼和, 黎曼积分这样的名词.
但要注意, 在乘积里并没有类似的概念. 我们所熟知的只有和.
虽然我们对于乘积了解得并不多, 但会看到对数可以把乘积转化成和,
这样就能进入熟悉的领域. 如果你不清楚对数为什么有用,
那现在是时候来了解它了. 对数法则是标准化测试的内容,
所以我们在这里不展开讨论. 实际上, 对数法则是解决很多问题的好方法.
```

- __几何级数公式__:
  - 设 `r` 是一个绝对值小于 `1` 的实数, 那么
  - $$ \sum_{n = 0}^{\infty} r^n = 1 + r + r^2 + r^3 + ... = \frac{1}{1 - r} $$

## 基本概率定律

```
从罗素悖论中可以推出一个结论,
那就是我们无法通过简单地收集具有给定性质的所有对象来形成集合.
幸运的是, 我们在概率论中遇到的绝大多数集合都没有这个问题,
但重要的是意识到潜在的危险, 并且要正确, 认真地理解证明.
```

- $$ A \times B $$:
  称为 `A` 和 `B` 的`笛卡儿乘积`.
  它是全体有序对 `(a, b)` 的集合, 其中
  $$ a \in A $$
  且
  $$ b \in B $$.
  - 当 `A = B` 时, 我们通常用
    $$ A^2 $$
    来表示
    $$ A \times A $$.
  - 更一般地, 如果有 `n` 个 `A` 相乘, 则记作
    $$ A^n $$.
- $$ \mathcal{P} (A) $$:
  称作 `A` 的幂集. 它是 `A` 的所有子集的集合.
  如果 `A = {x, y}`, 那么

$$
\mathcal{P} (A) =
  \left \{
    \varnothing,
    \left \{ x \right \},
    \left \{ y \right \},
    A
  \right \}
$$.

> 注意,
  $$ \mathcal{P} (A) $$
  中的元素自身就是集合.

```
一个有趣的问题是怎样以严格的, 集合论的方式来构造整数集
(或者更一般地构造实数集). 令人惊奇的是,
在只有一个空集的前提下就可以实现这一点!
我们可以利用空集 ø 来构造一个集合, 即 {ø} (包含空集的集合).
按照这种方法, 我们还能构造出 {ø, {ø}},
继续进行下去又得到了 {∅, {ø}, {ø, {ø}}}.
如果让 ø 对应于 0, {ø} 对应于 1, {ø, {ø}} 对应于 2, 等等,
那么不难看出, 每个"数"都是比它大的那个数的真子集
(因此, 集合的包含关系相当于"小于").
```

- 概率空间的有用规则: 设
  $$ (\Omega, \sum, Prob) $$
  是一个概率空间, 那么可以得到如下结论.
  - (1) __全概率公式__: 如果
    $$ A \in \sum $$,
    那么
    $$ Pr(A) + Pr(A^c) = 1 $$.
  - 也就是说,
    $$ Pr(A) = 1 - Pr(A^c) $$.
  - (2)
    $$ Pr(A \cup B) = Pr(A) + Pr(B) - Pr(A \cap B) $$.
  - 这个式子可以进一步推广. 例如, 如果有三个事件, 那么
  - $$ Pr(A_1 \cup A_2 \cup A_3) =
       Pr(A_1) + Pr(A_2) + Pr(A_3) -
       Pr(A_1 \cap A_2) - Pr(A_1 \cap A_3)- Pr(A_2 \cap A_3) +
       Pr(A_1 \cap A_2 \cap A_3) $$.
  - 这也被称为`容斥原理`.
  - (3) 如果
    $$ A \subset B $$,
    那么
    $$ Pr(A) \leqslant Pr(B) $$.
    然而, 如果 `A` 是 `B` 的真子集, 那么不一定有
    $$ Pr(A) < Pr(B) $$,
    但我们确定有
    $$ Pr(B) = Pr(A) + Pr(B \cap A^c) $$,
    其中
    $$ B \cap A^c $$
    指的是 `B` 中不属于 `A` 的所有元素.
  - (4) 如果对于任意的
    $$ i $$,
    均有
    $$ A_i \subset B $$,
    那么
    $$ Pr(\cup_i A_i) \leqslant Pr(B) $$.

## 条件概率, 独立性和贝叶斯定理

- __条件概率__: 设 `B` 是满足条件
  $$ Pr(B) > 0 $$
  的事件. 那么已知 `B` 时 `A` 的条件概率就等于
  - $$ Pr(A \mid B) = Pr(A \cap B) / Pr(B) $$.

- __一般乘法法则__: 我们有
  - $$ Pr(A \cap B) = Pr(A \mid B) · Pr(B) $$.

- __独立性 (两个事件)__: 如果事件 `A` 和 `B` 满足
  - $$ Pr(A \cap B) = Pr(A) · Pr(B) $$,
  - 那么 `A` 和 `B` 就是独立的.

- __独立性 (三个事件)__: 如果事件 `A`, `B` 和 `C` 满足
  - (1)
    $$ Pr(A \cap B \cap C) = Pr(A) · Pr(B) · Pr(C) $$,
    并且
  - (2) 其中任意两个事件都是独立的,
  - 那么 `A`, `B` 和 `C` 就是相互独立的.

- __独立性 (一般情形)__: 如果事件
  $$ A_1, ..., A_n $$
  满足
  - (1)
    $$ Pr(A_1 \cap ... \cap A_n) = Pr(A_1) ... Pr(A_n) $$,
    并且
  - (2)
    $$ \left \{ A_1, ..., A_n \right \} $$
    的任意一个非空子集都是相互独立的,
  - 那么
    $$ A_1, ..., A_n $$
    就是相互独立的.

> 关于三个或更多个事件的独立性, 这里有个重要的警告:
  当任意两个事件都独立时, 三个或更多事件可能会相互依赖.

---

- __贝叶斯定理__: 由一般乘法法则可以推出:
  对于事件 `A` 和 `B`, 有
  - $$ Pr(B \mid A) · Pr(A) = Pr(A \mid B) · Pr(B) $$.
  - 因此, 只要
    $$ Pr(B) ≠ 0 $$,
    我们就有
  - $$ Pr(A \mid B) = Pr(B \mid A) · \frac{Pr(A)}{Pr(B)} $$.

- __划分成两部分__: 设 `B` 是满足
  $$ 0 < Pr(B) < 1 $$
  的事件 (那么对于事件
  $$ B^c $$,
  即 `B` 不发生, 也是如此).
  - 于是, 我们可以将事件 `A` 划分成两个互不相交的事件, 即
    $$ A \cap B $$
    和
    $$ A \cap B^c $$,
    而且有
  - $$ Pr(A) = Pr(A \mid B) Pr(B) + Pr(A \mid B^c) Pr(B^c) $$.
- 这个公式是很合理的. 通过大声朗读这个式子, 我们看到,
  `A` 发生的概率就是 (已知 `B` 发生时 `A` 发生的概率) 乘以
  (`B` 发生的概率), 然后再加上 (已知 `B` 不发生时 `A` 发生的概率)
  乘以 (`B` 不发生的概率).
  - 我们分成了两种情况: `B` 发生时的结果, 和 `B` 不发生时的结果.

```
遗憾的是, 贝叶斯定理很难应用于实际情况. 我们需要明确地知道 Pr(A) 和 Pr(B) 是多少.
通常, 虽然无法确切地知道 Pr(B) 和 Pr(A) 都是什么, 但我们会得到一些条件概率,
由此可以计算出 Pr(B) 或 Pr(A). 利用这种方法, 我们可以构造一般版本的贝叶斯定理.
但是, 为了做到这一点, 必须先提高对划分理论的认识.
```

- 在开始之前, 我们先了解一些术语. 记住, 如果集合 `A` 和集合 `B` 满足
  $$ A \cap B = \varnothing $$,
  那么它们就是不相交的.
  - 也就是说, 如果 `A` 和 `B` 没有相同的元素, 那么它们就不相交.
- 样本空间 `S` 的一个划分就是满足下列条件的可数个集合
  $$ \left \{ A_1, A_2, ... \right \} $$.
  - (1) 如果
    $$ i ≠ j $$,
    那么
    $$ A_i $$
    和
    $$ A_j $$
    不相交. 我们通常用
    $$ A_i \cap A_j = \varnothing $$
    来表示这两个集合的交是空集.
  - (2) 全体
    $$ A_i $$
    的并就是整个样本空间:
    $$ \cup_i A_i = S $$.

---

- __全概率法则__: 如果
  $$ \left \{ B_1, B_2, ... \right \} $$
  构成了样本空间 `S` 的一个划分 (分成了至多可数个部分), 那么对于任意的
  $$ A \subset S $$,
  我们有
  - $$ Pr(A) = \sum_{n} Pr(A \mid B_n) · Pr(B_n) $$.
- 对于所有的 `n`, 都应该有
  $$ 0 < Pr(B_n) < 1 $$,
  否则条件概率就是无定义的.
  - 注意, 如果有一个
    $$ B_n $$
    的概率为 `0`, 那么我们就不需要这个
    $$ B_n $$
    了, 因为它会给出因子
    $$ Pr(B_n) = 0 $$;
    但如果它的概率是 `1`, 那么其他所有项都是不必要的.

---

- __贝叶斯定理__: 设
  $$ \left \{ A_i \right \}_{i=1}^n $$
  是样本空间的一个划分, 那么
  - $$
      Pr(A \mid B) = \frac
      {Pr(B \mid A) · Pr(A)}
      {\sum_{i=1}^{n} Pr(B \mid A_i) · Pr(A_i)}
    $$.
  - 通常情况下, `A` 就是某个
    $$ A_i $$.

## 计数 II: 容斥原理

- __对立事件__: 在很多问题中, 要想求出 `A` 的概率,
  最简单的方法就是求出 `A` 不发生的概率, 因为
  $$ Pr(A) = 1 - Pr(A^c) $$.
  - 这在解决`"至少一个"`的问题上是非常有用的,
    因为它的对立事件就是什么都没有发生.

---

- 我们可以写得简洁一些. 设
  $$ A_{l_1 l_2 ... l_k} = A_{l_1} \cap A_{l_2} \cap ... \cap A_{l_k} $$
  (因此
  $$ A_{12} = A_1 \cap A_2 $$
  且
  $$ A_{489} = A_4 \cap A_8 \cap A_9 $$
  ), 于是

$$
\begin{align}
  \mid \cup_{i=1}^{n} A_i \mid
  & = \sum_{i=1}^{n} \mid A_i \mid                   \\
  & - \sum_{1 \le i < j \le n} \mid A_{ij} \mid      \\
  & + \sum_{1 \le i < j < k \le n} \mid A_{ijk} \mid \\
  & - ...                                            \\
  & + (-1)^{n-2}
      \sum_{1 \le l_1 < l_2 < ... < l_{n-1} \le n}
      \mid A_{l_1 l_2 ... l_{n-1}} \mid              \\
  & + (-1)^{n-1} \mid A_{1 2 ... n} \mid             \\
\end{align}
$$.

- 如果
  $$ A_i $$
  均为有限集, 并且我们使用的计数度量以结果空间中每个元素都是等可能的为基础,
  那么可以把上面所有的 `|S|` 都替换成 `Pr(S)`.

---

- __等可能集合的容斥原理__: 在涉及容斥原理的很多问题中, 所有集合
  $$ A_i $$
  都具有相同的大小, 所有集合
  $$ A_i \cap A_j = A_{ij} $$
  也具有相同的大小, 而且所有集合
  $$ A_i \cap A_j \cap A_k = A_{ijk} $$
  同样具有相同的大小, 等等.
  - 这使得计数更加简单, 于是公式被简化成了

$$
\begin{align}
  \mid \cup_{i=1}^{n} A_i \mid
    & = n \mid A_1 \mid                 \\
    & - \tbinom{n}{2} \mid A_{12} \mid  \\
    & + \tbinom{n}{3} \mid A_{123} \mid \\
    & - ...                             \\
    & + (-1)^{n-1} \mid A_{1 2 ... n} \mid
\end{align}
$$.

---

- 我们对容斥原理的证明是以二项式定理为基础的, 也就是
  - $$
      (x + y)^n =
      \sum_{k = 0}^{n}
      \binom{n}{k}
      x^{k}y^{n - k}
    $$;

---

- 从`"至少"`到`"恰好"`的方法:
  $$ N(K) $$
  表示至少有 `k` 个事件发生的方法数;
  $$ E(k) $$
  表示恰好有 `k` 个事件发生的方法数.
  - 那么
    $$ E(k) = N(k) - N(k + 1) $$.
  - 等价说法是,
  - $$ Pr(恰好有 k 个发生) = Pr(至少有 k 个发生) - Pr(至少有 k + 1 个发生) $$.

---

- __多项式系数__: 设 `N` 是一个正整数, 且
  $$ n_1 $$,
  $$ n_2 $$,
  ...,
  $$ n_k $$
  是满足和为 `N`
  $$ (n_1 + ... + n_k = N) $$
  的非负整数. 那么多项式系数就是

$$
\binom{N}{n_1, n_2, ..., n_k} =
\frac{N!}{n_{1}! n_{2}! ... n_{k}!}
$$

## 离散型随机变量

- __离散型随机变量的`概率密度`函数__: 设 `X` 是一个随机变量,
  它定义在离散的结果空间
  $$ \Omega $$
  上 (
  $$ \Omega $$
  是有限的或至多可数的).
  - 那么 `X` 的`概率密度`函数 (常记作
    $$ f_X $$
    ) 就是 `X` 取某个特定值的概率:
  - $$ f_{X} (x) = Prob (\omega \in \Omega : X(\omega) = x) $$.
- 注意, 有些教材用`概率质量`函数的说法, 而非概率密度函数.
- 概率密度函数的值总是大于或等于 `0`, 并且和始终为 `1`.

---

- __离散型随机变量的`累积分布`函数__: 设 `X` 是一个随机变量,
  它定义在一个有限的或至多可数的离散结果空间
  $$ \Omega $$
  上.
  - 回忆一下, `X` 的`概率密度`函数 (常记作
    $$ f_X $$
    ) 就是 `X` 取某个特定值的概率.
- `累积分布`函数 (常记作
  $$ F_X $$
  ) 则表示 `X` 不超过某个特定值的概率.
  - 它们分别记作
  - $$ f_{X} (x) = Prob (\omega \in \Omega : X(\omega) = x) $$
  - $$ F_{X} (x) = Prob (\omega \in \Omega : X(\omega) ≤ x) $$.

## 工具: 期望

- __泰勒级数__: 如果 `f` 是 `n` 次可微分的 (其中
  $$ f^{(k)}(x) $$
  表示 `f` 在 `x` 处的 `k` 阶导数),
  那么 `f` 在 `a` 点处的 `n` 阶泰勒级数就是

$$
T_{n} (x) := f(a) + f'(a)(x - a) +
\frac{f''(a)}{2!} (x - a)^2 + ... +
\frac{f^{(n)} (a)}{n!} (x - a)^n =
\sum_{k = 0}^{n} \frac{f^{(k)} (a)}{k!} (x - a)^k
$$.

- 我们把
  $$ f^{(k)} (a) / k! $$
  称为 `f` 关于 `a` 的第 `k` 个`泰勒系数`.
  - 在很多应用中, 我们希望得到原点处的泰勒级数, 所以 `a = 0`
    (在一些教材中, 这被称作麦克劳林级数).
- 泰勒级数给出了函数及其导数在一点处的性质,
  由此可以估算出该函数在其他点处的值.

---

- __期望值, 矩__: 设 `X` 是定义在
  $$ \mathbb{R} $$
  上的随机变量, 它的概率密度函数是
  $$ f_{X} $$.
  函数 `g(X)` 的`期望值`是:

$$
\mathbb{E} \left [ g(X) \right ] =
\begin{cases}
  \int_{- \infty}^{\infty} g(x) \cdot f_{X} (x) dx &
  \mbox{若 } X \mbox{ 是连续的} \\
  \sum_{n} g(x_n) \cdot f_{X} (x_n) &
  \mbox{若 } X \mbox{ 是离散的}
\end{cases}
$$

- 最重要的情形是
  $$ g(x) = x^r $$.
  我们把
  $$ \mathbb{E} \left [ X^r \right ] $$
  称为 `X` 的 `r` 阶`矩`, 把
  $$ \mathbb{E} \left [ ( X - \mathbb{E} \left [ X \right ] )^r \right ] $$
  称为 `X` 的 `r` 阶`中心矩`.

---

- __均值和方差__: 设 `X` 是一个连续型或离散型的随机变量,
  它的概率密度函数是
  $$ f_X $$.
  - (1) `X` 的均值 (即平均值或期望值) 是一阶矩.
    我们把它表示为
    $$ \mathbb{E} \left [ X \right ] $$
    或
    $$ μX $$
    (当随机变量很明确时, 通常不给出下标 `X`, 而只写 `μ`). 具体地说,
  - $$
      μ =
      \begin{cases}
        \int_{- \infty}^{\infty} x \cdot f_{X} (x) dx &
        \mbox{若 } X \mbox{ 是连续的} \\
        \sum_{n} x_n \cdot f_{X} (x_n) &
        \mbox{若 } X \mbox{ 是离散的}
      \end{cases}
    $$
  - (2) `X` 的方差, 记作
    $$ \sigma_{X}^2 $$
    或
    $$ Var(X) $$,
    是二阶中心距, 也可以说是
    $$ g(X) = (X - μ_{X})^2 $$
    的期望值. 同样, 当随机变量很明确时, 通常不给出下标 `X`, 而只写
    $$ \sigma^2 $$.
    把它完整地写出来, 就是
  - $$
      \sigma_{X}^2 =
      \begin{cases}
        \int_{- \infty}^{\infty} (x - μ_{X})^{2} f_{X} (x) dx &
        \mbox{若 } X \mbox{ 是连续的} \\
        \sum_{n} (x_{n} - μ_{X})^{2} f_{X} (x_n) &
        \mbox{若 } X \mbox{ 是离散的}
      \end{cases}
    $$
  - 因为
    $$ μ_{X} = \mathbb{E} \left [ X \right ] $$,
    所以在一系列代数运算后, 我们有
  - $$
      \sigma^2 =
      \mathbb{E} \left [ (X - \mathbb{E} \left [ X \right ] )^2 \right ] =
      \mathbb{E} \left [ X^2 \right ] - \mathbb{E} \left [ X \right ] ^2
    $$.
  - 这个式子把方差和 `X` 的前二阶矩联系起来, 在很多计算中都非常有用.
    标准差是方差的平方根, 即
    $$ \sigma_{X} = \sqrt{\sigma_{X}^2} $$.
  - (3) 技术说明: 为了保证均值存在, 我们希望
    $$ \int_{- \infty}^{\infty} \mid x \mid f_{X} (x) dx $$
    (在连续的情形下) 或
    $$ \sum_n \mid x_n \mid f_{X} (x_n) $$
    (在离散的情形下) 是有限的.

- __方差与标准差__: 与方差相比, 标准差的优势在于它和均值有相同的单位.
  - 因此, 标准差是衡量结果在均值附近波动幅度的自然尺度.

---

- __联合概率密度函数__: 设
  $$ X_1 $$,
  $$ X_2 $$,
  ...,
  $$ X_n $$
  都是连续型随机变量, 它们的概率密度函数分别是
  $$ f_{X_1} $$,
  $$ f_{X_2} $$,
  ...,
  $$ f_{X_n} $$.
- 假设每个
  $$ X_i $$
  都定义在
  $$ \mathbb{R} $$
  (实数集) 的一个子集上.
  - 那么,
    $$ (X_1, ..., X_n) $$
    的联合概率密度函数就是一个非负的可积函数
    $$ f_{X_1, ..., X_n} $$,
    满足:
  - 对于每一个恰当的集合
    $$ S \subset \mathbb{R} $$,
    均有

$$
Prob((X_1, ..., X_n) \in S) =
\int
...
\int_{S}
f_{X_1, ..., X_n} (x_1, ..., x_n) d x_{1} ... d x_{n}
$$,

- 并且

$$
f_{X_i} (x_i) =
\int_{x_1 = - \infty}^{\infty}
...
\int_{x_{i - 1} = - \infty}^{\infty}
\int_{x_{i + 1} = - \infty}^{\infty}
...
\int_{x_n = - \infty}^{\infty}
f_{X_1, ..., X_{i - 1}, X_{i + 1}, ..., X_n}
(x_1, ..., x_{i - 1}, x_{i + 1}, ..., x_n)
\prod_{j = 1, j \ne i}^{n} d x_j
$$.

- 我们把
  $$ f_{X_i} $$
  称为
  $$ X_i $$
  的`边缘概率密度函数`, 可以通过对其他 `n - 1` 个变量求积分来得到.
  - 这 `n` 个随机变量
    $$ X_1 $$,
    ...,
    $$ X_n $$
    相互独立, 当且仅当
  - $$ f_{X_1, ..., X_n} (x_1, ..., x_n) = f_{X_1}(x_1) ... f_{X_n}(x_n) $$.
  - 对于离散型随机变量, 只需要把积分替换成求和即可.

---

- __期望的线性性质__ 设
  $$ X_1 $$,
  ...,
  $$ X_n $$
  是随机变量, 并设
  $$ g_1 $$,
  ...,
  $$ g_n $$
  是满足下列条件的函数:
  $$ \mathbb{E} \left [ \mid g_i (X_i) \mid \right ] $$
  存在且有限. 令
  $$ a_1 $$,
  ...,
  $$ a_n $$
  表示任意实数. 那么
  - $$
      \mathbb{E} \left [ a_1 g_1 (X_1) + ... + a_n g_n (X_n) \right ] =
      a_1 \mathbb{E} \left [ g_1 (X_1) \right ] + ... +
      a_n \mathbb{E} \left [ g_n (X_n) \right ]
    $$.
  - 注意, 随机变量不一定是相互独立的.
  - 另外, 如果
    $$ g_i (X_i) = c $$
    (这里的 `c` 是固定常数), 那么
    $$ \mathbb{E} \left [ g_i (X_i) \right ] = c $$.
- 设 `X` 是一个随机变量, 它的均值为
  $$ μ_{X} $$,
  方差为
  $$ σ_{X}^2 $$.
  如果 `a` 和 `b` 是任意两个固定常数, 那么随机变量
  $$ Y = aX + b $$
  有下列结果
  - $$ μ_{Y} = a μ_{X} + b $$
  - 和
  - $$ σ_{Y}^2 = a^2 σ_{Y}^2 $$.
- 设 `X` 是一个随机变量, 那么
  - $$
      Var (X) = \mathbb{E} \left [ X^2 \right ] -
      \mathbb{E} \left [ X \right ] ^2
    $$.

---

- 如果 `X` 和 `Y` 是相互独立的随机变量, 那么

$$
\mathbb{E} \left [ X Y \right ] =
\mathbb{E} \left [ X \right ]
\mathbb{E} \left [ Y \right ]
$$.

- 一种特别重要的情况是

$$
\mathbb{E} \left [ (X - μ_{X}) (Y - μ_{Y}) \right ] =
\mathbb{E} \left [ X - μ_{X} \right ]
\mathbb{E} \left [ Y - μ_{Y} \right ] = 0
$$.

- __随机变量之和的均值与方差__ 设
  $$ X_1 $$,
  ...,
  $$ X_n $$
  是 `n` 个随机变量, 它们的均值是
  $$ μ_{X_1} $$,
  ...,
  $$ μ_{X_n} $$,
  方差是
  $$ σ_{X_1}^2 $$,
  ...,
  $$ σ_{X_n}^2 $$.
  如果
  $$ X = X_1 + ... + X_n $$,
  那么
  - $$ μ_{X} = μ_{X_1} + ... + μ{X_n} $$.
- 如果随机变量是相互独立的, 那么还能得到
  $$ σ_{X}^2 = σ_{X_1}^2 + ... + σ_{X_n}^2 $$
  或
  $$ Var(X) = Var(X_1) + ... + Var(X_n) $$.
- 如果这些随机变量是独立同分布的 (因此, 每个随机变量的均值都是
  $$ μ $$,
  方差都是
  $$ σ^2 $$
  ), 那么
  $$ μ_{X} = n μ $$
  且
  $$ σ_{X}^2 = n σ^2 $$.

---

- __协方差__: 设 `X` 和 `Y` 是两个随机变量.
  `X` 和 `Y` 的协方差记作
  $$ σ_{XY} $$
  或者
  $$ Cov(X, Y) $$,
  它的表达式为

$$
σ_{XY} = \mathbb{E} \left [ (X - μ_{X}) (Y - μ_{Y}) \right ]
$$.

- 注意,
  $$ Cov(X, X) $$
  等于 `X` 的方差. 另外, 如果
  $$ X_1 $$,
  ...,
  $$ X_n $$
  都是随机变量, 并且
  $$ X = X_1 + ... + X_n $$,
  那么

$$
Var(X) =
\sum_{i=1}^n Var(X_i) +
2 \sum_{1 ≤ i < j ≤ n} Cov(X_i, X_j)
$$.

```
由于相互独立的随机变量的协方差是 0,
因此, 协方差衡量的是一个变量的变化会如何影响另一个变量的变化.

但是, 值得注意的是, 协方差为 0 并不表示两个随机变量是相互独立的.

协方差测量的是两个变量之间的线性相关程度.
协方差大于 0 表明了两个变量是正相关的,
协方差小于 0 则意味着它们是负相关的.
```

- 与协方差密切相关的一个术语是`相关系数`. 相关系数
  $$ \rho $$
  被定义为
  $$ \rho = \frac{Cov(X, Y)}{σ_{X} σ_{Y}} $$.
- 相关系数是对协方差的标准化, 我们始终有
  $$ \rho \in \left [ -1, 1 \right ] $$.
  - 它描述了两个变量之间的线性相关强度.
  - 相关系数越接近 `-1` 或 `1`, 线性相关性就越强.

---

- __定义__ 设 `X` 和 `Y` 是定义在
  $$ \mathbb{R} $$
  上的两个相互独立的连续型随机变量, 它们的概率密度函数分别是
  $$ f_{X} $$
  和
  $$ f_{Y} $$.
  `X` 和 `Y` 的卷积记作
  $$ f_{X} * f_{Y} $$,
  其表达式为

$$
(f_{X} * f_{Y}) (z) =
\int_{- \infty}^{\infty} f_{X}(t) f_{Y}(z - t) dt
$$.

- 如果 `X` 和 `Y` 都是离散型随机变量, 那么

$$
(f_{X} * f_{Y}) (z) = \sum_{n} f_{X} (x_n) f_{Y} (z - x_n)
$$.

- 当然, 要注意, 除非
  $$ z - x_n $$
  等于 `Y` 有正概率时的取值 (即
  $$ z - x_n $$
  取某个具体的
  $$ y_m $$
  ), 否则
  $$ f_{Y} (z - x_{n}) = 0 $$.

- __定理__ 设 `X` 和 `Y` 是定义在
  $$ \mathbb{R} $$
  上的两个相互独立的连续型或离散型随机变量,
  它们的概率密度函数分别是
  $$ f_{X} $$
  和
  $$ f_{Y} $$.
  如果
  $$ Z = X + Y $$,
  那么
  - $$ f_{Z} (z) = (f_{X} * f_{Y}) (z) $$.
  - 另外, 卷积是可交换的:
  - $$ f_{X} * f_{Y} = f_{Y} * f_{X} $$.

### 工具: 卷积和变量替换

- 卷积运算满足:
  - 交换律
  - 结合律
- 卷积: 用两个函数作为输入, 返回一个函数作为输出.
- 对于独立的随机变量, 它们的和的概率密度函数就是它们概率密度函数的卷积.

### 卡方分布

```
相互独立且服从卡方分布的随机变量之和也服从卡方分布. 因此, 卡方分布是一个稳定的分布,
这意味着独立的随机变量之和的形状与每个随机变量的形状相同. 这是个很不寻常的性质,
并且通常难以成立. 例如, 服从均匀分布的随机变量之和不服从均匀分布,
服从指数分布的随机变量之和也不服从指数分布. 另外, 还有其他的稳定分布
(连续型分布包括正态分布和柯西分布, 离散型分布包括泊松分布).
它们在分析中非常有用, 因为函数的形式没有改变.
```

### 不等式和大数定律

- [马尔可夫不等式](https://en.wikipedia.org/wiki/Markov%27s_inequality)
- [切比雪夫不等式](https://en.wikipedia.org/wiki/Chebyshev%27s_inequality)
- [布尔不等式](https://en.wikipedia.org/wiki/Boole%27s_inequality)
- [大数定律](https://en.wikipedia.org/wiki/Law_of_large_numbers)

### 斯特林公式

- [Γ 函数](https://en.wikipedia.org/wiki/Gamma_function)

### 生成函数与卷积

- [斐波那契数](https://en.wikipedia.org/wiki/Fibonacci_sequence)

```
对于相互独立的离散型随机变量, 它们和的概率密度函数就是各随机变量概率的卷积!
```

### 傅里叶分析与中心极限定理

```
解决这个难题的一个方法是研究概率密度函数的傅里叶变换, 它在概率论中被称为特征函数.
稍后我们将看到, 与矩母函数不同, 特征函数总是存在的,
而且是对矩母函数的一个非常接近的类比.
它有更好的性质 (比如存在性!), 而且更易于分析.
这样我们就可以采用之前的证明.
整个思路与之前相似, 但代数运算会略有不同.
```

```
在数学上, 我们可以做的事情是无穷无尽的.
我们几乎可以定义任何东西, 问题是哪些定义是有用的, 哪些定义会带来好的观点.
我们看到了卷积的傅里叶变换就是傅里叶变换的乘积.
当研究随机变量的和时, 我们很难不尝试使用卷积,
因为这是寻找概率密度函数最自然的方法.
由于傅里叶变换与卷积可以很好地相互作用, 我们利用傅里叶变换去证明也就不奇怪了.
```

------------------

- [应用随机过程 (第 11 版)](https://book.douban.com/subject/26761202/)

```
原书已经出了第 12 版, 网上评价这一版翻译较差!
所以买过来随便翻一翻, 不打算认真看.
```

> 没有概率论的严格化 (测度论).

- 期待
  [应用随机过程: 概率模型导论 (第 12 版)](https://www.ituring.com.cn/book/2795)
  - 图灵数学经典

### 条件概率与条件期望

```
马尔可夫不等式和切比雪夫不等式的重要性在于,
在只有概率分布的均值或者均值和方差已知时,
它们使我们能推得所求概率的上界.
当然, 如果真实分布已知,
那么所求的概率可以精确地计算,
我们就不需要求助于上界.
```

```
与强大数定律并驾齐驱地占有概率论中首要荣誉的结果是中心极限定理.
除了它理论上的价值和重要性以外,
它还对于计算独立随机变量的和的近似概率提供了一个比较简单的方法.
它也解释了为什么有那么多自然"总体"的经验频率显示为钟形 (即正态) 曲线这个显著的事实.
```

### 马尔可夫链

- [查普曼-科尔莫戈罗夫等式](https://en.wikipedia.org/wiki/Chapman-Kolmogorov_equation)

### 连续时间的马尔可夫链

- 事实上, 上面的事实给了我们定义连续时间的马尔可夫链的另一个途径.
  即它是一个具有以下性质的随机过程: 每次进入状态 `i` 时有
  - (i) 在转移到不同的状态前, 它处在这个状态的时间是均值为
    $$ 1 / v_i $$
    的指数随机变量;
  - (ii) 当过程离开状态 `i` 时, 以某个概率
    $$ P_{ij} $$
    进入下一个状态 `j`, 当然
    $$ P_{ij} $$
    必须满足
  - $$ P_{ii} = 0 $$,
    对于一切 `i`;
    $$ \sum_{j} P_{ij} = 1 $$,
    对于一切 `i`
- 换句话说, 连续时间的马尔可夫链是一个随机过程,
  它按一个 (离散的) 马尔可夫链从状态运动到状态,
  但是在进入下一个状态前, 停留在每个状态的时间是按指数分布的.
  - 此外, 过程停留在状态 `i` 的时间和下一个访问的状态必须是独立的随机变量.
  - 因为如果下一个访问的状态依赖
    $$ T_i $$,
    那么过程已经在状态 `i` 停留多久的信息将影响下一个状态的预报,
    而这与马尔可夫性假定矛盾.
