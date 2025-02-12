---
title: 泛函分析导论及应用 - (上)
description: 缺月挂疏桐, 漏断人初静. 谁见幽人独往来, 缥缈孤鸿影.
date: 2022-02-11
---

- [泛函分析导论及应用](https://book.douban.com/subject/35941956/)
  - 本书可称优秀教材, 行文工整;
    但未见奇思妙语, 亦即: 难显宗师风范~
  - 然后, 建议先系统的学习一些量子力学,
    这样对于这一套理论的存在意义就不用困惑了~

## 度量空间

```
在这样的抽象研究方法中, 人们通常从满足某些公理的一个集合出发,
并且故意不指定集合元素的特征.
由这些公理导出的一些逻辑结果被作为定理反复使用.
这就意味着我们从公理体系出发得到了一个数学结构,
这个数学结构的理论又以抽象的方法得到讨论.
而后, 可把得到的通用定理应用到满足公理体系的各种特殊集合上去.

例如, 在代数中曾用这种方法研究域, 环和群; 在泛函分析中,
我们将用这种方法来研究抽象空间. 这些空间是基本的, 也是重要的,
我们将详细地研究其中的某些空间 (如巴拿赫空间, 希尔伯特空间).
以后我们还会看到, "空间"这个概念广泛得惊人.
抽象空间不过是满足有关公理体系的 (非特指的) 元素集合.
如果选用不同的公理体系, 便能得到不同类型的抽象空间.

目前所给出的度量空间的概念, 就是经过 60 多年的发展过程才确定的,
它在泛函分析及其应用中是基本的, 也是极为有用的.
```

- 定义 (__度量空间__, 度量) 所谓`度量空间`, 就是指对偶
  $$ (X, d) $$,
  其中
  $$ X $$
  是一个集合,
  $$ d $$
  是
  $$ X $$
  上的一个度量 (或
  $$ X $$
  上的距离函数), 即
  $$ d $$
  是定义在
  $$ X \times X $$
  上且对所有
  $$ x, y, z \in X $$
  满足以下四条公理的函数.
  - $$ (M_1) $$
    $$ d $$
    是实值, 有限和非负的.
  - $$ (M_2) $$
    当且仅当
    $$ x = y $$
    时,
    $$ d(x, y) = 0 $$.
  - $$ (M_3) $$
    $$ d(x, y) = d(y, x) $$
    (对称性).
  - $$ (M_4) $$
    $$ d(x, y) ≤ d(x, z) + d(z, y) $$
    (三角不等式).
- 为叙述方便, 我们给出下面几个有关的术语.
  - $$ X $$
    叫作
    $$ (X, d) $$
    的基集,
    $$ X $$
    的元素叫作空间
    $$ (X, d) $$
    的点.
  - 给定
    $$ x, y \in X $$,
    我们把非负实数
    $$ d(x, y) $$
    叫作
    $$ x $$
    和
    $$ y $$
    之间的距离.
  - $$ M_1 $$
    到
    $$ M_4 $$
    叫作`度量公理`.
- 在不引起混淆的情况下, 我们常将度量空间
  $$ (X, d) $$
  简写成
  $$ X $$.
- 如果取子集
  $$ Y \subseteq X $$
  且把
  $$ d $$
  限制在
  $$ Y \times Y $$
  上, 则可得
  $$ (X, d) $$
  的一个`子空间`
  $$ (Y, \tilde{d}) $$;
  因而
  $$ Y $$
  上的度量就是限制
  - $$ \tilde{d} = d \mid_{Y \times Y} $$.
  - $$ \tilde{d} $$
    叫作
    $$ d $$
    在
    $$ Y $$
    上导出的度量.

- 符号
  $$ \times $$
  表示集合的`笛卡儿积`:
  $$ A \times B $$
  是所有`序偶`
  $$ (a, b) $$
  的集合, 其中
  $$ a \in A $$,
  $$ b \in B $$.
  - 因此,
    $$ X \times X $$
    是
    $$ X $$
    的元素构成的所有序偶的集合.

```
读者将体会到, 这里考虑问题的方式与微积分大不相同.
在微积分中, 我们通常研究一个函数或同时研究几个函数.
而这里, 一个函数变成了更大的空间中的点.
```

- [赫尔德不等式](https://en.wikipedia.org/wiki/Hölder%27s_inequality)
  - [共轭指数](https://en.wikipedia.org/wiki/Conjugate_index)
- [柯西-施瓦茨不等式](https://en.wikipedia.org/wiki/Cauchy-Schwarz_inequality)
- [闵可夫斯基不等式](https://en.wikipedia.org/wiki/Minkowski_inequality)

### 开集, 闭集和邻域

- 若
  $$ M \subseteq X $$
  是
  $$ x_0 $$
  的一个邻域, 则称
  $$ x_0 $$
  是集合
  $$ M $$
  的一个`内点`.
  $$ M $$
  的所有内点构成的集合叫作
  $$ M $$
  的`内部`, 可以记为
  $$ M^0 $$
  或
  $$ Int(M) $$,
  没有公认的记法.
  - $$ Int(M) $$
    是开集, 并且是包含在
    $$ M $$
    中的最大开集.
- 若把
  $$ X $$
  的所有开子集构成的集族记为
  $$ \mathcal{T} $$,
  则不难证明
  $$ \mathcal{T} $$
  有如下性质:
  - ($$ T_1 $$)
    $$ \varnothing \in \mathcal{T} $$,
    $$ X \in \mathcal{T} $$;
  - ($$ T_2 $$)
    $$ \mathcal{T} $$
    中任意个成员之并仍属于
    $$ \mathcal{T} $$;
  - ($$ T_3 $$)
    $$ \mathcal{T} $$
    中有限个成员之交仍属于
    $$ \mathcal{T} $$.

- 据此, 我们定义: 给定集合
  $$ X $$
  和
  $$ X $$
  的满足公理
  $$ T_1 \sim T_3 $$
  的子集构成的集族
  $$ \mathcal{T} $$,
  则
  $$ (X, \mathcal{T}) $$
  叫作`拓扑空间`.
  - 集合
    $$ \mathcal{T} $$
    叫作
    $$ X $$
    的一个`拓扑`. 从这个定义可知: __度量空间是拓扑空间__.

- 重要而有趣的是, 连续映射能够用开集的术语表征如下.
  定理: (__连续映射__) 度量空间
  $$ X $$
  到度量空间
  $$ Y $$
  中的映射
  $$ T $$,
  当且仅当
  $$ Y $$
  的任意开子集的逆像是
  $$ X $$
  中的开子集时, 才是连续的.

- 现在我们再引入两个互相关联的概念. 令
  $$ M $$
  是度量空间
  $$ X $$
  的一个子集. 若点
  $$ x_0 \in X $$
  的每个邻域至少含有一个异于
  $$ x_0 $$
  的点
  $$ y \in M $$,
  则
  $$ x_0 $$
  (它可以是, 也可以不是
  $$ M $$
  的点) 叫作
  $$ M $$
  的`聚点` (或极限点).
  - $$ M $$
    的所有点和所有聚点构成的集合, 叫作
    $$ M $$
    的`闭包`, 记为
    $$ \overline{M} $$.
  - 它是包含
    $$ M $$
    的最小闭集.
  - 在
    $$ R^3 $$
    中, 开球
    $$ B(x_0; r) $$
    的闭包
    $$ \overline{B(x_0; r)} $$
    就是闭球
    $$ \widetilde{B} (x_0; r) $$,
    而在一般度量空间中却未必如此.
- 定义 (__稠密集__, __可分空间__) 度量空间
  $$ X $$
  的子集
  $$ M $$
  若满足
  $$ \overline{M} = X $$,
  则称
  $$ M $$
  在
  $$ X $$
  中`稠密`.
  - 若
    $$ X $$
    有一个可数的稠密子集, 则称
    $$ X $$
    是`可分`的.
  - 因此, 若
    $$ M $$
    在
    $$ X $$
    中稠密, 则
    $$ X $$
    中的每一个球, 不管多小, 总含有
    $$ M $$
    的点.
  - 换句话说, 在这种情况下不存在点
    $$ x \in X $$
    满足有一个不含
    $$ M $$
    的点的邻域.
  - 我们将会看到, 可分度量空间比不可分度量空间简单.

### 收敛性, 柯西序列和完备性

- 若序列
  $$ (x_n) $$
  满足柯西准则的条件, 我们便把它叫作`柯西序列`.
  柯西准则简单地说就是, 实数序列或复数序列在
  $$ R $$
  上或
  $$ C $$
  中收敛的充分必要条件是它是柯西序列.
  - __遗憾的是__, 在一般的度量空间中, 情况变得复杂起来,
    可能有不收敛的柯西序列.
  - 这种空间缺少一个极为重要的性质, 即所谓的完备性.
- 定义( __柯西序列__, __完备性__) 度量空间
  $$ X = (X, d) $$
  中的序列
  $$ (x_n) $$,
  如果对于给定的任意正数
  $$ ε $$,
  都存在
  $$ N = N(ε) $$,
  使得
  - 对于所有
    $$ m, n > N $$
    有
    $$ d(x_m, x_n) < ε $$,
  - 则称
    $$ (x_n) $$
    是`柯西序列` (或基本序列).
  - 如果空间
    $$ X $$
    中的每个柯西序列都是收敛序列 (即有属于
    $$ X $$
    的极限), 则称
    $$ X $$
    是`完备度量空间`.

```
用完备性来表述的话, 柯西收敛准则意义如下.
```

- 定理 (__实直线, 复平面__) __实直线和复平面都是完备度量空间__.

```
更一般地, 从定义可以直接看出, 完备度量空间是这样的空间,
在其中柯西条件是序列收敛的充分必要条件.
```

- 定理 (__闭包__, __闭集__) 令
  $$ M $$
  是度量空间
  $$ (X, d) $$
  的非空子集,
  $$ \overline{M} $$
  是闭包, 则
  - (a)
    $$ x \in \overline{M} $$,
    当且仅当在
    $$ M $$
    中存在收敛到
    $$ x $$
    的序列
    $$ (x_n) $$.
  - (b)
    $$ M $$
    是闭集, 当且仅当
    $$ M $$
    中的序列
    $$ (x_n) $$
    收敛到
    $$ x $$
    蕴涵
    $$ x \in M $$.

- 定理 (__完备子空间__) 完备度量空间
  $$ X $$
  的子空间
  $$ M $$
  是完备的, 当且仅当集合
  $$ M $$
  在
  $$ X $$
  中是闭的.

- 定理 (__连续映射__) 度量空间
  $$ (X, d) $$
  到度量空间
  $$ (Y, \widetilde{d}) $$
  中的映射
  $$ T: X \rightarrow Y $$
  在点
  $$ x_0 \in X $$
  连续, 当且仅当
  - $$ x_n \rightarrow x_0 $$
    蕴涵
    $$ T_{x_n} \rightarrow T_{x_0} $$.

### 完备性的例子

- $$ R^n $$
  和
  $$ C^n $$
  的完备性: 欧几里得空间
  $$ R^n $$
  和酉空间
  $$ C^n $$
  是完备的.

- $$ l^∞ $$
  的完备性: 空间
  $$ l^∞ $$
  是完备的.

- $$ c $$
  的完备性: 空间
  $$ c $$
  是所有收敛的复数序列
  $$ x = (ξ_j) $$
  构成的, 其度量是由空间
  $$ l^∞ $$
  的度量导出的.
  - 空间
    $$ c $$
    是完备的.

- $$ l^p $$
  的完备性: 空间
  $$ l^p $$
  是完备的, 其中
  $$ p $$
  是固定的实数且
  $$ 1 ≤ p < +∞ $$.

- $$ C[a, b] $$
  的完备性: 函数空间
  $$ C[a, b] $$
  是完备的, 其中
  $$ [a, b] $$
  是
  $$ R $$
  上给定的任意闭区间.

- 定理 (__一致收敛性__) 在空间
  $$ C[a, b] $$
  中收敛性
  $$ x_m \to x $$
  是一致收敛的. 也就是说,
  $$ (x_m) $$
  在
  $$ [a, b] $$
  上一致收敛到
  $$ x $$.
  - 因此,
    $$ C[a, b] $$
    上的度量描述了
    $$ [a, b] $$
    上的一致收敛性. 为此, 有时把它叫作`一致度量`.

> 下面是不完备的例子

- __多项式__ 令
  $$ X $$
  是所有多项式的集合, 而每个多项式看作定义在某个有限闭区间
  $$ J = [a, b] $$
  上的
  $$ t $$
  的函数. 在
  $$ X $$
  上定义度量
  $$ d $$
  如下:
  - $$ d(x, y) = \max_{t \in J} \mid x(t) - y(t) \mid $$.
  - 这个度量空间
    $$ (X, d) $$
    是不完备的. 事实上, 能构造一个多项式序列, 它在
    $$ J $$
    上一致收敛到不是多项式的连续函数. 这就给出了在
    $$ X $$
    中没有极限的柯西序列.

- __连续函数__ 令
  $$ X $$
  是
  $$ J = [0, 1] $$
  上所有连续实值函数的集合, 且定义
  - $$ d(x, y) = \int_0^1 \mid x(t) - y(t) \mid dt $$.
  - 这个度量空间
    $$ (X, d) $$
    是不完备的.

### 度量空间的完备化

- 定义 (__等距映射__, __等距空间__) 令
  $$ X = (X, d) $$
  和
  $$ \widetilde{X} = (\widetilde{X}, \widetilde{d}) $$
  是两个度量空间, 则
  - (a) 如果映射
    $$ T: X \to \widetilde{X} $$
    保持距离不变, 也就是说对于所有
    $$ x, y \in X $$
    有
    $$ \widetilde{d}(Tx, Ty) = d(x, y) $$,
    则称
    $$ T $$
    是`等距映射`或`等距`, 其中
    $$ Tx $$
    和
    $$ Ty $$
    分别是
    $$ x $$
    和
    $$ y $$
    的像.
  - (b) 若存在一个
    $$ X $$
    到
    $$ \widetilde{X} $$
    上的等距一一映射, 则称空间
    $$ X $$
    和
    $$ \widetilde{X} $$
    是`等距`的. 空间
    $$ X $$
    和
    $$ \widetilde{X} $$
    称为`等距空间`.

```
因此, 在等距空间之间, 至多是它们的元素的特征有所不同,
但从度量的角度来看, 是没有什么区别的.
而在抽象的研究中, 点的特征不是本质的.
所以可把两个等距空间视为同一个空间, 或同一个抽象空间的两个副本.
```

- 定理 (__完备化__) 对于度量空间
  $$ X = (X, d) $$,
  存在完备度量空间
  $$ \hat{X} = (\hat{X}, \hat{d}) $$,
  使得子空间
  $$ W \subseteq \hat{X} $$
  与
  $$ X $$
  等距且在
  $$ \hat{X} $$
  中稠密.
  - 如果对等距空间不加区分, 则空间
    $$ \hat{X} $$
    是唯一的, 也就是说, 若完备空间
    $$ \hat{X} $$
    也有稠密子空间
    $$ \widetilde{W} $$
    和
    $$ X $$
    等距, 则
    $$ \widetilde{X} $$
    与
    $$ \hat{X} $$
    是等距的.

## 赋范空间和巴拿赫空间

- 定义 (__赋范空间和巴拿赫空间__) 所谓`赋范空间`
  $$ X $$,
  是指在其上定义了范数的向量空间. `巴拿赫空间`就是完备赋范空间
  (这里的完备性是按范数定义的度量来衡量的.)
  - 所谓 (实或复) 向量空间
    $$ X $$
    上的`范数`, 是指定义在
    $$ X $$
    上的实值函数, 它在
    $$ x \in X $$
    的值记为
    $$ |\ x \| $$
    (读作
    $$ x $$
    的范数), 并且具有如下性质.
  - ($$ N_1 $$)
    $$ \| x \| ≥ 0 $$.
  - ($$ N_2 $$)
    $$ \| x \| = 0 \Longleftrightarrow x = 0 $$.
  - ($$ N_3 $$)
    $$ \| α x \| = \mid α \mid \| x \| $$.
  - ($$ N_4 $$)
    $$ \| x + y \| ≤ \| x \| + \| y \| $$
    (三角不等式).
  - $$ x $$
    和
    $$ y $$
    是
    $$ X $$
    中的任意向量,
    $$ α $$
    是任意标量.
- 向量空间
  $$ X $$
  上的范数在
  $$ X $$
  上定义的度量
  $$ d $$
  为
  - $$ d(x, y) = \| x - y \| $$,
    其中
    $$ x, y \in X $$,
  - 叫作`由范数导出的度量`. 相关的赋范空间记为
    $$ (X, \| ⋅ \|) $$,
    或简记为
    $$ X $$.

- 为后面的需要, 注意可从
  $$ N_4 $$
  推出
  $$ \mid \| y \| - \| x \| \mid ≤ \| y - x \| $$.
  这意味着范数有如下重要性质.
  - 范数是连续的, 即
    $$ x \longmapsto \| x \| $$
    是从
    $$ (X, \| · \|) $$
    到
    $$ R $$
    的连续映射.

- 引理 (__平移不变性__) 在赋范空间
  $$ X $$
  上, 由范数导出的度量
  $$ d $$,
  对于所有
  $$ x, y, a \in X $$
  及每一个标量
  $$ α $$
  都满足
  - $$ d(x + a, y + a) = d(x, y) $$,
  - $$ d(αx, αy) = \mid α \mid d(x, y) $$.

- 定理 (__巴拿赫空间的子空间__) 巴拿赫空间
  $$ X $$
  的赋范子空间
  $$ Y $$
  是完备的, 当且仅当
  $$ Y $$
  在
  $$ X $$
  中是`闭的`.

- (i) 赋范空间
  $$ X $$
  中的序列
  $$ (x_n) $$
  是收敛的, 是指存在
  $$ x \in X $$
  使得
  - $$ \lim_{n \to \infty} \| x_n - x \| = 0 $$,
  - 记为
    $$ x_n \to x $$,
    把
    $$ x $$
    叫作
    $$ (x_n) $$
    的极限.
- (ii) 赋范空间
  $$ X $$
  中的序列
  $$ (x_n) $$
  是`柯西序列`, 是指对于任意正数
  $$ ε $$,
  存在
  $$ N $$
  使得
  - 对于所有
    $$ m, n > N $$
    有
    $$ \| x_m - x_n \| < ε $$.

```
在赋范空间 X 中, 当且仅当 X 是完备的, 绝对收敛性才蕴涵收敛性.

级数收敛性的概念可以用来定义空间的基.
```

- 若赋范空间
  $$ X $$
  包含具有以下性质的序列
  $$ (e_n) $$:
  对于每个
  $$ x \in X $$
  都存在唯一的标量序列
  $$ (a_n) $$
  使得
  - 当
    $$ n \to ∞ $$
    时有
    $$ \| x - (α_1 e_1 + ... + α_n e_n) \| \to 0 $$,
  - 则称
    $$ (e_n) $$
    为
    $$ X $$
    的一个`绍德尔基` (或基).
  - 和为
    $$ x $$
    的级数
    $$ \sum_{k = 1}^{\infty} α_k e_k $$
    叫作
    $$ x $$
    关于基
    $$ (e_n) $$
    的表达式, 记为
    $$ x = \sum_{k = 1}^{\infty} α_k e_k $$.

```
若赋范空间 X 有一个绍德尔基, 则 X 是可分的.
反过来, 每一个可分巴拿赫空间都有绍德尔基吗?
这是巴拿赫本人提出的著名问题.
几乎所有已知的可分巴拿赫空间, 都证明了有绍德尔基.
然而, 这个问题的答案却令人惊异一是否定的.
这是由恩弗罗 (1973) 给出的,
他构造了一个没有绍德尔基的可分巴拿赫空间.
```

- 定理 (__完备化__) 若
  $$ X = (X, \| · \|) $$
  是赋范空间, 则存在巴拿赫空间
  $$ \hat{X} $$
  和
  $$ X $$
  到
  $$ \hat{X} $$
  的稠密子空间
  $$ W $$
  上的等距映射
  $$ A $$.
  - 若不区分等距空间, 则空间
    $$ \hat{X} $$
    是唯一的.

### 有限维赋范空间

- 引理 (__线性组合__) 设
  $$ \{ x_1, ..., x_n \} $$
  是 (任意维数的) 赋范空间
  $$ X $$
  中的线性无关组, 则对选定的任意一组标量
  $$ α_1 $$,
  ...,
  $$ α_n $$,
  存在正的常数
  $$ c $$
  使得
  - $$
      \| α_1 x_1 + ... + α_n x_n \| ≥
      c(\mid a_1 \mid + ... + \mid α_n \mid)
    $$.

- 定理 (__完备性__) 赋范空间
  $$ X $$
  的每一个有限维子空间
  $$ Y $$
  都是完备的. 特别是, 每个有限维赋范空间都是完备的.

- 定理 (__封闭性__) 赋范空间
  $$ X $$
  中的每一个有限维子空间
  $$ Y $$
  在
  $$ X $$
  中都是闭的.
  - 要注意的是, 无穷维子空间不一定是闭的.

- 定义 (__紧性__) 如果度量空间
  $$ X $$
  的每一个序列都有一个收敛的子序列, 则称
  $$ X $$
  是`紧的`.
  $$ X $$
  的子集
  $$ M $$,
  作为
  $$ X $$
  的子空间若是紧的, 也就是说,
  $$ M $$
  的每一个序列都有一个在
  $$ M $$
  中收敛的子序列, 则称
  $$ M $$
  是`紧集`.

- 引理 (__紧性__) 度量空间
  $$ X $$
  的紧子集
  $$ M $$
  是有界闭集.
  - 这个引理的逆一般是不成立的.

> 我开始能够自然的接纳`拓扑`的概念了~

### 线性算子

### 线性泛函

### 有限维空间中的线性算子和泛函

### 算子赋范空间和对偶空间

## 内积空间和希尔伯特空间

### 正交补与直和

### 规范正交集和规范正交序列

### 勒让德, 埃尔米特和拉盖尔多项式

### 希尔伯特空间中泛函的表示

### 希尔伯特伴随算子

### 自伴算子, 酉算子和正规算子

## 赋范空间和巴拿赫空间的基本定理

### 佐恩引理

### 哈恩-巴拿赫定理

### 应用到 C[a, b] 上的有界线性泛函

### 伴随算子

### 自反空间

### 范畴定理和一致有界性定理

### 强收敛和弱收敛

### 算子序列和泛函序列的收敛

### 在序列可和性方面的应用

### 数值积分和弱星收敛

### 开映射定理

### 闭线性算子和闭图定理

## 附录 A

### 集合

- $$ A^C = X - A $$,
  $$ A $$
  在
  $$ X $$
  中的余集 (其中
  $$ A \subseteq X $$)
  (当省略
  $$ X $$
  有可能产生混乱时, 记为
  $$ C_{X} A $$)
  - $$ (A^C)^C = A $$,
  - $$ X^C = \varnothing $$,
  - $$ \varnothing^C = X $$.

---

- `德·摩根定律`是
  ($$ A $$
  和
  $$ B $$
  是
  $$ X $$
  的任意子集)
  - $$ (A \bigcup B)^C = A^C \bigcap B^C $$,
  - $$ (A \bigcap B)^C = A^C \bigcup B^C $$.
  - 显然,
  - $$ A \subseteq B \Longleftrightarrow A^C \supseteq B^C $$,
  - $$
      A \bigcap B = \varnothing \Longleftrightarrow
      A \subseteq B^C \Longleftrightarrow
      B \subseteq A^C
    $$,
  - $$
      A \bigcup B = X \Longleftrightarrow
      A^C \subseteq B \Longleftrightarrow
      B^C \subseteq A
    $$.
- 给定的集合
  $$ S $$
  的所有子集的集合, 叫作
  $$ S $$
  的`幂集`, 记为
  $$ \mathcal{P}(S) $$.
- 两个给定的非空集合
  $$ X $$
  和
  $$ Y $$
  的`笛卡儿积` (或积)
  $$ X \times Y $$
  是所有`序偶`
  $$ (x, y) $$
  的集合, 其中
  $$ x \in X $$
  且
  $$ y \in Y $$.

```
若集合 M 是有限的 (有有限个元素), 或者 M 的每个元素唯一地对应一个正整数,
并且反过来每个正整数 1, 2, 3, ... 也唯一地对应 M 中的一个元素,
则称 M 是可数集合.
```
