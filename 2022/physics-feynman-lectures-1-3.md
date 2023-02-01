---
title: 费曼物理学讲义 (卷一) 下
description: 青泥何盘盘! 百步九折萦岩峦. 扪参历井仰胁息, 以手抚膺坐长叹.
date: 2022-05-14
---

## 气体分子动理论

```
任何一个企图分析实际问题中物质性质的人, 可能都想从写出基本方程式出发,
然后再从数学上求出它们的解. 虽然有一些人试图采用这一条途径,
但他们都是这个领域中的失败者; 真正的成功来自那些从物理观点出发考虑的人,
他们对于要做的事情具有大致的概念, 并且在给定的复杂状况下知道哪些是重要的,
哪些是次要的, 然后开始作正确的近似. 这些问题是如此复杂,
即使获得那种不精确和不完全的初步理解也是很有价值的,
因此在整个物理课程中, 我们将一再碰到这个课题, 而且一次比一次更为准确.
```

```
分子沿所有方向运动的机会是相等的, 不过我们怎样来表示这一点呢?
当然, 它们不可能沿某一特定方向运动, 因为某一特定方向过于严格,
所以我们必须说每单位"某某". 我们的概念是在以碰撞点为中心的球面上,
通过任何一块面积的分子数正好等于通过在球面上任何其他相等面积的分子数.
因而碰撞的结果将使分子的方向这样分布,
使得球面的每个相等的面积有相同的分子通过.
```

- 计算每秒钟施加给活塞的动量是不难的, 我们可以分两步来求:
- 首先, 找出一个特定的原子在和活塞的一次碰撞中传给活塞的动量,
  然后, 再乘上每秒钟原子与活塞壁发生碰撞的次数.
  - 力就是这两个因子的乘积.
- 现在我们来看看两个因子是怎样的:
  - 首先, 我们假定活塞对原子来说是一个理想的"反射体",
    否则, 整个理论就是错误的, 活塞将开始变热, 事情将发生变化.
- 但是最后, 当平衡建立后, 总的效果是碰撞仍是有效的完全弹性碰撞.
  - 平均而言, 每个粒子飞来和离开时都带有相同的能量.
  - 我们想象气体处在稳定的状态下, 并且由于活塞静止不动,
    所以对于活塞我们没有损耗能量.
  - 在这种情况下, 如果某一质量的粒子以一定的速率飞来,
    它也以同样的质量和同样的速率离开.
- 如果原子的速度为 `v`, `v` 的 `x` 分量为
  $$ v_x $$,
  则"入射"粒子动量的 `x` 分量为
  $$ m v_x $$;
  - "出射"粒子动量的分量和它相等, 这样,
    粒子在一次碰撞中施加给活塞的总动量是
    $$ 2 m v_x $$,
    因为这个粒子是被"反射"回来的.

---

- 离活塞太远, 那么在时间 `t` 内只能向着活塞跑过一段路程, 而不能到达活塞.
  - 非常清楚, 只有离活塞的距离在
    $$ v_x t $$
    之内的那些分子, 才会在时间 `t` 内打在活塞上.
  - 因而在时间 `t` 内的碰撞次数等于在距离为
    $$ v_x t $$
    内的区域里的原子数, 并且由于活塞的面积是 `A`,
    所以能在时间 `t` 内碰到活塞的原子所占有的体积是
    $$ v_x t A $$.
  - 但是碰撞到活塞的原子数等于这个体积乘以单位体积的原子数, 即为
    $$ n v_x t A $$.
  - 当然, 我们并不要求时间 `t` 内的碰撞次数, 而是每秒钟的碰撞次数,
    因而只要除以时间 `t`, 就得到
    $$ n v_x A $$
    (这个时间 `t` 可以很短; 如果我们觉得需要更精确一些,
    可以称它为 `dt`, 然后再求微商, 但结果是相同的).
