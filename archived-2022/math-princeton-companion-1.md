---
title: 普林斯顿数学指南 第一卷
description: 花间一壶酒, 独酌无相亲. 举杯邀明月, 对影成三人.
date: 2022-10-14
---

- [普林斯顿数学指南 (第一卷)](https://book.douban.com/subject/25817381/)
  - 蜻蜓点水, __不推荐!__

$$
\Delta f =
\frac{\partial ^2 f}{\partial x ^ 2} +
\frac{\partial ^2 f}{\partial y ^ 2} +
\frac{\partial ^2 f}{\partial z ^ 2}
$$

- $$ \Delta $$
  称为拉普拉斯算子. 那么,
  $$ \Delta f $$
  关于函数 `f` 提供了什么信息呢? 答案是:
  - 它告诉我们当这个邻域的大小趋于零时, `f` 在
    `(x, y, z)` 点的值与它在
    `(x, y, z)` 点的紧接着的邻域里的平均值的比较.

---

- 如果 `X` 和 `Y` 是某一个特定的数学结构的两个例子, 例如同是群, 域或向量空间,
  那么如同我们在讨论`对称性`时提到过的那样,
  有一类从 `X` 到 `Y` 的函数特别有意义,
  具体说就是`"保持结构"`的那些函数.
  - 粗略地说,一个函数
    $$ f: X \to Y $$
    保持 `X` 的结构, 就是说, 如果 `X` 中的元素之间存在着一个用这个结构来表示的关系,
    则这些元素的像之间也存在着用 `Y` 的结构来表示的同样的关系.
  - 举例来说, 设 `X` 和 `Y` 是群, 而 `a, b, c` 是 `X` 的元素,
    而且 `ab = c`, 那么如果 `f` 保持 `X` 的结构, 则在 `Y` 中必有
    `f(a)f(b) = f(c)`
  - (这里采用通常的做法, 即用乘法的记号来表示使得 `X` 和 `Y` 是群的那个二元运算).
  - 与此类似, 若 `X` 和 `Y` 是域,
    而我们用通常表示加法和乘法的标准记号来表示其中的二元运算,
    则只有适合以下关系的函数
    $$ f: X \to Y $$
    才是有意义的:
  - 当 `a + b = c` 时, `f(a) + f(b) = f(c)`;
    `ab = c` 时 `f(a)f(b) = f(c)`.
  - 对于向量空间, 有意义的函数就是保持线性组合的函数:
  - 若 `V`, `W` 是向量空间, 则
    `f(av + bw) = af(v) + bf(w)`.
- 一个保持结构的函数就称为一个`同态` (homomorphism), 然而,
  特定的数学结构的同态常有专门的名字, 例如向量空间的同态就称为线性映射.

---

- 如果我们有好运气, 同态就可能有一些有用的性质.
  为了明白为什么具有这些进一步的性质是值得的, 请看下面的例子.
  - 设 `X` 和 `Y` 是群, 而
    $$ f: X \to Y $$
    把 `X` 的任意元素都映为 `Y` 的恒等元 `e`.
  - 按照上面的定义, 这个 `f` 就是保持结构的函数, 因为只要
    `ab = c`, 则必有 `f(a)f(b) = ee = e = f(c)`.
  - 然而, 这时我们说 `f` 使得原有的结构都`坍塌`了.
  - 更准确一些, 可以把这里的思想说得更确切一点, 虽然当
    `ab = c` 时 `f(a)f(b) = f(c)`, 其`逆则不成立`.
  - 完全有可能 `f(a)f(b) = f(c)` 而 `ab` 并不等于 `c`,
    实际上, 上面的例子正是这个情况.
- 两个结构 `X` 和 `Y` 间的同构就是这样一个同态
  $$ f: X \to Y $$,
  其逆
  $$ g: Y \to X $$
  也是一个同态, 对于绝大多数代数结构 (例如群), 可以证明,
  `若 f 有逆 g, 则 g 自动地也是同态`, 在这种情况下,
  我们可以说`同构`就是同时也是`双射的同态`.
  - 就是说, `f` 是 `X` 和 `Y` 之间的保持结构的一对一的对应.

---

- 和代数结构的同态
  $$ \phi $$
  相关的一个重要概念是它的`核`的概念.
  - `核`定义为 `X` 中所有使得
    $$ \phi (x) $$
    为 `Y` 中的恒等元的那些 `x` 的集合
    (当 `X` 和 `Y` 涉及`加法`和`乘法`两个二元运算时,
    这里说的恒等元`仅指`加法恒等元).
- 同态的核时常是 `X` 的具有有趣性质的子结构.
  - 例如说, 如果 `G` 和 `K` 是群, 则由 `G` 到 `K`
    的同态的核是 `G` 的一个正规子群;
  - 反过来, 若 `H` 是 `G` 的在正规子群, 则把 `G` 的一个元素 `g`
    映为左陪集 `gH` 的商映射是由 `G` 到商群
    `G/H` 的一个同态而以 `H` 为核.
  - 类似地, 环同态的核必是一个理想, 而环 `R` 的每一个理想 `I`,
    又都是由 `R` 到 `R/I` 的`"商映射"`的核
    (这个商结构将在条目`环, 理想与模`中更详细地讨论).

### 几何学

```
克莱因坚持下来了, 而且在 1871-1873
三年的三篇文章里证明了所有已知的几何学都是射影几何学的子几何学.
他的思想是把几何学重新铸造成为对于作用在空间上的某个群的研究.
图形 (即空间的某个子集合) 的在此群作用下不变的性质就是几何性质.
所以, 例如对于某一维的射影空间,
适合于射影几何学的群就是所有映直线为直线的所有线性变换的群,
而其中把某一给定的圆锥映入此圆锥内域的线性变换所成的子群,
就可以看成非欧几何的变换群.
```

### 数学分析的严格性的发展

```
康托逐步达到了一个观点, 即集合可以起整个数学的基础的作用.
早在 1882 年, 他就写道, 集合的科学包含了算术, 函数论和几何学,
而且以基数概念为基础, 给出一个"更高级的统一".
然而这个提议表述得很含混, 因而开始时没有吸引到追随者.
然而, 集合还是设法进入了分析的语言,
最值得注意的是通过测度和集合的可测性的概念这条路.
事实上, 分析被集合理论吸收,
一条重要途径就是通过寻求哪些函数可以用来在抽象的意义下
"测度" 一个集合这条路走来的.
```

### 数学基础中的危机

```
关于基础的辩论, 在思想和结果上, 在关键的洞察和发展上, 都留下了很丰富的遗产,
包括公理化集合论和直觉主义的兴起.
最重要的发展之一是现代数理逻辑作为公理学的改进的发展,
引导到递归和可计算性理论在 1936 年左右的发展.
在这个过程中, 我们对于形式系统的特征, 可能和局限性的理解都大大澄清了.
```

### 选择公理

```
选择公理是从一些集合做出其他集合的几个规则之一.
这种规则的两个典型例子是下面的命题:

对于任意的集合 A 可以作出其一切子集合的集合, 称为 A 的幂集.

还有对于任意的集合 A 和任意的性质 p 可以作出 A
中的所有具有性质 p 的元素的集合.

这两条规则分别叫做幂集公理和概括公理. 粗略地说,
选择公理说的就是允许我们在作出一个新集合的时候作任意多次未加特别说明的选择.
```

- `选择公理`在日常的数学生活里比上述的基本形式用得更多的还有两个形式.
  - 其一是`良序原理`, 它宣称所有的集合都可以良序.
  - 另一个是`佐恩引理`, 它指出, 在一定条件下必有"最大"元素存在.
  - 例如, 一个向量空间的基底就是最大的线性无关集合,
    而结果是, 若对向量空间的线性无关集合的整体应用佐恩引理,
    就可以证明每一个向量空间都有基底存在.
- 这两个命题都被说成是选择公理的形式, 是因为它们都等价于选择公理, 就是说,
  在其他的构造集合的规则都存在的条件下, 它们的每一个都蕴含着选择公理,
  也可以从选择公理导出.
  - 要想看出为什么选择公理的这两个形式都有一种非构造的感觉,
    一个好办法是花上几分钟想一想怎样找出实数集合的良序,
    或者找出有所有实数序列所成的向量空间的基底.

### 贝叶斯分析

### Calabi-Yau 流形

> 物理学中的 Calabi-Yau 流形

- 爱因斯坦的引力理论, 即广义相对论,
  建立了黎曼时空流形的度量必须满足的方程.
  这个方程中涉及了`3`个张量:
  - 度量张量, 里奇 (Ricci) 曲率张量, 及物质的能量动量张量.
  - 一个里奇曲率为零的流形, 当没有物质时是这个方程的一个解,
    而且是一个爱因斯坦流形的特例.
  - 一个具有唯一的 `SU(n)` 完整群的 Calabi-Yau 流形具有零里奇曲率,
    所以在广义相对论中是有意义的.
- 理论物理学的一个基本问题是如何把爱因斯坦理论融入粒子的量子理论中.
  - 这个事业称为量子引力理论.
  - Calabi-Yau 流形在首选的量子引力理论即弦论方面起突出的作用.
- 在弦论中, 基本的对象是`1`维的`"弦"`. 弦在时空里的运动用一个`2`维的轨迹来描述,
  这个轨迹称为`世界叶`, 所以世界叶的每一点都用此点在时空里的位置来标记.
  - 于是, 可以这样来构造弦论, 即把它作为从`2`维的黎曼曲面到时空流形
    `M` 的映射的量子场论.
  - 对这个 `2` 维的曲面应该赋以一个黎曼度量,
    而可供考虑的黎曼度量形成了一个无限维空间.
  - 这意味着我们必须在 `2` 维中解决量子引力的问题 --
    这个问题和它的 `4` 维的同伴一样, 是太难了.
  - 然而, 如果 `2` 维的世界叶理论是共形的 (即在局部的尺度变换下是不变的),
    则留下的就只是一个共形不等价度量的有限维空间, 而这个理论就能适当地定义.
- Calabi-Yau 条件就是从这样的考虑中产生的. 要求 `2` 维理论是共形的,
  使得弦论有意义, 实质上就是要求时空的里奇张量为零.
  - 这样, `2` 维条件引导出一个时空方程, 而且恰好就是无物质的爱因斯坦方程.
  - 对这个条件还要再加上一个`"唯象的"`判据, 即这个理论应该具有`"超对称"`,
    就是要求时空流形 `M` 是复流形.
  - 就是一个 Calabi-Yau 流形.
  - 根据丘成桐的定理, 这种 `M` 的选择很容易用代数几何的方法来描述.

### 基数

- 更准确地说, 如果两个集合之间有一个双射,
  就说两个集合有相同的`势`, 即相同`基数`.
- 那么, 有些什么样的基数呢?
- 首先是`有限势`, 就是有限集合的势:
  - 一个集合具有`"势 n"`, 如果它恰好有 `n` 个元素的话.
  - 然后就是`可数`与`不可数`集合,
    所有这种可数集合都有同样的势 (这可以从可数性的定义得出),
    通常记为
    $$ \aleph_{0} $$.
  - 例如自然数集合, 整数集合, 有理数集合都具有势
    $$ \aleph_{0} $$.
  - 然而实数集合是不可数的, 所以其势不是
    $$ \aleph_{0} $$.
  - 事实上, 它的势记为
    $$ 2 ^ {\aleph_{0}} $$.
- 可以证明, 基数可以相加和相乘, 甚至可以取其他基数的幂, 所以
  $$ 2 ^ {\aleph_{0}} $$
  不是一个单独的记号, 而是对一个势为
  $$ \aleph_{0} $$
  的集合进行某种运算的结果.

### 范畴

- 范畴就是允许我们抽象地来讨论这样一些性质的数学结构.
  - 它包含了一组`对象`, 还有这些对象之间的`态射`.
  - 就是说, 如果 `a` 和 `b` 是此范畴的两个对象,
    范畴中还包括了这两个对象之间的一组态射,
    也有态射的复合这个概念,
    若 `f` 是由 `a` 到 `b` 的态射,
    `g` 是由 `b` 到 `c` 的态射,
    则存在 `f` 和 `g` 的一个复合为由 `a` 到 `c` 的态射.
  - 这个复合必须是结合的.
  - 此外, 对每一个对象 `a` 都存在一个"恒等态射", 它的性质是:
  - 如果把它与任意态射 `f` 复合起来, 则仍会得到 `f`.
- 正如前面的讨论暗示的那样, 范畴的一个例子是群的范畴.
  - 这个范畴的对象就是群, 而态射就是群同态,
    复合和恒等态射都如我们习惯的那样定义.
  - 然而, 下面的例子表明, 绝非所有的范畴都是这样的:
- `(i)` 可以这样来构造一个范畴, 其对象为自然数,
  而由 `n` 到 `m` 的态射是所有具有实数元的
  `n × m` 矩阵, 态射的复合和恒等态射就定义为矩阵的乘法和恒等矩阵.
  - 正常情况下, 不会把 `n × m` 矩阵想成一个由数 `n` 到数 `m` 的映射,
    然而范畴的公理是得到了满足的.
- `(ii)` 任何集合都可以变成一个范畴, 对象就是此集合的元素,
  而由 `x` 到 `y` 的态射就是断言 `"x = y"`.
  - 也可以把一个有序集合变成一个范畴, 而令由 `x` 到 `y` 的态射为断言
    `"x ≤ y"` (`"x ≤ y"` 和 `"y ≤ z"` 的"复合"则是 `"x ≤ z"`).
- `(iii)` 任意的群也可以像下面那样变成一个范畴, 它仅有一个对象,
  而由此对象到其自身的态射就是群中的元素,
  态射的复合则定义为群中的乘法.
- `(iv)` 还有一个明显的范畴, 其对象为拓扑空间, 态射则为连续函数.
  - 还有一个不那么明显的范畴, 其对象和上面说的一样,
    但是不以连续函数而以连续函数的同伦类为态射.
- 态射也叫映射. 然而正如上面的例子表明的那样,
  范畴中的映射与我们熟悉的映射的样子可以很不相像.
  - 这些映射也称为箭头, 这样的称呼部分地是为了强调一般的范畴具有比较抽象的特性,
    部分地则是因为将用箭头来"画"出态射.

```
由于范畴理论的抽象本性以及不依赖于其他数学分支,
可以看成是"基础性的". 事实上, 也有人建议,
以范畴理论来作为数学基础的另一个候补对象,
把态射作为最基本的概念, 而所有其他概念都要由它派生出来,
而不像在集合论基础里面使用集合的属于关系作为最基本的概念.
```

### 紧性与紧化

```
紧化的另一个用途是, 它时常能够严格地把一种类型的数学对象看成其他对象的极限.
例如, 只要把圆周的空间适当紧化, 使之包括直线,
就可以把直线看成越来越大的圆周的极限.
这种前景使我们能够从关于圆周的定理导出关于直线的定理,
或者反过来从关于直线的定理导出关于很大的圆周的定理.
再举在一个很不相同的数学领域里的例子, 狄拉克的 delta 函数本来不是严格意义下的函数,
但是在某些函数空间里, 例如在某种测度空间或者广义函数空间里,
存在某种 (局部的) 紧化, 使我们可以把 delta 函数看成经典的函数的极限.
我们还可以利用紧化把连续的东西看成离散的东西的极限,
例如循环群序列 Z/2Z, Z/3Z, Z/4Z, ...
就可以紧化为圆群 T = R/Z.
这些简单的例子可以推广为紧化的很精巧的例子,
而在几何, 分析与代数中有很多应用.
```

### 可数与不可数集合

```
可数集合是"最小的"无限集合. 然而实数集合绝非"最大的"无限集合.
事实上, 上面的论证说明任意一个集合 X 都不能与它自己的所有子集合的集合一一对应.
所以, 实数集合的所有子集合的集合"严格地大于"实数集合, 等等.
```

### 傅里叶变换

- 傅里叶变换是把函数分成许多成分, 而每一个成分恰好有一个准确的频率.
  但在有些应用中, 采取一种比较"模糊"的途径更为有用.
  - 这时, 函数被分解成的成分数目要少一些,
    但是每一个成分所含的频率构成一个频段,
    而不是单个频率.
  - 这样一种分解有一个优势, 就是受到不确定性原理的限制较少.
  - 因为按照不确定性原理, 一个函数及其傅里叶变换不可能同时局限在
    $$ R^d $$
    的很小的区域里.
  - 这样会导致傅里叶变换的某些变体, 如`小波变换`,
    它对许多应用数学和计算数学问题更为适合,
    也对某些调和分析和微分方程的问题更为适合.
- 对于量子力学起基本作用的不确定性原理也把傅里叶变换与数学物理联系起来,
  特别是经典物理和量子物理的联系,
  可以通过几何量子化和微局部分析的方法作严格的研究.

### 哈密顿函数

```
初看起来, 现代物理学的许多理论和方程表现出令人眼花缭乱的多样性,
例如, 把经典力学与量子力学比较, 把非相对论物理与相对论物理比较,
或者把粒子物理和统计力学比较, 就可以看到这一点.

然而, 有许多强大的起统一作用的主题把它们联系起来,
其中之一就是在所有这些理论中, 物理系统随时间的演化
(以及这些系统的定常状态) 在很大程度上是受到一个单个的对象的控制,
即这个系统的哈密顿函数.

这个函数时常可以解释为这个系统的总能量. 大略地说, 每一个物理现象
(电磁现象, 原子键, 势阱中的粒子等等) 都对应于一个哈密顿函数 H,
而每一种类型的力学 (经典, 量子, 统计力学)
都相应于用这个哈密顿函数来描述一个物理系统的不同方法.
```

```
数学的许多领域都与自己的物理对应物密切地缠在一起, 所以, 毫不奇怪,
哈密顿函数的概念也出现在纯粹数学里面.

例如, 受到经典物理的启发, 哈密顿函数 (及其下述的推广, 如矩映射)
在动力系统, 微分方程, 李群理论, 辛几何里面都起重要作用.
受到量子力学的启发, 哈密顿函数 (及其下述的推广, 如可观测量, 拟微分算子)
在算子代数, 谱论, 表示理论, 微分方程和微局部分析中同样也很突出.

因为哈密顿函数在那么多物理和数学领域里都出现,
它在建立表面上似乎无关的领域间的桥梁中就很有用,
例如, 建立经典力学与量子力学, 辛力学和算子代数的联系.

一个给定的哈密顿函数的性质时常会揭示出与此哈密顿函数相关的物理或数学对象的众多性质.
例如, 哈密顿函数的对称性时常会诱导出用此哈密顿函数表示的对象的对称性,
虽然不能说一个数学或物理对象的所有有趣的性质都可以直接从它们的哈密顿函数读出,
但是在理解这些对象的性质和动态时哈密顿函数仍然起着基本的作用.
```

### 无理数和超越数

```
30 年后, 康托用完全不同的方法又发现了超越数的存在,
他证明了代数数的集合是可数的, 粗略地说,
就是代数数可以按次序列成一个清单. 精确地说,
就是存在一个由自然数的集合 N 到代数数集合的一个满射.

与之相对照, 实数集合 R 则是不可数的. 关于这个问题, 康托的著名证明,
用对角线论证来证明不论用什么样的方法来列出实数的清单, 必定是有遗漏的.
所以, 一定存在不是代数数的实数.
```

### 纽结多项式

```
HOMFLY 多项式与亚历山大多项式不同, 它没有已知的用经典的代数拓扑的解释.
但是, 它可以陈述为状态和的集合, 这里是对扭结的图式的某些标号来求和.
这就令人想起来自统计物理学的思想: 在 Kauffman (1991) 中有初等的讲解.
整个 HOMFLY 多项式理论的放大, 引导到共形场论的一个版本, 称为拓扑量子场论.
```

### 数论中的局部与整体

- 亨泽尔证明了只要许可无限展开式, 而且许可其中有有限多个 `11` 的负幂,
  有时还有 `11` 的分数幂, 则对于所有的代数数就都能这样做
  - 所以, 可以处理
    $$ \frac{5}{33} $$
    和类似的东西.
- 他争辩说, 这就给出了`"局部在 11"`的信息, 对于所有的素数 `p` 都有这样的事情.
  - 所以, 如果有素数 `p`, 就能`"局部在 p"`考虑一个数,
    只要取这个数的 `p` 的幂的展开式即可.
  - 而这个展开式就称为此数的 `p 进展开式`.
- 和在函数的情况类似, `p` 进展开式告诉我们这个数在多大程度上可以用 `p` 整除,
  但是把此数关于其他的素数的情况都隐藏起来了, 在这个意义下, 它是真正`"局部的"`.

---

- 最好的答案总是会提出新问题. 既已发现了任意的有理数都有 `p` 进展开式,
  而目可以用来直接"做算术", 就不可避免地会问,
  这样做是否已经扩大了所考虑的数的世界.
- 一旦选定了一个素数 `p`, 则任意有理数就给了一个 `p` 进展开,
  但是是否每一个这样的展开都是来自一个有理数?
  - 毫无可能.
- 容易看到, 这种展开式的集合远大于所有有理数的集合.
  - 所以亨泽尔的下一步棋, 就是指出所有 `p` 进展开式的集合
    $$ Q_p $$
    是一个新的数的领域, 他把这些数称为 `p` 进数,
    其中不仅有有理数, 还有更多的东西.

### 拟阵

- 更惊人的是`拟阵`是`贪婪算法`能够管用的唯一的结构. 更精确地说, 设
  $$ \mathcal{L} $$
  是一个集合 `E` 的一个子集合族, 而且具有以下的性质:
  - 若
    $$ A \in \mathcal{L} $$
    而
    $$ B \subseteq A $$
    则
    $$ B \in \mathcal{L} $$.
  - 设 `w` 是任意权函数, 而问题是选取
    $$ \mathcal{L} $$
    的一个具有最大权重元素
    $$ B \in \mathcal{L} $$,
    而所谓一个集合的权重就是其中各个元素权重的和.
- 和上面一样, 贪婪算法从选取具有最大权重的元素 `e` 开始,
  然后再从余下的元素中选取具有最大权重的元素,
  但要服从一个附带要求, 就是在任何阶段,
  选出的元素构成一个属于
  $$ \mathcal{L} $$
  的子集合.
- 因此, 以下事实为真:
  - 当且仅当
    $$ \mathcal{L} $$
    是一个拟阵的所有独立集合的集合时,
    贪婪算法在赋有任意权重函数的
    $$ \mathcal{L} $$
    上管用.
  - 这样, 拟阵成了许多优化问题的"自然的家".
  - 此外, 拟阵这个概念是真正有用的,
    因为许多出现在这种问题中的拟阵都不是从向量空间或从图导出的.

### 模形式


### 赋范空间与巴拿赫空间

### 数域

### 优化与拉格朗日乘子

### 轨道流形

### 序数

### 佩亚诺公理

### 置换群

### 相变

### 概率分布

### 射影空间

### 二次型

### 量子计算

### 量子群

### 四元数, 八元数和赋范除法代数

### 表示

### 里奇流

### 黎曼曲面

### 黎曼函数

### 环, 理想与模

### 概型

### 薛定谔方程

### 单形算法

### 特殊函数

### 谱

### 球面调和

### 辛流形

### 张量积

### 拓扑空间

### 变换

### 三角函数

### 万有覆叠

### 变分法

### 簇

### 向量丛

### 冯·诺依曼代数

### 小波