---
title: 具体数学 计算机科学基础 上
description: 斜月半窗还少睡, 画屏闲展吴山翠. 衣上酒痕诗里字, 点点行行, 总是凄凉意.
date: 2021-08-28
---

- [具体数学](https://book.douban.com/subject/21323941/)
  - 副标题: 计算机科学基础
  - 作者: Ronald L.Graham, Donald E.Knuth
  - 原作名: Concrete Mathematics: A Foundation for Computer Science
  - 出版年: 2013-4

- __具体数学__ 究竟是什么呢?
  - 它融合了连续数学和离散数学. 更具体地说,
    它是利用一组求解问题的技术对数学公式进行有控制的操作.
  - 理解了本书的内容之后, 你所需要的就是颗冷静的头脑,
    一大张纸以及较为工整的书写, 以便对看上去令人恐怖的和式进行计算,
    求解复杂的递归关系, 以及发现数据中隐藏的精妙规律.
  - 你会对代数技巧得心应手, 从而常常会发现,
    得到精确的结果比求出仅在一定意义下成立的近似解更为容易.

- 这本书要探讨的主题包括`和式`, `递归式`, `初等数论`, `二项式系数`,
  `生成函数`, `离散概率`以及`渐近方法`.
  - 其重点是强调处理技术, 而不是存在性定理或者组合推理,
  - 目的是使每一位读者熟悉离散性运算 (如最大整数函数以及有限求和),
  - 就好像每一位学习微积分的学生都熟悉连续性运算一样 (如绝对值函数以及不定积分)

## 整值函数

- __底__ (`floor`, 最大整数) 函数, __顶__ (`ceiling`, 最小整数) 函数
- 对所有实数 `x`, 其定义如下:
  - $$ \lfloor x \rfloor $$:
    小于或等于 `x` 的最大整数
  - $$ \lceil x \rceil $$:
    大于或等于 `x` 的最小整数
  - $$ \lfloor e \rfloor = 2 $$
  - $$ \lfloor -e \rfloor = -3 $$
  - $$ \lceil e \rceil = 3 $$
  - $$ \lceil -e \rceil = -2 $$
  - $$ x - 1 < \lfloor x \rfloor \le x \le \lceil x \rceil < x + 1 $$
  - $$ \lfloor -x \rfloor = - \lceil x \rceil $$
  - $$ \lceil -x \rceil = - \lfloor x \rfloor $$

---

- `x` 和
  $$ \lfloor x \rfloor $$
  之间的差称为 `x` 的分数部分 (fractional part),
  它在应用中经常出现, 所以值得拥有自己的记号:

$$ \{ x \} = x - \lfloor x \rfloor $$

- 我们有时称
  $$ \lfloor x \rfloor $$
  是 `x` 的整数部分 (integer part), 因为

$$ x = \lfloor x \rfloor + \{ x \} $$

---

- 这一节里的最后一个应用是研究所谓的 __谱__, 我们定义,
  一个实数 `α` 的谱 (spectrum) 是整数组成的一个无限多重集合:

$$
Spec(α) = \{
\lfloor α \rfloor,
\lfloor 2α \rfloor,
\lfloor 3α \rfloor,
... \}
$$

- 一个多重集合与一个集合相似, 不过它可以有重复的元素.
  - 例如, `1/2` 的谱的开头部分是 `{0, 1, 1, 2, 2, 3, 3, ...}`.
- 容易证明, 没有两个谱是相等的, 也就是说, `α ≠ β`
  就意味着 `Spec(α) ≠ Spec(β)`.
- 不失一般性, 假设 `α < β`, 就存在一个正整数 `m`
  使得 `m (β - α) ≥ 1`.
  - (事实上, 任何一个
    $$ m \ge \lceil 1 / (β - α) \rceil $$
    都行, 但是我们无需卖弄有关底和顶的知识.)
  - 从而 `mβ - mα ≥ 1`, 且
    $$ \lfloor mβ \rfloor > \lfloor mα \rfloor $$.
  - 于是谱 `Spec(β)` 有少于 `m` 个元素
    $$ ≤ \lfloor mα \rfloor $$,
    而 `Spec(α)` 至少有 `m` 个这样的元素.

---

$$ x \mod y = x - y \lfloor x / y \rfloor, y \ne 0 $$.

- 分配律是 `mod` 最重要的代数性质, 对所有实数 `c`, `x` 和 `y`, 我们有

$$ c(x \mod y) = (cx) \mod (cy) $$

## 数论

$$
m \setminus n \Leftrightarrow m > 0
且对某个整数 k 有 n = mk
$$

- 两个整数 m 和 n 的最大公因子是能整除它们两者的最大整数:

$$
gcd(m, n) =
max \{ k | k \setminus m 且 k \setminus n \}
$$

- `gcd(0, n) = n`

## 二项式系数

- $$ \begin{Bmatrix} n \\ k \end{Bmatrix} $$
  就是二项式系数, 之所以这样称呼它, 是因为二项式定理,
  我们将此符号读作`"n选取k"`.
- 要用更熟悉的东西来表示数
  $$ \begin{Bmatrix} n \\ k \end{Bmatrix} $$,
  最容易的做法是, 首先确定从有 `n` 个元素的集合中选取 `k`
  个元素的序列 (而不是子集) 的个数.
  - 对序列来说, 要考虑元素的次序, 我们证明过 `n!` 是 `n` 个物体的排列数.
  - 由于每 `k` 个元素组成的子集都恰好有 `k!` 种不同的排序,
    所以序列的个数对每一个子集恰好计算了 `k!` 次,
    为得到答案只需要直接用 `k!` 来除:

$$
\begin{Bmatrix} n \\ k \end{Bmatrix} =
\frac{n(n-1)...(n-k+1)}{k(k-1)...(1)}
$$

---

- `gcd` 的一个最好的性质是它容易计算, 可以用有`2300`年之久的欧几里得算法来计算它.
- 为了对给定的值 `0 ≤ m < n` 计算 `gcd(m, n)`,
  欧几里得算法用到递归式
  - `gcd(0, n) = n`;
  - `gcd(m, n) = gcd(n mod m, m), m > 0`.
- 欧几里得算法还给我们更多的东西: 我们可以对它加以推广, 用它来计算满足
  `m'm + n'n = gcd(m, n)` 的整数 `m'` 和 `n'`.
  - 做法是: 如果 `m = 0`, 我们直接就取 `m' = 0` 以及 `n' = 1`;
  - 反之就令 `r = n mod m`, 并用 `r` 和 `m` 替换 `m` 和 `n`, ...

$$
k \setminus m 和
k \setminus n \Leftrightarrow k \setminus gcd(m, n)
$$

---

- 有时我们需要对 `n` 的所有因子求和. 在这种情形下, 方便的法则

$$
\sum_{m \setminus n} a_m =
\sum_{m \setminus n} a_{n / m},
整数 n > 0
$$

- 常常很有用, 此式成立是由于当 `m` 取遍 `n` 所有的因子时
  `n / m` 也取遍 `n` 所有的因子.
- 还有一个更一般的恒等式

$$
\sum_{m \setminus n} a_m =
\sum_{k} \sum_{m > 0} a_m[n = mk]
$$

---

- 仅有一种方式将 `n` 按照素数非减的次序写成素数的乘积.
  - 这个命题称为 __算术基本定理__

- 对于很大的 `n`, 为了更加精确地近似 `n!`,
  我们可以利用斯特林公式:

$$
n! \sim \sqrt{2 \pi n} \left ( \frac{n}{e} \right ) ^ n
$$

- 一个更加精密的近似会告诉我们渐近相对误差:
  - 斯特林公式与 `n!` 的相对误差大概是 `1/(12n)`.
  - 即便是对比较小的 `n`, 这个更加精确的估计也是非常好的了.

---

$$
m \perp n \Leftrightarrow
m, n 是整数, 且 gcd(m, n) = 1
$$

- 一个分数 `m/n` 是最简分数, 当且仅当
    $$ m \perp n $$
- 由于我们是通过消去分子和分母的最大公因子来将它化为最简分数的, 因而一般来说,
  我们推测有

$$ m / gcd(m, n) \perp n / gcd(m, n) $$

- 而这的确为真.
- 它可以从一个更加一般的规则 `gcd(km, kn) = k gcd(m, n)` 推导出来.

$$ k \perp m 且 k \perp n \Leftrightarrow k \perp mn  $$

- 有一种非常好的方法来构造由满足
  $$ m \perp n $$
  的全部非负的分数 `m/n` 组成的集合, 它称为 Stern-Brocot 树.
- 其思想是从两个分数
  $$ \left ( \frac{0}{1}, \frac{1}{0} \right ) $$
  出发, 然后依照你希望的次数重复下面的操作:
  - 在两个相邻接的分数
    $$ \frac{m}{n} $$
    和
    $$ \frac{m'}{n'} $$
    之间插入
    $$ \frac{m + m'}{n + n'} $$
  - 新的分数 `(m + m')/(n + n')` 称为
    `m/n` 和 `m'/n'` 的`中位分数`

## 特殊的数

### 斯特林数

## 生成函数

## 离散概率

## 渐进式
