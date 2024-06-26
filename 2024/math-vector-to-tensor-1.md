---
title: 从矢量到张量 - 矢量场
description: 深居俯夹城, 春去夏犹清. 天意怜幽草, 人间重晚晴.
date: 2023-12-26
---

- [从矢量到张量](https://book.douban.com/subject/36000538/)
  - 副标题: 细说矢量与矢量分析, 张量与张量分析
  - 封面人物不错, 数学家黎曼

> 关于印刷错误, 倒也无伤大雅!
  除非校对特别投入, 或者篇幅较短. (比如: `狄拉克讲广义相对论`)
  否则, 角标出错, 几乎必然. 类似题材书籍大多如此~

---

> `向量空间`的定义: 类似于`域`的定义, 定义基于数域的向量空间.
  两个运算: 向量加法, 向量数乘.

- `矢量积`即`叉乘`

- [拉格朗日恒等式](https://en.wikipedia.org/wiki/Lagrange%27s_identity)
- [爱因斯坦求和约定](https://en.wikipedia.org/wiki/Einstein_notation)
  - [抽象指标记号](https://en.wikipedia.org/wiki/Abstract_index_notation)

### 矢量的矢量混合积和矢量三重积

> 这里有一点与主流说法的差异:
  本书的`混合积`其实是`标量三重积`;
  而`三重积`其实是`矢量三重积`.

- [三重积](https://en.wikipedia.org/wiki/Triple_product)

- 引入符号
  $$
    [\mathbf{A} \mbox{ } \mathbf{B} \mbox{ } \mathbf{C}] =
    \mathbf{A} \cdot (\mathbf{B} \times \mathbf{C})
  $$,
  则最后有
  - $$
      [\mathbf{A} \mbox{ } \mathbf{B} \mbox{ } \mathbf{C}] =
      \mathbf{A} \cdot (\mathbf{B} \times \mathbf{C}) =
      \begin{vmatrix}
        a_1 & a_2 & a_3 \\
        b_1 & b_2 & b_3 \\
        c_1 & c_2 & c_3
      \end{vmatrix}
    $$

### 矢量三重系

- 矢量三重系, 或简称`三重系`, 是指通常的三维空间中的任意三个线性无关的矢量
  $$ \mathbf{e}_1 $$,
  $$ \mathbf{e}_2 $$,
  $$ \mathbf{e}_3 $$,
  而且我们还要求它们是正向的, 即
  $$ [\mathbf{e}_1 \mbox{ } \mathbf{e}_2 \mbox{ } \mathbf{e}_3] > 0 $$,
  因此它们就形成一个广义的`右手系`.

- 对于矢量三重系
  $$ \mathbf{e}_1 $$,
  $$ \mathbf{e}_2 $$,
  $$ \mathbf{e}_3 $$,
  用矢量的内积可构成
  - $$ g_{ij} ≡ \mathbf{e}_i \cdot \mathbf{e}_j $$,
    $$ i, j = 1, 2, 3 $$
- 由于
  $$ i = 1, 2, 3 $$,
  $$ j = 1, 2, 3 $$,
  所以一共有 `9` 个量, 这 `9` 个量称为
  $$ \mathbf{e}_1 $$,
  $$ \mathbf{e}_2 $$,
  $$ \mathbf{e}_3 $$
  给出的`度规`. 由于
  - $$
      g_{ji} =
      \mathbf{e}_j \cdot \mathbf{e}_i =
      \mathbf{e}_i \cdot \mathbf{e}_j
    $$,
    $$ i, j = 1, 2, 3 $$
- 所以
  $$ g_{ij} $$
  关于它的 `2` 个下标是`对称`的.
  - 这样
    $$ g_{ij} $$
    就有 `6` 个独立量:
    $$ g_{11} $$,
    $$ g_{22} $$,
    $$ g_{33} $$,
    $$ g_{12} $$,
    $$ g_{13} $$,
    $$ g_{23} $$.

---

- 因为
  $$
    \mathbf{V} =
    \sum_{i=1}^{3} v^{i} \mathbf{e}_i =
    \sum_{j=1}^{3} v^{j} \mathbf{e}_j =
    \sum_{k=1}^{3} v^{k} \mathbf{e}_k =
    ...
  $$
  - 即求和指标可以用任意字母来表示, 而不影响结果, 我们就把这一类指标称为`哑标`.
  - 今后我们会频繁地使用求和号
    $$ \sum $$,
    因此我们再作一步简化: __略去求和号__.
- 于是上式就成为
  - $$
      \mathbf{V} =
      v^{i} \mathbf{e}_i =
      v^{j} \mathbf{e}_j =
      v^{k} \mathbf{e}_k =
      ...
    $$
  - 这约定称为`爱因斯坦规约`.

---

- 利用
  $$ \mathbf{e}_1 $$,
  $$ \mathbf{e}_2 $$,
  $$ \mathbf{e}_3 $$
  以及矩阵
  $$ (\mathbf{g}^{ij}) $$,
  我们定义
  - $$ \mathbf{e}^{i} = \mathbf{g}^{ij} \mathbf{e}_{j} $$,
    $$ i = 1, 2, 3 $$
  - 这样, 我们就得出了
    $$ \mathbf{e}^1 $$,
    $$ \mathbf{e}^2 $$,
    $$ \mathbf{e}^3 $$
    $$ \longleftrightarrow $$
    $$ \mathbf{e}_1 $$,
    $$ \mathbf{e}_2 $$,
    $$ \mathbf{e}_3 $$
    的`对偶系`.

- $$ [\mathbf{e}_1 \mbox{ } \mathbf{e}_2 \mbox{ } \mathbf{e}_3] = \sqrt{g} $$,
  $$ [\mathbf{e}^1 \mbox{ } \mathbf{e}^2 \mbox{ } \mathbf{e}^3] = 1 / \sqrt{g} $$
  - `g` 是
    $$ g_{ij} $$
    的行列式
  - 即
    $$ g = det \mid g_{ij} \mid $$
    和
    $$ \frac{1}{g} = det \mid g^{ij} \mid $$

---

- $$ \mathbf{e}_1 = \sqrt{g} (\mathbf{e}^2 \times \mathbf{e}^3) $$,
  $$ \mathbf{e}_2 = \sqrt{g} (\mathbf{e}^3 \times \mathbf{e}^1) $$,
  $$ \mathbf{e}_3 = \sqrt{g} (\mathbf{e}^1 \times \mathbf{e}^2) $$

- 设定三重系
  $$ \mathbf{e}_1 $$,
  $$ \mathbf{e}_2 $$,
  $$ \mathbf{e}_3 $$
  和它的对偶系
  $$ \mathbf{e}^1 $$,
  $$ \mathbf{e}^2 $$,
  $$ \mathbf{e}^3 $$,
  于是对任意矢量
  $$ \mathbf{V} $$
  有
  - $$ \mathbf{V} = v^i \mathbf{e}_i = v_i \mathbf{e}^i $$
- 这样, 客观量
  $$ \mathbf{V} $$
  在
  $$ \mathbf{e}_1 $$,
  $$ \mathbf{e}_2 $$,
  $$ \mathbf{e}_3 $$
  的构架中用分量
  $$ (v^1, v^2, v^3) $$
  来描述, 而在
  $$ \mathbf{e}^1 $$,
  $$ \mathbf{e}^2 $$,
  $$ \mathbf{e}^3 $$
  的构架中用分量
  $$ (v_1, v_2, v_3) $$
  来描述. 那么这两种描述之间有怎样的联系呢?

---

- 用矩阵形式表示就有
  - $$
      \begin{pmatrix}
        v_1 \\
        v_2 \\
        v_3
      \end{pmatrix} =
      \begin{pmatrix}
        g_{11} & g_{12} & g_{13} \\
        g_{21} & g_{22} & g_{23} \\
        g_{31} & g_{32} & g_{33}
      \end{pmatrix}
      \begin{pmatrix}
        v^1 \\
        v^2 \\
        v^3
      \end{pmatrix}
    $$
- 利用
  $$ (g_{ij}) $$
  的逆矩阵
  $$ (g^{ij}) $$,
  可得
  - $$
      \begin{pmatrix}
        v^1 \\
        v^2 \\
        v^3
      \end{pmatrix} =
      \begin{pmatrix}
        g^{11} & g^{12} & g^{13} \\
        g^{21} & g^{22} & g^{23} \\
        g^{31} & g^{32} & g^{33}
      \end{pmatrix}
      \begin{pmatrix}
        v_1 \\
        v_2 \\
        v_3
      \end{pmatrix}
    $$

- 我们把
  $$ v^1 $$,
  $$ v^2 $$,
  $$ v^3 $$,
  也即由
  $$ \mathbf{V} = v^i \mathbf{e}_i $$
  得出的分量称为
  $$ \mathbf{V} $$
  的`逆变分量`, 而把
  $$ v_1 $$,
  $$ v_2 $$,
  $$ v_3 $$,
  也即由
  $$ \mathbf{V} = v_i \mathbf{e}^i $$
  得出的分量称为
  $$ \mathbf{V} $$
  的`协变分量`.
  - 不过,
    $$ v_1 $$,
    $$ v_2 $$,
    $$ v_3 $$
    不必用对偶系的线性表示得出, 而直接可以用
    $$ \mathbf{V} $$
    与三重系的内积得出, 即
  - $$ v_j = \mathbf{e}_j \cdot \mathbf{V} $$

### 三重系变换下的张量

- [张量](https://en.wikipedia.org/wiki/Tensor)

- __三重系变换下的张量定义__ 设量
  $$ \mathbf{T} $$
  在坐标基矢
  $$ \mathbf{e}_1 $$,
  $$ \mathbf{e}_2 $$,
  $$ \mathbf{e}_3 $$
  下的分量为
  $$
    \mathbf{T}_{j_1 ... j_q}^{i_1 ... i_p},
    1 ≤ i_1, ... i_p; j_1, j_2, ... j_q ≤ 3
  $$,
  而在坐标基矢
  $$ \mathbf{e}_{1'} $$,
  $$ \mathbf{e}_{2'} $$,
  $$ \mathbf{e}_{3'} $$
  下的分量为
  $$
    \mathbf{T}_{j_{1'} ... j_{q'}}^{i_{1'} ... i_{p'}},
    1 ≤ i_{1'}, ... i_{p'}; j_{1'}, j_{2'}, ... j_{q'} ≤ 3
  $$,
  若
  $$ \mathbf{e}_{i'} = a_{i'}^{j} \mathbf{e}_j $$,
  则有
  - $$
      \mathbf{T}_{j_{1'} ... j_{q'}}^{i_{1'} ... i_{p'}} =
      a_{j_{1'}}^{l_1} ... a_{j_{q'}}^{l_q}
      a_{k_1}^{i_{1'}} ... a_{k_p}^{i_{p'}}
      \mathbf{T}_{l_1 ... l_q}^{k_1 ... k_p}
    $$
- 那么称量
  $$ \mathbf{T} = (T_{j_1 ... j_q}^{i_1 ... i_p}) $$
  是一个逆变 `p` 阶, 协变 `q` 阶的 `m = p + q` 阶张量.
  - 如果同时有
    $$ p ≠ 0 $$,
    $$ q ≠ 0 $$,
    则称
    $$ \mathbf{T} $$
    为`混合张量`.
- 由于各指标均可取值 `1`, `2`, `3`, 所以 `m` 阶张量共有
  $$ 3^m = 3^p · 3^q = 3^{p + q} $$
  个分量. 当两个张量具有相同的 `p` 和 `q` 时, 则称它们是`同类张量`.
- 当 `q = 0` 时, 有逆变 `p` 阶, 协变 `0` 阶的张量,
  简称为 (`p` 阶) 逆变张量, 如前面的
  $$ \mathbf{V} = (v^i) $$
  就是 `1` 阶逆变张量, 即 `1` 阶逆变矢量, 而
  $$ \mathbf{G}^{'} = (g^{ij}) $$
  就是 `2` 阶逆变张量.
  - 当 `p = 0` 时, 有逆变 `0` 阶, 协变 `q` 阶的张量, 简称为 (`q` 阶) 协变张量.
  - 如前面的
    $$ \mathbf{V}^{'} = (v_i) $$
    就是 `1` 阶协变张量, 即 `1` 阶协变矢量, 而
    $$ \mathbf{G} = (g_{ij}) $$
    就是 `2` 阶协变张量, 因此
    $$ (g_{ij}) $$
    称为`度规张量`.
- 当 `p = q = 0` 时, 我们得到只有 `1` 个分量的张量即是`标量`或`不变量`.

---

### 三维空间正交变换下的张量 - 笛卡儿张量

### 闵可夫斯基空间中的张量

### 变矢量的微分运算

### 数量场的梯度

### 矢量场的散度

### 矢量场的旋度

### 矢量场的线积分与面积分

### 散度定理, 斯托克斯定理和格林恒等式