- 这样, 我们求得力为
  - $$ F = n v_x A · 2 m v_x $$.
    (`39.3`)
  - 可见, 若保持粒子密度不变, 而改变面积, 则力与面积成正比. 于是压强为
  - $$ P = 2 n m v_x^2 $$.
    (`39.4`)
- 不过我们注意到在这个分析中有一些小小的麻烦:
  - 首先, 并非所有分子都具有同样的速度,
    而且它们并不都以同样的方向运动.
  - 因而, 所有这些
    $$ v_x^2 $$
    项都不相同!
  - 因为每个分子都有它自己的贡献, 所以,
    我们要做的自然是对这些
    $$ v_x^2 $$
    取平均.
- 即我们要求的是
  $$ v_x $$
  平方对所有分子的平均值
  - $$ P = n m \langle v_x^2 \rangle $$.
    (`39.5`)
  - 这里我们是不是忘了写上因子 `2`?
  - 不, 在所有的原子中, 只有一半是朝着活塞跑的,
    另一半朝着相反的方向运动.
  - 对正的
    $$ v_x $$,
    $$ v_x^2 $$
    的平均值等于对所有
    $$ v_x $$
    所求平均值的一半.
- 当原子向四面八方运动时, 显然在`"x 方向"`上没有什么特殊之处;
  原子同样可以上下, 左右, 前后地运动.
  - 因此在运动过程中, 表征原子在一个方向上平均运动的
    $$ \langle v_x^2 \rangle $$
    值和在其他两个方向上的平均值全都相等

$$
\langle v_x^2 \rangle =
\langle v_y^2 \rangle =
\langle v_z^2 \rangle
$$.
(`39.6`)

- 因此, 只要稍微用一点点数学技巧就可看出, 每一项等于这三项总和的三分之一,
  而这三项之和当然就是速率的平方

$$
\langle v_x^2 \rangle =
\frac{1}{3} \langle v_x^2 + v_y^2 + v_z^2 \rangle =
\frac{\langle v^2 \rangle}{3}
$$.
(`39.7`)

- 这个式子的方便之处在于我们毋须考虑任何特殊的方向, 于是,
  可把压强公式重新写为

$$
P = (\frac{2}{3}) n
\langle \frac{m v^2}{2} \rangle
$$.
(`39.8`)

- 把最后一个因子写成
  $$ \langle m v^2 / 2 \rangle $$
  是因为这是一个分子的质心运动的动能. 由此我们得出

$$
PV = N (\frac{2}{3})
\langle \frac{m v^2}{2} \rangle
$$.
(`39.9`)

- 如果我们知道速率, 用这个公式就可计算出压强有多大.

---

- 举一个十分简单的例子, 我们考虑氦气或其他任何气体,
  例如水银蒸气, 足够高温度下的钾蒸气或氩气,
  其中所有分子都是单原子分子, 对这些单原子分子,
  我们可以假定在分子中没有内部运动.
  - 如果是复杂的分子, 其中就可能存在某些内部运动,
    相互间的振动, 等等.
  - 假设我们忽略这些运动
    (实际上, 这些运动是很重要的, 以后我们再回过头来考虑);
    这样做还是可行的.
- 由于我们假定原子内部的运动可以不考虑,
  质心运动的动能就是分子所具有的全部能量.
  所以, 对于单原子气体, 动能就是总能量.
  - 通常我们称 `U` 为总能量
    (有时也称 `U` 为总内能.
    我们或许会感到奇怪, 因为对气体来说, 并没有外能),
    它就是在气体中, 或无论什么东西中所有分子的全部能量.
  - 我们假设单原子气体的总能量 `U` 等于原子数乘以每个原子的平均动能,
    因为我们不考虑原子内部任何可能的运动或激发.
  - 于是, 在这些条件下, 我们有
  - $$ PV = \frac{2}{3} U $$.
    (`39.10`)

---

