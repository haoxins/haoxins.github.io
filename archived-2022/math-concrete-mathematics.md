---
title: 具体数学
description: 计算机科学基础 (第2版)
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

- __底__ (`floor`, 最大整数) 函数
- __顶__ (`ceiling`, 最小整数) 函数
- 对所有实数 `x`, 其定义如下:
  - $$ \lfloor x \rfloor $$
  - 小于或等于 `x` 的最大整数
  - $$ \lceil x \rceil $$
  - 大于或等于 `x` 的最小整数
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
  - $$ \{ x \} = x - \lfloor x \rfloor $$
- 我们有时称
  $$ \lfloor x \rfloor $$
  是 `x` 的整数部分 (integer part),
  - 因为
    $$ x = \lfloor x \rfloor + \{ x \} $$.

---

- 这一节里的最后一个应用是研究所谓的 __谱__, 我们定义,
  一个实数 `α` 的谱 (spectrum) 是整数组成的一个无限多重集合:
- $$ Spec(α) = \{ \lfloor α \rfloor, \lfloor 2α \rfloor, \lfloor 3α \rfloor, ... \} $$
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

- $$ x \mod y = x - y \lfloor x / y \rfloor, y \ne 0 $$.

- 分配律是 `mod` 最重要的代数性质, 对所有实数 `c`, `x` 和 `y`, 我们有

$c(x \mod y) = (cx) \mod (cy)$

## 数论

## 二项式系数

## 特殊的数

## 生成函数

## 离散概率

## 渐进式
