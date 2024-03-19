---
title: 阅读的闲书
description: 东篱把酒黄昏后, 有暗香盈袖. 莫道不销魂, 帘卷西风, 人比黄花瘦.
date: 2023-07-17
---


- [拓扑与物理](https://book.douban.com/subject/35388292/)

- [惰者集](https://book.douban.com/subject/27603987/)

- [黑体辐射](https://book.douban.com/subject/36701663/)
  - __阅读之前__: 终于有一本细分点切入, 一以贯之的书了~
    市面上泛泛而谈的科普书太多了, 不是量子就是相对论,
    照葫芦画瓢, 没啥特色~
  - 同时支持一下国人作品!

- [图解 TCP/IP (第 6 版)](https://book.douban.com/subject/36739612/)
  - 有些年头没看网络相关的东西了~
  - 废话不少~

- [图数据库: 理论与实践](https://book.douban.com/subject/36730737/)
  - 首先是推销自家产品;
  - 然后是概括性介绍;
  - 末尾的应用比较鸡肋.
  - 那些推荐序, 推荐语, 当真是阅读了之后写的?

- [光子之舞](https://book.douban.com/subject/36463573/)
  - 第一眼看了下目录, 感觉一般般~
  - 废话较多, 乏善可陈!
  - 本书主题: 量子隐形传态~ 其实就是附录部分的一篇文章的篇幅就够了!

---

- [法律的悖论](https://book.douban.com/subject/36624253/)
  - 罗翔
  - 实话实说, 对我而言, 一开始没太大的阅读吸引力~
  - 前 `1/3` 认真阅读了, 后面简单看了看.
  - 可能是因为抖音看过不少罗翔的视频, 所以没啥印象深刻的内容.

---

- [量子计算: 一种应用方法](https://book.douban.com/subject/35812490/)
  - 嗯, 这本书其实没啥新意! 买来是为了赞助
    [Qiskit/qiskit](https://github.com/Qiskit/qiskit).
  - 为啥要赞助 __Qiskit__? 因为孵化了
    [Qiskit/rustworkx](https://github.com/Qiskit/rustworkx).
  - 本书的篇幅主要就两部分, 一部分是代码, 另一部分是数学 (线性代数);
    剩余章节均很薄弱! 倒是印刷质量确实不错~
  - 既然作者自己的定位已经是
    [量子计算与量子信息](https://book.douban.com/subject/35777059/)
    的补充, 还不如直接删除数学部分.
  - 至于所谓的前沿, 也没啥展开描述, 所以也就剩下个代码部分了~

```
执行不可逆运算就会丢失信息, 因为这相当于对系统的状态进行了测量.
这样一个计算周期便完成了, 程序无法继续执行.
相反, 如果使用可逆逻辑门, 只要保持系统的相干性, 就可以继续将算子作用于量子比特.
```

> 不可逆运算, 相当于测量~

```
只有当所考虑的向量的项全为实数时, 点积和内积才是一致的.
```

```
数字向量构成阿贝尔群.
```

> 注: 加法

- 域
  $$ \mathbb{F} $$
  上的一个向量空间
  $$ \mathbf{V} $$
  由一个阿贝尔群
  $$ \mathbf{V} $$
  以及一个域
  $$ \mathbb{F} $$
  在
  $$ \mathbf{V} $$
  上的数乘运算构成.
- 域
  $$ \mathbb{F} $$
  上的向量空间
  $$ \mathbf{V} $$
  的一个子集
  $$ \mathbf{S} \subset \mathbf{V} $$
  是
  $$ \mathbf{V} $$
  的子空间, 当且仅当
  $$ \mathbf{S} $$
  是域
  $$ \mathbb{F} $$
  上的一个向量空间.
- 域
  $$ \mathbb{F} $$
  上的向量空间
  $$ \mathbf{V} $$
  的子集
  $$ \mathbf{S} \subset \mathbf{V} $$
  是
  $$ \mathbf{V} $$
  的子空间, 当且仅当它满足以下性质.
  - __存在单位元__:
    $$ 0 \in \mathbf{S} $$,
    这里的
    $$ 0 $$
    是向量空间
    $$ \mathbf{V} $$
    中的加法单位元.
  - __加法封闭性__: 对任意
    $$ \mathbf{u}, \mathbf{v} \in \mathbf{S} $$,
    $$ \mathbf{u} + \mathbf{v} \in S $$.
  - __数乘封闭性__: 对任意
    $$ a \in \mathbb{F} $$
    以及任意
    $$ \mathbf{v} \in \mathbf{S} $$,
    $$ a \cdot \mathbf{v} \in S $$.

- [希尔伯特空间](https://en.wikipedia.org/wiki/Hilbert_space)

- 由 `n` 个量子比特组成的量子寄存器是向量空间的一个维数为
  $$ 2^n $$
  的张量积.
