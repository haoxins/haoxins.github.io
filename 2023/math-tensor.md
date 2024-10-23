---
title: 矢量 张量
description: 碧云天, 黄叶地, 秋色连波, 波上寒烟翠. 山映斜阳天接水, 芳草无情, 更在斜阳外.
date: 2023-01-30
---

- [张量学习三讲](https://book.douban.com/subject/30236465/)

> 印刷错误很多!

```
对偶坐标系, 指标表示, 求和约定, 坐标变换.
```

- 约定 1: 省去求和符号;
- 约定 2: 自由标;
- 约定 3: 指标.

```
对偶记法在张量分析中非常有用:
既区分不同的坐标系和它的基矢量, 又便于微分和乘法运算.
```

### 斜角直线坐标系

- 由此给出了基矢量的定义
  $$ \mathbf{g}_i = \frac{\partial \mathbf{r}}{\partial x^i} $$
  或
  $$ \mathbf{g}^i = \frac{\partial \mathbf{r}}{\partial x_i} $$,
  它与笛卡儿坐标系的单位矢量之间的关系很容易得出
  - $$
      \mathbf{g}_i =
      \frac{d \mathbf{r}}{d x^i} =
      \frac{\partial \mathbf{r}}{\partial x^i} =
      \frac{\partial x}{\partial x^1} \mathbf{i} +
      \frac{\partial y}{\partial x^2} \mathbf{j} +
      \frac{\partial z}{\partial x^3} \mathbf{k}
    $$

### 曲线坐标系

```
显然, 对于笛卡儿直角坐标系, 单位基矢量不随坐标的改变而变化, 克氏符号为零.
因此, 可以将克氏符号理解为基矢量的增量与坐标增量之间的比例系数 (也称作联络系数),
也可以理解为曲线坐标系中同一个矢量平移时, 方向的改变引起的附加增量
(可以设想, 这些平移矢量 (切线) 在局地形成的所谓"切丛"之间的联络系数,
反映在不同点处矢量方向的改变, 又称为纤维丛, 在规范场中具有重要意义,
其中"丛"和"联络"的原义来之于灌木丛及其枝杈交叉的类比).
要注意, 由拉梅常数也可以表示克氏符号, 但克氏符号不是张量的分量, 只在曲线坐标系才有意义.
```

### 运算规则

- [Jacobian matrix and determinant](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant)

- 为了描述流体质点在流场中的运动, 两个坐标系:
  - 作用在流体质点上的力矢量在随流体质点运动的坐标系
    (可以分解为三个基矢量);
  - 参考坐标系, 通常的笛卡尔坐标系
    (运动的坐标系的每个基矢量可在此分解为三个基矢量).
- 张量在这个意义下, 可以说是矢量的矢量或多重矢量,
  它的分量组成作用力 __F__ 的二阶张量
  - $$
      \begin{align}
        \mathbf{F}_{ij}
          & = \mathbf{F} \mathbf{e}_i \mathbf{g}_j \\
          & = \begin{bmatrix}
                F_{xx} & F_{xy} & F_{xz} \\
                F_{yx} & F_{yy} & F_{yz} \\
                F_{zx} & F_{zy} & F_{zz}
              \end{bmatrix}
      \end{align}
    $$
  - 换句话说, 当一个作用量的分量在不同的方向上对物体均有影响或作用时,
    就需要张量描述.

---

- 其实两个矢量 __a__ 和 __b__ 的并矢就是二者的相互作用, 各自有 `3` 个分量,
  相互作用形成 `9` 个分量
  ($$ a_i b_j $$
  或
  $$ a^i b^j $$)
  的集合就是张量, 这种相互作用用
  $$ \otimes $$
  符号表示 (或称作直积或线性投影算子), 也可以省略, 如下式所示
  - $$
      \mathbf{a} \otimes \mathbf{b} =
      \mathbf{a} \mathbf{b} =
      a^i b^j \mathbf{g}_i \mathbf{g}_j =
      a_i b_j \mathbf{g}^i \mathbf{g}^j =
      a_i b^j \mathbf{g}^i \mathbf{g}_j =
      a^i b_j \mathbf{g}_i \mathbf{g}^j
    $$

- 张量的并矢表示
  ($$ T^{ij} \mathbf{g}_i \mathbf{g}_j $$)
  在新旧坐标系中具有相同的形式, 即:
  $$
    T^{ij} \mathbf{g}_i \mathbf{g}_j =
    T^{i'j'} \mathbf{g}_{i'} \mathbf{g}_{j'}
  $$,
  因此, 这种表示也称作不变性表示, 意指不随坐标系的不同而改变, 反映了物理规律的客观性.

------------------

- [线性代数入门](https://book.douban.com/subject/36432607/)
  - 语言简练
  - 排版较差

> 支持一下`图灵数学经典`, 希望后面的翻译能快一点~

- 映射是一般化的函数概念.

> 第一章 平面向量和空间向量:
  先把`线性变换`的定义拎出来, 再在二三阶矩阵下验证.
  提了一下二三阶行列式的几何意义.

```
注: 根据这些性质, 我们可知 n 阶可逆矩阵全体的集合是一个"群".
换言之, 集合中的元素可进行乘法运算且满足结合律. 与此同时,
单位矩阵属于这个集合且集合中每个元素都存在逆矩阵.
```

- 两个对角矩阵满足乘法交换律, 是可交换矩阵.
  - 对角矩阵 __A__ 可逆的充分必要条件是
    $$ a_i ≠ 0 $$
    $$ (i = 1, 2, ..., n) $$.

- `n` 阶矩阵 __A__ 可逆的充分必要条件是 __A__ 的秩等于 `n`.

- 实际上, 写出
  $$ n \times 2n $$
  矩阵
  $$ (\mathbf{A} $$
  $$ \mathbf{E}) $$,
  只对它进行上述初等行变换, 最后得到的结果就是
  $$ (\mathbf{E} $$
  $$ \mathbf{A}^{-1}) $$.
  - 如果上述过程中途进行不下去了, 可说明 __A__ 不可逆.
  - 换言之, 这个方法还可以判断 __A__ 是否可逆.

- [酉矩阵](https://en.wikipedia.org/wiki/Unitary_matrix)

> 第二章 矩阵:
  可惜了, `酉矩阵`未详细展开

- 在 `n` 元置换中, 我们把只交换两个元素,
  固定其他 `(n - 2)` 个元素的置换叫作`换位`.
  - 任何置换都可用多个换位之积表示.
  - 实际上, 通过多次交换相邻两个元素,
    我们总能够把 `n` 个元素按照任何顺序排列.
- 任何置换都可用多个换位之积表示. 但是,
  换位次数的奇偶性由最初的置换决定,
  与换位之积的表示方法无关.

- 把矩阵 __A__ 的某行或某列乘以某数, 再把它加到另一行或另一列,
  行列式的值与最初的矩阵 __A__ 的行列式
  $$ \mid \mathbf{A} \mid $$
  相等.

- 方块矩阵 __A__ 可逆的充分必要条件是
  $$ \mid \mathbf{A} \mid ≠ 0 $$.

> 第三章 行列式:
  从`置换`与`群`的视角开始.

### 线性空间

> 从`集合`与`映射`的现代视角开始.

- 定义: 设 `T` 为从
  $$ \mathbf{V} $$
  到
  $$ \mathbf{V}' $$
  的线性映射, 此时, 像空间
  $$ T (\mathbf{V}) $$
  的维数称为 `T` 的`秩`.
  - 可知, `T` 的秩与
    $$ dim \mathbf{V} - dim T^{-1} (\mathbf{0}') $$
    相等.

- 对于 __V__ 的两个元素 __x__, __y__, 规定其内积为
  $$ \mathbb{K} $$
  的元素 (记作 (__x__, __y__)). 具体性质如下.
  - (1)
    $$
      (\mathbf{x}, \mathbf{y}_1 + \mathbf{y}_2) =
      (\mathbf{x}, \mathbf{y}_1) + (\mathbf{x}, \mathbf{y}_2)
    $$,
    $$
      (\mathbf{x}_1 + \mathbf{x}_2, \mathbf{y}) =
      (\mathbf{x}_1, \mathbf{y}) + (\mathbf{x}_2, \mathbf{y})
    $$.
  - (2)
    $$ (c \mathbf{x}, \mathbf{y}) = c (\mathbf{x}, \mathbf{y}) $$,
    $$ (\mathbf{x}, c \mathbf{y}) = \bar{c} (\mathbf{x}, \mathbf{y}) $$.
  - (3)
    $$ (\mathbf{x}, \mathbf{y}) = \bar{(\mathbf{y}, \mathbf{x})} $$.
  - (4)
    $$ (\mathbf{x}, \mathbf{x}) $$
    的值可为 `0` 或正数, 当且仅当
    $$ \mathbf{x} = \mathbf{0} $$
    时,
    $$ (\mathbf{x}, \mathbf{x}) = 0 $$.
- 当
  $$ \mathbb{K} = \mathbb{R} $$
  时, 即不存在共轭复数, 字母上的横杠可以去掉.
  实度量线性空间也称为`欧几里得空间`, 简称`欧氏空间`.
  复度量线性空间称为`酉空间`.
- $$ (\mathbf{x}, \mathbf{x}) $$
  的非负平方根称为 __x__ 的`长度`或`范数`, 记作
  $$ \| \mathbf{x} \| $$.
  - 当
    $$ (\mathbf{x}, \mathbf{y}) = 0 $$
    时, 我们称 __x__ 和 __y__ 正交.

- 对于度量空间 __V__ 的子空间 __W__, __V__ 中正交于 __W__
  中所有元素的元素集合也是 __V__ 的子空间.
  - 我们把它称为 __W__ 的`正交补空间`, 记作
    $$ \mathbf{W}^{\perp} $$.
  - 定理: __V__ 是 __W__ 和
    $$ \mathbf{W}^{\perp} $$
    的直和.
  - $$ (\mathbf{W}^{\perp})^{\perp} = \mathbf{W} $$.
  - $$
      (\mathbf{W}_{1} + \mathbf{W}_{2})^{\perp} =
      \mathbf{W}_{1}^{\perp} \cap \mathbf{W}_{2}^{\perp}
    $$.
  - $$
      (\mathbf{W}_{1} \cap \mathbf{W}_{2}) =
      \mathbf{W}_{1}^{\perp} + \mathbf{W}_{2}^{\perp}
    $$.

---

- 定义: `酉空间` (`实度量空间`) __V__ 到 __V__
  自身的等距同构映射称为 __V__ 的`酉变换` (`正交变换`).

- __V__ 的酉变换 (正交变换) `T` 在任意标准正交基
  $$ (E; \varphi) $$
  下的矩阵为酉矩阵 (正交矩阵).
  - 反之, 若 __V__ 的线性变换 `T` 在任意标准正交基下的矩阵为酉矩阵 (正交矩阵),
    则 `T` 为酉变换 (正交变换).

### 特征值和特征向量

- 若非零向量 __x__ 是 `T` 的特征向量, 则 __x__ 张成的一维子空间
  $$ \left \{ c \mathbf{x} \mid c \in \mathbb{K} \right \} $$
  是 `T-不变子空间`.
- 当 `a` 是 `T` 的特征值时, 零向量和对应于 `a` 的所有 `T`
  的特征向量构成的集合
  $$ \mathbf{W}_{a} $$
  是 __V__ 的非零线性空间 `T-不变子空间`,
  我们把它称为对应于特征值 `a` 的 `T` 的`特征空间`.
  - `T` 到
    $$ \mathbf{W}_{a} $$
    上的限制
    $$ T_{\mathbf{W}_{a}} $$
    与数乘变换
    $$ a I $$
    相等.
- 当 __A__ 是 `n` 阶矩阵时, 由 __A__ 确定的
  $$ \mathbb{C}^{n} $$
  (注意不是
  $$ \mathbb{R}^{n} $$
  !) 的线性变换
  $$ T_{\mathbf{A}} $$
  的特征值, 特征向量, 特征空间分别为矩阵 __A__
  的特征值, 特征向量, 特征空间.
- 当 `T` 是复线性空间 __V__ 的线性变换时,
  若 `T` 在 __V__ 的任意基
  $$ (E; \varphi) $$
  下的矩阵为 __A__, 则 `T` 和 __A__ 的特征值相同,
  特征向量, 特征空间分别随
  $$ \varphi $$
  发生变化.
- 若
  $$ \mathbb{K} $$
  上的线性空间 __V__ 的线性变换 `T` 的一个特征值为 `0`,
  那么根据定义可知, `T` 为不可逆变换.

---

- 矩阵 __A__ 与对角矩阵相似 (也就是存在正规矩阵 __P__ 使
  $$ \mathbf{P}^{-1} \mathbf{A} \mathbf{P} $$
  为对角矩阵) 的充分必要条件是, 对应于 __A__ 的各特征根 `a`
  的特征空间的维数与 `a` 的重数相同.
  - 若 __A__ 的特征根全部不同, 则 __A__ 与对角矩阵相似.
  - 若 __A__ 为实矩阵且其特征根全为实数,
    则选取的 __P__ 一定是实可逆矩阵.

------------------

- [线性代数](https://book.douban.com/subject/34820335/)

> 需要开始习惯英文的数学, 物理书籍了.

```
2023 年 5 月, Gilbert Strang 大师, 正式退休.
致敬!
```

- [Graphic notes on Gilbert Strang's "Linear Algebra for Everyone"](https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra)

```
Gilbert Strang, an MIT mathematics professor,
received a standing ovation after giving his
last linear algebra lecture on Monday.

After 63 years teaching and over 10 million
views on his online lectures, MIT professor
Gilbert Strang received a standing ovation
from his students Monday once he completed
his last linear algebra lecture.

The mathematics professor graduated from MIT
in 1955 and has since published several books
on linear algebra and differential equations.
He was one of the first professors to publish
his lectures on the institute's online
open learning library OpenCourseWare, or OCW,
and continues to fall within the top 10
most viewed lecturers at MIT.
```

### Solving Linear Equations

> 首先, 强调`线性变换`的概念.

- You may like the row picture better,
  but only for one day.
  - 哈哈哈

---

- If `A` and `B` are `n` by `n`, so is `AB`. It contains
  $$ n^2 $$
  dot products, row of `A` times column of `B`.
  Each dot product needs `n` multiplications,
  so the computation of `AB` uses
  $$ n^3 $$
  separate multiplications.
  - For `n = 100` we multiply a million times.
  - For `n = 2` we have
    $$ n^3 = 8 $$.
- Mathematicians thought until recently that `AB`
  absolutely needed
  $$ 2^3 = 8 $$
  multiplications. Then somebody found a way to do it with `7`
  (and extra additions). By breaking `n` by `n` matrices into
  `2` by `2` blocks, this idea also reduced the count
  to multiply large matrices.
  - Instead of
    $$ n^3 $$
    multiplications the count has now dropped to
    $$ n^{2.376} $$.
  - Maybe
    $$ n^2 $$
    is possible?
  - But the algorithms are so awkward that scientific
    computing is done the regular
    $$ n^3 $$
    way.

### Vector Spaces and Subspaces

- A matrix multiplies a vector: __A__ _times_ __x__.
  - At the first level this is only numbers.
  - At the second level __Ax__ is a
    combination of column vectors.
  - The third level shows subspaces.

### Orthogonality

- The __orthogonal complement__ of a subspace __V__
  contains __every__ vector that is perpendicular to __V__.
  - This orthogonal subspace is denoted by
    $$ V^{\perp} $$.

### Eigenvalues and Eigenvectors

- To explain eigenvalues, we first explain eigenvectors.
  Almost all vectors change direction,
  when they are multiplied by `A`.
  - Certain exceptional vectors __x__ are in the same
    direction as
    $$ A \mathbf{x} $$.
  - Those are the "eigenvectors".
  - Multiply an eigenvector by `A`, and the vector
    $$ A \mathbf{x} $$
    is a number
    $$ \lambda $$
    `times` the original __x__.
- The basic equation is
  $$ A \mathbf{x} = \lambda \mathbf{x} $$.
  - The number
    $$ \lambda $$
    is an eigenvalue of `A`.

### The Singular Value Decomposition (SVD)

- The singular value theorem for `A` is the eigenvalue theorem for
  $$ A^{T} A $$
  and
  $$ A A^{T} $$.
- The Singular Value Decomposition (SVD) separates any matrix
  into simple pieces.

------------------

- [物理学家用的张量和群论导论](https://book.douban.com/subject/25934965/)

### Tensors

- To make this concrete, consider a rank `2` tensor `T`,
  whose job it is to eat two vectors `v` and `w` and produce
  a number which we will denote as `T(v, w)`.
  - For such a tensor, __multilinearity__ means
  - $$ T(v_1 + c v_2, w) = T(v_1, w) + c T(v_2, w) $$
  - $$ T(v, w_1 + c w_2) = T(v, w_1) + c T(v, w_2) $$

```
One possible objection to our approach is that matrices
and tensors are often thought of as linear operators which
take vectors into vectors, as opposed to objects which
eat vectors and spit out numbers.
```

---

- That said, an (__abstract__) __vector space__ is a set
  __V__ (whose elements are called vectors),
  together with a set of scalars __C__
  (for us, __C__ is always
  $$ \mathbb{R} $$
  or
  $$ \mathbb{C} $$
  ) and operations of addition and scalar multiplication
  that satisfy the following axioms:
  1. `v + w = w + v`
    for all `v`, `w` in `V` (__Commutativity__)
  2. `v + (w + x) = (v + w) + x`
    for all `v`, `w`, `x` in `V` (__Associativity__)
  3. There exists a vector `0` in `V` such that
    `v + 0 = v` for all `v` in `V`
  4. For all `v` in `V` there is a vector `-v`
    such that `v + (-v) = 0`
  5. `c(v + w) = cv + cw` for all `v` and `w` in
    `V` and scalars `c` (__Distributivity__)
  6. `1v = v` for all `v` in `V`
  7. $$ (c_1 + c_2) v = c_1 v + c_2 v $$
    for all scalars
    $$ c_1 $$,
    $$ c_2 $$
    and vectors `v`
  8. $$ (c_1 c_2) v = c_1 (c_2 v) $$
    for all scalars
    $$ c_1 $$,
    $$ c_2 $$
    and vectors `v`

---

- A `linear operator` on a vector space __V__ is a
  function __T__ from __V__ to itself satisfying
  the `linearity condition`.
- So __T__ is `invertible` if and only if the only
  vector it sends to `0` is the zero vector.
- An important point to keep in mind is that a
  `linear operator` is not the same thing as a matrix;
  just as with vectors, the identification can only
  be made once a basis is chosen.

```
Roughly speaking, a dual vector is an object that
eats a vector and spits out a number.
```

- Given a vector space __V__ with scalars `C`,
  a __dual vector__ (or __linear functional__)
  on __V__ is a C-valued linear function `f` on __V__.
