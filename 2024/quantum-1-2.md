---
title: 量子力学 科恩 第一卷 (下)
description: 别来春半, 触目愁肠断. 砌下落梅如雪乱, 拂了一身还满.
date: 2022-10-31
---

- [量子力学 (第一卷)](https://book.douban.com/subject/25954720/)

# 自旋 1/2 和二能级体系

- 我们将会看到, 一个顺磁性中性原子的角动量 (或磁矩) 沿
  $$ O_z $$
  方向的分量只能取某一离散集合中的若干个数值.
  - 例如, 就一个基态的银原子而言, 其角动量的分量
    $$ S_z $$
    只有两个可能值
    ($$ + \frac{\hbar}{2} $$
    和
    $$ - \frac{\hbar}{2} $$).
  - 因此, 我们说一个基态银原子是自旋为
    $$ \frac{1}{2} $$
    的粒子.

## 自旋为 1/2 的粒子: 角动量的量子化

```
对于处在基态的银原子 (如原子注中的那些原子), 角动量就是外电子的自旋,
因此, 只有这个电子关系到磁矩的存在. 这是因为, 这个电子的轨道角动量等于零;
此外, 全体内层电子的轨道角动量和自旋角动量也都等于零;
最后, 在我们所达到的实验条件下, 核的自旋所引起的效应是完全可以忽略的.
这就说明了为什么基态的银原子像电子一样具有自旋 1/2.
```

```
现在完全没有必要用量子力学来处理每一个原子的外部变量 r 和 p;
我们只要利用沿经典轨迹前进的几乎呈点状的波包来进行分析就可以了.
```

- 自旋态空间
  $$ \mathcal{E}_S $$
  中的最一般的 (归一化的) 右矢, 是
  $$ \mid + \rangle $$
  和
  $$ \mid - \rangle $$
  的某种线性叠加:
  - $$ \mid ψ \rangle = α \mid + \rangle + β \mid - \rangle $$
  - 其中
    $$ α $$
    与
    $$ β $$
    应满足下列关系式:
    $$ |α|^2 + |β|^2 = 1 $$
- 在基
  $$ \{ \mid + \rangle, \mid - \rangle \} $$
  中, 表示可观察量
  $$ S_z $$
  的矩阵显然是对角的, 可将它写作:
  - $$
      (S_z) = \frac{\hbar}{2}
      \begin{pmatrix}
        1 & 0 \\
        0 & -1
      \end{pmatrix}
    $$

- 观察算符
  $$ S_x $$
  和
  $$ S_y $$
  分别与
  $$ \mathcal{L} $$
  的分量
  $$ \mathcal{L}_x $$
  和
  $$ \mathcal{L}_y $$
  相联系. 在基
  $$ \{ \mid + \rangle, \mid - \rangle \} $$
  中, 算符
  $$ S_x $$
  和
  $$ S_y $$
  应该用
  $$ 2 \times 2 $$
  的厄米矩阵来表示.

> $$ \mathcal{L} $$
  貌似并不是原书采用的符号, 但我也没找到相似的~

- 到`量子力学中角动量的普遍性质`一章我们将会看到, 在量子力学中,
  一个角动量的三个分量并不互相对易, 而是满足完全确定的对易关系式.
  根据这一点, 我们可以证明, 在目前所研究的自旋
  $$ \frac{1}{2} $$
  的情况下, 在
  $$ S_z $$
  的本征矢
  $$ \mid + \rangle $$
  和
  $$ \mid - \rangle $$
  所构成的基中,
  $$ S_x $$
  和
  $$ S_y $$
  的矩阵是:
  - $$
      (S_x) = \frac{\hbar}{2}
      \begin{pmatrix}
        0 & 1 \\
        1 & 0
      \end{pmatrix}
    $$
  - $$
      (S_y) = \frac{\hbar}{2}
      \begin{pmatrix}
        0 & -i \\
        i & 0
      \end{pmatrix}
    $$

- 算符
  $$ S_x $$,
  $$ S_y $$
  和
  $$ S_u $$
  的本征值都与
  $$ S_z $$
  的相同, 即
  $$ + \frac{\hbar}{2} $$,
  $$ - \frac{\hbar}{2} $$.
  从物理上看, 这个结果是可以预期的;
  由于空间的一切方向的性质都相同.

- [拉莫尔进动](https://en.wikipedia.org/wiki/Larmor_precession)

## 二能级体系的一般研究

```
在物理学中还有很多别的问题, 如果只需一级近似, 也可用同样简单的方式来处理.
譬如, 我们考虑一个具有两种状态的物理体系, 对应于这两个状态的能量相差很小,
但这两个能量值与体系的一切其他状态的能量值却又相差很大.
现在我们希望计算外界微扰 (或以前被忽略了的内部相互作用) 对这两个能级的影响.
当扰动的强度足够弱时, 可以证明, 如果只需要一级近似,
那么要计算扰动对这两个能级的影响, 可以完全不考虑该体系的所有其他能级.
这样一来, 我们就可以在态空间的一个二维子空间中进行全部运算.
```

- 假设现在我们要考虑在
  $$ H_0 $$
  中原来忽略不计的外界微扰或体系内部的相互作用, 则哈密顿算符变为:
  - $$ H = H_0 + W $$
  - 我们用
    $$ \mid ψ_{±} \rangle $$
    和
    $$ E_{±} $$
    表示
    $$ H $$
    的本征态和本征值:
  - $$ H \mid ψ_+ \rangle = E_+ \mid ψ_+ \rangle $$
  - $$ H \mid ψ_- \rangle = E_- \mid ψ_- \rangle $$
- $$ H_0 $$
  通常叫做未微扰的哈密顿算符,
  $$ W $$
  叫做微扰或耦合. 在这里, 我们假定
  $$ W $$
  不依赖于时间. 在由
  $$ H_0 $$
  的本征态 (叫做未微扰的态) 组成的基
  $$ \{ \mid φ_1 \rangle, \mid φ_2 \rangle \} $$
  中,
  $$ W $$
  由一个厄米矩阵表示:
  - $$
      (W) =
      \begin{pmatrix}
        W_{11} & W_{12} \\
        W_{21} & W_{22}
      \end{pmatrix}
    $$
  - $$ W_{11} $$
    和
    $$ W_{22} $$
    都是实数. 此外
    $$ W_{12} = W_{21}^{*} $$
- 没有耦合时,
  $$ E_1 $$
  和
  $$ E_2 $$
  是体系的可能的能量值, 而态
  $$ \mid φ_1 \rangle $$
  和
  $$ \mid φ_2 \rangle $$
  都是定态 (就是说,
  如果使体系处于这两个态中的一个, 则它将永远处于这个态).
  现在的问题是要计算引入耦合
  $$ W $$
  之后出现的修正.

- 耦合的后果
  - α.
    $$ E_1 $$
    和
    $$ E_2 $$
    不再是体系的可能的能量值
  - β.
    $$ \mid φ_1 \rangle $$
    和
    $$ \mid φ_2 \rangle $$
    不再是定态 (由
    $$ W $$
    引起的两个未微扰的态之间的跃迁, 所以称
    $$ W $$
    为两个态之间的`耦合`)

### 静态方面: 耦合对体系的定态的影响

- $$ H $$
  的本征值及本征态的表示式
  - 在基
    $$ \{ \mid φ_1 \rangle, \mid φ_2 \rangle \} $$
    中, 我们可将
    $$ H $$
    的矩阵写作:
  - $$
      (H) =
      \begin{pmatrix}
        E_1 + W_{11} & W_{12} \\
        W_{21} & E_2 + W_{22}
      \end{pmatrix}
    $$

- 下面我们将要讨论的一切有趣的效应都起源于微扰
  $$ W $$
  具有非对角矩阵元
  $$ W_{12} = W_{21}^{*} $$
  (如果
  $$ W_{12} = 0 $$,
  那么,
  $$ H $$
  的本征态就和
  $$ H_0 $$
  的相同, 新的本征值就是
  $$ E_1 + W_{11} $$
  和
  $$ E_2 + W_{22} $$).
  - 为简单起见, 我们从现在起假设矩阵
    $$ (W) $$
    纯粹是非对角的, 也就是说,
    $$ W_{11} = W_{22} = 0 $$.

- 现在我们讨论耦合
  $$ W $$
  对于能量
  $$ E_+ $$
  及
  $$ E_- $$
  (作为
  $$ E_1 $$
  和
  $$ E_2 $$
  的函数) 的影响. 为此, 我们假设
  $$ W_{12} $$
  是固定的, 并引入下列两个参量
  - $$ E_m = \frac{1}{2} (E_1 + E_2) $$
  - $$ Δ = \frac{1}{2} (E_1 - E_2) $$
  - 立即可以看出,
    $$ E_+ $$
    及
    $$ E_- $$
    随
    $$ E_m $$
    的变化是非常简单的: 改变
    $$ E_m $$
    就归结为移动能量轴的原点. 此外, 可以证实矢量
    $$ \mid ψ_+ \rangle $$
    和
    $$ \mid ψ_- \rangle $$
    并不依赖于
    $$ E_m $$.
    于是, 我们需要注意的仅仅是参量
    $$ Δ $$
    的影响.
  - 我们将四个能量
    $$ E_1 $$,
    $$ E_2 $$,
    $$ E_+ $$
    和
    $$ E_- $$
    作为
    $$ Δ $$
    的函数画在同一张图上. 对于
    $$ E_1 $$
    和
    $$ E_2 $$,
    我们得到两条直线, 其斜率为
    $$ +1 $$
    和
    $$ -1 $$.
  - 进一步有:
  - $$ E_+ = E_m + \sqrt{Δ^2 + \mid W_{12} \mid^2} $$
  - $$ E_- = E_m - \sqrt{Δ^2 + \mid W_{12} \mid^2} $$

- 当
  $$ Δ $$
  变化时,
  $$ E_{+} $$
  和
  $$ E_{-} $$
  的值描绘出相对于坐标轴为对称的双曲线的两支,
  它们的渐近线就是对应于未微扰能级的两条直线,
  它们的顶点间的距离为
  $$ 2 \mid W_{12} \mid $$.

- 此外, 我们还可以看出, 不论
  $$ Δ $$
  的值如何, 恒有:
  - $$ \mid E_{+} - E_{-} \mid > \mid E_1 - E_2 \mid $$
  - 于是我们得到在物理学其他领域中 (例如在电路理论中)
    常见的一个规律: 耦合使固有频率互相远离.

```
当两个未微扰能级的能量相等时, 耦合的影响尤其重要.
```

### 动态方面: 体系在两个未微扰态之间的振荡

- [拉比公式](https://en.wikipedia.org/wiki/Rabi_cycle)

- 对于弱耦合
  $$ (E_1 - E_2 \gg \mid W_{12} \mid) $$,
  微扰态与未微扰态的差异不大. 实际上, 除了总的相位因子
  $$ e^{-i φ/2} $$
  以外,
  $$ \mid ψ_+ \rangle $$
  几乎等于
  $$ \mid φ_1 \rangle $$,
  因为态
  $$ \mid φ_2 \rangle $$
  的微小贡献仅引起轻微的修正.
  - 反之, 对于强耦合
    $$ (E_1 - E_2 \ll \mid W_{12} \mid) $$,
    态
    $$ \mid ψ_+ \rangle $$
    和
    $$ \mid ψ_- \rangle $$
    完全不同于态
    $$ \mid φ_1 \rangle $$
    和
    $$ \mid φ_2 \rangle $$;
    这是因为, 前者是后者的线性叠加, 其系数具有相同的模.
  - 于是, 我们看到, 与能量的情况相似,
    在两个未微扰态的交点附近,
    本征态受到重大修正.

- 当
  $$ E_1 = E_2 = E_m $$
  时,
  $$ H_0 $$
  对应的能量是二重简并的. 正如我们刚才所看到的, 耦合
  $$ W_{12} $$
  将消除这种简并, 特别是, 出现了这样一个能级, 它的能量下降了
  $$ \mid W_{12} \mid $$.
  - 换句话说, 如果一个物理体系的基态是二重简并的
    (而且对应的能级与其他所有能级相隔足够远), 那么,
    这两个态之间的任何 (纯粹非对角的)
    耦合都将降低体系基态的能量, 于是体系变得更加稳定.

# 一维谐振子

- 这种体系的最简单的例子, 就是处在下述势场中的一个质量为
  $$ m $$
  的粒子, 此势场只依赖于
  $$ x $$,
  其形式为:
  - $$ V(x) = \frac{1}{2} k x^2 $$
  - ($$ k $$
    是一个正的实常数). 粒子受到的恢复力为:
  - $$ F_x = - \frac{dV}{dx} = - kx $$
  - 这个力正比于粒子与平面
    $$ x = 0 $$
    之间的距离
    $$ x $$,
    在这个力的作用下, 粒子总是被拉向平面
    $$ x = 0 $$
    ($$ V(x) $$
    为极小值的位置, 对应于稳定平衡位置).
    我们知道, 在经典力学中, 此粒子的运动在
    $$ Ox $$
    轴上的投影是围绕着点
    $$ x = 0 $$
    的正弦型振荡, 其角频率为:
  - $$ ω = \sqrt{\frac{k}{m}} $$

  - 在这一章里还要引入算符
    $$ a^{\dagger} $$
    和
    $$ a $$,
    特地用它们来描述从能级
    $$ n $$
    到能级
    $$ n + 1 $$
    或能级
    $$ n - 1 $$
    的过渡. 这两个算符分别叫做产生算符, 湮没算符,
    是量子统计力学和量子场论中经常用到的算符.

### 经典力学中的谐振子

- 粒子的运动遵从下列的动力学方程:
  - $$ m \frac{d^2 x}{dt^2} = - \frac{dV}{dx} = -kx $$
  - 这个方程的通解具有下列形式:
  - $$ x = x_M \cos (ωt - φ) $$
  - 积分常数
    $$ x_M $$
    和
    $$ φ $$
    由运动的初始条件所确定. 由此可见, 粒子在原点
    $$ O $$
    附近作正弦型`振荡`, 振幅是
    $$ x_M $$,
    角频率是
    $$ ω $$.

- 粒子的动能为
  - $$ T = \frac{1}{2} m (\frac{dx}{dt})^2 = \frac{p^2}{2m} $$
  - 其中
    $$ p = m \frac{dx}{dt} $$
    是粒子的动量. 因而总能量为:
  - $$ E = T + V = \frac{p^2}{2m} + \frac{1}{2} m ω^2 x^2 $$
  - 进一步得到:
  - $$ E = \frac{1}{2} m ω^2 x_M^2 $$
  - 由此可见, 粒子的能量与时间无关 (这是保守体系的普遍性质); 而且由于
    $$ x_M $$
    可取任意值, 故能量可以为任意正数或零.

- 我们来考虑任意的势
  $$ V(x) $$,
  它的极小值位于
  $$ x = x_0 $$
  处. 将函数
  $$ V(x) $$
  在点
  $$ x_0 $$
  附近展为泰勒级数.
  - 因为点
    $$ x_0 $$
    对应于
    $$ V(x) $$
    的极小值, 故
    $$ (x - x_0) $$
    的一次项等于零.
  - 点
    $$ x = x_0 $$
    就是粒子的稳定平衡位置. 这是因为, 在
    $$ x = x_0 $$
    处,
    $$ F_x $$
    为零; 对于充分小的
    $$ (x - x_0) $$,
    $$ F_x $$
    与
    $$ (x - x_0) $$
    是反号的.
  - 如果粒子在
    $$ x_0 $$
    附近运动的振幅足够小, 以致式中的
    $$ (x - x_0)^3 $$
    项 (从而, 式中与之对应的
    $$ (x - x_0)^2 $$
    项) 与前面的项相较可以忽略. 那么,
    我们要处理的就是一个谐振子的问题了.
  - 由于运动的振幅始终很小, 故谐振子的能量将是很小的.

- 如果能量
  $$ E $$
  的值较大, 那么粒子将在两个极端位置
  $$ x_1 $$
  和
  $$ x_2 $$
  之间进行`周期性的但非正弦型的运动`. 如果将表示粒子位置的函数
  $$ x(t) $$
  展为傅里叶级数, 我们得到的将不是一个而是一系列正弦项,
  各项的频率都是前项频率的倍数.
  - 这时我们称这体系为`非谐性振子`.

### 哈密顿算符的一般性质

- 在量子力学中, 经典量
  $$ x $$
  和
  $$ p $$
  应分别用观察算符
  $$ X $$
  和
  $$ P $$
  来代替, 它们满足关系:
  - $$ [X, P] = i \hbar $$
  - 于是, 我们很容易得到体系的哈密顿算符:
  - $$ H = \frac{P^2}{2m} + \frac{1}{2} m ω^2 X^2 $$
  - 由于
    $$ H $$
    与时间无关 (保守体系), 对谐振子的量子研究便归结为求解本征值方程:
  - $$ H \mid φ \rangle = E \mid φ \rangle $$
  - 在
    $$ \{ \mid x \rangle \} $$
    表象中, 此式可以写作:
  - $$
      [ - \frac{\hbar^2}{2m} \frac{d^2}{dx^2} +
      \frac{1}{2} m ω^2 x^2 ] φ(x) = E φ(x)
    $$

- 在详细研究之前, 我们先指出可从势函数得到的一些重要性质:
  - (i) __哈密顿算符的本征值都是正的__.
    事实上, 我们可以普遍证明, 如果势函数
    $$ V(x) $$
    具有下界, 则哈密顿算符
    $$ H = \frac{P^2}{2m} + V(x) $$
    的各本征值都大于
    $$ V(x) $$
    的极小值, 即若
    $$ V(x) ≥ V_m $$,
    则
    $$ E > V_m $$,
    对于现在所要讨论的谐振子, 我们已经选择能量的原点使得
    $$ V_m $$
    为零.
  - (ii)
    $$ H $$
    __的本征函数具有确定的宇称__. 这是因为势
    $$ V(x) $$
    为一个偶函数:
    $$ V(-x) = V(x) $$.
    因此, 我们可以在具有确定宇称的那些函数中去寻找
    $$ H $$
    在
    $$ \{ \mid x \rangle \} $$
    表象中的本征函数 (事实上, 我们将会看到,
    $$ H $$
    的本征值都是非简并的; 因而,
    定态波函数一定或为偶函数或为奇函数).
  - (iii) __能谱是离散的__. 实际上, 不论总能量的数值如何,
    粒子的经典运动总是局限在
    $$ Ox $$
    轴上的一个有界区间内, 我们可以证明, 在这种情况下,
    哈密顿算符的本征值构成一个离散集合.

## 哈密顿算符的本征值


> 计算过程注意关注`对称化`

### 谱的确定

### 本征值的简并度

## 哈密顿算符的本征态

### 与定态相联系的波函数

## 讨论

### 基态的性质

### 平均值随时间变化

# 量子力学中角动量的普遍性质

- 凡有经典类比的一切角动量, 我们都称之为`轨道`角动量 (用
  $$ L $$
  表示对应的可观察量), 凡属基本粒子的一切内禀角动量,
  我们都称之为`自旋`角动量 (对此, 我们沿用符号
  $$ S $$).
  - 在一个复杂体系中, 例如在原子, 原子核或分子中,
    构成该体系的各个基本粒子 (电子, 质子, 中子, ...) 的各轨道角动量
    $$ L_i $$
    互相组合并且和这些粒子的自旋角动量
    $$ S_i $$
    组合, 这样, 便构成了该体系的总角动量
    $$ J $$.

## 角动量所特有的对易关系式



- 量子力学中的角动量理论完全建立在对易关系式的基础上. 要注意,
  这些关系式意味着: 角动量的三个分量是不可能同时测量的; 但是,
  $$ J^2 $$
  和
  $$ J $$
  的任意一个分量却都是相容的.

- 在一般情况下, 也是这样: 任何角动量
  $$ J $$
  的诸分量都是不可对易的, 不可能将它们同时对角化.
  - 于是, 我们将去寻求
    $$ J^2 $$
    和
    $$ J_z $$
    的共同本征矢的集合, 这两个算符分别对应于角动量的模平方和角动量在
    $$ O_z $$
    轴上的分量.

## 角动量的普遍理论

## 应用于轨道角动量

# 中心势场中的粒子; 氢原子

## 中心势场中粒子的定态

### 变量的分离

### 中心势场中粒子的定态

## 在有相互作用的双粒子体系中质心的运动和相对运动

### 经典力学中的质心运动和相对运动

### 量子力学中变量的分离

## 氢原子

> 本节跳过~

