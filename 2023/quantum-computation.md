---
title: 量子计算导论 & 人人可懂的量子计算
description: 郁孤台下清江水, 中间多少行人泪. 西北望长安, 可怜无数山.
date: 2023-12-08
---

- [量子计算导论: 从线性代数到量子编程](https://book.douban.com/subject/36329438/)
  - __购书原因__: 首先是`密码学`章节, 其次是居然有 `Q#` 章节;
    买书时尚不确定是否就是
    [microsoft/qsharp](https://github.com/microsoft/qsharp).
  - `基于格的密码学`章节, 正好呼应
    [Module-Lattice-Based Key-Encapsulation Mechanism Standard](https://csrc.nist.gov/pubs/fips/203/ipd)
    和
    [Module-Lattice-Based Digital Signature Standard](https://csrc.nist.gov/pubs/fips/204/ipd).

> 本书开始: 废话连篇~ (数处细节错误, 印刷没人校对?)

### 基本量子理论

```
在量子力学中, 量子态对应于希尔伯特空间中的向量.
粒子动量等性质都与某些算子密切相关. 另外, 请记住, 向量是矩阵.
这意味着这些向量都有特征值和特征向量.
在量子力学中, 算子的特征值对应于该性质的值, 如动量.
与该特征值对应的特征向量是一个量子态. 物理学家称之为本征态.
```

- 具体而言, 玻恩定理指出, 如果与自伴算子 __A__ 对应的某些可观测量
  (如位置, 动量等) 是在带有归一化波函数
  $$ \mid Ψ \rangle $$
  的系统中被测量的, 那么最终结果将是 __A__ 的特征值之一.
  - 自伴算子: 在一个有限维的内积复向量空间里, 自伴算子就等于自己的伴随算子,
    它是从向量到自身的线性映射.
  - 请注意, 此处的向量空间是复向量空间.
  - 这使我们想到了厄米矩阵, 厄米矩阵指等于其自身共轭转置的方阵.
  - 共轭转置是指先对矩阵取转置, 再取复共轭.
  - 复希尔伯特空间里的每个线性算子也有一个伴随算子, 有时称为厄米伴随算子.

```
自旋数表示一个粒子完成一次旋转时有多少个对称面.
因此, 1/2 自旋意味着粒子必须旋转两次 (即 720°) 才能回到原始位置.
```

### 量子计算对密码学的影响

```
对称密码算法不受量子计算机的攻击, 原因很简单. 顾名思义, 对称密码只有一个密钥.
反过来, 这又意味着算法的安全性并不是基于相互关联的两个密钥.
非对称密码之所以有效, 是因为两个独立的密钥 (公钥和私钥) 是通过一些基础数学相关联的.
这种数学相对安全, 只是因为要解决特定的数学问题很难; 但是,
对称密码算法的安全性并不是建立在某些潜在的数学问题的安全性之上的.
本质上, 量子计算机不需要解决基本的数学问题来破解对称密码, 它能做的可能就是加速暴力攻击.
```

------------------

- [人人可懂的量子计算](https://book.douban.com/subject/34996717/)
  - 不值一读~

### 自旋

> `自旋`, 讲得很一般, 蜻蜓点水~

### 线性代数

> 你都舍弃`复数`只取`实数`了, 还说啥呢?

### 经典逻辑, 门和电路

- 有一个名为`与非`的二进制运算,
  任何布尔函数都逻辑等价于某些只使用`"与非"`运算的表达式.

### 量子门和电路

- 在经典, 可逆的计算中, 只有两种布尔操作会作用于一个比特:
  - 不改变比特值的单位操作,
  - 以及翻转 `0` 和 `1` 值的非操作.
- 对于量子比特, 则有无限多个可能的门!

```
这种操作改变了一个概率振幅的符号,
有时我们称它为改变了量子比特的相对相位.
```

### 量子算法

```
我们用正交矩阵表示量子门, 而量子电路由量子门组合而成, 这些组合对应于正交矩阵的乘法.
由于正交矩阵的乘积仍然是正交矩阵, 所以任何量子电路都可以用一个正交矩阵来描述.
正如我们所看到的, 正交矩阵对应于基的变化 -- 一种看待问题的不同方式, 而且这是一种很关键的思想.
相比经典计算, 量子计算为我们提供了更多观察问题的方法.
但是为了有更高的效率, 必须要有一个观点表明能将正确答案从其他可能的错误答案中分离出来.
量子计算机能够比经典计算机更快地解决问题, 这需要一个只有在我们使用正交矩阵变换它时才可见的结构.
```

------------------

- [张朝阳的物理课](https://book.douban.com/subject/36150946/)

```
作为中文的本土书籍, 必须支持下!
希望这本书只是开始~
```

```
2022年11月28日, 周一.
拿到了书, 随便翻了一下,
穿插的手稿图片是一个不错的排版亮点.

还是那句话: 希望这本书只是开始~
```

### 经典力学问题

- $$ \overrightarrow{a} = \frac{d \overrightarrow{v}}{dt} $$
- $$ \overrightarrow{F} = m \overrightarrow{a} $$
- $$ F = G \frac{m_{1} m_{2}}{r^2} $$
  - 在地球附近, 有如下关系:
  - $$ F = mg = G \frac{Mm}{R^2} $$

> 相对于`粗体`表示矢量, 貌似还是`箭头`更清晰~

```
虽然电磁现象可以通过麦克斯韦理论描述, 但是电磁力可以被区分成很多种力,
这里介绍的是电荷间的作用力, 更严格地说是静电荷之间的力.
```

- $$ F = k \frac{q_{1} q_{2}}{r^2} $$

### 光电问题

- 一个带电量为 `q` 的运动电荷在距其 `r` 处的某一点
  (可记作 `A` 点) 产生的电磁场是:

$$
\overrightarrow{E} =
\frac{q}{4 \pi \varepsilon_0}
\left [
  \frac{\overrightarrow{e}_{r'}}{r'^2} +
  \frac{r'}{c} \frac{d}{dt} \frac{\overrightarrow{e}_{r'}}{r'^2} +
  \frac{1}{c^2} \frac{d^2}{dt^2} \overrightarrow{e}_{r'}
\right ]
$$

- 其中 `r'` 是电荷在时间为
  $$ t - \frac{r'}{c} $$
  时刻与点 `A` 的距离,
  $$ \overrightarrow{e}_{r'} $$,
  为在
  $$ t - \frac{r'}{c} $$
  时刻电荷指向 `A` 点的单位向量.

### 热力学与统计物理问题

- 得到气体粒子平均动能与温度之间的关系.

$$
\langle \frac{1}{2} mv^2 \rangle = \frac{3}{2} kT
$$

- 从微观上讲, 温度表征了气体粒子运动的剧烈程度.
  - 温度越高, 微观粒子运动越剧烈, 气体越热.
- 根据能量均分定理, 以上公式表明每个自由度上平均分配的能量是
  $$ \frac{1}{2} kT $$,
  假设在某温度下理想气体粒子可以激发的自由度总共为 `i`,
  那么理想气体的总内能为
  $$ U = \frac{i}{2} NkT = \frac{1}{\gamma - 1} NkT $$,
  其中
  $$ \gamma $$
  是新引入的参量, 其意义会在后面的绝热膨胀中体现出来.

---

- 理想气体内能与温度的关系
  $$ U = \frac{1}{\gamma - 1} NkT $$,
  结合理想气体状态方程
  $$ pV = NkT $$,
  就可以得到内能与体积和压强的关系
  $$ U = \frac{1}{\gamma - 1} pV $$.
- 将它带回绝热过程的热力学第一定律公式, 可得
  $$ \frac{1}{\gamma - 1} d(pV) = -pdV $$,
  解此微分方程, 即可得到理想气体绝热方程:
  - $$ pV^{\gamma} = C $$
  - 其中 `C` 为常数, 可由该过程中任意状态下的压强与体积确定.
  - 以上绝热方程显示了绝热过程中压强 `p` 与体积 `V` 的关系, 其中
    $$ \gamma $$
    大于 `1`, 所以当体积 `V` 增大时, 压强减小.

### 相对论问题

- [世界线](https://en.wikipedia.org/wiki/World_line)
- [固有时](https://en.wikipedia.org/wiki/Proper_time)

## Confidence Computing

- [FIPS 203](https://csrc.nist.gov/pubs/fips/203/ipd)
  - Module-Lattice-Based Key-Encapsulation Mechanism Standard
- [FIPS 204](https://csrc.nist.gov/pubs/fips/204/ipd)
  - Module-Lattice-Based Digital Signature Standard
- [FIPS 205](https://csrc.nist.gov/pubs/fips/205/ipd)
  - Stateless Hash-Based Digital Signature Standard

```
Initial Public Draft

Date Published: August 24, 2023
Comments Due:   November 22, 2023
```

- [OpenSK](https://github.com/google/OpenSK)
  - This repository contains a Rust implementation
    of a FIDO2 authenticator.

- [Noise Protocol Framework](https://noiseprotocol.org)

- [Schnorr's identification protocol](https://www.zkdocs.com/docs/zkdocs/zero-knowledge-protocols/schnorr/)

- [Solana](https://github.com/solana-labs/solana)
  - Solana is a decentralized blockchain built to
    enable scalable, user-friendly apps for the world.
- There are 8 key innovations that make the
  Solana network possible:
  - Proof of History (POH)
  - Tower BFT - a PoH-optimized version of PBFT;
  - Turbine - a block propagation protocol;
  - Gulf Stream - Mempool-less transaction forwarding protocol;
  - Sealevel - Parallel smart contracts runtime;
  - Pipelining - a Transaction Processing Unit
    for validation optimization;
  - Cloudbreak - Horizontally-Scaled Accounts Database;
  - Archivers - Distributed ledger store.

- [Drand](https://github.com/drand/drand)
  - A Distributed Randomness Beacon Daemon

- https://eprint.iacr.org/2011/344.pdf
- https://eprint.iacr.org/2011/277.pdf

### The OPAQUE Asymmetric PAKE Protocol

- https://github.com/cfrg/draft-irtf-cfrg-opaque

### Events

- 2022-08, 期待以太坊, 一鲸落, 万物生.

```
The 2022 Gödel Prize is awarded to the following papers:

Zvika Brakerski, Vinod Vaikuntanathan:
Efficient Fully Homomorphic Encryption from (Standard) LWE.
FOCS 2011: 97-106. SIAM Journal of Computing 43(2): 831-871 (2014)

Zvika Brakerski, Craig Gentry, Vinod Vaikuntanathan:
(Leveled) fully homomorphic encryption without bootstrapping.
ITCS 2012: 309-325. ACM Transactions on Computation Theory 6(3): 13:1-13:36 (2014)

The above papers made transformative contributions to cryptography
by constructing efficient fully homomorphic encryption (FHE) schemes.

The above papers presented entirely new constructions of
fully homomorphic encryption whose security relied only on
the hardness of Regev's learning with errors (LWE) problem.
They have led to a new generation of practically efficient FHE.
```

------------------

- [机密计算](https://book.douban.com/subject/36319416/)
  - 不抱期待, 没啥干货!

```
全同态加密相对于部分同态加密和类同态加密,
在运算形式和电路深度方面更为自由,
可以支持任意次数的加法与乘法运算.
```

```
GSW 方案在功能上得到了扩展, 不需要计算密钥, 只需要公钥就可以进行同态运算,
所以基于 GSW 方案可以构造基于身份的同态加密方案和基于属性的同态加密方案.
```

------------------

- [从区块链到 Web3: 构建未来互联网生态](https://book.douban.com/subject/36686046/)
  - 差评! 乱七八糟!