- 为了略微更普遍一些, 虽则我们仍然对气体作某些十分特殊的假设,
  我们将不写
  $$ PV = 2U / 3 $$,
  而写
  - $$ PV = (\gamma - 1) U $$.
    (`39.11`)
  - 按照习惯, 把它写成
    $$ (\gamma - 1) $$
    乘以 `U`, 因为在以后处理的少数其他情况中,
    `U` 前面的因子不是 `2/3`, 而是其他的数值.
  - 所以, 为了更一般起见, 我们称它为
    $$ (\gamma - 1) $$,
    因为人们已经这样称呼了近一百年了.
  - 对于像氦这样的单原子气体, 因为 `(5/3 - 1)` 是 `2/3`, 所以
    $$ \gamma $$
    等于 `5/3`.
- 我们已经注意到, 压缩气体时所做的功是 `-PdV`.
  既不加入热能也不取走热能的压缩过程称为绝热压缩.
  - ("绝热"这个词在物理中有几种不同的用法,
    有时很难看出它们之间有什么共同含义.)
  - 这就是说, 对于绝热压缩, 所作的全部功都转变为内能.
  - 没有其他能量损失 -- 这就是关键,
    因而我们有
    $$ PdV = -dU $$.
  - 但因
    $$ U = PV / (\gamma - 1) $$,
    可得
  - $$ dU = \frac{PdV + VdP}{\gamma - 1} $$.
    (`39.12`)
- 因而我们有
  $$ PdV = -(PdV + VdP) / (\gamma - 1) $$,
  或者整理一下, 得
  - $$ \gamma PdV = - VdP $$
  - 或
    $$ \frac{\gamma dV}{V} + \frac{dP}{P} = 0 $$.
    (`39.13`)
- 幸运的是, 假定
  $$ \gamma $$
  是常数 (比如对单原子气体),
  我们就能进行积分: 即
  $$ \gamma ln V + ln P = ln C $$,
  这里 `C` 是积分常数.
  - 对两边取指数, 就得到定律
  - $$ PV^{\gamma} = C (常数) $$.
    (`39.14`)
- 换句话说, 在绝热条件下, 在气体的压缩过程中, 由于没有热量流失,
  因而温度升高, 对单原子气体来说, 压强乘以体积的 `5/3` 次方是一个常数!
  - 虽然我们是从理论上推出这个结论的, 但事实上,
    单原子气体在实验上的表现也是如此.

---

- 而光子具有一定的动量 `p` (当我们学习分子动理论时, 会一再遇到麻烦:
  `p` 既是压强, 又是动量; `v` 既是体积, 又是速度;
  `T` 既是温度, 又是动能, 时间或者力矩;
  我们必须保持警惕).
  - 这里 `p` 是动量, 是矢量.
  - 按照与前面相同的分析, 正是矢量 `p` 的 `x` 分量产生"反冲"的,
    矢量 `p` 的 `x` 分量的两倍是在反冲中给出的动量.
  - 于是
    $$ 2 p_x $$
    代替了
    $$ 2 m v_x $$,
    而在计算碰撞次数时,
    $$ v_x $$
    仍为
    $$ v_x $$,
    这样当我们继续采取以前的所有步骤后,
    发现式 (`39.4`) 中的压强可用下式来代替
  - $$ P = 2n p_x v_x $$.
    (`39.15`)
- 在作平均时, 它变为 `n` 乘以
  $$ p_x v_x $$
  的平均值 (因子 `2` 的情况同上),
  最后计入另外两个方向, 我们求得
  - $$ PV = \frac{N}{3} \langle p \cdot v \rangle $$.
    (`39.16`)
- 此式与 (`39.9`) 相符, 因为动量是 `mv`; 只是它稍微更一般些, 如此而已.
  - 总之, 压强乘体积等于原子总数乘
    $$ (p \cdot v) / 3 $$
    的平均值.
