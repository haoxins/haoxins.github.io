---
title: 伽罗瓦理论 - 群论
description: 天高地迥, 觉宇宙之无穷; 兴尽悲来, 识盈虚之有数.
date: 2021-05-24
---

[研究之美]: https://book.douban.com/subject/7064456/

* 日本原版的封面更好, 哈哈哈

* [Group Explorer](https://github.com/nathancarter/group-explorer)

## 数学女孩5: 伽罗瓦理论

* [数学女孩5: 伽罗瓦理论](https://book.douban.com/subject/35385260/)
  - [结城浩](https://book.douban.com/author/104541/)

* 这一本开启了 数学女孩系列 **新的高度**
  - 期待 **结城浩** 开启数学科普新的篇章
  - 毕竟, 几个学生对话的形式, 对我而言, 不甚喜欢
  - 相较而言, 同样对话形式, 高德纳的 [研究之美](研究之美) 感觉好得多
  - 但是, 作者的讲解, 确实自成体系
  - 想必有了这一套图书的经验, 作者可以重新梳理自己的数学科普体系

* 期待: **数学女孩6: 庞加莱猜想**

* 搭配: [群论彩图版](https://book.douban.com/subject/34879608/)
  - 出版年: 2019-10-01

* 对称多项式的基本定理: **对称多项式可以用基本对称多项式表示**.
  - 由此可知, 只要是*解的*对称多项式,
    不管怎样的式子都可以用*解的*基本对称多项式
    `a+b` 和 `ab` 来表示.
* *解的*对称多项式可以用*解的*基本对称多项式表示.
  - *根据对称多项式的基本定理*
* 从根与系数的关系得知, *解的*基本对称多项式可以用系数表示.
  - 因此, *解的*对称多项式可以用系数表示.
* 而且, 由于二次方程的*解的*对称多项式在调换解的情况下,
  结果仍维持不变, 所以:
  - 在调换解的情况下结果仍维持不变的式子可以用系数来表示.

---

* 群的定义 (群公理)
  - 满足以下公理的集合称为群.
  - 1) 运算 `*` 具有**封闭性**.
  - 2) 对任意的元素而言, **结合律**成立.
  - 3) 存在**单位元**.
  - 4) 对于任意的元素, 存在此元素的**逆元素**.

* 不存在拥有2个单位元的群.

```
始于拉格朗日, 由鲁菲尼, 阿贝尔继承,
被天才伽罗瓦总结而成的方程,
其理论的根本思想是将隐藏在方程解法之中的,
有关置换解的对称性,
通过群的概念, 从光辉之中取出,
将群的作用中的不变性作为扩大域时的原理.
                    - 志贺浩二
```

```
复数系, 1 的 n次方根
  -> 正n边形
  -> 三角函数
  -> 棣莫弗公式
```

* 棣莫弗公式 (三角函数版)

$$ \cos n\theta + i \sin n\theta = \left( \cos \theta + i \sin \theta \right)^n $$

* 棣莫弗公式 (指数函数版)

$$ e^{in\theta} = \left( e^{i\theta} \right)^n $$

* 向量空间的意义在于提供了这样一个角度:
  - 从数学的许多研究对象中,
  - 只挑出**加法**与**点积**这个"*运算的骨架*"来看.
  - (志贺浩二)

---

* `1` 的 `n` 次方根: n 次方等于 1 的数
* `1` 的*原始* `n` 次方根: n 次方后*第一次*等于 1 的数

---

