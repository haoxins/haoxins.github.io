---
title: 庞加莱猜想, 基础拓扑学
description: 梧桐更兼细雨, 到黄昏, 点点滴滴. 这次第, 怎一个愁字了得!
date: 2022-09-30
---

- [数学女孩6: 庞加莱猜想](https://book.douban.com/subject/36072389/)
  - https://www.ituring.com.cn/book/2786
  - 数学女孩系列, 有始有终~

> 总的来说, 比较失望~ 数学的内核淡了, 多余的人物对话反而占据了过多篇幅!

```
从第五本 数学女孩 5: 伽罗瓦理论 出版到本书完成已经过了六年.
会隔那么久, 主要是因为我需要一段时间好好消化庞加莱猜想的内容.
本书提到的数学内容主要包括:
拓扑学, 基本群, 非欧几何, 微分方程, 流形, 傅里叶展开式以及庞加莱猜想.
```

```
数学女孩 6: 庞加莱猜想 中介绍了基本群 (一维同伦群).
拓扑学相关的书中会出现与同伦群名称相似的同调群, 不过二者并不相同.
我刚开始读拓扑学的书时, 就把同伦群和同调群弄混了.
初次接触拓扑学的读者还请将上述内容牢记在心.
```

- 无内外之分的性质在数学上称为`不可定向性`.
  - `不可定向性`在闭曲面的分类上是一个很重要的基准.

```
闭曲面的分类 (连通和)
可定向
球面与 n 个环面的连通和 (n = 0, 1, 2, ...)
不可定向
球面与 n 个射影平面的连通和 (n = 1, 2, 3, ...)

闭曲面的分类 (连通和)
可定向
将 n 个环柄粘在有 n 个圆形切口的球面上形成的闭曲面 (n = 0, 1, 2, ...)
不可定向
将 n 个默比乌斯带粘在有 n 个圆形切口的球面上形成的闭曲面 (n = 1, 2, 3, ...)
```

> 从`开集公理`开始, 然后是`映射连续`的定义, 再到`同胚`.

- 在拓扑的世界中, 所有距离的概念都会被舍弃.

```
拓扑空间是在支撑集 S 中添加拓扑结构建立而成的,
这与群论中往集合里添加群结构时的情况相同.
正如我们可以用群公理来定义群,
我们也可以用开集公理来定义拓扑空间.
```

### 非欧几何

```
球面几何
不存在通过直线 l 外一点 P 且不与 l 相交的直线

欧几里得几何
存在一条通过直线 l 外一点 P 且不与 l 相交的直线

双曲几何
存在两条或两条以上通过直线 l 外一点 P 且不与 l 相交的直线
```

```
彼时, 以平行公理作为起点构建起来的几何学体系,
已经朝着通过引入其他公理取代平行公理来创立新几何学的方向进步了.
黎曼又向世人展示了不必执着于平行公理, 通过度量便可构建出无数几何学这一理论.
这使得人们对于空间的研究前进了一大步. 其研究对象, 在现代数学中被称为黎曼流形.
```

> 黎曼先生, 千古!

### 流形

```
试着想象一下无边无际的宇宙.
在宇宙中漂浮着一个立体图形, 其外围的整个宇宙,
就是第八个立方体的内部. 这个内外翻转的,
内部包含了整个宇宙的立方体有六个正方形的面,
各个面分别与六个金字塔的底面黏合.
```

```
三维球面和三维骰子面同胚, 是三维流形的一种.
因此, 我们可以把三维球面和三维骰子面当成同样的东西.
```

- 振动是旋转的投影

```
在拓扑空间 X 上取一固定点 p

设集合 F 为以 p 为基点的所有自环的集合

将同伦视为一种等价关系. 将集合 F 除以等价关系 ~,
可得到所有同伦类的集合 F/~

集合 F/~ 的元素为"连续变形后可视为等价的自环的集合"

加入群的运算方法, 使集合 F/~ 成为一个群.
考虑集合 F/~ 的元素, 也就是同伦类之间"连接"的操作,
将其视为群内的运算方法. 因为所有自环共享基点 p,
所以这些自环一定可以连接起来

由这种方法得到的群就叫作"在拓扑空间 X 中, 以 p 为基点的基本群"
```

### 高斯绝妙定理

- 不变量十分重要. 只要没有伸缩曲面, 那么曲面上任意点的高斯曲率就不会改变.
  球面上任意一点的高斯曲率皆等于
  $$ \frac{1}{R^2} $$,
  而平面上任意一点的高斯曲率皆等于 `0`.
  - 也就是说, 在没有伸缩的情况下, 我们不可能将球面展开在平面上.
  - 只要知道曲面的高斯曲率不是 `0`, 便可判断出该曲面无法展开在平面上.

- 在曲面上, 由长度和角度得到的量称为`内蕴量`;
  由曲面镶嵌于空间中的方式所决定的量称为`外蕴量`.
  - 虽然高斯曲率 `K` 是通过外蕴量来定义的,
    但高斯的计算最终证明了它其实是内蕴量.
  - 高斯曲率是第一个被发现的内蕴量.
- 高斯曲率明明是由外蕴性的量定义出来的,
  却可表现出内蕴性的量是多少. 这实在太绝妙了.
  - 因此, 高斯就把这个定理称作`绝妙定理`.

---

- 在球面几何, 欧几里得几何, 双曲几何中, 高斯曲率 `K` 为常数.
  若高斯曲率 `K` 为常数, 则可称该空间拥有`齐性`.
  - 高斯曲率不会随着空间内位置的变化而发生改变.
- 我们可以设齐性条件不成立, 以此进行一般化.
  这表示高斯曲率 `K` 会随着空间中点 `p` 位置的变化而发生改变.
  - 此时高斯曲率就会变成 `K(p)` 这样的函数.
- 于是, 我们之前想到的求
  $$ ΔABC $$
  面积的公式, 就不是单纯的乘积, 而是积分了.
  - 法国数学家博内将公式扩展后, 得到了`高斯-博内定理`.
  - $$ α + β + γ - π = KS_{ΔABC} $$
    当高斯曲率为常数 `K` 时
  - $$ α + β + γ - π = \iint_{S_{ΔABC}} K(p) dS $$
    当高斯曲率为函数 `K(p)` 时
- 高斯曲率是函数 `K(p)`, 表示我们只要知道曲面中的位置,
  就能知道高斯曲率是多少.
  - 因为弯曲程度不会随着方向的变化而改变是前提,
    所以这里还有进一步一般化的余地.
    这样的性质称为`各向同性`.
  - 从数学层面考虑某个点 `p` 的弯曲程度时,
    不会将其想成高斯曲率这种实数,
    而是会将其想成`曲率张量`.

### 庞加莱猜想

```
物理学的世界 vs 数学的世界

热传导方程      里奇流方程
热传导体        三维闭流形
位置 x         位置 x
时间 t         参数 t
温度           黎曼度量 (里奇曲率)
温度的均匀化    里奇曲率的均匀化
```

------------------

- [基础拓扑学 (修订版)](https://book.douban.com/subject/34899142/)
  - 原作名: __Basic Topology__

> 本书并未提前详述一些分析的概念, 所以需要阅读前置书籍, 比如:
  [普林斯顿数学分析读本](https://book.douban.com/subject/35172355/)

```
常见变换的性质比较

变换名称 自由度 不变性质
欧氏变换  6    长度, 夹角, 体积
相似变换  7    体积比
仿射变换  12   平行性, 体积比
射影变换  15   接触平面的相交和相切
```

- 一个`多面体`是指按下述意义很好地拼凑在一起的有限多个`平面多边形`:
  - 若两个多边形相交, 则它们交于一条公共边;
    多边形的每一条边恰好还是另一个 (且只有这一个) 多边形的边.
  - 不仅如此, 还要求对于每个顶点, 那些含有它的多边形可以排列成
    $$ Q_1, Q_2, ..., Q_k $$,
    使得
    $$ Q_i $$
    与
    $$ Q_{ i + 1 } $$
    有一条公共边,
    $$ 1 ≤ i < k $$,
    而
    $$ Q_k $$
    与
    $$ Q_1 $$
    有一条公共边.
  - 换句话说, 这些多边形拼成围绕着该顶点的一块区域
    (多边形的数目 `k` 则可以随顶点的不同而变动).
- 其中最后一个条件就使两个立方体只在一个公共顶点相衔接的情形排除在外了.

---

- __Euler 定理__ 设 `P` 为满足下列条件的多面体:
  - (1) `P` 的任何两个顶点可以用一串棱相连接;
  - (2) `P` 上任何由直线段 (不一定非是 `P` 的棱) 构成的圈,
    把 `P` 分割成两片.
  - 则对于 `P` 来说, `v - e + f = 2`.
  - 若以 `T` 来记`树`形, 则可以写成公式 `v(T) - e(T) = 1`

- 拓扑等价的多面体具有相同的 `Euler` 数.

```
空间的每点有一组"邻域", 这些邻域又引出了连续映射的适当定义, 这就是关键所在.
注意在欧氏空间内定义邻域时完全依靠两点之间的欧氏距离, 在构造抽象空间时,
我们希望保留邻域的概念, 但要避免对距离概念的任何依赖 (拓扑等价不保持距离).
```

- [拓扑空间](https://en.wikipedia.org/wiki/Topological_space)
  - __邻域__

- __定义__ 曲面是这样的拓扑空间,
  - 它的每一点有同胚于平面的邻域,
  - 并且任意不同的两点有不相交的邻域.

- __分类定理__ 任何闭曲面或者同胚于球面,
  或者同胚于添加了有限多个环柄的球面,
  或者同胚于挖去有限多个圆盘而以莫比乌斯带代替的球面.
  - 而这些曲面中的任何两个都不同胚.

- [基本群](https://en.wikipedia.org/wiki/Fundamental_group)

### 连续性

- __定义__ 集合 __X__ 上的一个`拓扑`是由 __X__ 的子集所构成的一个非空组,
  它的成员叫作开集, 它们满足下列要求:
  - 任意多个开集的并集是开集,
  - 有限多个开集的交集是开集,
  - __X__ 与空集是开集.
- 集合配备了它上面的一个拓扑以后叫作`拓扑空间`.
  - 以后, 我们将采用这个定义.

- [度量空间](https://en.wikipedia.org/wiki/Metric_space)

- __Tietze 扩张定理__
  在度量空间的闭子集上定义的任何连续实值函数可以扩张到整个空间.

### 紧致性与连通性

- 连通性的定义可以用多种方式来陈述. __定理__
  对于空间 __X__, 下列条件是等价的:
  - (a) __X__ 连通;
  - (b) __X__ 内同时为开集与闭集的子集只有 __X__ 与空集;
  - (c) __X__ 不能表示为两个不相交非空开集的并集;
  - (d) 不存在连续满映射从 __X__ 到一个多于一点的离散拓扑空间上去.

### 单纯剖分

```
把全体拓扑空间作为我们讨论的对象未免过于宽泛.
在前几章我们曾经看到怎样建立拓扑空间与连续映射的抽象理论, 并且证明了许多重要结果.
但是, 在这样宽泛的基础上进行工作, 很快就会碰到两类困难.
一方面, 当人们试图证明具体的几何结果, 比如像曲面的拓扑分类时,
曲面的 (局部欧氏的) 纯拓扑结构不能提供很多从何着手的依据;
另一方面, 虽然能对很一般的拓扑空间定义代数的不变量, 诸如基本群,
但是, 除非我们能对足够广泛的一类空间对这些不变量进行计算, 它们的用处仍然显不出来.
但如果空间可由很多我们所熟识的空间很好地拼凑起来构成,
即空间是所谓可单纯剖分的空间, 这两个问题都能得到有效的处理.
```

- [单纯复形](https://en.wikipedia.org/wiki/Simplicial_complex)
  - [单纯形](https://en.wikipedia.org/wiki/Simplex)
- [自由群](https://en.wikipedia.org/wiki/Free_group)
  - [自由积](https://en.wikipedia.org/wiki/Free_product)
- [同调论](https://en.wikipedia.org/wiki/Homology_(mathematics))
- [塞弗特-范坎彭定理](https://en.wikipedia.org/wiki/Seifert-Van_Kampen_theorem)

```
这里给出无穷复形的一个尝试性的定义, 并不算最广义的, 但对我们的需要来说已经足够.
```

- __定义__ 欧氏空间
  $$ \mathbf{E}^n $$
  内一个由单纯形构成的无穷集合, 如果满足下列条件就叫作无穷单纯复形:
  - (a) 若某个单纯形属于这个集合, 则它所有的面也属于该集合;
  - (b) 这个集合的单纯形很好地拼合;
  - (c) 这个集合全体单纯形的并集是
    $$ \mathbf{E}^n $$
    内的闭集;
  - (d) 在这个并集上, 诱导拓扑与粘合拓扑重合.

- __定理__ 设 `K` 为
  $$ \mathbf{E}^n $$
  内的无穷单纯复形, 以
  $$ \mid K \mid $$
  表示它的多面体, 则
  - (a) `K` 是有限维的;
  - (b) `K` 的单纯形总数是可数的;
  - (c) `K` 是局部有限的 (就是说, `K` 的每个顶点只在有限多个单纯形上);
  - (d)
    $$ \mathbf{E}^n $$
    的每一点有那样的邻域, 它至多只与有限多个 `K` 的单纯形相交.

### 曲面

- [曲面](https://en.wikipedia.org/wiki/Surface_(topology))

- [欧拉示性数](https://en.wikipedia.org/wiki/Euler_characteristic)

- __定理__ 每个闭曲面同胚于标准闭曲面之中的一个.

```
H(p) 叫作亏格为 p 的标准可定向曲面, M(q) 叫作亏格为 q 的标准不可定向曲面.
一旦知道一个闭曲面的亏格以及是否可定向, 这个闭曲面就完全决定了.
```

---

- 近来拓扑学方面的许多工作围绕着关于流形的研究. 这是类似于曲面的高维对象.
  一个 `n` 维流形, 或简称 `n` 流形, 是一个第二可数的 Hausdorff 空间,
  它的每一点有邻域同胚于
  $$ \mathbf{E}^n $$.
- 空间
  $$ \mathbf{E}^n $$,
  $$ S^n $$,
  $$ P^n $$
  都是 `n` 流形;
  $$ S^3 \times S^1 $$
  是闭的 `4` 流形 ("闭" 意思是紧致连通);
  `n` 流形内的任何开集是 `n` 流形, 因此,
  $$ GL(n) $$
  是
  $$ n^2 $$
  维流形;
  $$ SO(n) $$
  是一个
  $$ n (n-1) / 2 $$
  维闭流形; 最后, 透镜空间
  $$ L(p, q) $$
  都是闭 `3` 流形.
  - 这方面的研究虽然取得了很大进展, 但许多基本问题尚未得到解答.
  - 最重要的是著名的 `Poincaré` 猜想.
  - 如果表达成问题的形式, 它问道, 是否每一个单连通的三维闭流形同胚于
    $$ S^3 $$.

---

- [同调](https://en.wikipedia.org/wiki/Homology_(mathematics))
- [映射度](https://en.wikipedia.org/wiki/Degree_of_a_continuous_mapping)
- [Lefschetz fixed-point](https://en.wikipedia.org/wiki/Lefschetz_fixed-point_theorem)

------------------

- [普林斯顿数学指南 (第二卷)](https://book.douban.com/subject/25817383/)

> 放弃阅读!
  涵盖内容过广, 每个独立章节又不够深入, 无从看起~

---

- [李群与李代数基础](https://book.douban.com/subject/35533338/)
  - [柯西-利普希茨定理](https://en.wikipedia.org/wiki/Picard-Lindelöf_theorem)
  - [利普希茨连续](https://en.wikipedia.org/wiki/Lipschitz_continuity)
  - [隐函数定理](https://en.wikipedia.org/wiki/Implicit_function_theorem)
  - [魏尔斯特拉斯预备定理](https://en.wikipedia.org/wiki/Weierstrass_preparation_theorem)

> 买书之后, 闲置了蛮长时间, 2024-07-22, 决定放弃阅读本书.
  因为等到有计划 (时间, 预备知识储备) 阅读本书的时候,
  估计会选择更优质的书籍~