- 对光子来说,
  $$ p \cdot v $$
  是什么?
  - 动量与速度方向相同, 而速度就是光速,
    所以这就是每个光子的动量与光速的乘积.
  - 每个光子的动量乘光速是它的能量:
    $$ E = pc $$,
    因而这些项就是每个光子的能量, 当然,
    我们应当取光子的平均能量乘光子数.
  - 这样, `PV` 的乘积是气体中能量的三分之一
  - $$ PV = \frac{U}{3} (光子气体) $$.
    (`39.17`)
- 于是, 对光子来说, 由于前面的系数是 `1/3`, 即在式 (`39.11`) 中的
  $$ (\gamma - 1) $$
  是 `1/3`, 所以
  $$ \gamma = 4/3 $$,
  因而我们发现容器内的辐射满足规律
  - $$ PV ^ {4/3} = C (常数) $$.
    (`39.18`)
- 从而我们知道了辐射的压缩性! 这就是用在分析恒星上辐射压强贡献的关系式.
  这也是我们算出辐射压强的方法, 它也表示当我们压缩光子气体时,
  压强是怎样变化的.
  - 瞧, 多么奇妙的事情我们也都能处理!

---

- 当然, 现在我们可以把温度的定义代入式 (`39.9`) 中,
  从而找到气体压强与温度之间的函数关系:
  - 即压强乘体积等于原子总数乘以普适常数 `k` 再乘以温度
    $$ PV = NkT $$.
    (`39.22`)
- 而且, 在同样的温度, 同样的压强与同样的体积下, 原子数是确定的;
  这也是一个普适常数! 所以, 根据牛顿定律, 在同样的温度和同样的压强下,
  相同体积的不同气体中具有相同的分子数.
  - 这是一个令人惊异的结论!

---

- 关于质心运动平均动能的定理是普遍的:
  当把任何物体考虑为一个整体时, 无论是否有力存在,
  在这个物体的每个独立的运动方向上, 其平均动能都是 `kT / 2`.
  - 这些"独立的运动方向"有时也称为系统的自由度.
- 由
  $$ \gamma $$
  个原子组成的分子的自由度数是
  $$ 3 \gamma $$,
  因为每个原子都需要有三个坐标来确定它的位置.
  - 分子的总动能既可以表示为各个原子的动能的和,
    也可以表示为质心运动的动能与内部运动的动能之和,
    后者有时可以表示为分子转动动能与振动动能之和,
    但这是一个近似.
- 把我们的定理应用到
  $$ \gamma $$
  个原子的分子时表明, 分子平均动能将是
  $$ 3 \gamma kT / 2 $$,
  其中
  $$ 3 kT / 2 $$
  是整个分子的质心运动的动能, 其余的
  $$ 3 (\gamma - 1) kT / 2 $$
  则是分子内部的振动与转动动能.

## 统计力学原理

## 布朗运动

## 分子动理论的应用

## 扩散

## 热力学定律

## 热力学示例

## 棘轮和掣爪

```
这样我们就必须讲一下无序是什么意思, 有序又是什么意思.
这不是什么有序合我们的意, 无序不合我们意的问题.
在上节所提到的例子中, 混合与不混合的差别如下:
假设我们把空间划分成许多小体积元.
如果将白分子和黑分子分布在这些体积元中, 并使白分子分布在一边,
黑分子分布在另一边, 试问有几种这样的分布方式?
另一方面, 如果对黑白分子分布到哪里不加任何限制, 又有多少种分布方式?
显然, 在后一种情况下的排列方式要多得多,
我们以在从外部看来完全一样的条件下,
内部可能有的排列方式的数目来作为"无序"的量度.
这种排列方式的数目的对数就是熵.
在黑白分子分开的情况下, 排列方式的数目较少, 故熵较小, 或"无序性"较小.
```