* $$ \langle a \rangle $$ 即:
  - 数 `a` 的 `n` `(n = 1, 2, 3, ...)` 次方可以得到的数的集合
  - 假设 $$
    \zeta{12} =
    cos\frac{2\pi}{12} +
    i sin\frac{2\pi}{12}
    $$,
    以下式子成立.
  - $$ \langle \zeta{12} \rangle = \{
    \zeta {1}_{12},
    \zeta {2}_{12},
    \zeta {3}_{12},
    \zeta {4}_{12},
    \zeta {5}_{12},
    \zeta {6}_{12},
    \zeta {7}_{12},
    \zeta {8}_{12},
    \zeta {9}_{12},
    \zeta {10}_{12},
    \zeta {11}_{12},
    \zeta {12}_{12} \} $$
  - "来做一道题吧. `n` 有无数个, 但为什么集合
    $$ \langle \zeta{12} \rangle $$
    中只有12个元素?"
  - "12 个元素会绕一圈 ..., 比如,
    $$ \zeta \begin{align} {13}\\{12} \end{align} $$
    等于
    $$ \zeta \begin{align} {1}\\{12} \end{align} $$.
    不管多少次方, 都不会超过 `12` 个."

---

* 所有 `1` 的原始 `12` 次方根都能生成循环群
  $$ \langle \zeta{12} \rangle $$.
$$
\langle \zeta {1}_{12} \rangle =
\langle \zeta {5}_{12} \rangle =
\langle \zeta {7}_{12} \rangle =
\langle \zeta {11}_{12} \rangle = \{
\zeta {1}_{12},
\zeta {2}_{12},
\zeta {3}_{12},
\zeta {4}_{12},
\zeta {5}_{12},
\zeta {6}_{12},
\zeta {7}_{12},
\zeta {8}_{12},
\zeta {9}_{12},
\zeta {10}_{12},
\zeta {11}_{12},
\zeta {12}_{12} \}
$$
* 生成元的个数
  - 满足以下等式的整数 `k`, 在 `1≤k<12` 的范围内有 `4` 个.
  - $$
    \langle \zeta{12} \rangle =
    \langle \zeta \begin{align} {k}\\{12} \end{align} \rangle
    $$

---

* 在思考三等分角问题时, 我们能做的只有这些.
  - **直尺**: 画出通过给定的2个点的直线
  - **圆规**: 以给定的2个点的其中一点为中心,
    画出通过另一个点的圆
* 我们明确了使用直尺与圆规可以做的事情, 这是规则.
* 我们可以在*有限的次数*内重复使用直尺与圆规, 因此能画出各种图形.
  刚才已经画出正三角形了.
* 我们要研究的是"用直尺与圆规能画出的图形是什么".

---

* 现在你知道*加减乘除*运算都能用*直尺与圆规*来实现了吧.
  - 整数是*规矩数*, 可以进行*加减乘除*运算,
  - 而有理数是`整数/0以外的整数`, 所以*有理数*都是*规矩数*.
* $$ \mathbb{Z} \subset D $$,
  而且因为 `D` 的*加减乘除*运算具有*封闭性*, 所以也可以说
  $$ \mathbb{Q} \subset D $$.

---

* 因为*规矩数*进行四则运算之后, 仍属于*规矩数*,
  具有*封闭性*, 所以可以说*规矩数*的集合是**域**.

---

* "直线可以写成一次方程, 圆可以写成二次方程,
  它们的交点可以用联立方程组求出来.
  联立方程组中只会出现一次方程与二次方程,
  所以可以通过作图表示的数,
  只有一次方程的解或二次方程的解."
* "然后呢?"
* "一次方程可以用四则运算来解.
  你想想求根公式就知道二次方程要用加减乘除与开根号来解,
  也就是只能用 `2` 次方根来解."
* "没错."
* "总之, 规矩数是:"
  - *重复进行加减乘除运算与开根号运算能得出的数*

---

* $$ x^3 - 3x - 1 = 0 $$
  - 这个三次方程有 `3` 个解, 其中一个解是 `2cos20°`.
  - 所以如果能证明这个方程的解中没有*规矩数*,
    便能证明 `2cos20°` 无法用直尺与圆规作图.
  - 既然 `2cos20°` 不能作图, 那么 `cos20°` 也不能作图;
    既然 `cos20°` 不能作图, 那么 `20°` 也不能作图;
  - 既然 `20°` 不能作图, `60°` 就无法通过直尺与圆规实现三等分.
  - 我想证明的正是这个!

---

