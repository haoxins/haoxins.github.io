---
title: 量子力学概论 格里菲斯
description: 待燃犀下看, 凭栏却怕, 风雷怒, 鱼龙惨. 峡束苍江对起, 过危楼, 欲飞还敛.
date: 2023-12-11
---

- [量子力学概论](https://book.douban.com/subject/36460137/)
  - `科恩`系列之后, 为何还要买这本入门书?
  - 其实数年前购买过
    [英文注释版](https://book.douban.com/subject/35257979/),
    但是, 低估了英文阅读的障碍~
  - 所以, 是心结, 是必须填补的遗憾 (强迫症).
  - 相对于`科恩`, `格里菲斯`更适合快速阅读.
    如果不打算花太多时间, 那就选择`格里菲斯`;
    如果打算细致把玩, 则建议`科恩`.
  - 翻译版印刷的错误不少! 符号风格也不是很主流 (规范)~
    翻译水平一般!
  - 顺便一提: 不推荐阅读`费曼物理学讲义 (第三卷)`.
  - 2024-06, 翻译的实在机械, 再次购买了
    [量子力学概论 (英文注释版)](https://book.douban.com/subject/35257979/).

> 怯怯地说: 本书没有感受到那种宗师豪情~

```
本书的目的是教你如何学习量子力学.
除了在第 1 章中一些必备的基础知识外, 更深的准哲学问题将留在书末.
我们不相信一个人在对量子力学是干什么的有一个透彻的理解之前,
他可以明智地讨论量子力学的意义.
但是, 如果你急不可待, 在学习过第 1 章后可立即阅读 <跋>.
```

> `教你如何学习量子力学`. 原文是:
  teach you how to _do_ quantum mechanics.

> 关于印刷错误: 这一方面的质量明显不如`量子力学 (科恩)`.

## 波函数

### 薛定谔方程

- [薛定谔方程](https://en.wikipedia.org/wiki/Schrödinger_equation)

```
从逻辑上讲, 薛定谔方程所起的作用等同于牛顿第二定律:
同在经典力学中由牛顿定律确定以后任意时刻的 x(t) 一样,
量子力学利用所给定的适当初始条件 (一般来说是 Ψ(x, 0)),
通过求解薛定谔方程得到以后任意时刻的波函数 Ψ(x, t).
```

### 统计诠释

- $$
    \int_{a}^{b} \mid Ψ (x, t) \mid ^2 dx =
    \begin{Bmatrix}
      \mbox{在 t 时刻发现粒子位于} \\
      \mbox{a 和 b 之间的几率.}
    \end{Bmatrix}
  $$

```
当然, 如果你关闭一个狭缝, 或者设法去探测每个电子通过的是哪一个狭缝,
干涉图样将会消失; 这时通过 (狭缝) 的粒子波函数和前面的完全不同
(第一种情况属于薛定谔方程的边界条件发生了改变, 第二种情况对应于波函数测量引起坍缩).
但两个狭缝都打开, 电子飞行过程中不受到干扰, 每个电子和自己本身发生干涉.
它不是通过两个狭缝中的某一个, 而是同时通过两个狭缝.
```

> __和自己本身发生干涉__

### 归一化

> `平凡`居然翻译为`平庸`, 无语~

- 但是, 假定在
  $$ t = 0 $$
  时刻把波函数归一化了. 我们如何能知道当
  $$ Ψ $$
  随时间演化时它能保持归一化?
  - (你不能让 __A__ 变成时间的函数来保持波函数的归一化,
    那样的话它就不再是薛定谔方程的解了.)
  - 幸运的是, 薛定谔方程具有一个不同寻常的特性, 它能自动保持波函数的归一化.
  - 没有这个关键的性质, 薛定谔方程将会同统计诠释不相容, 整个理论将会崩溃.

> 演化公设

### 动量

- 简而言之, 期望值是对一个全同系统的系综测量的平均值,
  而不是对同一个系统重复测量的平均值.
  - [系综诠释](https://en.wikipedia.org/wiki/Ensemble_interpretation)

> 原文翻译为`相同系统`, 改为了`全同系统`;
  系综诠释: 个人习惯把`系综` vs `统计`, 视同`期望` vs `均值`的语境差异;
  所以赞同`系综诠释`比`统计诠释`更佳~

- [分部积分法](https://en.wikipedia.org/wiki/Integration_by_parts)

- `算符`是对后面的函数执行某些操作的指令,
  它接收一个函数, 然后输出另一个函数.

> 接收一个函数, 输出一个函数.

- [埃伦费斯特定理](https://en.wikipedia.org/wiki/Ehrenfest_theorem)

- Actually, it is customary to work with __momentum__
  ($$ p = mv $$),
  rather than velocity:
  - $$
      \langle p \rangle =
      m \frac{d \langle x \rangle}{dt} =
      -i \hbar \int (Ψ^{*} \frac{\partial Ψ}{\partial x}) dx
    $$.
- Let me write the expressions for
  $$ \langle x \rangle $$
  and
  $$ \langle p \rangle $$
  in a more suggestive way:
  - $$ \langle x \rangle = \int Ψ^{*} [x] Ψ dx $$,
  - $$ \langle p \rangle = \int Ψ^{*} [-i \hbar (\partial / \partial x)] Ψ dx $$.
- We say that the operator
  $$ x $$
  "represents" position, and the operator
  $$ -i \hbar (\partial / \partial x) $$
  "represents" momentum; to calculate expectation values
  we "sandwich" the appropriate operator between
  $$ Ψ^{*} $$
  and
  $$ Ψ $$,
  and integrate.
  - An "operator" is an instruction to do something to the
    function that follows; it takes in one function,
    and spits out some other function.
  - The position operator tells you to multiply by
    $$ x $$;
    the momentum operator tells you to differentiate with respect to
    $$ x $$
    (and multiply the result by
    $$ -i \hbar $$).
- To calculate the expectation value of any such quantity,
  $$ Q(x, p) $$,
  we simply replace every
  $$ p $$
  by
  $$ -i \hbar (\partial / \partial x) $$,
  insert the resulting operator between
  $$ Ψ^{*} $$
  and
  $$ Ψ $$,
  and integrate:
  - $$
      \langle Q(x, p) \rangle =
      \int Ψ^{*} [Q(x, -i \hbar \partial / \partial x)] Ψ dx
    $$.

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

傅里叶分析中的一个定理可以给出这种情况的一个严格证明, 不过目前仅涉及定性讨论.
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

> `波包`确实不如`科恩`讲述地详细, 弱化了公式的推导.
  或者说, 放在了习题里面.

## 定态薛定谔方程

- [分离变量法](https://en.wikipedia.org/wiki/Separation_of_variables)

### 定态

- [定态](https://en.wikipedia.org/wiki/Stationary_state)
  - 概率密度与时间无关;
  - 哈密顿量不变.

> 定态: time independent; stationary state

```
一旦解出了定态薛定谔方程的分离变量解,
就可以从中得到含时薛定谔方程的通解,
这在原则上是简单明了的.
```

```
I claimed that the most general solution to the
(time-dependent) Schrödinger equation is a
linear combination of stationary states.
```

- That does it: Given the initial wave function
  $$ Ψ(x, 0) $$,
  we first compute the expansion coefficients
  $$ c_n $$,
  and then plug these to obtain
  $$ Ψ(x, t) $$.

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

- 定态薛定谔方程的解是一个无限的解集 (每个正整数
  $$ n $$
  对应一个解).
  它们看起来像位于一个长度为
  $$ a $$
  的弦上的驻波. 波函数
  $$ ψ_1 $$
  具有最低的能量, 称为`基态`, 其他状态的能量正比于
  $$ n^2 $$,
  称为`激发态`. 总结一下, 函数
  $$ ψ_n (x) $$
  具有如下有趣和重要的性质:
  - 波函数
    $$ ψ_n (x) $$
    相对于无限深势阱的中心是奇偶交替的.
  - 随着能量的增加, 相继状态的`节点数` (与
    $$ x $$
    轴交点) 逐次增 `1`.
  - __它们是相互正交的__.
  - 它们是`完备`的, 也就是说对其他任意函数
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

- [胡克定律](https://en.wikipedia.org/wiki/Hooke%27s_law)

```
事实上, 对于任何振动来说,
只要其振幅足够小, 都可以近似看作简谐振动;
这就是谐振子为什么如此重要的原因.
```

- 求解势能函数的薛定谔方程:
  - 幂级数法求解微分方程;
  - 或者,
    [阶梯算符](https://en.wikipedia.org/wiki/Ladder_operator)

```
和无限深方势阱情况一样, 谐振子的所有定态解都是相互正交的.
```

- [厄米多项式](https://en.wikipedia.org/wiki/Hermite_polynomials)

### 自由粒子

```
对自由粒子而言, 分离变量解并不代表物理上可实现的状态.
自由粒子不能存在于定态上; 或者, 换句话说,
世界上不存在一个自由粒子具有确定的能量.

但这并不意味着分离变量解对我们没有任何用途.
因为它们扮演一个完全独立于物理释义的数学角色.
含时薛定谔方程的一般解仍旧是分离变量解的线性叠加.
```

```
正弦波扩展到无限远, 它们是不可归一化的.
但是这种波的叠加会产生干涉, 从而使得可以局域化和归一化.
```

> __波包__

- [普朗克尔定理](https://en.wikipedia.org/wiki/Plancherel_theorem)

```
波函数中对应的粒子速度不是某一个波纹的速度 (即所谓的相速度),
而是包络线的速度 (群速度) -- 这个速度, 取决于波包的本质,
可以大于, 等于或者小于其组成波包的波纹的速度.

对于绳子上的波, 其群速度等于相速度.
对于水波, 当你向水塘扔进一块石头, 其群速度是相速度的一半
(如果你留意其中一个波纹, 会发现它在后部生成, 向前运动越过波群,
在前面消失, 而波群则以个别波纹的一半速度传播).

量子力学中自由粒子波函数的群速是相速的两倍 -- 正好等于经典粒子的速度.
```

- [相速度](https://en.wikipedia.org/wiki/Phase_velocity)
- [群速度](https://en.wikipedia.org/wiki/Group_velocity)

### δ 函数势

- 我们已经接触到了定态薛定谔方程的两类不同的解:
  对无限深方势阱和谐振子两种情况它们的解是可归一化的,
  其解由分立的指标 `n` 标记;
  对自由粒子情况它们是不可归一化的,
  其解用一个连续的变量 `k` 标记.
  - 前者本身代表物理上可实现的状态, 而后者则不是.
  - 但是, 在两种情况下含时薛定谔方程的一般解都是定态解的线性叠加:
  - 对第一类情况这种叠加是采取求和的形式 (对 `n`),
  - 而对第二类情况这种叠加则是一个积分 (对 `k`).
  - 这种差别的物理意义是什么?
- 在经典力学中, 不含时的一维势场可以导致两种迥然不同的运动情况.
  - 如果
    $$ V(x) $$
    的两边都高于粒子的总能
    ($$ E $$),
    则粒子的运动被`限制`在势阱内: 它在两个拐点之间往返运动, 但是它不能逃逸.
  - 我们称之为`束缚态`.
  - 另一方面, 如果
    $$ E $$
    在一边 (或两边) 大于
    $$ V(x) $$,
    则从`无限远`过来的粒子在势场的影响下减速或加速, 然后折回到无限远处.
  - 我们称这种情况为一个`散射态`.
  - 某些势场仅允许束缚态 (例如谐振子);
    某些势场仅允许散射态 (例如一个逐渐升高而不下降的斜坡形的势场);
    依据粒子能量的大小, 还有一些势场两者则都允许.
- 薛定谔方程的两类解恰好对应着束缚态和散射态. 因为`隧穿现象`,
  允许粒子`泄漏`通过任何有限势垒, 这种区别在量子领域更为明显.
  - 因此唯一重要的是无限远处的势:
  - $$
      \begin{cases}
        E < [ V(- \infty) \mbox{ } 和 \mbox{ } V(\infty) ]
        \Rightarrow 束缚态, \\
        E > [ V(- \infty) \mbox{ } 或 \mbox{ } V(\infty) ]
        \Rightarrow 散射态
      \end{cases}
    $$
- 自然界中大多数的势场在无限远处趋于零,
  在这种情况下, 上面的判据变得更为简化:
  - $$
      \begin{cases}
        E < 0 \Rightarrow 束缚态, \\
        E > 0 \Rightarrow 散射态
      \end{cases}
    $$
  - 由于无限深方势阱和谐振子势在
    $$ x \rightarrow \pm \infty $$
    时都趋于无限大, 它们仅存在束缚态;
  - 由于自由粒子的势处处为零, 它仅存在散射态.

- [狄拉克 δ 函数](https://en.wikipedia.org/wiki/Dirac_delta_function)

```
这些结果很简洁, 但我们不能完全忽视一个棘手的原则问题:
这些散射波函数是不可归一化的, 所以它们不代表实际的可能粒子状态.
我们知道解决这个问题的方法:
构造定态解的可归一化的线性组合, 正如我们处理自由粒子那样 --
真正的实物粒子是由产生的波包所表示的.
虽然原理上很简单, 但实际上这是一件麻烦的事情,
在这一点上, 最好把问题交给计算机解决.
```

- [散射矩阵](https://en.wikipedia.org/wiki/S-matrix)
- [传递矩阵法](https://en.wikipedia.org/wiki/Transfer-matrix_method)
- [简并能级](https://en.wikipedia.org/wiki/Degenerate_energy_levels)

## 形式理论

> 真正意义上的第一章!

### 希尔伯特空间

```
量子理论是建立在两个概念的基础上的: 波函数和算符.
体系的状态用它的波函数来表示, 可观测量用算符来表示.
数学上, 波函数满足抽象矢量的定义条件,
算符作为线性变换作用于矢量之上.
因此, 量子力学的自然语言是线性代数.
但是, 我估计它并不是你们已所熟悉的线性代数的形式.
```

- 在
  $$ N $$
  维空间中, 矢量
  $$ \mid α \rangle $$
  可以非常简单地用它的
  $$ N $$
  个组元: 特定的一组正交归一基
  $$ \{ a_n \} $$
  来表示.
  - 两个矢量的`内积` (三维空间标量积的推广)
    $$ \langle α \mid β \rangle $$
    是一个复数:
  - $$
      \langle α \mid β \rangle =
      a_1^{*} b_1 +
      a_2^{*} b_2 +
      ...
      a_N^{*} b_N
    $$.
  - 线性变换
    $$ T $$
    用`矩阵` (对应特定的基矢) 表示,
    通过标准的矩阵运算作用于矢量上 (得到新的矢量).
- 但在量子力学中, __我们遇到的矢量是波函数__ (绝大多数情况下),
  且它们存在于无穷维空间中. 对于它们, 用
  $$ N $$
  个`组元/矩阵`的记法不便处理, 而且,
  在有限维情况下通用的矩阵运算在这里可能会存在问题.

---

- 所有
  $$ x $$
  的函数的集合构成了一个矢量空间, 但对我们讨论的问题来说,
  它确实太大了. 为了表示一个可能的物理状态, 波函数
  $$ Ψ $$
  必须是归一化的:
  - $$ \int \mid Ψ \mid^2 dx = 1 $$.
  - 在一个特定区间内, 所有的`平方可积`函数的集合,
    $$ f(x) $$
    满足
    $$ \int_{a}^{b} \mid f(x) \mid^2 dx < \infty $$,
    构成一个 (非常小) 矢量空间.
  - 数学家称之为
    $$ L^2 (a, b) $$;
    而物理学家称它为`希尔伯特空间`.
    因此, 在量子力学中, 波函数存在于希尔伯特空间中.
- 两个函数
  $$ f(x) $$
  和
  $$ g(x) $$
  的`内积`定义如下:
  - $$ \langle f \mid g \rangle \equiv \int_a^b f(x)^{*} g(x) dx $$.
  - 如果
    $$ f $$
    和
    $$ g $$
    都是平方可积的 (也就是说, 两者都在希尔伯特空间中),
    它们的内积是肯定存在的. 这点可以从
    [施瓦茨不等式](https://en.wikipedia.org/wiki/Cauchy-Schwarz_inequality)
    给出.
  - 特别注意到
    $$ \langle g \mid f \rangle = \langle f \mid g \rangle^{*} $$.
  - 此外,
    $$ f(x) $$
    与`本身`的内积,
    $$ \langle f \mid f \rangle = \int_a^b \mid f(x) \mid^2 dx $$,
    它是一个非负实数, 仅当
    $$ f(x) = 0 $$
    时为零.

```
严格地讲, 一个希尔伯特空间是一个完备的内积空间,
平方可积函数的集合只是希尔伯特空间的一个例子 --
的确, 每一个有限维矢量空间是一个平凡的希尔伯特空间.
但是, 既然 L2 空间是量子力学的舞台,
这就是物理学家讲希尔伯特空间时的通常含义.

顺便说一下, 完备一词在这里的意思是:
希尔伯特空间中任何函数的柯西序列收敛于一个同样在希尔伯特空间中的函数;
这个空间没有孔洞, 就像所有的实数的集合没有孔洞一样.
(与此相比, 例如, 所有多项式的空间, 像所有有理数的集合一样, 的确是有孔洞的.)
空间的完备性同一组函数的完备性 (遗憾的是用了同一词) 没有任何关系.
这组函数的完备性是指任何函数都可以表示为这组函数的线性组合.
```

```
一个函数除了几个孤立的点之外, 处处是零, 那会是怎样?
尽管函数本身不为零, 但它的积分式仍然是零.
如果对这一点感到困惑, 你应该是学数学的.
物理学中这种病态函数并不会出现, 但无论如何, 在希尔伯特空间中,
如果两个函数差的绝对值平方的积分为零, 我们称这两个函数是等价的.
严格地讲, 希尔伯特空间中的矢量代表函数的等价类.
```

- 如果函数与自身的内积为 `1`, 我们称之为该函数是`归一化`的;
  如果两个函数的内积为 `0`, 那么这两个函数是`正交`的; 如果一组函数
  $$ | f_n | $$
  既是归一的也彼此相互正交, 称它们为`正交归一`:
  - $$ \langle f_m \mid f_n \rangle = δ_{mn} $$.
  - 最后, 如果存在一个函数集, 其他任何函数 (希尔伯特空间中)
    都可以表示为该函数集的线性叠加, 那么称该函数集是`完备`的:
  - $$ f(x) = \sum_{n=1}^{\infty} c_n f_n (x) $$.
  - 如果函数
    $$ | f_n (x) | $$
    是正交归一的, 上式中的常数可以由傅里叶变换得到:
    $$ c_n = \langle f_n \mid f \rangle $$.

> 函数, 矢量, 傅里叶

### 可观测量

- 可观测量
  $$ Q(x, p) $$
  的`期望`值可以非常简洁地用内积符号表示出来:
  - $$
      \langle Q \rangle =
      \int ψ^{*} \hat{Q} ψ dx =
      \langle ψ \mid \hat{Q} ψ \rangle
    $$.
  - 现在, 一次测量的结果应该是实数,
    更确切地说, 它是多次测量值的平均值:
    $$ \langle Q \rangle = \langle Q \rangle^{*} $$.
  - 但一个内积的复共轭是颠倒两个函数乘积顺序, 因此
    $$
      \langle ψ \mid \hat{Q} ψ \rangle =
      \langle \hat{Q} ψ \mid ψ \rangle
    $$,
    对任意波函数
    $$ ψ $$
    都成立.
  - 因此, 表示可观测量的算符具有下面非常特殊的性质:
  - $$
      \langle f \mid \hat{Q} f \rangle =
      \langle \hat{Q} f \mid f \rangle
    $$
    对任何
    $$ f(x) $$
    成立.
  - 该算符称为`厄米算符`.

> __注意__: `期望`的符号表示!

- 事实上, 大多数书籍都要求表面上更严格的条件:
  - $$
      \langle f \mid \hat{Q} g \rangle =
      \langle \hat{Q} f \mid g \rangle
    $$
    对任意
    $$ f(x) $$
    和
    $$ g(x) $$
    成立.
  - 事实证明, 尽管表面上看来不同, 但这完全等同于我们的定义.
    因此, 这两种形式无论哪一个都可以随意使用.
  - __本质是厄米算符既可以作用于内积中的第一项也可以作用于第二项__,
    其结果一样, 由于厄米算符的期望值是实数, 它们很自然出现在量子力学中:
  - __可观测量由厄米算符表示__.

> `由于厄米算符的期望值是实数, 它们很自然出现在量子力学中.`
  这个说法, 如何?

> 此处摘引一段
  [惰者集](https://book.douban.com/subject/27603987/)
  中的文字~

```
也就是说, 数学运算支配了作为量子力学对象的物理现象.
这种数学运算与物理现象的关系,
并非是通过解析叠加的物理意义而将其用数学公式表现出来,
而是将 "波函数的线性组合可以描述状态的叠加" 视为公理,
然后依据数学运算来确定叠加的意义.
正如费曼所言, 除了数学之外, 没有其他方法能说明态叠加原理了.
我们只能认为量子力学基于数学的无穷魔法,
因此我认为物理现象的背后存在着固有的数学现象.
```

> 摘引结束~

- 算符
  $$ \hat{Q} $$
  的`厄米共轭`算符 (或者`伴`算符) 是
  $$ \hat{Q}^{\dagger} $$,
  满足
  - $$
      \langle f \mid \hat{Q} g \rangle =
      \langle \hat{Q}^{\dagger} f \mid g \rangle
    $$
    对所有的
    $$ f $$
    和
    $$ g $$.
  - 那么, 厄米算符等同于它的厄米共轭:
    $$ \hat{Q} = \hat{Q}^{\dagger} $$.

### 厄米算符的本征函数

- $$ \hat{Q} ψ = q ψ $$.
  - 这就是算符
    $$ \hat{Q} $$
    的`本征值方程`;
    $$ ψ $$
    是
    $$ \hat{Q} $$
    的`本征函数`,
    $$ q $$
    是相应的`本征值`.
  - 因此
    $$ Q $$
    的确定值态是
    $$ \hat{Q} $$
    的本征函数.
  - 在该态上对
    $$ Q $$
    进行测量一定能够得到本征值
    $$ q $$.
- 注意到本征值是一个数 (既不是算符也不是函数).
  任何本征函数乘以一常数, 仍然是具有相同本征值的本征函数.
  - 零不能称作为本征函数 (我们从定义中把它排除,
    否则任何一个数都是它的本征值, 因为对任意的线性算符
    $$ \hat{Q} $$
    和所有的
    $$ q $$,
    都有
    $$ \hat{Q} 0 = q 0 = 0 $$).
  - 但是, `0` 作为本征值是不存在任何问题的.
  - 算符所有本征值的集合称为该算符的`谱`.
  - 有时候两个 (或者更多) 线性独立的本征函数具有相同的本征值;
    在这种情况下称为谱的`简并`.

```
The collection of all the eigenvalues of
an operator is called its spectrum.
Sometimes two (or more) linearly independent
eigenfunctions share the same eigenvalue;
in that case, the spectrum is said to be degenerate.
```

> 下面摘录一个极简特征方程的例子:

- The eigenvalue equation,
  - $$ i \frac{d}{d ϕ} f(ϕ) = q f(ϕ) $$,
  - has the general solution
  - $$ f(ϕ) = A e^{-i q ϕ} $$.
  - Also restricts the possible values of the
    $$ q $$,
  - $$ e^{-i q 2π} = 1 \Rightarrow q = 0, ±1, ±2, ... $$
  - The spectrum of this operator is the set of
    all integers, and it is nondegenerate.

- 现在, 我们把注意力集中在厄米算符的本征函数上
  (从物理角度: 可观测量的确定值态). 它们可分成两类情况:
  - 如果谱是`离散`的 (即, 本征值是分离的),
    则本征函数位于希尔伯特空间中并且构成物理上可实现的态;
  - 如果谱是`连续`的 (即, 本征值填满整个范围),
    那么本征函数是不可归一化的, 并且它们无法代表可能的波函数
    (尽管它们的线性组合, 这必定涉及本征值的一个分布, 可能是可归一化的).
  - 某些算符仅有离散谱 (例如谐振子的哈密顿),
    某些仅有连续谱 (例如自由粒子的哈密顿),
    还有一些既有离散谱部分也有连续谱部分 (例如有限深方势阱中的哈密顿).
  - 离散谱情况比较容易处理, 因为相关的内积一定存在. 实际上,
    这和有限维理论相似 (厄米矩阵的本征矢量).
- __离散谱__
  - 数学上, 厄米算符的可归一化本征函数具有两个重要性质:
  - 定理 `1`: 它们的本征值是实数.
  - 定理 `2`: 属于不同本征值的本征函数是正交的.

```
定理 1 是令人欣慰的:
如果你在一个确定的状态下测量粒子的一个观测量,
至少会得到一个实数.
```

```
这就是无限深方势阱的定态, 或者谐振子的定态, 都是正交的原因.
它们是哈密顿量具有不同本征值的本征函数.
但这一性质并不单单是它们所特有的, 甚至仅是哈密顿量所特有 --
对任何可观测量的定态都是如此.
```

- 遗憾的是, 定理 `2` 没有涉及任何关于简并态
  ($$ q' = q $$)
  的问题. 不过, 如果两个 (或者更多) 本征函数具有相同的本征值,
  它们的任何线性组合仍是具有同样本征值的本征函数, 而且, 在每一个简并的子空间中,
  可以利用`格拉姆-施密特正交化`步骤构建相互正交的本征函数.
  - 这在原则上总是可以做到的, (谢天谢地) 但几乎没有必要明确的这样做.
  - 所以, 即使存在简并情况, 本征函数依然可以选择彼此正交, 并且我们假定已是如此.
  - 依据基函数的正交归一性, 这就允许我们使用相应的傅里叶技巧.
- 在一个有限维的矢量空间中, 厄米矩阵的本征矢量具有第三个基本性质:
  - 它们贯穿整个空间 (任何一个矢量都可以用它们的线性组合来表示).
    遗憾的是, 其证明不能推广到无限维的空间.
  - 但是这个性质本身对量子力学内在的自洽性是必需的, 所以 (遵从狄拉克)
    我们将它作为一个公理 (或者, 更确切地说,
    可以看作是加在可观测量厄米算符上的一个限制条件):
  - 公理: __可观测量算符的本征函数是完备的__:
    (在希尔伯特空间中的) 任何函数都可以用它们的线性组合来表示.

- [动量算符](https://en.wikipedia.org/wiki/Momentum_operator)
- [位置算符](https://en.wikipedia.org/wiki/Position_operator)

```
如果厄米算符的谱是连续的, 本征函数是不可归一化的,
它们不位于希尔伯特空间内, 且不表示可能的物理状态;
无论如何, 实数本征值的本征函数满足狄拉克正交归一性,
并且是完备的 (由求和变为积分).
幸运的是, 这正是我们真正所需要的.
```

### 广义统计诠释

- __广义统计诠释__: 如果你对处于
  $$ Ψ (x, t) $$
  状态粒子的可观测量
  $$ Q (x, p) $$
  进行测量, 那么, 你一定会得到厄米算符
  $$ \hat{Q} (x, -i \hbar d/dx) $$
  的本征值中的某一个. 如果
  $$ \hat{Q} $$
  的谱是离散的, 得到与本征函数
  $$ f_n (x) $$
  (正交归一) 相应的本征值
  $$ q_n $$ 的几率是
  - $$ | c_n |^2 $$,
    其中
    $$ c_n = \langle f_n \mid Ψ \rangle $$.
  - 如果是连续谱, 且具有实数本征值
    $$ q(z) $$
    和 (`狄拉克-正交归一`的) 本征函数
    $$ f_z (x) $$,
    则在
    $$ dz $$
    范围内, 得到结果几率是
  - $$ | c(z) |^2 dz $$,
    其中
    $$ c(z) = \langle f_z \mid Ψ \rangle $$.
  - 测量之后, 波函数坍缩于相应的本征态.

> 无处不在的傅里叶

- 可观测量算符的本征函数是完备的, 所以波函数可以写成它们的线性组合:
  - $$ Ψ (x, t) = \sum_{n} c_n (t) f_n (x) $$.
  - (简单起见, 假设谱是离散的.)
- 由于本征函数是正交归一的, 展开系数由傅里叶变换得出:
  - $$
      c_n (t) =
      \langle f_n \mid Ψ \rangle =
      \int f_n (x)^{*} Ψ (x, t) dx
    $$.
  - 定性地讲,
    $$ c_n $$
    告诉我们
    "$$ Ψ $$
    中包含有多少
    $$ f_n $$",
    考虑到每次测量一定得到算符
    $$ \hat{Q} $$
    的一个本征值, 所以, 得到特定本征值
    $$ q_n $$
    的几率取决于
    $$ Ψ $$
    中 "包含的
    $$ f_n $$
    量的大小" 似乎是合理的.
  - 但由于几率是由波函数的绝对值平方决定的, 因此精确的测量实际上是
    $$ | c_n |^2 $$.
  - 这才是广义统计诠释的精髓所在.
- __再说一下__, 这里小心地避开十分普遍的论述
  "$$ | c_n |^2 $$
  是粒子处于
  $$ f_n $$
  态的概率".
  - 这毫无意义. 粒子是处于态
    $$ Ψ $$.
  - 而
    $$ | c_n |^2 $$
    是对
    $$ \hat{Q} $$
    进行测量得到值为
    $$ q $$
    的几率. 这种测量会使态向本征函数
    $$ f_n $$
    坍缩.
  - 所以一种正确说法应该是
    "$$ | c_n |^2 $$
    是处于
    $$ Ψ $$
    态的粒子在对
    $$ \hat{Q} $$
    值进行测量后将处于
    $$ f_n $$
    态的几率".
  - 但是这是完全不同的论述.

> 参见: 科恩, 卷一, Page 17, `波函数; 薛定谔方程`

- Similarly, the expectation value of
  $$ Q $$
  should be the sum over all possible outcomes of the
  eigenvalue times the probability of getting that eigenvalue:
  - $$ \langle Q \rangle = \sum_{n} q_n \mid c_n \mid^2 $$.
  - Indeed,
  - $$
      \langle Q \rangle =
      \langle Ψ \mid \hat{Q} Ψ \rangle =
      \langle (\sum_{n'} c_{n'} f_{n'})
      \mid
      (\hat{Q} \sum_{n} c_n f_n) \rangle
    $$,
  - but
    $$ \hat{Q} f_n = q_n f_n $$,
    so
  - $$
      \langle Q \rangle =
      \sum_{n'} \sum_{n} c_{n'}^{*} c_n q_n
      \langle f_{n'} \mid f_n \rangle =
      \sum_{n'} \sum_{n} c_{n'}^{*} c_n q_n δ_{n' n} =
      \sum_{n} q_n \mid c_n \mid^2
    $$.
  - So far, at least, everything looks consistent.

- [位置空间与动量空间](https://en.wikipedia.org/wiki/Position_and_momentum_spaces)

- The __momentum space wave function__,
  $$ Φ(p, t) $$.
  It is essentially the Fourier transform of the
  (__position space__) wave function
  $$ Ψ(x, t) $$,
  which, by Plancherel's theorem,
  is its _inverse_ Fourier transform:
  - $$
      Φ(p, t) = \frac{1}{\sqrt{2 \pi \hbar}}
      \int_{- \infty}^{+ \infty}
      e^{-ipx / \hbar} Ψ(x, t) dx
    $$;
  - $$
      Ψ(x, t) = \frac{1}{\sqrt{2 \pi \hbar}}
      \int_{- \infty}^{+ \infty}
      e^{ipx / \hbar} Φ(p, t) dp
    $$.
- According to the generalized statistical interpretation,
  the probability that a measurement of momentum would
  yield a result in the range
  $$ dp $$
  is
  - $$ \mid Φ(p, t) \mid^2 dp $$.

### 不确定性原理

- $$ σ_A^2 σ_B^2 \ge (\frac{1}{2i} \langle [\hat{A}, \hat{B}] \rangle)^2 $$.
  - 这就是 (广义的) __不确定原理__.
  - 你或许会认为复数
    $$ i $$
    使得这个式子无意义, 等式的右边不是负值吗? 其实不然,
    因为两个厄米算符的对易式本身具有
    $$ i $$
    因子, 因此两者相互抵消掉; 括号中的数值为实数, 它的平方是正数.
  - 更确切地说, 两个厄米算符的对易式本身是个反厄米算符
    $$ (\hat{Q}^{\dagger} = - \hat{Q}) $$,
    且它的期望值是虚数.
  - 非对易的矩阵不能同时对角化 (即它们不能被同一个相似变换变为对角矩阵),
    而对易厄米矩阵可以同时被对角化.

> 注: 尝试理解
  $$ i $$
  代表的对称性~

> [不确定性原理](https://en.wikipedia.org/wiki/Uncertainty_principle),
  这个词条好详细!

```
事实上, 对每一对可观测量, 如果其算符不对易, 都将存在一个不确定原理 --
我们称它们为不相容可观测量. 不相容可观测量没有共同的本征函数 --
至少, 它们不可能有共同本征函数的完备集.
相比之下, 相容 (可对易) 的可观测量却可以有共同的本征函数完备集
(也就是说, 对两个可观测量都是确定的状态).
```

```
需要注意的是, 不确定原理并不是量子力学中的一个额外假定, 它是统计诠释的结果.
你或许感到奇怪, 这在实验室是如何实施的呢?
为什么就不能同时确定 (比方说) 粒子的位置和动量呢?
当然你可以测量粒子的位置, 但是测量行为使波函数坍缩为一个尖峰,
这样在傅里叶展开中必然带来一个很宽范围的波长 (动量) 分布.
如果此时你对粒子动量进行测量, 这个状态将坍缩成一个有确定波长的长正弦波 --
但这时的粒子已经不再位于你第一次测量时的位置.
那么, 因此, 问题在于第二次测量会使第一次测量的结果过时.
只有当波函数同时是两个可测量量的本征态时,
才可能在不破坏粒子状态的情况下进行第二次测量 (这种情况下, 第二次坍缩不改变任何状态).
但一般来说, 这只有在两个可观测量是相容的情况下才有可能.
```

- 的确, 在狭义相对论的情况下,
  `能量-时间不确定`原理的形式可以被认为是`位置-动量不确定`原理形式的一个推论, 因为
  $$ x $$
  和
  $$ t $$
  (或者说
  $$ ct $$)
  合在一起为`坐标-时间空间`的四矢量, 而
  $$ p $$
  和
  $$ E $$
  (或者说
  $$ E/c $$)
  一起为`能量-动量空间`的四矢量.
  - 但现在我们不是在讨论相对论量子力学. 薛定谔方程显然是非相对论的: 式中赋予
    $$ x $$
    和
    $$ t $$
    完全不同的地位 (在同一个微分方程中,
    $$ t $$
    是一阶导数, 而
    $$ x $$
    是二阶导数).
  - 现在目的是推导出`能量-时间不确定`原理, 并且使你明白,
    这的确是完全不同的另外一件事情,
    而它与`位置-动量不确定`原理表面上的相似确实是一种误导.
  - 毕竟, 位置, 动量和能量都是系统的动力学变量,
    体系在任何给定时刻的可观测特性. 但时间本身并不是动力学变量
    (在非相对论理论中, 任何情况下都不是):
    你不可能像测量位置或者能量一样去测量粒子的时间.
  - 时间是一个独立变量, 动力学量是它的函数.
    特别是, `能量-时间不确定`原理中的
    $$ Δt $$
    不是一组时间测量值的标准偏差.
    粗略地讲, 正是体系发生实质性的变化经历的时间.

- 在算符不明显含时的典型情况下,
  算符期望值的变化率由该算符与哈密顿量的对易式确定.
  - 特别是, 如果
    $$ \hat{Q} $$
    与
    $$ \hat{H} $$
    对易, 则
    $$ \langle Q \rangle $$
    是常量; 在这个意义上
    $$ Q $$
    是一个`守恒`量.

- $$ Δt $$
  表示
  $$ Q $$
  的期望值大小变化为一个标准差时所需的时间的多少.
  - 特别是,
    $$ Δt $$
    完全依赖于你想要观察的那个可观测量
    $$ (Q) $$,
    对于一个可观测量的变化可能很快, 而对于另一个则很慢.
  - 但是, 如果
    $$ ΔE $$
    很小的话, 则所有可观测量的变化速率一定是非常平缓的;
  - 或者, 换个方式来叙述, 如果任一可观测量变化很快的话,
    能量的不确定必定很大.

- 人们常说, 不确定原理意味着在量子力学中能量不严格守恒;
  就是说你可以`借出`能量
  $$ ΔE $$,
  只要在
  $$ Δt ≈ \hbar / (2 ΔE) $$
  时间内可以`返还`的话; 对守恒破坏越大, 它所经历的时间周期越短.
  - 现在有很多关于`能量-时间不确定`原理的标准读物,
    但是本书不属于它们中的一个.
  - 量子力学没有任何地方允许违反能量守恒定律.
  - 但不确定原理是如此强大坚实:
    它可以被误用而不会导致严重的错误结果,
    因而很多物理学家习惯于草率地应用它.

> 但不确定原理是如此强大坚实:
  它可以被误用而不会导致严重的错误结果,
  因而很多物理学家习惯于草率地应用它.

> 哈哈, 想起`曹则贤`在`黑体辐射`中的类似说法:
  物理学其实容错性很强, 所以容易混淆视听.

### 矢量和算符

> 本书的排版质量真是一言难尽~

- 量子力学中体系的状态也是如此. 它由希尔伯特空间中的一个矢量来描述,
  $$ \mid S(t) \rangle $$,
  且我们可以用任何数目的不同基矢来表示它. __波函数__
  $$ Ψ(x, t) $$
  __实际上是__
  $$ \mid S(t) \rangle $$
  在坐标本征函数为基上展开的
  $$ x $$
  __分量__:
  - $$ Ψ(x, t) = \langle x \mid S(t) \rangle $$

- 正如矢量的表示一样, 算符 (对某个特殊的基) 是用它们的`矩阵元`来表示:
  - $$ \langle e_m \mid \hat{Q} \mid e_n \rangle \equiv Q_{mn} $$.

- The same is true for the state of a system in quantum mechanics.
  It is represented by a _vector_,
  $$ \mid S(t) \rangle $$,
  that lives "out there in Hilbert space",
  but we can express it with respect to any number of different bases.
  The wave function
  $$ Ψ(x, t) $$
  is actually the
  $$ x $$
  "component" in the expansion of
  $$ \mid S(t) \rangle $$
  in the basis of position eigenfunctions:
  - $$ Ψ(x, t) = \langle x \mid S(t) \rangle $$,
  - (the analog to
    $$ \hat{l} \cdot A $$)
    with
    $$ \mid x \rangle $$
    standing for the eigenfunction of
    $$ \hat{x} $$
    with eigenvalue
    $$ x $$.
- The momentum space wave function
  $$ Φ(p, t) $$
  is the
  $$ p $$
  component in the expansion of
  $$ \mid S(t) \rangle $$
  in the basis of momentum eigenfunctions:
  - $$ Φ(p, t) = \langle p \mid S(t) \rangle $$
  - (with
    $$ \mid p \rangle $$
    standing for the eigenfunction of
    $$ \hat{p} $$
    with eigenvalue
    $$ p $$).
- Or we could expand
  $$ \mid S(t) \rangle $$
  in the basis of energy eigenfunctions
  (supposing for simplicity that the spectrum is discrete):
  - $$ c_n (t) = \langle n \mid S(t) \rangle $$
  - (with
    $$ \mid n \rangle $$
    standing for the `n`th eigenfunction of
    $$ \hat{H} $$).
  - But it's all the same state; the functions
    $$ Ψ $$
    and
    $$ Φ $$,
    and the collection of coefficients
    $$ \{ c_n \} $$,
    contain exactly the same information, they are simply
    three different ways of identifying the same vector.

---

- Just as vectors look different when expressed in
  different bases, so too do operators (or,
  in the discrete case, the matrices that represent them).
  We have already encountered a particularly nice example:
  - $$ \hat{x} $$
    (the position operator)
    $$ \rightarrow $$
    $$
      \begin{cases}
        x
        & \mbox{ } (\mbox{in position space}) \\
        i \hbar \partial / \partial p
        & \mbox{ } (\mbox{in momentum space})
      \end{cases}
    $$
  - $$ \hat{p} $$
    (the momentum operator)
    $$ \rightarrow $$
    $$
      \begin{cases}
        -i \hbar \partial / \partial x
        & \mbox{ } (\mbox{in position space}) \\
        p
        & \mbox{ } (\mbox{in momentum space})
      \end{cases}
    $$

```
"Position space" is nothing but the position basis;
"momentum space" is the momentum basis.
```

- If someone asked you, "What is the operator,
  $$ \hat{x} $$,
  representing position, in quantum mechanics?"
  - you would probably answer "Just
    $$ x $$
    itself". But an equally correct reply would be
    "$$ i \hbar \partial / \partial p $$",
    and the best response would be "With respect to what basis"?

- I have often said "the state of a system is
  represented by its wave function,
  $$ Ψ(x, t) $$",
  and this is true, in the same sense that an
  ordinary vector in three dimensions is
  "represented by" the triplet of its components;
  but really, I should always add "in the position basis".
  - After all, the state of the system
    is a vector in Hilbert space,
    $$ \mid S(t) \rangle $$;
    it makes no reference to any particular basis.
  - Its connection to
    $$ Ψ(x, t) $$
    is given by equation:
    $$ Ψ(x, t) = \langle x \mid S(t) \rangle $$.
  - Having said that, for the most part we do in fact work
    in position space, and no serious harm comes from referring
    to the wave function as "the state of the system".

- 假如
  $$ \mid α \rangle $$
  是一个归一化矢量, 算符
  - $$ \hat{P} \equiv \mid α \rangle \langle α \mid $$
  - 将会从其他的任意矢量中挑选出 "沿
    $$ \mid α \rangle $$
    方向" 的部分:
  - $$ \hat{P} \mid β \rangle \equiv \langle α \mid β \rangle \mid α \rangle $$;
  - 我们称它为投影到由
    $$ \mid α \rangle $$
    张开的一维子空间上的`投影算符`.
- 如果
  $$ \{ \mid e_n \rangle \} $$
  是一离散的正交归一基,
  $$ \langle e_m \mid e_n \rangle = δ_{mn} $$,
  - 则有
    $$ \sum_{n} \mid e_n \rangle \langle e_n \mid = 1 $$
    (称`恒等算符`).
- 如果我们把该算符作用在任意矢量
  $$ \mid α \rangle $$
  上, 得到
  $$ \mid α \rangle $$
  以
  $$ \{ \mid e_n \rangle \} $$
  为基的展开式:
  - $$
      \sum_{n} \mid e_n \rangle \langle e_n \mid α \rangle =
      \mid α \rangle
    $$.
  - 类似地, 假如
    $$ \{ \mid e_z \rangle \} $$
    是一组狄拉克正交归一的连续基,
  - $$ \langle e_z \mid e_{z'} \rangle = δ (z - z') $$,
  - 那么
    $$ \int \mid e_z \rangle \langle e_z \mid dz = 1 $$.

```
偶尔我们也会遇到算符是个函数形式, 它们通常由幂级数展开式来定义.
```

- 我们该如何看待
  $$ \langle \hat{Q} f \mid f \rangle $$
  呢?
  - $$ \langle \hat{Q} f \mid $$
    的意思是
    $$ \hat{Q} \mid f \rangle $$
    的对偶.

- Just as the wave function takes different forms in
  different bases, so do operators.
  The position operator is given by
  $$ \hat{x} \rightarrow x $$
  in the position basis,
  - or
    $$ \hat{x} \rightarrow i \hbar \frac{\partial}{\partial p} $$
    in the momentum basis.
- However, Dirac notation allows us to do away with the arrows
  and stick to equalities. Operators act on kets (for instance,
  $$ \hat{x} \mid S(t) \rangle $$);
  the outcome of this operation can be expressed in any basis
  by taking the inner product with an appropriate basis vector.
  - That is,
  - $$ \langle x \mid \hat{x} \mid S(t) \rangle = $$
    action of position operator in
    $$ x $$
    basis
    $$ = x Ψ(x, t) $$,
  - or
  - $$ \langle p \mid \hat{x} \mid S(t) \rangle = $$
    action of position operator in
    $$ p $$
    basis
    $$ = i \hbar \frac{\partial Φ}{\partial p} $$.
  - In this notation it is straightforward to
    transform operators between bases.

## 三维空间中的量子力学

### 薛定谔方程

- [拉普拉斯算符](https://en.wikipedia.org/wiki/Laplace_operator)

- [伴随勒让德多项式](https://en.wikipedia.org/wiki/Associated_Legendre_polynomials)
  - [勒让德多项式](https://en.wikipedia.org/wiki/Legendre_polynomials)
  - [罗德里格斯公式](https://en.wikipedia.org/wiki/Rodrigues%27_formula)
- [球谐函数](https://en.wikipedia.org/wiki/Spherical_harmonics)
  - [球贝塞尔函数](https://en.wikipedia.org/wiki/Bessel_function#Spherical_Bessel_functions)
- [主量子数](https://en.wikipedia.org/wiki/Principal_quantum_number)

### 氢原子

- [玻尔模型](https://en.wikipedia.org/wiki/Bohr_model)
  - [玻尔半径](https://en.wikipedia.org/wiki/Bohr_radius)
  - [基态](https://en.wikipedia.org/wiki/Ground_state)

- [拉盖尔多项式](https://en.wikipedia.org/wiki/Laguerre_polynomials)

### 角动量

- 一般说来, 粒子的角动量 (相对于原点) 可由下式给出:
  - $$ \mathbf{L} = \mathbf{r} \times \mathbf{p} $$,
  - 也就是,
  - $$ L_x = y p_z - z p_y $$,
    $$ L_y = z p_x - x p_z $$,
    $$ L_z = x p_y - y p_x $$.
  - 对应的量子算符由标准公式
    $$ p_x \rightarrow -i \hbar \partial / \partial x $$,
    $$ p_y \rightarrow -i \hbar \partial / \partial y $$,
    $$ p_z \rightarrow -i \hbar \partial / \partial z $$
    得到.

- [阶梯算符](https://en.wikipedia.org/wiki/Ladder_operator)

### 自旋

- 自旋代数理论是轨道角动量理论的翻版, 从基本的对易关系出发:
  - $$ [S_x, S_y] = i \hbar S_z $$,
    $$ [S_y, S_z] = i \hbar S_x $$,
    $$ [S_z, S_x] = i \hbar S_y $$.
  - 与以前一样,
    $$ S^2 $$
    和
    $$ S_z $$
    的本征矢满足
  - $$
      S^2 \mid s \mbox{ } m \rangle =
      \hbar^2 s (s + 1) \mid s \mbox{ } m \rangle
    $$;
    $$
      S_z \mid s \mbox{ } m \rangle =
      \hbar m \mid s \mbox{ } m \rangle
    $$;
  - 以及
  - $$
      S_± \mid s \mbox{ } m \rangle =
      \hbar \sqrt{s (s + 1) - m(m ± 1)} \mid s \mbox{ } m ± 1 \rangle
    $$,
  - 式中,
    $$ S_± ≡ S_x ± i S_y $$.
    但现在的本征矢不再是球谐函数 (它们根本不是
    $$ θ $$
    和
    $$ ϕ $$
    的函数), 我们也没有任何理由把
    $$ s $$
    和
    $$ m $$
    的半整数值排除在外:
  - $$ s = 0, \frac{1}{2}, 1, \frac{3}{2}, ... $$;
    $$ m = -s, -s+1, ..., s-1, s $$.
- 碰巧的是每个基本粒子都有一个`特定且不变`的
  $$ s $$
  值, 我们称之为特定粒子的`自旋` (spin):
  $$ π $$
  介子的自旋为 `0`, 电子的自旋为 `1/2`, 光子的自旋为 `1`,
  $$ Δ $$
  重子的自旋为 `3/2`, 引力子的自旋为 `2` 等.
  - 相比之下, 轨道角动量量子数
    $$ l $$
    (比如说氢原子中的电子) 可以取任意 (整数) 值,
    当系统受到扰动时, 它们会从一个变化到另一个.
  - 但对于任何给定的粒子而言,
    $$ s $$
    都是固定不变的, 这使得自旋理论相对比较简单.

- 自旋 `1/2` 粒子的一般状态可由二元的列矩阵 (或`旋量`) 表示:
  $$ χ = \binom{a}{b} = a χ_+ + b χ_- $$,
  其中
  - $$ χ_+ = \binom{1}{0} $$
  - 代表自旋向上, 而
  - $$ χ_- = \binom{0}{1} $$
  - 代表自旋向下.

---

- 由于
  $$ S_x $$,
  $$ S_y $$
  和
  $$ S_z $$
  都含有因子
  $$ \hbar / 2 $$,
  $$ S $$
  可以更简洁地写为
  $$ S = (\hbar / 2) σ $$,
  其中
  - $$
      σ_x ≡
      \begin{pmatrix}
        0 & 1 \\
        1 & 0
      \end{pmatrix}
    $$,
  - $$
      σ_y ≡
      \begin{pmatrix}
        0 & -i \\
        i & 1
      \end{pmatrix}
    $$,
  - $$
      σ_z ≡
      \begin{pmatrix}
        1 & 0 \\
        0 & -1
      \end{pmatrix}
    $$.
  - 这就是著名的泡利自旋矩阵. 注意
    $$ S_x $$,
    $$ S_y $$,
    $$ S_z $$
    和
    $$ S^2 $$
    都是厄米矩阵 (因为它们都表示可观测量). 另一方面,
    $$ S_+ $$
    和
    $$ S_- $$
    不是厄米的, 显然它们不是可观测量.
- (当然)
  $$ S_z $$
  的本征旋量是
  - $$ χ_+ = \binom{1}{0} $$,
    本征值为
    $$ + \frac{\hbar}{2} $$;
  - $$ χ_- = \binom{0}{1} $$,
    本征值为
    $$ - \frac{\hbar}{2} $$.
  - 如果对粒子状态
    $$ χ $$
    的
    $$ S_z $$
    值进行测量, 只有这两种可能性:
  - 得到的结果是
    $$ + \hbar / 2 $$,
    几率为
    $$ |a|^2 $$;
    或者是
    $$ - \hbar / 2 $$,
    几率为
    $$ |b|^2 $$,
    则
    $$ |a|^2 + |b|^2 = 1 $$,
    即旋量必须是归一化的.

- 一个带电旋转粒子构成一个磁偶极子. 它的磁偶极矩
  $$ μ $$
  正比于其自旋角动量
  $$ S $$:
  - $$ μ = γS $$,
  - 式中, 比例常数
    $$ γ $$
    称为`旋磁比`.
- 当一个磁偶极子处在磁场
  $$ B $$
  中时, 它受到力矩
  $$ μ \times B $$
  作用, 使得磁偶极子趋于与磁场方向平行 (像指南针一样). 与力矩相关的能量为
  - $$ H = -μ \cdot B $$,
  - 所以静止在磁场
    $$ B $$
    中带电自旋粒子的哈密顿是
  - $$ H = -γ B \cdot S $$,
  - 式中,
    $$ S $$
    是相应的自旋矩阵.

> 群

## 全同粒子

### 双粒子体系

- 量子力学巧妙地适应了原则上不可分辨粒子的存在: 我们只是构造了一个波函数,
  该波函数对于哪个粒子处于哪个状态是不确定的. 实际上有两种不同的构造方法:
  - $$
      ψ_± (r_1, r_2) =
      A [ψ_a(r_1) ψ_b(r_2) ± ψ_b(r_1) ψ_a(r_2)]
    $$;
  - 这个理论将允许两种完全相同的粒子:
    玻色子, 上式取正号; 费米子, 上式取负号.
  - 玻色子是交换对称的,
    $$ ψ_+ (r_1, r_2) = ψ_+ (r_2, r_1) $$;
    费米子是交换反对称的,
    $$ ψ_- (r_1, r_2) = -ψ_- (r_2, r_1) $$;
    碰巧的是,
  - $$
      \begin{cases}
      所有自旋为整数的粒子为玻色子, \\
      所有自旋为半整数的粒子为费米子.
      \end{cases}
    $$
  - 自旋和统计之间的这种联系 (玻色子和费米子具有完全不同的统计性质)
    可以在相对论量子力学中得到证明;
    在非相对论理论中, 只是简单地把它作为一个公理.
- 因此, 两个相同的费米子 (例如, 两个电子) 不能占据相同的状态. 因为如果
  $$ ψ_a = ψ_b $$,
  将有
  - $$
      ψ_- (r_1, r_2) =
      A [ψ_a (r_1) ψ_a (r_2) - ψ_a (r_1) ψ_a (r_2)]
      = 0
    $$,
  - 我们将得不到任何波函数. 这就是著名的`泡利不相容原理`. 这不是
    (正如你可能已经相信的那样) 一个只适用于电子的奇怪的特定假设,
    而是构造两个粒子波函数规则的结果, 适用于所有相同的费米子.

- 在自旋和坐标之间没有耦合的情况下,
  我们可以自由地假设状态在其自旋和空间坐标中是可分离的.
  这只是说, 测量自旋向上的几率与其粒子的位置无关.
  在存在耦合的情况下, 一般状态将采用线性组合的形式:
  - $$ ψ_+ (r) χ_+ + ψ_- (r) χ_- $$.

- 简单起见, 假设粒子之间没有相互作用, 自旋和位置之间没有耦合
  (总态函数是位置函数和自旋函数的乘积), 且势不显含时间.
  但是, 对于全同玻色子/费米子, 基本的对称化/反对称化要求要普遍得多.
  让我们定义`交换算符`
  $$ \hat{P} $$,
  它交换两个粒子:
  - $$ \hat{P} \mid (1, 2) \rangle = \mid (2, 1) \rangle $$
  - 很明显,
    $$ \hat{p}^2 = 1 $$,
    而且
    $$ \hat{p} $$
    的本征值为
    $$ ±1 $$.
  - 现在, 如果两个粒子是全同粒子, 其哈密顿量也是一样的:
    $$ m_1 = m_2 $$,
    $$ V(r_1, r_2, t) = V(r_2, r_1, t) $$.
    因此,
    $$ \hat{P} $$
    和
    $$ \hat{H} $$
    是相容的可观测量,
    $$ [\hat{P}, \hat{H}] = 0 $$,
    且有
    $$ \frac{d \langle \hat{P} \rangle}{dt} = 0 $$.
- 如果系统以
  $$ \hat{P} $$
  的本征态开始, 对称
  ($$ \langle \hat{P} \rangle = 1 $$),
  或者反对称
  ($$ \langle \hat{P} \rangle = -1 $$),
  那么它将会永远处在这个态上.
  - `对称化公理`告诉我们, 对于全同粒子, 状态不但是允许的, 而且必须满足
  - $$ \mid (1, 2) \rangle = ± \mid (2, 1) \rangle $$
  - 式中, 正号为玻色子; 负号对应费米子. 如果有
    $$ n $$
    个全同粒子, 当然, 交换其中任意两个粒子, 状态必须是对称或反对称的:
  - $$
      \mid (1, 2, ..., i, ..., j, ..., n) \rangle =
      ± \mid (1, 2, ..., j, ..., i, ..., n) \rangle
    $$,
  - 这是一般性描述.

## 跋

### 贝尔定理

```
然后, 我们需要区分两种不同类型的影响:
一种是 "因果" 变化, "因果" 变化导致接收器的某些物理特性发生实际变化,
仅通过对该子系统的测量即可检测到;
另一种是 "空灵" 类型, 它不传输能量或信息,
唯一的证据是在两个独立的子系统上采集的数据中的相关性 --
这种相关性从本质上来说, 无法通过单独测量其中一个数据列表所检测到.

因果效应不能传播得比光快, 但没有令人信服的理由说明空灵效应不能传播.
与波函数坍缩相关的影响属于 "空灵" 类型,
它们传播的速度超过光速这一事实可能会令人惊讶, 但这毕竟不是灾难性的.
```

> 类似此段的描述其实随处可见, 但有一个词, 使得此处表述优于它处.
  __因果__~ (比`信息`二字, 往前多迈了很小的一步.)

> `无法通过单独测量其中一个数据列表所检测到`;
  摘录
  [HELGOLAND](https://book.douban.com/subject/36255869/)
  书中的一段话如下:

```
相对我们而言某些事件发生的概率是由相对我们而言的波函数 ψ 的演变确定的,
这一波函数包含了与其他所有系统的动态互动,
但不受相对于其他系统而言发生的事件的影响.

探讨两个距离遥远的, 相互纠缠的物体之间相互交流时出现的表面上的矛盾,
其实是因为忽略了这一事实: 要揭示相关性并赋予其真实性,
必须存在与两个物体共同互动的第三个物体.
表面上的矛盾, 是因为忽略了特性是为某一对象展现的.
两个物体之间的关联性是两个物体之间的特性,
所以也就跟其他所有特性一样, 只有与除此之外的第三个物体关联时才存在.
```

### 混合态和密度矩阵

- 但还有其他方法来阐述该理论, 一个特别有用的方法是从定义`密度算符`开始,
  $$ \hat{ρ} \equiv \mid Ψ \rangle \langle Ψ \mid $$.
  - 它实际上是状态
    $$ \mid Ψ \rangle $$
    上的`投影算符`.
  - 对于一组正交归一基
    $$ \{ \mid e_j \rangle \} $$,
    算符用一个矩阵表示; 矩阵
    $$ A $$
    用于表示算符
    $$ \hat{A} $$,
    其矩阵元
    $$ A_{ij} $$
    是
    $$ A_{ij} = \langle e_i \mid \hat{A} \mid e_j \rangle $$.
- 特别地, `密度矩阵`的矩阵元
  $$ ρ_{ij} $$
  为
  - $$
      ρ_{ij} =
      \langle e_i \mid \hat{ρ} \mid e_j \rangle =
      \langle e_i \mid Ψ \rangle \langle Ψ \mid e_j \rangle
    $$.
- 对于纯态, 密度矩阵有几个有趣的性质:
  - $$ \mathbf{ρ}^2 = \mathbf{ρ} $$,
    (__幂等性__)
  - $$ \mathbf{ρ}^{\dagger} = \mathbf{ρ} $$,
    (__厄米性__)
  - $$ Tr(\mathbf{ρ}) = \sum \mathbf{ρ}_{ii} = 1 $$,
    (`迹`是 `1`)
  - 可观测量
    $$ A $$
    的期望值为
    $$ \langle A \rangle = Tr(\mathbf{ρ} \mathbf{A}) $$.
- 我们可以用密度矩阵代替波函数来表示粒子的状态.

```
不要将两个纯态的线性组合 (其本身仍然是个纯态) 与混合态相混淆,
混合态不能用希尔伯特空间中的任何一个 (单个) 矢量来表示
(希尔伯特空间中两个矢量的和仍是希尔伯特空间中的一个矢量).
```

- 可以简单地列出粒子在每个可能状态
  $$ \mid Ψ_k \rangle $$
  下的几率
  $$ p_k $$.
  一个可观测系统的期望值将是对一个体系的系综上进行测量的平均值,
  这些系综不是事先做好的完全相同的体系 (它们并非都处于相同的状态);
  相反, 它们中的每一部分
  $$ p_k $$
  处于各个 (纯) 态
  $$ \mid Ψ_k \rangle $$
  上:
  - $$
      \langle A \rangle =
      \sum_{k} p_k
      \langle Ψ_k \mid \hat{A} \mid Ψ_k \rangle
    $$.
- 通过推广密度算符, 有一种巧妙的方法来表示这些信息:
  - $$
      \hat{ρ} \equiv \sum_{k} p_k
      \mid Ψ_k \rangle \langle Ψ_k \mid
    $$.
  - 同样, 对一特定基来说, 它变成一个矩阵:
  - $$
      ρ_{ij} =
      \sum_{k} p_k
      \langle e_i \mid Ψ_k \rangle
      \langle Ψ_k \mid e_j \rangle
    $$.
- 密度矩阵包含了我们可以获取的有关系统的所有信息.
  - 同任何几率一样
    $$ 0 ≤ p_k ≤ 1 $$
    且
    $$ \sum_{k} p_k = 1 $$.
- 混合态的密度矩阵保留了前面讨论过的纯态密度矩阵的大多数特性:
  - $$ ρ^{\dagger} = ρ $$,
  - $$ Tr(ρ) = 1 $$,
  - $$ \langle A \rangle = Tr(ρ A) $$,
  - $$ i \hbar \frac{d \hat{ρ}}{dt} = [\hat{H}, \hat{ρ}] $$
    (当对所有的
    $$ k $$,
    有
    $$ \frac{d p_k}{dt} = 0 $$).
- 但
  $$ ρ $$
  只有在表示纯态时才是幂等的:
  - $$ ρ^2 ≠ ρ $$,
  - (事实上, __这是一种快速检验体系状态是否为纯态的方法__.)

- [布洛赫球面](https://en.wikipedia.org/wiki/Bloch_sphere)

## 对称性和守恒律

```
在量子力学中, 我们说一个系统具有对称性时,
是指哈密顿量通过某种形式的变换而保持不变,
比如旋转或平移变换.
```

- 平移算符作用一个函数上并将其移动一段距离
  $$ a $$.
  完成此操作的算符由下式定义:
  - $$ \hat{T}(a) ψ(x) = ψ'(x) = ψ(x - a) $$.
  - 这个符号起初可能会令人感到迷惑; 这个方程表示平移函数
    $$ ψ' $$
    在
    $$ x $$
    处的值等于未平移函数
    $$ ψ $$
    在
    $$ x - a $$
    处的值, 函数本身已向右移动了
    $$ a $$.

---

- 函数通过原点反射对称的算符称一维`宇称算符`, 定义如下:
  - $$ \hat{Π} ψ(x) = ψ'(x) = ψ(-x) $$.
  - 在三维坐标中, 宇称改变所有 3 个坐标的符号:
  - $$ \hat{Π} ψ(x, y, z) = ψ(-x, -y, -z) $$.
- 在极坐标中, 将函数绕
  $$ z $$
  轴旋转
  $$ φ $$
  角的算符自然而然地可表示为
  - $$ \hat{R}_{z} (φ) ψ(r, θ, ϕ) = ψ'(r, θ, ϕ) = ψ(r, θ, ϕ - φ) $$.
- 在二维中, 变换
  $$ ψ'(x, y) = ψ(-x, -y) $$
  与旋转
  $$ 180° $$
  没有区别. 我们仅在一维或三维空间反演变换中使用宇称这一术语,
  $$ \hat{Π} ψ(r) = ψ(-r) $$.

### 变换算符

- $$ \hat{T}(a) $$
  与动量算符密切相关, 可以用动量算符来表示它. 为此, 我们用
  $$ ψ(x - a) $$
  的泰勒级数代替
  $$ ψ(x - a) $$:
  - $$
      \begin{align}
        \hat{T}(a) ψ(x)
        & = ψ(x - a) \\
        & = \sum_{n = 0}^{\infty} \frac{1}{n!} (-a)^n
            \frac{d^n}{dx^n} ψ(x) \\
        & = \sum_{n = 0}^{\infty} \frac{1}{n!}
            (\frac{-ia}{\hbar} \hat{p})^n ψ(x)
      \end{align}
    $$
  - 方程的右边是指数函数, 因此
  - $$ \hat{T}(a) = \exp [- \frac{ia}{\hbar} \hat{p}] $$.
  - 我们说动量是平移算符的`生成元`.

- 思考一下平移一个算符的意义是什么. 平移后算符
  $$ \hat{Q}' $$
  定义为它在未平移状态
  $$ ψ $$
  中的期望值与
  $$ \hat{Q} $$
  在平移状态
  $$ ψ' $$
  中的期望值相同:
  - $$
      \langle ψ' \mid \hat{Q} \mid ψ' \rangle =
      \langle ψ \mid \hat{Q}' \mid ψ \rangle
    $$.
  - 平移对期望值的影响有两种方法可以计算. 我们可以将波函数移动一段距离
    (这称为主动变换); 或者将波函数留在原来的位置,
    把坐标系原点向相反方向移动等同的量 (被动变换). 算符
    $$ \hat{Q}' $$
    是这个移动坐标系中的算符. 所以,
  - $$
      \langle ψ \mid \hat{T}^{\dagger} \hat{Q} \hat{T} \mid ψ \rangle
      = \langle ψ \mid \hat{Q}' \mid ψ \rangle
    $$.
  - 这里, 利用伴算符的定义: 即如果
    $$ \hat{T} \mid f \rangle ≡ \mid Tf \rangle $$,
    那么
    $$ \langle Tf \mid = \langle f \mid \hat{T}^{\dagger} $$.
  - 由此可见
    $$ \hat{Q}' = \hat{T}^{\dagger} \hat{Q} \hat{T} $$.

---

- 如果系统哈密顿量在平移变换下保持不变,
  则系统是`平移不变`的 (等同于说它具有平移对称性):
  - $$ \hat{H}' = \hat{T}^{\dagger} \hat{H} \hat{T} = \hat{H} $$.
  - 由于
    $$ \hat{T} $$
    是幺正的, 方程两端同时乘上
    $$ \hat{T} $$
    得到
  - $$ \hat{H} \hat{T} = \hat{T} \hat{H} $$.
  - 因此, 如果系统哈密顿量与平移算符对易, 则系统具有平移对称性:
  - $$ [ \hat{H}, \hat{T} ] = 0 $$.

- 如果系统具有连续平移对称性, 那么对于选择任意的
  $$ a $$
  值, 系统哈密顿量与
  $$ \hat{T}(a) $$
  都对易. 在这种情况下, 考虑`无限小平移`非常有用
  - $$
      \hat{T} (δ) = e^{-iδ \hat{p} / \hbar}
      ≈ 1 - i\frac{δ}{\hbar} \hat{p}
    $$,
  - 其中
    $$ δ $$
    是一个无限小的长度.
- 如果系统哈密顿量具有连续平移对称性,
  那么它在包括无限小在内的任何平移下都必须保持不变;
  也就是说, 它与平移算符对易, 因此
  - $$
      [\hat{H}, \hat{T} (δ)] =
      [\hat{H}, 1 - i \frac{δ}{\hbar} \hat{p}] = 0
      \Rightarrow
      [\hat{H}, \hat{p}] = 0
    $$.
  - 所以, 如果系统哈密顿量具有连续平移对称性, 它必须与动量对易.
    如果系统哈密顿量与动量对易, 那么按照`广义埃伦菲斯特定理`
  - $$
      \frac{d}{dt} \langle p \rangle =
      \frac{i}{\hbar} \langle [\hat{H}, \hat{p}] \rangle
      = 0
    $$.
  - 这就是`动量守恒`的表述, 现在我们已经证明,
    连续平移对称性意味着系统动量守恒.
    这是得到的第一个非常重要的普遍原理的例子:
    __对称意味着存在守恒定律__.

### 宇称

- 如果系统哈密顿量在宇称变换下保持不变, 则系统具有`反演对称性`:
  - $$ \hat{H}' = \hat{Π}^{\dagger} \hat{H} \hat{Π} = \hat{H} $$,
  - 或者, 利用宇称算符的幺正性,
  - $$ [\hat{H}, \hat{Π}] = 0 $$.
- 若系统哈密顿量描述的是处在一维势场
  $$ V(x) $$
  中质量为
  $$ m $$
  的粒子, 那么, 反演对称性表明势是位置的偶函数:
  - $$ V(x) = V(-x) $$.
  - 反演对称性的含义有两个: 首先, 可以找到
    $$ \hat{Π} $$
    和
    $$ \hat{H} $$
    的一组完备的共同本征态. 把这样的本征态写成
    $$ ψ_n $$;
    则满足
  - $$ \hat{Π} ψ_n(x) = ψ_n(-x) = ± ψ_n(x) $$,
  - 由于宇称算符的本征值必须为
    $$ ±1 $$.
    因此, 若势函数是位置的偶函数, 其定态本身就是偶函数或奇函数
    (或者, 在简并的情况下, 可以这样选择).
  - 这个性质在谐振子, 无限深方势阱 (如果原点位于势阱的中心) 和狄拉克
    $$ δ $$
    函数势中很普遍.
  - 其次, 根据埃伦菲斯特定理, 如果哈密顿量具有反演对称性, 有
  - $$
      \frac{d}{dt} \langle \hat{Π} \rangle =
      \frac{i}{\hbar} \langle [\hat{H}, \hat{Π}] \rangle = 0
    $$.
  - 所以对处于对称势场中的粒子, 其宇称守恒; 不仅是期望值,
    还包括测量中任何给定结果的几率都是守恒的.
    宇称守恒是指若处在谐振子势中的粒子波函数在
    $$ t = 0 $$
    时刻为偶函数, 那么, 在以后的任何时刻
    $$ t $$
    它都将是偶函数.

---

- 三维宇称算符的空间反演是
  - $$ \hat{Π} ψ(r) = ψ'(r) = ψ(-r) $$.
  - 算符
    $$ \hat{r} $$
    和
    $$ \hat{p} $$
    的变换是
  - $$ \hat{r}' = \hat{Π}^{\dagger} \hat{r} \hat{Π} = - \hat{r} $$,
  - $$ \hat{p}' = \hat{Π}^{\dagger} \hat{p} \hat{Π} = - \hat{p} $$.
  - 任意算符变换为
  - $$
      \hat{Q}'(\hat{r}, \hat{p}) =
      \hat{Π}^{\dagger} \hat{Q}(\hat{r}, \hat{p}) \hat{Π} =
      \hat{Q}(- \hat{r}, - \hat{p})
    $$.

- 在三维空间中, 如果势场满足
  $$ V(r) = V(-r) $$,
  则在
  $$ V(r) $$
  中运动的质量为
  $$ m $$
  的粒子的哈密顿量具有反演对称性.
  重要的是, 对任意的中心势场都满足这一条件.
  - 与一维情况一样, 此类系统是宇称守恒的,
    并且哈密顿量的本征态可选为宇称的共同本征态.

- [拉波特定则](https://en.wikipedia.org/wiki/Laporte_rule)

### 旋转对称性

- 正如线动量是平移生成元一样, 角动量也是转动生成元.
  与位置算符转动变换方式相同的任何算符都称为`矢量算符`.
  - `变换方式相同`是指
    $$ V' = DV $$,
    其中
    $$ D $$
    与
    $$ r' = Dr $$
    中的
    $$ D $$
    是同一个矩阵.

- `标量算符`是一个简单的量, 它在转动变换下不变;
  这等同于说标量算符和角动量
  $$ \hat{L} $$
  对易:
  - $$ [\hat{L}_i, \hat{f}] = 0 $$.
  - 现在我们可以根据算符与
    $$ \hat{L} $$
    的对易关系 (它们在转动操作下如何变换) 将算符分为标量算符或矢量算符,
    也可以根据算符与
    $$ \hat{Π} $$
    的对易关系 (它们在宇称操作下如何变换) 将算符分为`真`或赝矢 (标) 量.

---

- __连续旋转对称__ 质量为
  $$ m $$
  的粒子在势场
  $$ V(\mathbf{r}) $$
  中运动,
  - $$ \hat{H} = \frac{\hat{p}^2}{2m} + V(\mathbf{r}) $$,
  - 如果
    $$ V(\mathbf{r}) = V(r) $$
    (中心势), 则哈密顿量具有旋转不变性.
  - 在这种情况下, 哈密顿量与绕任意轴和任意角度的旋转算符都对易:
  - $$ [\hat{H}, \hat{R}_n (φ)] = 0 $$.
  - 特别是, 对`无限小角度`的转动,
  - $$
      \hat{R}_n (φ) ≈
      1 - \frac{iδ}{\hbar} \mathbf{n} \cdot \hat{L}
    $$,
  - 也就是说, 哈密顿量与
    $$ L $$
    的三个分量对易:
  - $$ [\hat{H}, \hat{L}] = 0 $$.
  - 那么, 旋转不变性的结果是什么呢? 对于中心势, 由埃伦菲斯特定理得
  - $$
      \frac{d}{dt} \langle L \rangle =
      \frac{i}{\hbar} \langle [\hat{H}, \hat{L}] \rangle
      = 0
    $$.
  - 因此, __角动量守恒是旋转不变性的结果__.
    角动量守恒还意味着几率分布 (角动量的每个分量) 与时间无关.

### 简并

### 旋转对称选择定则

### 时间变换

- 在本书中, 我们一直是在薛定谔绘景中讨论问题,
  狄拉克之所以这样命名, 是因为它是薛定谔本人心目中的绘景.
  在薛定谔绘景中, 波函数根据薛定谔方程随时间演化:
  - $$
      \hat{H} Ψ(x, t) =
      i \hbar \frac{\partial}{\partial t} Ψ(x, t)
    $$.
  - 算符
    $$ \hat{x} = x $$
    和
    $$ \hat{p} = -i \hbar \partial_{x} $$
    本身和时间无关, 期望值 (或者更一般地说, 矩阵元)
    对时间依赖性来自波函数对时间依赖性:
  - $$
      \langle \hat{Q} \rangle =
      \langle Ψ(t) \mid \hat{Q} \mid Ψ(t) \rangle
    $$.
  - 在海森伯绘景中, 波函数不随时间改变,
    $$ Ψ_H(x) = Ψ(x, 0) $$,
    算符随时间演化. 在海森伯绘景中, 期望值 (或矩阵元)
    对时间依赖性由算符来体现.
  - $$
      \langle \hat{Q} \rangle =
      \langle Ψ_H \mid \hat{Q}_{H}(t) \mid Ψ_H \rangle
    $$.
  - 当然, 两个绘景是完全相同的, 因为
  - $$
      \langle Ψ(t) \mid \hat{Q} \mid Ψ(t) \rangle =
      \langle Ψ(0) \mid
        \hat{U}^{\dagger} \hat{Q} \hat{U}
      \mid Ψ(0) \rangle =
      \langle Ψ_H \mid \hat{Q}_{H}(t) \mid Ψ_H \rangle
    $$.

```
对这两个绘景做一个很好的类比.
对普通的时钟, 指针顺时针方向移动, 而表盘数字固定不动.
但人们同样可以设计一个指针固定, 表盘数字逆时针移动的时钟.
若让指针代表波函数和表盘数字代表算符,
这两个时钟之间的对应关系大致相当于薛定谔绘景和海森伯绘景之间的对应关系.
还可以介绍其他的一些绘景, 其中时钟指针和表盘上的数字都以中间速率运动,
这样的时钟仍能显示正确的时间.
```

- __时间平移不变性__ 如果哈密顿量是含时的,
  我们仍然可以利用时间平移算符
  $$ \hat{U} $$
  写出薛定谔方程的形式解,
  - $$ Ψ(x, t) = \hat{U}(t, t_0) Ψ(x, t_0) $$,
  - 但
    $$ \hat{U} $$
    不再采用简单形式. 对于无穷小的时间间隔
    $$ δ $$
  - $$
      \hat{U}(t_0 + δ, t_0) ≈
      1 - \frac{i}{\hbar} H(t_0) δ
    $$.
- `平移不变性`意味着时间演化与我们考虑的时间间隔无关. 换句话说, 对于选择任意的
  $$ t_1 $$
  和
  $$ t_2 $$,
  - $$ \hat{U} (t_1 + δ, t_1) = \hat{U} (t_2 + δ, t_2) $$,
  - 这确保了如果体系在
    $$ t_1 $$
    时刻从状态
    $$ \mid α \rangle $$
    出发, 经过一段时间
    $$ δ $$
    到达状态
    $$ \mid β \rangle $$,
    和体系在
    $$ t_2 $$
    时刻从状态
    $$ \mid α \rangle $$
    出发, 经过一段时间
    $$ δ $$
    回到相同状态
    $$ \mid β \rangle $$
    是一样的.
  - 比如, 假设实验条件相同, 周四的实验应该与周二的相同.
    结合上述两式, 可以看到这个结论成立的条件是
    $$ \hat{H}(t_1) = \hat{H}(t_2) $$,
    且既然这对所有的
    $$ t_1 $$
    和
    $$ t_2 $$
    都成立, 所以哈密顿量必须是不含时的 (时间平移不变性成立):
  - $$ \frac{\partial \hat{H}}{\partial t} = 0 $$.
  - 这种情况下, 广义埃伦菲斯特定理给出
  - $$
      \frac{d}{dt} \langle \hat{H} \rangle =
      \frac{i}{\hbar} \langle [ \hat{H}, \hat{H} ] \rangle +
      \langle \frac{\partial \hat{H}}{\partial t} \rangle = 0
    $$.
  - 因此, __能量守恒是时间平移不变性的结果__.

## 定态微扰理论

> 从此处开始, 后续属于应用部分, 选择性略读~

- 首先, 把新的系统哈密顿量写成两项之和:
  - $$ H = H^0 + λH' $$,
  - 式中,
    $$ H' $$
    是微扰项 (上标
    $$ 0 $$
    总是表示未微扰的物理量).
  - 开始, 将
    $$ λ $$
    取为一个很小的数; 稍后我们将它调大到
    $$ 1 $$,
    $$ H $$
    是真实系统的哈密顿量. 然后, 把
    $$ ψ_n $$
    和
    $$ E_n $$
    展开为
    $$ λ $$
    的幂级数形式:
  - $$ ψ_n = ψ_n^0 + λ ψ_n^1 + λ^2 ψ_n^2 + ... $$;
  - $$ E_n = E_n^0 + λ E_n^1 + λ^2 E_n^2 + ... $$.
  - 这里,
    $$ E_n^1 $$
    为第
    $$ n $$
    个本征值的`一阶修正`,
    $$ ψ_n^1 $$
    为第
    $$ n $$
    个本征函数的`一阶修正`;
    $$ E_n^2 $$
    和
    $$ ψ_n^2 $$
    分别为相应的`二阶修正`, 以此类推.

### 非简并微扰理论

- $$ E_n^1 = \langle Ψ_n^0 \mid H' \mid Ψ_n^0 \rangle $$
  (能量一阶修正)
  - 这就是一阶微扰理论最基本的结论;
    实际上, 它很可能是量子力学中最常用的方程.
  - 它说明能量的一阶修正对应于在未微扰状态下微扰项的期望值.
- $$
    ψ_n^1 = \sum_{m ≠ n}
    \frac{\langle ψ_m^0 \mid H' \mid ψ_n^0 \rangle}{(E_n^0 - E_m^0)}
    ψ_m^0
  $$
  (波函数一阶修正)
  - 注意到只要未微扰情况下能级是非简并的, 上式的分母就不为零 (因为不存在
    $$ m = n $$
    的系数).
  - 但如果两个未微扰状态具有相同的能量,
    我们将会遇到很大的麻烦 (得到的分母为
    $$ 0 $$);
    在这种情况时, 需要有一个`简并微扰理论`.

### 简并微扰理论

- "好"态定理: 设一厄米算符
  $$ A $$
  分别和
  $$ H^0 $$,
  $$ H' $$
  对易. 如果
  $$ ψ_a^0 $$
  和
  $$ ψ_b^0 $$
  ($$ H^0 $$
  的简并本征函数) 同样也是
  $$ A $$
  的不同本征值的本征函数,
  - $$ A ψ_a^0 = μ ψ_a^0 $$,
    $$ A ψ_b^0 = ν ψ_b^0 $$,
    且
    $$ μ ≠ ν $$,
  - 因此,
    $$ ψ_a^0 $$
    和
    $$ ψ_b^0 $$
    是微扰理论可以使用的"好"态.

## 变分原理

- 假设你想计算由哈密顿量
  $$ H $$
  描述的系统的基态能量
  $$ E_{gs} $$,
  但你又无法直接求解 (不含时) 薛定谔方程. 变分原理将给出一个
  $$ E_{gs} $$
  的上限, 有时候这是你所需要的; 而且如果你足够熟练的话,
  这个上限通常会非常接近精确值. 它的原理是: 任意选择归一化函数
  $$ ψ $$,
  有
  - $$ E_{gs} ≤ \langle ψ \mid H \mid ψ \rangle ≡ \langle H \rangle $$.
  - 也就是说, 处于 (可能是不正确的) 状态
    $$ ψ $$
    下
    $$ H $$
    的期望值一定会高估基态能量.
  - 当然, 如果
    $$ ψ $$
    恰好是其中的一个激发态, 那么显然
    $$ \langle H \rangle $$
    高于
    $$ E_{gs} $$;
    关键是对无论选取任何的波函数
    $$ ψ $$,
    这一点都适用.

- 变分原理非常有用, 而且使用起来非常简单.
  物理化学家们如果想要找到一些复杂分子的基态能量,
  只需写下含有大量可调参数的尝试波函数, 计算
  $$ \langle H \rangle $$,
  然后调整参数就可以得到能量可能的最小值. 即使
  $$ ψ $$
  与真实的波函数几乎没有相似之处, 通常你得到的
  $$ E_{gs} $$
  值也可以达到不可思议的精确.
  - 当然, 如果你能猜出一个真实的
    $$ ψ $$,
    那样就更好了.
  - 该方法存在的唯一问题是, 你永远无法知道你离目标有多近,
    所能确定的就是你只能得到它的一个上限.
    此外, 目前这种方法仅适用于基态问题.

## WKB 近似

- WKB 方法的基本思想是: 假设能量为
  $$ E $$
  的粒子穿过势能
  $$ V(x) $$
  的区域, 其中
  $$ V(x) $$
  为常量. 当
  $$ E > V $$
  时, 则波函数的形式为
  - $$ ψ(x) = Ae^{±ikx} $$,
    且
    $$ k ≡ \sqrt{2m(E - V)} / \hbar $$.
  - 正号表示粒子向右运动, 而负号表示它向左运动
    (当然, 通解是这两项的线性组合).
  - 波函数是振荡的, 波长固定
    ($$ λ = 2π / k $$),
    振幅
    ($$ A $$)
    不变. 现在假设
    $$ V(x) $$
    不再是常数, 但与
    $$ λ $$
    相比变化相当缓慢, 因此在包含许多波长的区域中, 势可以认为`基本上`是不变的.
  - 这样, 除了波长和振幅随
    $$ x $$
    缓慢地变化外, 可以合理地假设
    $$ ψ $$
    实际上仍然保持正弦形式.
    这就是 WKB 近似灵感的来源. 事实上, 它将对
    $$ x $$
    的依赖问题分为两种不同层次: 快速振荡, 由振幅和波长逐渐变化的调制.
- 同理, 当
  $$ E < V $$
  (其中
  $$ V $$
  为常量) 时,
  $$ ψ $$
  为指数形式:
  - $$ ψ(x) = A e^{±kx} $$,
    且
    $$ k ≡ \sqrt{2m(V - E)} / \hbar $$.
  - 如果
    $$ V(x) $$
    不是常量, 但
    $$ V(x) $$
    相比
    $$ 1/k $$
    变化十分缓慢, 除了
    $$ A $$
    和
    $$ k $$
    是随
    $$ x $$
    缓慢变化的函数外, 其解实际上仍然是指数形式.
- 现在,
  $$ V(x) $$
  仍然有一处使整个方法不能适用的地方, 这就是经典`转折点`的附近, 此处
  $$ E ≈ V $$.
  这里
  $$ λ $$
  (或者
  $$ 1/k $$)
  趋于无穷大, 相比之下
  $$ V(x) $$
  就很难说是"缓慢地"变化.
  - 恰当地处理转折点问题将是 WKB 近似最困难的一个方面,
    尽管最终的结果很简洁且易于实现.

## 散射

- 薛定谔方程的积分形式是
  - $$ ψ(r) = ψ_0 (r) + \int g(r - r_0) V(r_0) ψ(r_0) d^3 r_0 $$,
  - 其中
    $$ ψ_0 $$
    为入射波,
  - $$ g(r) ≡ - \frac{m}{2π \hbar^2} \frac{e^{ikr}}{r} $$
  - 是格林函数 (方便起见, 这里合并了因子
    $$ 2m / \hbar^2 $$),
    $$ V $$
    是散射势. 简略地表示为
  - $$ ψ = ψ_0 + \int gV ψ $$.
  - 取此式为
    $$ ψ $$
    的表达式, 并将其代入积分符号中:
  - $$ ψ = ψ_0 + \int gV ψ_0 + \int \int gV gV ψ $$.
  - 重复迭代该过程, 可得到
    $$ ψ $$
    的级数是
  - $$
      ψ = ψ_0 + \int gV ψ_0 + \int \int gV gV ψ_0
        + \int \int \int gV gV gV ψ_0 + ...
    $$.
  - 在每个被积函数中, 只出现入射波函数
    ($$ ψ_0 $$)
    和越来越多的
    $$ gV $$
    幂次项. 一阶玻恩近似就是该级数在第二项后截断;
    除此之外, 现在我们十分清楚如何生成高阶修正了.
- 玻恩级数可以理解为, 零阶波函数
  $$ ψ $$
  不受散射势的影响; 一阶波函数是被势`踢`一次, 然后向某个新的方向`传播`出去;
  二阶波函数则是先被势`踢`一次后, 传播到某个位置,
  再次被势`踢`一次, 然后沿着某个新方向传播出去; 以此类推.
  - 从这个角度来说, 格林函数有时被称为`传播子`,
    它告诉你微扰是如何在相邻两次相互作用之间传播的.
  - 玻恩级数是相对论量子力学费曼表述形式的灵感来源,
    它完全用由`顶点因子` (V) 和传播子 (g) 连接在一起的`费曼图`表示.

## 量子动力学

## 附录 线性代数

```
A vector space with an inner product is called
an inner product space.
```

- [柯西-施瓦茨不等式](https://en.wikipedia.org/wiki/Cauchy-Schwarz_inequality)

> 注: 本书原本用`上面加一个波浪号`表示转置矩阵, 一律改为
  $$ \mathbf{A}^T $$

- 厄米共轭矩阵, 或称`伴随`矩阵, 用
  $$ \mathbf{T}^{\dagger} $$
  表示, 是转置共轭矩阵.

- 如果一个方矩阵等于它的厄米共轭, 则它就是`厄米`矩阵, 或`自伴`矩阵;
  如果厄米共轭引入一个负号, 则矩阵为斜厄米矩阵, 或`反厄米`.
  - 厄米矩阵:
    $$ \mathbf{T}^{\dagger} = \mathbf{T} $$;
  - 反厄米矩阵:
    $$ \mathbf{T}^{\dagger} = - \mathbf{T} $$.

- 一般来说, 矩阵乘法不是可交换的 (即
  $$ \mathbf{S} \mathbf{T} ≠ \mathbf{T} \mathbf{S} $$),
  这两种次序之间所产生差别称为`对易子`:
  - $$ [\mathbf{S}, \mathbf{T}] = \mathbf{S} \mathbf{T} - \mathbf{T} \mathbf{S} $$.
- 两个矩阵积的转置矩阵是两个矩阵分别转置按逆次序的乘积:
  - $$ (\mathbf{S} \mathbf{T})^{T} = \mathbf{T}^{T} \mathbf{S}^{T} $$.
  - 厄米共轭矩阵同样也是这样的:
  - $$
      (\mathbf{S} \mathbf{T})^{\dagger} =
      \mathbf{T}^{\dagger} \mathbf{S}^{\dagger}
    $$.

---

- 没有逆矩阵的矩阵称为`奇异`矩阵.
  两个矩阵积的逆 (假设存在) 是各自逆矩阵按逆次序的乘积:
  - $$ (\mathbf{S} \mathbf{T})^{-1} = \mathbf{T}^{-1} \mathbf{S}^{-1} $$.
- 如果矩阵的逆等于它的厄米共轭, 则该矩阵是`幺正`矩阵:
  - 幺正矩阵:
    $$ \mathbf{U}^{\dagger} = \mathbf{U}^{-1} $$.
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
  $$ Tr(\mathbf{T}) \equiv \sum_{i=1}^{m} \mathbf{T}_{ii} $$,
  具有如下性质:
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

- 矩阵的`特征方程`: 它的解决定了矩阵本征值. 注意到它是一个
  $$ n $$
  阶方程, 根据代数基本定理, 所以它有
  $$ n $$
  个 (复数) 根.
  - 然而, 其中一些可能是重根, 所以我们可以肯定地说, 一个
    $$ n \times n $$
    矩阵至少有一个且最多有
    $$ n $$
    个不同的本征值.
  - 矩阵所有本征值的集合称为它的`谱`;
    如果两个 (或更多) 线性无关的本征矢有相同的本征值, 则称谱线是`简并`的.

> 注: 原书此处翻译为`根据线性代数基本定理`, 是个错误!
  应为`根据代数基本定理`.

- 将矩阵转化为对角形式有一个明显的优势: 很容易处理问题.
  遗憾的是, 并不是每一个矩阵都能对角化 --
  __本征矢量必须张开整个空间__.
  - 如果特征方程有
    $$ n $$
    个不同的根, 那么矩阵肯定是可对角化的, 即使是有多个重根,
    矩阵也可能是可对角化的.
- 在计算出所有本征矢之前, 事先知道给定的矩阵是否可对角化是很方便的. 一个有用的充分
  (尽管不是必要) 条件是: 如果矩阵与其厄米共轭对易, 则称其为`正规`矩阵:
  - 正规矩阵:
    $$ [\mathbf{N}^{\dagger}, \mathbf{N}] = 0 $$.
- 每个正规矩阵都是可对角化的 (其本征矢张开整个空间). 特别是,
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

```
Suppose we have two diagonalizable matrices;
in quantum applications, the question often arises:
Can they be simultaneously diagonalized
(by the same similarity matrix S)?

That is to say, does there exist a basis all of
whose members are eigenvectors of both matrices?
On this basis, both matrices would be diagonal.

The answer is yes if and only if the two matrices commute,
as we shall now prove. (By the way,
if two matrices commute with respect to one basis,
they commute with respect to any basis.)
```

- 在量子力学中, 厄米变换起着基础作用.
  厄米变换的本征值和本征矢有如下重要特性.
  - 厄米变换的本征值是实的
  - 厄米变换属于不同本征值的本征矢彼此正交
  - 更多特性参见:
    [厄米矩阵](https://en.wikipedia.org/wiki/Hermitian_matrix)

- [矩阵函数](https://en.wikipedia.org/wiki/Analytic_function_of_a_matrix)