```
这样, 有了上面对无序的术语上的定义, 我们就可以理解这个命题.
第一, 熵是无序的量度. 第二, 宇宙总是从"有序"变到"无序", 所以熵总是增加的.
"有序"并不是指我们所喜欢的排列这个意义的有序,
而是指从外部看来完全一样的条件下所具有的内部不同排列方式的数目是相当有限的.
在把气体混合的影片倒过来放的情况下, 并没有我们所想象的那么多的无序.
每个单个原子都恰好以正确的速率和方向出现. 熵并不像表面上看来那么大.
```

```
就我们所知, 所有的物理学基本定律, 像牛顿方程那样, 都是可逆的.
那么不可逆性究竟是从哪里来的呢? 它是从有序变到无序时产生的,
但是在我们知道有序性的起源以前, 我们并不理解这一点.
为什么我们自己每天所发现的情况总是不处在平衡态呢?
有一个可能的解释如下. 我们不妨再来看一下黑白分子混合的箱子.
如果我们等待足够长的时间, 大多数白分子都在一边,
大多数黑分子都在另一边的分布情况, 虽然总的讲是不大可能的,
但偶尔或许仍是可能的. 此后, 随着时间的推移,
连续不断地出现一些偶然事件, 它们又重新混合起来.
```

## 声, 波动方程

## 拍

## 波模

## 谐波

## 波

```
虽然我们已经完成了关于波的定量分析, 但是为了对与波有关的种种现象作一些定性的介绍,
我们增添了这一章. 由于这些现象太复杂, 在这里不能作详细的分析.
既然我们已经用了好几章篇幅来讨论波,
这一章的标题应该叫做"与波有关的一些较为复杂的现象"才更为恰当.
```

```
顺便提一下, 虽然我们认为要发声就必须有一个声源, 但非常有趣的是,
在介质中一旦物体运动得比声速快, 就会发出声音. 也就是说,
声音不一定具有某种纯音的振动特征. 任何一个穿过介质而运动的物体,
当它的速率大于波在介质中传播的速率时, 将自动地从运动本身向各个方向发出波.
这一现象对声音来讲很简单, 但是对光来说也会发生这种现象.

最初人们认为或许没有什么东西能够运动得比光速更快.
然而, 在玻璃内光的相速度比真空中的光速小,
而且我们有可能发射一个具有很高能量的带电粒子,
使它以接近于真空中光速的速率通过一块玻璃,
而光在玻璃中的速率仅为真空中光速的 2/3.

正在运动的比媒质中的光速快的粒子, 将产生一个以源为顶点的锥形光波,
就像汽艇前进时所形成的尾波 (事实上, 它来自同样的效应).
通过锥角的测量, 我们能够确定粒子的速率. 这种用来确定粒子速率的技术,
在高能研究中已作为一种测定粒子能量的方法.
所有要测量的只是光的方向.
```

## 物理定律的对称性

```
首先我们要问, 对称性是什么? 一条物理定律怎么会是"对称的"?
定义对称性的问题是一件有趣的事情, 我们曾提到过外尔给出了一个很好的定义,
其要点为, 如果有一样东西, 我们可以对它做某种事情, 在做完之后,
这个东西看起来仍旧和先前一样, 那它就是对称的.
目前我们要考虑的是, 可以对物理现象或实验中的物理状况做些什么事,
而其结果却和未做前一样.
```

- 下面列举了使种种物理现象得以保持不变的已知操作.
  - 空间平移
  - 空间反射
  - 时间平移
  - 全同原子或全同粒子的交换
  - 转过一定的角度
  - 量子力学的相位
  - 匀速直线运动变换 (洛伦兹变换)
  - 物质-反物质 (电荷共轭)
  - 时间反演

```
另外一个物理定律不对称的例子是我们熟知的: 当一个系统作均匀的角速度转动时,
其中的表观物理定律与一个不转动的系统的物理定律显得不相同.
如果我们安排好一个实验, 然后把所有的东西放到一个宇宙飞船里,
再在宇宙空间中让飞船本身以恒定的角速度自转, 实验仪器将不会照原样那样工作,
因为我们知道, 在飞船里的东西会被甩出去, 并且会发生其他一些情况.
这是由于离心力或科里奥利力等而造成的.
事实上, 我们不必向外看, 只要利用傅科摆就可觉察到地球在旋转.
```