* 在方程 $$ x^3 - 3x - 1 = 0 $$ 在域 `K`
  的范围内没有解的前提条件下, 假设在域 $$ K(\sqrt{r}) $$
  的范围内有 $$ p + q\sqrt{r} $$ 这种形式解, 会产生矛盾.
* 设 $$ P = p^3 - 3p - 1 + 3pq^{2}r $$ 和
  $$ Q = (3p^2 + q^{2}r - 3)q $$, 则
  $$ P + Q\sqrt{r} = 0 $$ 成立.
* 但是, 要**怎样引出矛盾呢**?

---

* **线性空间的公理**
  - 当*阿贝尔群* `V` 与*域* `S` 满足以下公理时,
    `V` 称为 `S` 上的**线性空间**
  - 其中 `v` 和 `w` 为 `V` 的任意元素, `s` 和 `t` 为 `S` 的任意元素.
  - VS1: `sv` 是 `V` 的元素. (向量与标量的积)
  - VS2: `s(v + w) = sv + sw` 成立. (标量乘法的分配律)
  - VS3: `(s + t)v = sv + tv`成立. (向量的分配律)
  - 左边的加法是标量的和, 右边的加法是向量的和
  - VS4: `(st)v = s(tv)` 成立. (标量乘法的结合律)
  - VS5: `1v = v` 成立.

---

* $$ \mathbb{Q}(\sqrt{2}) $$ 是在 $$ \mathbb{Q} $$ 中添加
  $$ \sqrt{2} $$ 形成的**域**.
* 首先, $$ \mathbb{Q} $$ 是有理数的集合,
  它可以做四则运算, 因此是**域**.
* 在 $$ \mathbb{Q} $$ 中添加 $$ \sqrt{2} $$ 的域
  $$ \mathbb{Q}(\sqrt{2}) $$ 是使用*有理数*与
  $$ \sqrt{2} $$ 进行*四则运算*时形成的**域**.
* 说几个 $$ \mathbb{Q}(\sqrt{2}) $$ 的元素.
* $$ \mathbb{Q}(\sqrt{2}) $$ 的元素是用*有理数*与
  $$ \sqrt{2} $$ 进行加减乘除的式子!
* `1`, `0`, `0.5`, `-1/3`, `√2`,
  `√2 / 3`, `(1 + 3√2) / (2 - √2)`
* 进行加减乘除的式子称为*有理式*.

---

* **维度**是什么?
  - 首先, 我们将**基**定义为向量的集合, 这个向量的集合能将
    线性空间中任意的点用线性组合表示, 而且是唯一的表示方法.
  - 接着, 将"基的元素数"称为**维度**. 也可以将维度解释为
    在用线性组合表示线性空间的任意一点时*必要且充分*的向量个数.
  - 坐标平面上的任意一点 $$ (a_x, a_y) $$ 可以用
    $$ \overrightarrow{e_x} $$ 和 $$ \overrightarrow{e_y} $$
    这两个向量的线性组合
    $$ a_x \overrightarrow{e_x} + a_y \overrightarrow{e_y} $$
    来表示, 而且是唯一表示方法, 所以这个线性空间是二维的.
  - 任意的复数 `a + bi` 可以用 `1` 与 `i` 这两个向量的线性组合
    `a*1 + b*i` 来表示, 而且是唯一表示方法,
    所以这个线性空间是二维的.

* **线性独立**
  - 假设 `V` 是 `S` 上的线性空间,
    $$ v, w \in V $$ 且 $$ s, t \in S $$.
  - 若以下条件成立, 向量 `v` 与向量 `w` 就是**线性独立**的.
  - $$ sv + tw = 0 \Longleftrightarrow s = 0 \land t = 0 $$
  - 向量 `v` 与 `w` 若不是*线性独立*的, 则是*线性相关*的.
  - *线性独立*又称为**一次无关**, *线性相关*又称为**一次相关**.

