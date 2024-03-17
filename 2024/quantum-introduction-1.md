---
title: 量子力学概论 格里菲斯 (上)
description: 待燃犀下看, 凭栏却怕, 风雷怒, 鱼龙惨. 峡束苍江对起, 过危楼, 欲飞还敛.
date: 2023-12-11
---

- [量子力学概论](https://book.douban.com/subject/36460137/)
  - `科恩`系列之后, 为何还要买这本入门书?
  - 其实数年前购买过
    [英文注释版](https://book.douban.com/subject/35257979/),
    但是, 低估了英文阅读的障碍~
  - 所以, 首先是心结, 是必须填补的遗憾 (强迫症).
  - 其次, 量子力学也不应该只看一套教材!
  - 同时, 这本书的特色也十分明显, 习题也是很好.
  - 不过, 最好选择后期修正的版本, 第一版印刷的错误不少!
  - __顺便一提__: 不推荐阅读`费曼物理学讲义 (第三卷)`.

```
本书的目的是教你如何学习量子力学.
除了在第 1 章中一些必备的基础知识外, 更深的准哲学问题将留在书末.
我们不相信一个人在对量子力学是干什么的有一个透彻的理解之前,
他可以明智地讨论量子力学的意义.
但是, 如果你急不可待, 在学习过第 1 章后可立即阅读 <跋>.
```

> 关于印刷错误: 这一方面的质量明显不如`量子力学 (科恩)`.

## 波函数

### 薛定谔方程

- [薛定谔方程](https://en.wikipedia.org/wiki/Schrödinger_equation)

```
从逻辑上讲, 薛定谔方程所起的作用等同于牛顿第二定律:
同在经典力学中由牛顿定律确定以后任意时刻的 x(t) 一样,
量子力学利用所给定的适当初始条件 (一般来说是 ψ(x, 0)),
通过求解薛定谔方程得到以后任意时刻的波函数 Ψ(x, t).
```

### 统计诠释

- $$
    \int_{a}^{b} \mid \psi (x, t) \mid ^2 dx =
    \begin{Bmatrix}
      在 \mbox{ } t \mbox{ } 时刻发现粒子位于 \\
      a \mbox{ } 和 \mbox{ } b \mbox{ } 之间的几率.
    \end{Bmatrix}
  $$

> 本书的翻译选`几率`而非`概率`, 差评~

```
当然, 如果你关闭一个狭缝, 或者设法去探测每个电子通过的是哪一个狭缝,
干涉图样将会消失; 这时通过 (狭缝) 的粒子波函数和前面的完全不同
(第一种情况属于薛定谔方程的边界条件发生了改变, 第二种情况对应于波函数测量引起坍缩).
但两个狭缝都打开, 电子飞行过程中不受到干扰, 每个电子和自己本身发生干涉.
它不是通过两个狭缝中的某一个, 而是同时通过两个狭缝.
```

> 和自己本身发生干涉

### 归一化

> `平凡解`翻译为`平庸解`, 不雅~

- 但是, 假定在
  $$ t = 0 $$
  时刻把波函数归一化了. 我们如何能知道当
  $$ Ψ $$
  随时间演化时它能保持归一化?
  - (你不能让 __A__ 变成时间的函数来保持波函数的归一化,
    那样的话它就不再是薛定谔方程的解了.)
  - 幸运的是, 薛定谔方程具有一个不同寻常的特性, 它能自动保持波函数的归一化.
  - 没有这个关键的性质薛定谔方程将会同统计诠释不相容, 整个理论将会崩溃.

> 演化公设

### 动量

- 简而言之, 期望值是对一个全同系统的系综测量的平均值,
  而不是对同一个系统重复测量的平均值.
  - [系综诠释](https://en.wikipedia.org/wiki/Ensemble_interpretation)

> 原文翻译为`相同系统`, 我改为了`全同系统`;
  系综诠释: 即`统计诠释`

- [分部积分法](https://en.wikipedia.org/wiki/Integration_by_parts)

- `"算符"`是对后面的函数执行某些操作的指令,
  它接收一个函数, 然后输出另一个函数.

> 啊哟: 接收一个函数, 输出一个函数.

- [埃伦费斯特定理](https://en.wikipedia.org/wiki/Ehrenfest_theorem)

### 不确定性原理

```
假设你握住一根长绳的一端, 通过有节奏地上下摆动而产生一列波.
如果有人问你: "精确来讲波在哪里?" 你可能会认为此人有点不合时宜:
精确来讲波不在任何地方 -- 它分布在一定的范围.
另一方面, 如果他问其波长是多少, 你可以给他一个大约合理的答案.

与此相反, 如果你突然抖动一下绳子, 可以得到一个沿绳子传播的相对很窄的凸峰.
对于这种情况, 第一个问题 (精确来讲波在那里) 就有意义了,
但是第二个问题 (波长是多少?) 就有点不合时宜 -- 它甚至没有一个明确的周期,
所以你如何能赋予它一个波长? 当然, 你也可以画出介于两者之间的情况,
波是可以很好地定域在一定范围内的, 波长也很明确. 但是这里不可避免地存在一个取舍:
波的位置越精确, 波长也就越不精确, 反之亦然.

傅里叶分析中的一个定理可以给出这种情况的一个严格证明, 不过目前我仅涉及定性讨论.
```

> 单从通俗性角度而言, 这一段描述比`科恩`和`费曼`的都要好.

```
应确切理解不确定原理的意义: 如同位置测量一样, 对动量测量也是同样的答案 --
这里 "弥散" 是指这样一个事实, 即对全同体系的测量而不会产生同样结果.
设想如果你可以构造一个态, 对其位置的重复测量的值都非常接近
(通过使 Ψ 成为一个局域的波包); 但你要付出的代价是:
对这个状态进行动量的测量的结果将是非常弥散的.
或者你也可以构造一个态, 对其动量的测量的结果是确定的
(使 Ψ 为一个很长的正弦波); 但这样的话, 位置的测量结果是非常弥散的.
```

- [波包](https://en.wikipedia.org/wiki/Wave_packet)

> 确实不如`科恩`讲述地详细, 弱化了公式的推导.
  或者说, 放在了习题里面.

## 定态薛定谔方程

- [分离变量法](https://en.wikipedia.org/wiki/Separation_of_variables)

### 定态

- [定态](https://en.wikipedia.org/wiki/Stationary_state)
  - 概率密度与时间无关;
  - 哈密顿量不变.

```
一旦解出了定态薛定谔方程的分离变量解,
就可以从中得到含时薛定谔方程的通解,
这在原则上是简单明了的.
```

- [哈密顿算符](https://en.wikipedia.org/wiki/Hamiltonian_(quantum_mechanics))

- 最后要注意一点, 由于常数
  $$ | c_n |^2 $$
  与时间无关, 得到一个特定能量值的几率也是如此; 更不用说
  $$ H $$
  的期望值了.
  - 这些都是`能量守恒`定律在量子力学中的表现.

### 无限深方势阱

- [无限深方势阱](https://en.wikipedia.org/wiki/Particle_in_a_box)

> 虽然翻译的比较急促, 但是有译者注还是蛮好的.

- 定态薛定谔方程的解是一个无限的解集 (每个正整数 `n` 对应一个解).
  它们看起来像位于一个长度为 `a` 的弦上的驻波. 波函数
  $$ ψ_1 $$
  具有最低的能量, 称为`基态`, 其他状态的能量正比于
  $$ n^2 $$,
  称为`激发态`. 总结一下, 函数
  $$ ψ_n (x) $$
  具有如下有趣和重要的性质:
  - 波函数
    $$ ψ_n (x) $$
    相对于无限深势阱的中心是奇偶交替的.
  - 随着能量的增加, 相继状态的`节点数` (与 `x` 轴交点) 逐次增 `1`.
  - 它们是相互`正交的`.
  - 它们是`完备的`, 也就是说对其他任意函数
    $$ f(x) $$,
    都可以用它们的线性组合来表示.

```
上述四个性质非常有用, 且它们不单单是一维无限深方势阱所特有.
只要势函数本身具有对称性, 第一个性质就成立;
无论势函数是什么形状, 第二个性质都是普适的.
波函数的正交归一性也是十分普遍的.

波函数的完备性对我们可能遇到的所有势场都是成立的,
但要去证明这一点确实棘手又费力;
恐怕大多数物理学家们只是简单地假定其是完备的, 并希望如此.
```

- [狄利克雷定理 (傅里叶级数)](https://en.wikipedia.org/wiki/Dirichlet-Jordan_test)

### 谐振子

### 自由粒子

### 函数势

### 有限方势阱

## 形式理论

### 希尔伯特空间

### 可观测量

### 厄密算符的本征函数

### 广义统计诠释

### 不确定性原理

### 矢量和算符

## 三维空间中的量子力学

### 薛定谔方程

### 氢原子

### 角动量

### 自旋

### 电磁相互作用

## 全同粒子

### 双粒子体系

### 原子

### 固体

## 对称性和守恒律

### 变换算符

### 守恒律

### 宇称

### 旋转对称性

### 简并

### 旋转对称选择定则

### 时间变换

## 附录 线性代数

> 其实放在附录不合适, 应该作为第一章. 同时本章内容略显简陋了~

- [柯西-施瓦茨不等式](https://en.wikipedia.org/wiki/Cauchy-Schwarz_inequality)

> 注: 本书原本用`上面加一个波浪号`表示转置矩阵, 一律改为
  $$ \mathbf{A}^T $$

- `厄米共轭`矩阵, 或称`伴随`矩阵, 用
  $$ \mathbf{T}^{\dagger} $$
  表示, 是`转置共轭`矩阵.

- 如果一个方矩阵等于它的`厄米共轭`, 则它就是`厄米`矩阵, 或`自伴`矩阵;
  如果`厄米共轭`引入一个负号, 则矩阵为`斜厄米`矩阵, 或`反厄米`.
  - __厄米矩阵__:
    $$ \mathbf{T}^{\dagger} = \mathbf{T} $$;
  - __斜厄米矩阵__:
    $$ \mathbf{T}^{\dagger} = - \mathbf{T} $$.

- 一般来说, 矩阵乘法不是可交换的 (即
  $$ \mathbf{S} \mathbf{T} ≠ \mathbf{T} \mathbf{S} $$),
  这两种次序之间所产生差别称为`对易子`:
  - $$ [\mathbf{S}, \mathbf{T}] = \mathbf{S} \mathbf{T} - \mathbf{T} \mathbf{S} $$.
- 两个矩阵积的转置矩阵是两个矩阵分别转置按逆次序的乘积:
  - $$ (\mathbf{S} \mathbf{T})^{T} = \mathbf{T}^{T} \mathbf{S}^{T} $$.
  - __厄米共轭矩阵同样也是这样的__:
  - $$
      (\mathbf{S} \mathbf{T})^{\dagger} =
      \mathbf{T}^{\dagger} \mathbf{S}^{\dagger}
    $$.

---

- 没有逆矩阵的矩阵称为`奇异`矩阵.
  两个矩阵积的逆 (假设存在) 是各自逆矩阵按逆次序的乘积:
  - $$ (\mathbf{S} \mathbf{T})^{-1} = \mathbf{T}^{-1} \mathbf{S}^{-1} $$.
- 如果矩阵的逆等于它的厄米共轭, 则该矩阵是`幺正`矩阵:
  - __幺正矩阵__:
  - $$ \mathbf{U}^{\dagger} = \mathbf{U}^{-1} $$.
- 假设基矢是正交归一的, 幺正矩阵的列构成正交归一集, 其行也构成正交集.
  - __幺正矩阵表示的线性变换保持内积不变__.

- 一般来说, 对于某个 (非奇异) 矩阵
  $$ \mathbf{S} $$,
  如果两个矩阵
  $$ \mathbf{T}_1 $$
  和
  $$ \mathbf{T}_2 $$
  满足
  $$ \mathbf{T}_2 = \mathbf{S} \mathbf{T}_1 \mathbf{S}^{-1} $$,
  那么称
  $$ \mathbf{T}_2 $$
  和
  $$ \mathbf{T}_1 $$
  `相似`.
  - 我们得到的结论是, __对于不同的基矢__, __表示相同线性变换的矩阵是相似的__.
  - 顺便提一下, 如果第一组基是正交基, 则当且仅当
    $$ \mathbf{S} $$
    是幺正矩阵时, 第二组基也将是正交归一基.
  - 因为我们总是研究正交归一基, 所以我们主要对幺正相似变换感兴趣.
- 虽然表示给定线性变换的矩阵元在新基中可能看起来很不一样,
  但与矩阵相关的两个特殊数值却保持不变:
  - 矩阵的`行列式`和`迹`.
- 乘积的行列式等于行列式的积, 因此
  - $$
      det(\mathbf{T}^{f}) =
      det(\mathbf{S} \mathbf{T}^{e} \mathbf{S}^{-1}) =
      det(\mathbf{S}) det(\mathbf{T}^{e}) det(\mathbf{S}^{-1}) =
      det(\mathbf{T}^{e})
    $$.
- `迹`是对角线元素的代数和:
  - $$ Tr(\mathbf{T}) \equiv \sum_{i=1}^{m} \mathbf{T}_{ii} $$,
  - 具有如下性质:
  - $$
      Tr(\mathbf{T}_{1} \mathbf{T}_{2}) =
      Tr(\mathbf{T}_{2} \mathbf{T}_{1})
    $$
  - 对任意两个矩阵
    $$ \mathbf{T}_{1} $$
    和
    $$ \mathbf{T}_{2} $$,
    有
  - $$
      Tr(\mathbf{T}^{f}) =
      Tr(\mathbf{S} \mathbf{T}^{e} \mathbf{S}^{-1}) =
      Tr(\mathbf{T}^{e} \mathbf{S}^{-1} \mathbf{S}) =
      Tr(\mathbf{T}^{e})
    $$.

---

- 矩阵的`特征方程`: 它的解决定了矩阵本征值. 注意到它是一个 `n` 阶方程,
  根据`代数基本定理`, 所以它有 `n` 个 (复数) 根.
  - 然而, 其中一些可能是重根, 所以我们可以肯定地说, 一个
    $$ n \times n $$
    矩阵至少有一个且最多有 `n` 个不同的本征值.
  - 矩阵所有本征值的集合称为它的`谱`;
  - 如果两个 (或更多) 线性无关的`本征矢有相同的本征值`, 则称谱线是`简并`的.

> 注: 原书此处翻译为`根据线性代数基本定理`, 是个错误!
  应为`根据代数基本定理`.

- 将矩阵转化为对角形式有一个明显的优势: 很容易处理问题.
  遗憾的是, 并不是每一个矩阵都能对角化 --
  __本征矢量必须张开整个空间__.
  - 如果特征方程有 `n` 个不同的根, 那么矩阵肯定是可对角化的, 即使是有多个重根,
    矩阵也可能是可对角化的.
- 在计算出所有本征矢之前, 事先知道给定的矩阵是否可对角化是很方便的. 一个有用的充分
  (尽管不是必要) 条件是: 如果矩阵与其厄米共轭对易, 则称其为`正规`矩阵:
  - __正规矩阵__:
  - $$ [\mathbf{N}^{\dagger}, \mathbf{N}] = 0 $$.
- 每个正规矩阵都是可对角化的 (其本征矢张开整个空间).
  - 特别是,
  - __每个厄米矩阵都是对角化的__,
  - __每个幺正矩阵也是对角化的__.

> 这翻译质量, 太仓促了.

- 假设有两个可对角化矩阵; 在量子力学应用中经常会遇到以下问题: (利用同样的相似矩阵
  $$ \mathbf{S} $$)
  它们能同时对角化吗?
  - 也就是说, 是否存在一组基矢, 其所有分量都是两个矩阵的本征矢?
  - 在这种基矢下, 两个矩阵都是对角的.
  - 事实上, __当且仅当两个矩阵对易时答案是肯定的__.
  - 顺便说一句, 如果两个矩阵在一组基矢对易, 那么它们相对于任何一组基矢都对易.

---

- 在量子力学中, `厄米变换`起着基础作用.
  厄米变换的本征值和本征矢有如下重要特性.
  - 厄米变换的本征值是实的
  - 厄米变换属于不同本征值的本征矢彼此正交
  - 更多特性参见:
    [埃尔米特矩阵](https://en.wikipedia.org/wiki/Hermitian_matrix)

> 这就戛然而止了?