```
下面我们来叙述一个很有趣的对称性, 即时间的可逆性.
初看起来, 这显然不成立. 很明显, 物理定律在时间上是不可逆的,
因为我们知道, 所有明显的现象在大尺度上都是不可逆的:
"挥笔写字, 写完再写, ..." 到现在为止我们所能说的是,
这种不可逆性是由于所牵涉的粒子的数量极其巨大而产生的,
倘若我们能够看到单个分子, 就将无法辨别变化是往正方向发展还是往逆方向发展.

更确切地说: 我们先制造一台小小的仪器, 就能知道其中所有原子的行为,
也能观察到它们的运动. 然后再制造一台类似的仪器,
这台仪器开始工作时的状况与前一台仪器的最终状况相同,
但所有的原子的速度正好相反. 那么, 这台仪器将经历完全相反的变化过程.

换句话说, 如果我们拍一部影片, 详细地记录了一块材料的所有内部情况,
然后再倒过来放, 没有一个物理学家会说: "这是违反物理定律的, 有些地方搞错了!"
当然, 如果我们没有去观察所有的细节, 事情将是完全明确的,
比如说, 当我们看见一个鸡蛋落在人行道上, 使蛋壳破碎时, 肯定会说:
"这是不可逆的!"
但是, 如果我们观察单个原子本身, 定律看来完全是可逆的.
当然, 发现这一点要难得多, 但很清楚, 在微观的基本的水平上,
物理学的基本定律在时间上确实是完全可逆的.
```

```
有这么一件事实: 在量子力学中,
对于每一个对称的规律都有一条守恒定律与之相对应.
这个最深奥和最美妙的事实对许多物理学家来说简直令他们感到震惊.
鉴于我们现在的讨论水平, 我们无法对之作更多的说明.
物理定律的对称性与守怕定律之间存在着一定的联系.
在这里我们只加叙述而不打算作任何解释.

举例说, 物理定律对空间平移是对称的.
如果与量子力学的原则相结合, 结果就意味着动量是守恒的.
物理定律对时间平移是对称的. 在量子力学中就意味着能量是守恒的.
关于空间转动一定角度后的不变性与角动量守恒定律相对应.
这些关系是非常有趣和非常美妙的!
```

- 顺便提一下, 量子力学中出现的有一些对称性并没有经典的类比,
  无法以经典物理的方式描述. 其中有一个就是:
  - 如果
    $$ \psi $$
    是某个过程的概率波幅, 我们知道
    $$ \psi $$
    的绝对值的平方就是这个过程出现的概率.
  - 现在, 如果有人进行计算时不用这个
    $$ \psi $$,
    而是用另一个
    $$ \psi ' $$,
    它与
    $$ \psi $$
    只是相差一个相位因子 (令
    $$ \Delta $$
    为某个常数, 把
    $$ e^{i \Delta} $$
    乘以原来的
    $$ \psi $$
    即得
    $$ \psi ' $$
    ), 那么, 作为该事件概率的
    $$ \psi ' $$
    的绝对值平方就等于
    $$ \psi $$
    的绝对值平方
  - $$ \psi ' = \psi e^{i \Delta}; \mid \psi ' \mid ^2 = \mid \psi \mid ^2 $$.
- 因此, 如果波函数的相位移动任意一个常数, 物理定律仍然不变, 这是另一种对称性.
  - 物理定律必须具有这样的性质, 即量子力学相位的移动不会产生什么差别.
  - 我们刚才说过, 在量子力学中, 对每个对称性都存在着一个守恒定律.
  - 与量子力学相位相关联的守恒定律看来是电荷守恒定律.
  - 总之, 这是一件非常有趣的事情!

---