* **线性独立** (**一般化**)
  - 将 `V` 视为 `S` 上的线性空间,
    $$ v_k \in V $$ 且
    $$ s_k \in S $$ `(k = 1, 2, 3, ..., m)`.
  - 若以下算式成立, 向量 $$ v_1, v_2, ..., v_m $$
    是**线性独立**的.
  - $$ s_1 v_1 + s_2 v_2 + ... + s_m v_m = 0
       \Longleftrightarrow
       s_1 = 0 \land s_2 = 0 \land ... \land s_m = 0
    $$
  - 若不成立, 向量
    $$ v_1, v_2, ..., v_m $$
    是**线性相关**的.

---

* "**域的扩张可以用线性空间的观点来理解**.
  域 `Q` 与扩域 `Q(a)` 之间扩张的程度, 可以用维度来记述."
* "把域 `Q(a)` 视为 `Q` 上的线性空间. 此时, 我们最多可以
  选择多少个线性独立的向量呢? 也就是说, `Q(a)` 在 `Q` 上是几维的呢?
  要回答这个问题, 就要定量掌握域的扩张, 也就是给 `a` 这个元的
  某个方面赋予某个特征, 而这与线性空间的研究有关."
* "研究? 什么研究?" 我问.
* "当然是对方程解法的研究."
* "方程?" 我疑惑不解. 为什么会提到方程呢?
* "用代数方式解方程, 关键在于因式分解. 做因式分解,
  必须厘清用哪个域来思考. 如果是包含方程的全部解的扩域,
  方程可以因式分解成一次式的积. 方程论就是域的理论."
* "在域中添加元素时, 域会扩张多少呢? 使用线性空间的维度概念
  可以定义扩张的程度 -- **扩张次数**.
  用线性空间的维度概念可以计算**域的扩张**.
  方程的解, 解的个数, 方程的次数, 求根公式这些概念
  对应于线性空间的什么概念呢? 这非常有意思, 因为**线性空间**是
  连接'**方程的世界**'与'**域的世界**'的桥梁.

---

* "对. 我们要站在域的观点来看.
  在系数域中添加 $$ \sqrt{} $$,
  接着添加 $$ \sqrt[3]{} $$,
  就能实现**最小分裂域**."
* "最小分裂域是什么?"
* "最小分裂域是将给定的三次方程分解成
  一次式的最小的域. 普通的三次方程从系数域开始,
  通过添加 $$ \sqrt{} $$ 与 $$ \sqrt[3]{} $$,
  能变成最小分裂域. 由此, 我们能求得三次方程的求根公式.
  在系数域中添加有理式的 `2次方根` $$ \sqrt{D} $$,
  形成新的域后添加求得的有理式的 `3次方根`,
  比如 $$ \sqrt[3]{A + \sqrt{D}} $$ 等,
  从而形成最小分裂域.
* "**在方程的系数域添加方根, 使之变成最小分裂域**,
  **并以此解开方程的过程就是以代数方式解方程**."

---

* 鲁菲尼与阿贝尔证明了五次方程在一般情况下无法解开.
  伽罗瓦指出五次方程在什么情况下能解开, 在什么情况无法解开.
* 除了五次方程, 伽罗瓦还指出了 `n` 次方程
  可以用代数方式解开的*充分必要*条件.

---

* "导出三次方程的求根公式吗?" 我看着卡片.
  - 红色卡片: 契尔恩豪森转换
  - 橙色卡片: 根与系数的关系
  - 黄色卡片: 拉格朗日预解式
  - 绿色卡片: 3次方的和
  - 蓝色卡片: 3次方的积
  - 靛色卡片: 从系数到解
  - 紫色卡片: 三次方程的求根公式

------------------

## 群论彩图版