- 我们来作一点说明. 矢量可以分为两类, 有一类是`"真正"`的矢量,
  比如空间中的位移
  $$ \Delta \boldsymbol{r} $$.
  - 如果在我们的仪器中, 这里有一个零件, 那里有另外一个零件,
    那么在一个镜像仪器里, 有前一个零件的镜像物, 也有后一个零件的镜像物.
  - 如果我们从"这个零件"到"那个零件"画出矢量, 那么一个矢量就是另一个矢量的镜像.
  - 矢量箭头变换了指向, 就好像整个空间翻了个身一样, 这一种矢量我们称为`极矢量`.
- 但是, 另一类与转动有关的矢量具有不同的性质.
  - 例如, 在三维空间中有某个物体在作转动.
  - 如果在镜子中看它, 将作为原来那个转动的镜像而转动着.
  - 现在我们约定用同样的规则表示镜像的转动, 它也是一个"矢量",
    在反射后, 并没有像`极矢量`那样改变,
    但是相对于`极矢量`以及空间的几何关系而言, 则正好反过来;
    这种矢量称为`轴矢量`.
- 现在, 如果反射对称定律在物理上是正确的, 我们必须这样来设计方程,
  即当我们改变每个`轴矢量`的符号和每个矢积的符号时 (它相当于反射),
  不应出现任何差别.
  - 比如, 当我们写出一个公式表明角动量为
    $$ \boldsymbol{L} = \boldsymbol{r} \times \boldsymbol{p} $$
    时, 这个方程是完全正确的, 因为如果我们换成左手坐标系时,
    __L__ 的符号改变了, 而 __p__ 和 __r__ 没有改变;
    但矢积的符号变化了, 因为我们要从右手规则变到左手规则.
  - 再举个例子, 我们知道作用于在磁场中运动的电荷上的力为
    $$ \boldsymbol{F} = q \boldsymbol{v} \times \boldsymbol{B} $$.
  - 但当我们从右旋变到左旋系统时, 由于 __F__ 和 __v__ 都是`极矢量`,
    所以由矢积所要求的变号应当被 __B__ 的变号所抵消, 这就意味着 __B__ 必须是`轴矢量`.
  - 换句话说, 如果进行这样一种反射, __B__ 必须成为 __-B__.
    所以, 在把坐标系从右手改为左手后, 我们也必须使磁铁的两极互换.

```
另一个问题当然就是要找出宇称守恒失败的规律.
有没有什么法则能告诉我们这种不守恒的情况在多大的范围内成立?
有. 这个法则是, 只有在非常慢的称为弱衰变的反应中, 守恒才遭到破坏,
而且在这种情况发生时, 有关的法则表明, 带有自旋的粒子, 例如电子,
中微子等等, 在出现时倾向于向左自旋.

这是一条倾向一面的法则, 它把速度极矢量与角动量轴矢量联系起来,
并且指出角动量与速度方向相反的可能性比一致的可能性要来得大一些.

这条法则就是如此, 但今天我们并不真正理解它的原因.
为什么这条法则是正确的, 它的基本原因是什么, 它与其他事情有何联系?
这件非对称的事实使我们感到如此的震惊,
以致此刻还没有能从惊讶中充分地恢复过来去理解对于所有其他规则来说这将意味着什么.
然而, 这个课题是有趣和新颖的, 也是仍未获得解决的,
所以看来我们讨论一些与此有关的问题是可取的.
```

- 利用正电子衰变来代替电子衰变的`β`衰变实验指出了这里的相互关系是:
  - 右旋物质的行为与左旋反物质的行为一样. 于是,
    现在终于可以说右与左的对称性仍然保持着!
  - 如果我们用反物质代替正物质制造一个左旋钟, 它将走得一样快.
  - 这样事情就变为, 代替我们的对称性表中的两条独立规则的,
    是把这两者结合在一起变成一条新规则,
    即右旋的物质与左旋的反物质是对称的.