* [群论彩图版](https://book.douban.com/subject/34879608/)
  - 这本书排版较差

* 凯莱图, (Cayley 图)

> 本书其实也从易于理解的角度, 而非一上来就严格的数学定义去介绍 **群**

* 群论
  - 对称
  - 模式

### 群的代数定义

* *群论*通常是以一种非常代数的方式来研究的,
  因此它所在的数学学科领域被称为*抽象代数*.

* 群运算总是满足*结合律*
* 群的每一个元素都有*逆元*

* **群的定义**
  - 一个*集合* `G` 称为一个*群*, 如果它满足下列条件
  - 1) `G` 上有一个二元运算 `*`
  - 2) 运算 `*` 满足*结合律*
  - $$ \forall a, b, c \in G, 都有 a * (b * c) = (a * b) * c 成立 $$
  - 3) 存在一个*单位元* `e`
  - $$ e \in G, \forall g \in G, 都有 eg = ge = g 成立 $$
  - 4) 每一个元素 $$ g \in G $$ 都有逆元 $$ g^{-1} $$
  - $$ g \in G, gg^{-1} = g^{-1}g = e $$

### 五个群族

* **阶**
  - *阶*是群论中用来描述群的大小或者元素个数的术语.
  - 当讨论整个*循环群族*或者不特指群族中的哪个成员时, 通常用 $$ C_n $$ 来表示,
  - 这意味着 `n` 可以取任意正整数.
  - 最常用的对 $$ C_n $$ 中元素的命名方式, 是把*单位元*叫做 `0`,
  - 把*顺时针*旋转一次叫做 `1`,
  - *顺时针*旋转两次叫做 `2`,
  - 以此类推, 直到 `n-1`.

* **阿贝尔群**
  - 名字来自群论的创始人之一 `Neils Abel`,
    是不管群中作用次序如何排列都没有关系的群.
  - 也就是说, 如果 `a` 和 `b` 是阿贝尔群中的任意两个作用,
    那么先作用 `b` 再作用 `a` 与先作用 `a` 再作用 `b` 是一样的结果.
  - 用代数语言说就是 `a` 与 `b` **可交换**,
    因此, 阿贝尔群也常常叫做**交换群**.
  - 等式 `ab = ba` 表明 `a` 与 `b` 可交换;
    当这个等式对群中的任意两个元素 `a` 和 `b` 都成立时,
    这个群就是**阿贝尔**的.

* 一个具有`n`条边的正多边形叫做正`n`边形,
  描述正`n`边形对称的二面体群记作 $$ D_n $$.
  由于旋转会保持正多边形占据的空间不变,
  所以 $$ C_n $$ 中的所有作用也是 $$ D_n $$ 中的作用.
* 然而, 由于正多边形还允许做翻转作用,
  所以我们猜测 $$ D_n $$ 含有比 $$ C_n $$ 更多的元素,
  而事实也确实如此.
* $$ C_n $$ 含有`n`个作用,
  而 $$ D_n $$ 含有的是 $$ C_n $$ 的两倍, 也就是`2n`个.

* 任何*非翻转元*乘*非翻转元*是*非翻转元*.
* 任何*非翻转元*乘*翻转元*是*翻转元*.
* 任何*翻转元*乘*非翻转元*是*翻转元*.
* 任何*翻转元*乘*翻转元*是*非翻转元*.

* Cayley
  - 每个群都同构于一个*置换群*.

### 子群

* 正则
  - 如果一个图在整个图中重复了其内部的每一个模式,
    那么我们就称这个图为*正则的*.
  - 特别地, 每个凯莱图都是正则的;
    不具有正则性的图不能表示群,
    因此不是凯莱图.

* **子群**
  - 当一个群完全包含在另一个群中时,
    内部的群称为外部群的一个*子群*.
  - 当群 `H` 是群 `G` 的一个子群时, 记为 `H<G`.

* 每个群都有子群, 原因如下:
  - 单位元自己构成的集合 `{e}`, 是任意群的一个子群, 称为*平凡子群*.
  - 另外, 严格来说, 每个群都是它自身的一个子群, 称为*非真子群*.

* *陪集*
  - 它们从结构上是一个子群的副本, 但本身不是群.

* 当集合被分成类, 每个元素恰好只属于一个类时,
  称之为集合的一个*划分*.

* 如果 `H` 是群 `G` 的一个子群,
  那么 `G` 的每个元素*属于且只属于* `H` 的一个*左陪集*.

* **拉格朗日定理**
  - 如果 `H<G`, 那么子群 `H` 的阶 `|H|` 整除群 `G` 的阶 `|G|`.

* 指数
  - 如果 `H<G`, 那么 `H` 在 `G` 中的指数, 记为 `[G:H]`,
  - 指的是 `|G|` 是 `|H|` 的多少倍. 即
  - `[G:H] = |G| / |H|`

### 积与商

* 正规子群
  - 子群 `H<G` 称为*正规的*,
    如果 `H` 的每个*左陪集*都是 `H` 的
    一个*右陪集*(反之亦然).
  - 我们用 $$ H \triangleleft G $$ 表示 `H` 是 `G` 的*正规子群*.

* 如果 `H<G`, 那么仅当 $$ H \triangleleft G $$ 时,
  才能构建*商群* `G/H`.

### 伽罗瓦理论

* **域**
  - 集合 `S` 关于加法和乘法构成一个*域*, 如果以下三个条件满足:
  - (1) `S` 关于加法构成一个*阿贝尔群*.
  - (2) 从这个群中删除*单位元*(*零元*)所得的集合关于
    乘法也构成一个*阿贝尔群*.
  - (3) 加法和乘法满足分配律: `a(b + c) = ab + ac`
  - *有理数*集 `Q`, *实数*集 `R`, *复数*集 `C` 都是*域*.

* 一个*多项式*等于零的方程的求解方法可用于求解任何*算术方程*,
  因为任何*算术方程*都可化简成这种形式.

---

* 无理数中与大问题最相关的是*平方根*, *立方根*和*其他方根*.
  如果能取平方根, 就可以用二次公式解任何二次方程.
  如果能取立方根, 就可以用三次公式解任何三次方程.
  如果能取四次方根, 就可以用四次公式解任何四次方程.
  你可以看出, 如果认为可利用五次方根写出一个公式解五次多项式方程,
  那是多么想当然的事. 然而*阿贝尔*和*伽罗瓦*对大问题的答案却是否定的.
  就在五次这个点上, 根式对解多项式方程失效了.

---

* 某些实数和复数不是任何代数方程的解, 这样的数称为**超越数**,
  那些是多项式方程解的数称为**代数数**. `π` 和 `e` 都是
  众所周知的*超越数*.
  - 根式的引人对 `Q` 的超越程度与解多项式方程一样吗?
  - 或者说多项式能否仅用*算术运算*和*根式*来解?
  - 大问题就是关于这两个基本数学运算之间的关系的.

* 古希腊人在几何领域提出过三个著名的问题:
  - 能否用几何的基本操作 (即用直尺和圆规)
    - 化圆为方
    - 立方倍积
    - 三等分角
* 你可以看出它们与大问题的相似性, 每个都是某种操作后能走多远的问题.
* 由于代数和几何的紧密关系, 这三个问题也能用伽罗瓦理论来回答.
* 当分析超出 `Q` 而到达新**域**的操作时, 伽罗瓦理论是有用的.
  大问题可以用伽罗瓦理论来回答, 数学中的一些其他历史问题也可以.
* 我之所以提起三大几何问题是为了说明伽罗瓦理论不仅能解决本章提出的问题.

---

* 每个*根集*都是它自身关于 `x` 轴的镜面反射,
  因此竖直翻转将保持*根集*的形状.
  看出多项式*根集*的对称性是伽罗瓦理论的第一步.
* *复共轭*
  - 对任意复数 `a + bi`, 我们称 `a - bi` 是它的*复共轭*(或简称*共轭*).
  - 若 `c` 为任意复数, 则用 $$ \overline{c} $$ 表示它的*复共轭*.

* *复共轭根定理*
  - 如果 `r` 是一个多项式的根,
  - 那么它的共轭 $$ \overline{r} $$ 也是该多项式的根.
  - 因此, 每个多项式的根集在复平面上关于 `x` 轴镜面对称.