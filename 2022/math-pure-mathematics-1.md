---
title: 纯数学教程 哈代
description: 昨夜闲潭梦落花, 可怜春半不还家. 江水流春去欲尽, 江潭落月复西斜.
date: 2022-02-11
---

- [纯数学教程](https://book.douban.com/subject/35132451/)
  - __哈代__, 看一看大师如何讲解基础概念

> 不推荐, 因为一些细节上, 现代数学的处理有细微变化~

## 实变量

- 但是容易看出: 不存在这样的有理数, 它的平方等于 `2`.
  事实上我们可以更进一步表述成:
  - 不存在平方等于 `m/n` 的有理数 (其中 `m/n` 是一个正的既约分数),
    除非 `m` 和 `n` 两者都是完全平方数.
- 这是因为, 如果有可能存在这样的有理数, 即可假设

$$ p^2 / q^2 = m / n $$

- 其中 `p` 与 `q` 没有公因子, `m` 和 `n` 也没有公因子. 那么就有
  $$ np^2 = mq^2 $$.
  - $$ q^2 $$
    的每个因子必定整除
    $$ np^2 $$,
    而 `p` 和 `q` 没有公因子,
    故而
    $$ q^2 $$
    的每个因子必定整除 `n`.
  - 从而有
    $$ n= \lambda q^2 $$,
    其中
    $$ \lambda $$
    是一个整数.
  - 但这样就有
    $$ m= \lambda p^2 $$,
    而由于 `m` 和 `n` 没有公因子, 故
    $$ \lambda $$
    必定为 `1`, 从而
    $$ m=p^2, n=q^2 $$,
    而这正是所要证明的.
- 特别地, 取 `n = 1` 我们得到:
  - 一个整数不可能是一个有理数的平方, 除非该有理数本身就是一个整数.

---

> 下面给出的不存在平方等于 `2` 的有理数的另一种证明是很有意思的.

- 如果存在平方等于 `2` 的有理数, 假设 `p/q` 是一个正的既约分数,
  它满足
  $$ (p / q)^2 = 2 $$,
  也即
  $$ p^2 = 2q^2 $$.
- 容易看出有
  $$ (2q - p)^2 = 2(p - q)^2 $$;
  因此
  $$ (2q - p) / (p - q) $$
  是另外一个有同样性质的分数.
- 但显然 `q < p < 2q`, 故而 `p - q < q`.
- 于是存在另外一个与 `p/q` 相等且有更小分母的分数,
  这与 `p/q` 是既约分数的假设矛盾.

---

- 一个更为一般的命题如下所述, 它由 `Gauss` 得出且前述诸结论为它的特例:
  - 一个整系数的代数方程不可能有非整数的有理根

$$
x^n + p_{1} x^{n-1} + p_{2} x^{n-2} + ... + p_n = 0
$$

---

- 这样我们就把正有理数分成了两个类 `L` 和 `R`, 使得:
  - `i)` `R` 中的每个元素都大于 `L` 中的每个元素;
  - `ii)` 可以找到 `L` 中一个元素与 `R` 中一个元素,
    使它们的差小到我们希望的程度;
  - `iii)` `L` 中没有最大的元素, `R` 中也没有最小的元素.
- 我们关于直线属性的普遍概念以及初等几何和初等代数的要求,
  都同样要求存在一个数 `x`, 它大于 `L` 中所有的元素,
  且小于 `R` 中所有的元素, 也要求直线
  $$ \Lambda $$
  上存在一个相对应的点 `P`.
  - 它把与 `L` 中的元素对应的点以及与 `R` 中的元素对应的点区分开来.
- 现在我们暂时假设存在这样一个数 `x`, 且对它可以用代数法则加以运算,
  - 例如
    $$ x^2 $$
    有确定的意义.
  - 那么
    $$ x^2 $$
    既不能小于 `2`, 也不能大于 `2`.
  - 因为比方说
    $$ x^2 $$
    小于 `2`, 那么由前面所述即得, 可以找到一个正有理数
    $$ \xi $$,
    使得
    $$ \xi^{2} $$
    在
    $$ x^2 $$
    和 `2` 之间.
  - 这就是说, 我们可以找到 `L` 中一个大于 `x` 的元素.
    这与 `x` 将 `L` 中的元素与 `R` 中的元素区分开来这一假设矛盾.
  - 从而
    $$ x^2 $$
    不可能小于 `2`; 类似地, 它也不可能大于 `2`. 这样一来, 我们就得到
    $$ x^2 = 2 $$,
    在代数中我们用
    $$ \sqrt{2} $$
    来记 `x` 所表示的数.
  - 这个数
    $$ \sqrt{2} $$
    不是有理数, 因为没有哪个有理数的平方能等于 `2`.
  - 这就是所谓的`无理数`的最简单的例子.

> 备注: 原书描述有误. 原文为:
> 从而 `x` 不可能小于 `2`; 类似地, 它也不可能大于 `2`.

- 这样可以表示成含有平方根的重复根式的更为复杂的无理数.
  正如读者自己容易看出来的那样, 不难用几何方法构造出一条线段,
  其长度等于任何一个这种类型的数.
  - 只有这几种无理数才可以用 Euclid 方法
    (即用直尺和圆规的几何作图法)
    构造出来, 这是一个关键的结论, 它的证明必须暂时延后.
  - 二次根式的这个性质使得它们特别有意义.

- 一般说来不可能对于高于`4`次的方程的根求得这样的表达式.
  于是, 除了可以用纯的或者混合的二次根式,
  或者用其他的根式以及这些根式的组合来表示的无理数以外,
  还存在另外一些无理数, 它们是代数方程的根,
  但不能用这样的方式加以表示.
  - 仅仅在非常特殊的情形下, 才可能对这种无理数找到这样的表达式.

---

- 于是在任何情形下, 要么 `L` 有最大元, 要么 `R` 有最小元.
  从而实数的任何分割都在如下的意义下与一个实数相"对应":
  - 有理数的分割有时 (但并不总是) 与一个有理数相对应.
  - 这个结论是非常重要的, 因为它表明了:
  - 考虑所有实数的分割并不能对于我们有关数的想法产生出任何进一步的推广.
  - 从有理数出发, 我们曾经发现有理数的分割将我们引导到数的一个新的概念
    -- 比有理数的概念更加一般的实数的概念.
  - 人们或许会期待实数分割的思想会将我们引导到数的更加一般性的概念.
- 上面的讨论表明事实并非如此. 实际上实数的集合,
  或者说连续统有一种有理数集合所缺乏的完全性,
  这种完全性可以用数学的语言表达成:
  - 连续统是封闭的.

---

- 我们刚刚证明的结果可以表述如下. `Dedekind` 定理:
  如果实数按照下述方式分成两个类 `L` 和 `R`:
  - (i) 每一个数都属于这两个类中的某一个类;
  - (ii) 每个类都至少含有一个数;
  - (iii) 类 `L` 中的每个元素都小于类 `R` 中的任何一个元素,
    那么就有一个数 `a` 存在, 它具有如下性质:
    所有小于它的数都属于 `L`, 而所有大于它的数都属于 `R`.
    数 `a` 本身则可以属于其中任何一个类.

---

- Weierstrass 定理:
  - 点集的一般理论在分析的较为高深的分支中具有特殊的意义和重要性,
    但是它的大部分内容对于本书来说过于艰深.
  - 然而通过 Dedekind 定理容易推出一个定理, 我们以后将会用到此定理.
  - 定理: 如果集合 `S` 包含无穷多个点, 且它完全包含在某个区间 `(a, b)` 的内部,
    那么区间中至少存在一个点是 `S` 的极限点.

## 实变函数

- 但在此之前, 我们必须指出:
  上面提及的函数的简单例子具有三个特征,
  这三个特征必定是包含在函数的一般性思想之中的:
  - (1) 对 `x` 的一切可能的值, `y` 都是确定的;
  - (2) 对 `x` 的每个值, 有且只有唯一一个 `y` 的值与之对应;
  - (3) `x` 和 `y` 之间的关系是用一个解析表达式给出的,
    根据这个解析公式, 对给定的 `x` 值,
    可以通过直接代入 `x` 的值计算出对应的 `y` 值.
- 的确, 这些重要的特征为许多极其重要的函数所具有.
  但是思考了下面的例子, 就会明白这些特征绝不是函数的本质.
  函数最本质的东西是:
  - 在 `x` 和 `y` 之间存在的某种关系,
    使得对于 `x` 的某个值总会有 `y` 的值与之对应.

### 多项式

- 一个关于 `x` 的多项式是一个形如
  $$ a_0 x^m + a_1 x^{m-1} + ... + a_m $$
  的函数, 其中
  $$ a_0, a_1, ..., a_m $$
  是常数.
  - 最简单的多项式是幂函数
    $$ y = x, x^2, x^3, ..., x^m, ... $$
  - 根据 `m` 是偶数还是奇数, 函数
    $$ x^m $$
    的图有两种不同的类型.

### 有理函数

- 在简单性和重要性仅次于多项式的函数类是有理函数类,
  有理函数是一个多项式被另一个多项式除所得的商.
  - 例如, 设 `P(x)`, `Q(x)` 是多项式, 则我们可以用
  - $$ R(x) = \frac{P(x)}{Q(x)} $$
    来表示一般的有理函数.
- 在 `Q(x)` 是常数这一特殊情形, `R(x)` 变成了一个多项式.
  从而有理函数类包含多项式函数类作为其子类.
  - 关于此定义有下面几点值得注意.
  - (1) 通常我们假设 `P(x)` 和 `Q(x)` 没有公因子 `x + a` 或者
    $$ x^p + ax^{p - 1} + bx^{p - 2} + ... + k $$,
    所有这样的因子都已经用除法约去了.
  - (2) 然而应该注意到: 约掉公因子通常的确改变了函数.
    例如, 考虑函数 `x / x`, 它是一个有理函数.
    而约掉公因子 `x` 之后, 我们得到 `1 / 1 = 1`.
    但是原来的函数并不永远等于 `1`:
    它仅当 `x ≠ 0` 时等于 `1`.
    如果 `x = 0`, 它取形式 `0 / 0`,
    而这是没有意义的. 从而函数 `x / x` 当 `x ≠ 0` 时等于 `1`,
    当 `x = 0` 时没有定义.
    于是它有别于函数 `1`, 函数 `1` 永远取值为 `1`.
- "有理"这个词的使用如下, 从 `x` 出发, 通过对 `x` 做有限多次运算,
  且这些运算只包含用 `x` 或者一个常数乘以其自身, 将这样得到的项相加,
  用这样的乘法和加法得到的一个函数被用相同方式得到的另一个函数相除就生成了有理函数
  `P(x) / Q(x)`.

### 显式代数函数

- 下一个重要的函数类是显式代数函数类. 显式代数函数是这样的函数:
  它们可以从 `x` 出发, 通过有限次地使用构造有理函数时所用到的那些运算,
  再加上有限多个根式运算而得到. 例如
  $$ \sqrt{x} + \sqrt{x + \sqrt{x}} $$
  就是显式代数函数,
  $$ x^{m/n} $$
  亦然, 其中 `m` 和 `n` 是任何整数.

### 隐式代数函数

- 容易验证, 如果
  $$ y = \frac{\sqrt{1 + x} - \sqrt[3]{1 - x}}{\sqrt{1 + x} + \sqrt[3]{1 - x}} $$,
  则有
  $$ (\frac{1 + y}{1 - y})^6 = \frac{(1 + x)^3}{(1 - x)^2} $$
- 又如果
  $$ y = \sqrt{x} + \sqrt{x + \sqrt{x}} $$,
  则有
  $$ y^4 - (4y^2 + 4y + 1)x = 0 $$

- 这些方程中的每一个都可以表示成
  $$ y^m + R_1 y^{m - 1} + ... + R_m = 0 $$
  - 其中,
    $$ R_1, R_2, ..., R_m $$
    是 `x` 的有理函数,
  - 读者容易验证:
    如果 `y` 是上面最后这组例子中的函数之一,
    那么 `y` 就满足一个这种类型的方程.

---

- 这样一来, 就引出了下面的定义:
  如果 `x` 是一个关于 `y` 的 `m` 次方程的根,
  且此方程的系数是 `x` 的有理函数,
  则 `y` 是 `x` 的一个 `m` 次的代数函数.
  - 不失一般性, 可以假设其首项系数为 `1`.
- 这类函数包括之前提到的所有的显式代数函数,
  但也包括其他的不能表示成显式代数函数的函数.

### 超越函数

- `x` 的所有非代数函数的函数称为超越函数.
  此定义是否定式的. 我们不打算给出超越函数的系统分类,
  但可以挑出一两个有特殊重要性的子类来加以讨论.
  - 正反三角函数或者圆函数.
  - 这些函数是初等三角中的正弦函数和余弦函数,
    它们的反函数, 以及从它们导出的函数.

### 其他超越函数类

- 在重要性方面仅次于三角函数的下一个函数类是指数函数和对数函数,
  它们将在后续章节中加以讨论, 现在超出了我们的讨论范围.
  - 而大多数性质已被研究过的其他超越函数类
    (如椭圆函数, `Bessel` 函数, `Legendre` 函数, `Г` 函数等等)
    也都超出了本书的范围.
- 不过有一些初等类型的函数, 尽管它们在理论上的重要性远不如有理函数,
  代数函数或者三角函数, 但是它们作为函数关系的可能种类的例证却有特别的指导意义.

## 复数

- 用 `i` 作乘法的几何解释
- 由于
  $$ (x + yi)i = -y + xi $$,
  故而推出: 如果 `x + yi` 对应于
  $$ \overline{OP} $$,
  画出与 `OP` 等长的 `OQ`, 使得 `POQ` 是一个正的直角,
  那么 `(x + yi)i` 与
  $$ \overline{OQ} $$
  对应.
  - 换句话说, 用 `i` 乘一个复数等同于将对应的位移转动一个直角.
- 从这个观点出发, 我们或许能将复数的整个理论建立起来.
  将 `x` 视为沿 `OX` 的一个位移,
  将 `i` 视为等同于将 `x` 旋转一个直角的运算.
  从这样的思想出发, 我们就会将 `yi` 视为沿 `OY` 所作的,
  大小为 `y` 的位移.

---

- De Moivre 定理
- 由加法和乘法的定义立即推出以下的性质:
  - (1) 两个复数的和的实 (虚) 部等于它们的实 (虚) 部的和;
  - (2) 两个复数的乘积的模等于它们的模的乘积;
  - (3) 两个复数的乘积的辐角或者等于它们的辐角的和, 或者与之相差 `2π`;
  - (4) 两个复数的商的模等于它们的模的商;
  - (5) 两个复数的商的辐角或者等于它们的辐角之差, 或者与之相差 `2π`;
  - (6) 任意多个复数的和之模不大于它们的模之和.

---

- __定理 1__ 任何有理函数 `R(z)` 都可以化成形式
  $$ X + Yi $$,
  其中 `X` 和 `Y` 是关于 `x` 和 `y` 的实系数的有理函数.
- __定理 2__ 如果
  $$ R(x + yi) = X + Yi $$,
  `R` 如前为一个有理函数, 但是有实系数, 那么就有
  $$ R(x - yi) = X - Yi $$.
- __定理 3__ 如果实系数方程
  $$ a_0 z^n + a_1 z^{n - 1} + ... + a_n = 0 $$
  的根不是实数的话, 则可以归结为具有两两成对共轭的形式.

### De Moivre 定理的一般形式

- 由上一节的结果推出, 如果 `q` 是正整数, 那么
  $$ (\cos \theta + i \sin \theta)^{1 / q} $$
  有一个值是
  $$ \cos (\theta / q) + i \sin (\theta / q) $$.
- 对这些表达式中的每一个取 `p` 次幂
  (其中 `p` 是任意一个正整数或负整数),
  我们就得到定理:
  $$ (\cos \theta + i \sin \theta)^{p / q} $$
  有一个值是
  $$ \cos (p \theta / q) + i \sin(p \theta / q) $$,
  或者说成: 如果 `a` 是任意一个有理数, 那么
  $$ (\cos \theta + i \sin \theta)^a $$
  有一个值是
  $$ \cos (a \theta) + i \sin(a \theta) $$.

## 正整变量函数的极限

- 假设
  $$ \phi (n) $$
  是 `n` 的任意一个函数, `P` 是
  $$ \phi (n) $$
  可能具有也可能不具有的任意一个性质,
  例如像其值为正整数或者其值大于 `1` 这样的性质.
  - 对每一个值 `n = 1, 2, 3, ...`, 研究
    $$ \phi (n) $$
    是否具有性质 `P`.
  - 那么就有三种可能性:
  - (a) 对所有的 `n` 值
    $$ \phi (n) $$
    都具有性质 `P`, 或者对其中除了有限多的 `N`
    个这样的值之外的所有其他值都具有性质 `P`;
  - (b) 对所有的 `n` 值
    $$ \phi (n) $$
    都不具有性质 `P`, 或者仅仅对其中有限多的 `N` 个值具有性质 `P`;
  - (c) `(a)` 与 `(b)` 皆不成立

---

- __定义 I__ 如果不论
  $$ \delta $$
  是如何小的正数, 对于充分大的 `n` 值,
  $$ \phi (n) $$
  与 `l` 的差都小于
  $$ \delta $$,
  我们就说当 `n` 趋向
  $$ \infty $$
  时函数
  $$ \phi (n) $$
  趋向极限 `l`.
  - 这个条件也可表述为, 如果不论
    $$ \delta $$
    是如何小的正数, 我们都能确定一个与
    $$ \delta $$
    相对应的数
    $$ n_0 (\delta) $$,
    使得对于所有大于等于
    $$ n_0 (\delta) $$
    的 `n` 值,
    $$ \phi (n) $$
    与 `l` 的差都小于
    $$ \delta $$.
- __定义 II__ 如果给定任意一个无论多么大的数
  $$ \Delta $$,
  我们都能确定
  $$ n_0 (\Delta) $$,
  使得当
  $$ n \ge n_0 (\Delta) $$
  时就有
  $$ \phi (n) > \Delta $$
  成立, 我们就说函数
  $$ \phi (n) $$
  与 `n` 一起趋向
  $$ + \infty $$
  (正无穷大).
  - 这个条件也可表述为, 不论
    $$ \Delta $$
    多么大, 对于充分大的 `n` 值都有
    $$ \phi (n) > \Delta $$.

---

- __定义__ 当 `n` 趋向
  $$ \infty $$
  时,
  $$ \phi (n) $$
  既不趋向一个极限, 也不趋向
  $$ + \infty $$,
  也不趋向
  $$ - \infty $$,
  我们就说当 `n` 趋向
  $$ \infty $$
  时
  $$ \phi (n) $$
  是振荡的.
- __定义__ 如果当 `n` 趋向
  $$ \infty $$
  时
  $$ \phi (n) $$
  是振荡的, 那么
  $$ \phi (n) $$
  将被称为是`有限振荡`的或者是`无限振荡`的, 根据是否能指定一个数 `K`, 使得
  $$ \phi (n) $$
  的所有值的绝对值都小于 `K`, 也即对所有 `n` 的值都有
  $$ | \phi (n) | < K $$.

---

- 假定
  $$ R \{ \phi (n), \psi (n), \chi (n), ... \} $$
  是
  $$ \phi (n), \psi (n), \chi (n), ... $$
  的任意一个有理函数,
  - 也即任何一个形如
  - $$
    P \{ \phi (n), \psi (n), \chi (n), ... \} /
    Q \{ \phi (n), \psi (n), \chi (n), ... \}
    $$
  - 的函数, 其中 `P` 和 `Q` 都是关于
  - $$ \phi (n), \psi (n), \chi (n), ... $$
    的多项式.
- 如果
  $$
  \lim \phi (n) = a, \lim \psi (n) = b, \lim \chi (n) = c, ...
  $$,
  且
  $$ Q (a, b, c, ...) \ne 0 $$,
  - 那么就有
  - $$
    \lim R \{ \phi (n), \psi (n), \chi (n), ... \}
    = R (a, b, c, ...)
    $$.

### 关于无穷级数的一般性定理

- 当处理无穷级数时, 常常会有机会使用下述某个一般性的定理.
  - (1) 如果
    $$ u_1 + u_2 + ... $$
    收敛, 且有和 `s`, 那么
    $$ a + u_1 + u_2 + ... $$
    收敛, 且有和 `a + s`. 类似地,
    $$ a + b + c + ... + k + u_1 + u_2 + ... $$
    收敛, 且有和 `a + b + c + ... + k + s`.
  - (2) 如果
    $$ u_1 + u_2 + ... $$
    收敛, 且有和 `s`, 那么
    $$ u_{m + 1} + u_{m + 2} + ... $$
    收敛, 且有和
    $$ s - u_1 - u_2 - ... - u_m $$.
  - (3) 如果 `(1)` 与 `(2)` 中所考虑的任何一个级数发散或者振荡,
    那么第二个级数也有同样性质.
  - (4) 如果
    $$ u_1 + u_2 + ... $$
    收敛, 且有和 `s`, 那么
    $$ k u_1 + k u_2 + ... $$
    收敛, 且有和 `ks`.
  - (5) 如果 `(4)` 中考虑的第一个级数发散或者振荡,
    那么第二个级数也有同样性质, 除非 `k = 0`.
  - (6) 如果
    $$ u_1 + u_2 + ... $$
    与
    $$ v_1 + v_2 + ... $$
    两者都收敛, 那么级数
    $$ (u_1 + v_1) + (u_2 + v_2) + ... $$
    也收敛, 且其和等于前两个级数之和.
  - (7) 如果
    $$ u_1 + u_2 + ... $$
    收敛, 那么
    $$ \lim u_n = 0 $$.
  - (8) 如果
    $$ u_1 + u_2 + u_3 + ... $$
    收敛,
    那么用任意方式将它的项加括号算作一个新的项所得到的新的级数亦收敛,
    且两个级数的和相同.
  - 这里定理的逆不真.
  - (9) 如果每一项
    $$ u_n $$
    都是正数 (或者是零), 那么级数
    $$ \sum u_n $$
    或者收敛, 或者发散于
    $$ + \infty $$.
  - 如果收敛, 它的和必定是正的 (除非所有的项都是零, 此时当然它的和为零).
  - (10) 如果每一项
    $$ u_n $$
    都是正数 (或者是零), 那么级数
    $$ \sum u_n $$
    收敛的充分必要条件是: 可以找到一个数 `K`,
    使得该级数中任意多项之和都小于 `K`;
    如果 `K` 可以找到, 那么该级数的和不大于 `K`.
  - (11) 如果
    $$ u_1 + u_2 + ... $$
    和
    $$ v_1 + v_2 + ... $$
    是由正的 (或为零的) 项组成的两个级数,
    第二个级数是收敛的, 且如果对所有的 `n` 值都有
    $$ u_n \leqslant K v_n $$,
    其中 `K` 是常数, 那么第一个级数也收敛,
    且它的和不超过第二个级数的和的 `K` 倍.
  - 因为如果
    $$ v_1 + v_2 + ... = t $$,
    那么对所有 `n` 的值都有
    $$ v_1 + v_2 + ... + v_n \leqslant t $$,
    所以
    $$ u_1 + u_2 + ... + u_n \leqslant K t $$,
    这就证明了定理.
  - 反之, 如果
    $$ \sum u_n $$
    发散, 且
    $$ v_n \geqslant K u_n $$,
    其中
    $$ K > 0 $$,
    则
    $$ \sum v_n $$
    发散.

### 有界函数的不定元的极限

- 假设
  $$ \phi (n) $$
  是有界函数, `M` 和 `m` 是它的上界和下界.
  让我们取任意一个实数 `ξ`, 现在来考虑在 `ξ` 与对很大的 `n` 值
  $$ \phi (n) $$
  所取的值之间有可能成立的不等式关系.
- 有三种相互排斥的可能性存在:
  - (1) 对所有充分大的 `n` 值都有
    $$ \xi \ge \phi (n) $$;
  - (2) 对所有充分大的 `n` 值都有
    $$ \xi \le \phi (n) $$;
  - (3) 对无穷多个 `n` 值有
    $$ \xi < \phi (n) $$,
    又对无穷多个 `n` 值有
    $$ \xi > \phi (n) $$.
- 在情形 (1), 我们说 `ξ` 是一个`优数`;
  在情形 (2), 说它是一个`劣数`;
  在情形 (3), 我们称它是一个`中数`.
  - 显然, 没有任何优数会小于 `m`, 也没有任何劣数能大于 `M`.
- 我们来考虑所有优数组成的集合.
  因为它的成员中没有任何一个是小于 `m` 的,
  所以它有一个下界, 我们用
  $$ \wedge $$
  来记这个下界.
  - 类似地, 劣数的集合有一个上界, 我们记之为
    $$ \leftthreetimes $$.
- 我们将
  $$ \wedge $$
  和
  $$ \leftthreetimes $$
  分别称为当 `n` 趋向无穷大时
  $$ \phi (n) $$
  的`不定元的上极限`和`不定元的下极限`;
  - 并记为
  - $$ \wedge = \overline{\lim} \phi (n) $$,
  - $$ \leftthreetimes = \underline{\lim} \phi (n) $$.

---

- 这些数有如下的性质:
  - (1)
    $$ m \le \leftthreetimes \le \wedge \le M $$;
  - (2) 如果有任何一个`中数`存在的话, 那么
    $$ \wedge $$
    和
    $$ \leftthreetimes $$
    就是中数组成的集合的上界和下界;
  - (3) 如果
    $$ \delta $$
    是任何一个正数, 那么对所有充分大的 `n` 值都有
    $$ \phi (n) < \wedge + \delta $$,
    对无穷多个 `n` 值有
    $$ \phi (n) > \wedge - \delta $$;
  - (4) 类似地, 对所有充分大的 `n` 值都有
    $$ \phi (n) > \leftthreetimes - \delta $$,
    对无穷多个 `n` 值有
    $$ \phi (n) < \leftthreetimes + \delta $$;
  - (5)
    $$ \phi (n) $$
    趋向一个极限的充分必要条件是
    $$ \wedge = \leftthreetimes $$,
    在此情形极限就是
    $$ \leftthreetimes $$
    和
    $$ \wedge $$
    共同的值 `l`.

---

- 在这些性质中, (1) 是定义的直接推论, 我们可以如下来证明 (2). 如果
  $$ \wedge = \leftthreetimes = l $$,
  那么就至多存在一个中数, 也就是 `l`, 也就没有什么需要证明的了.
  然后假设
  $$ \wedge > \leftthreetimes $$.
  任何一个中数 `ξ` 都要小于任何一个优数, 且大于任何一个劣数, 所以
  $$ \leftthreetimes \le \xi \le \wedge $$.
- 但是, 如果
  $$ \leftthreetimes < \xi < \wedge $$,
  那么 `ξ` 必定是一个中数, 因为它显然既不是一个优数, 也不是一个劣数.
  于是存在与
  $$ \leftthreetimes $$
  以及与
  $$ \wedge $$
  任意接近的中数.

---

- 为了证明 (3), 我们注意到:
  $$ \wedge + \delta $$
  是优数, 而
  $$ \wedge - \delta $$
  则是中数或者劣数. 于是这个结论就是定义的直接推论,
  而 (4) 的证明本质上与之相同.
- 最后, (5) 可以证明如下.
- 如果
  $$ \wedge = \leftthreetimes = l $$,
  那么对每一个正的
  $$ \delta $$
  值以及充分大的 `n` 值都有
  - $$ l - \delta < \phi (n) < l + \delta $$,
- 所以
  $$ \phi (n) \rightarrow l $$.
  - 反之, 如果
  $$ \phi (n) \rightarrow l $$,
  则上面所写的不等式对于所有充分大的 `n` 值成立.
  - 从而
    $$ l - \delta $$
    就是劣数, 而
    $$ l + \delta $$
    就是优数, 所以
  - $$ \leftthreetimes \ge l - \delta $$,
    $$ \wedge \le l + \delta $$,
- 这样就有
  $$ \wedge - \leftthreetimes \le 2 \delta $$.
  - 由于
    $$ \wedge - \leftthreetimes \ge 0 $$,
    从而这只能在
    $$ \wedge = \leftthreetimes $$
    时成立.

### 符号 O, o, ~

- 假设无论如何
  $$ f(n) $$
  与
  $$ \phi (n) $$
  都是对充分大的 `n` 值 (比方说对于
  $$ n \ge n_0 $$
  ) 有定义的两个 `n` 的函数, 且
  $$ \phi (n) $$
  是正的, 它随 `n` 的增加而递增或者随 `n` 的增加而递减,
  所以, 当
  $$ n \to \infty $$
  时,
  $$ \phi (n) $$
  趋向零, 或者趋向一个正的极限, 或者趋向无穷.
  - 实际上
    $$ \phi (n) $$
    是像 `1/n`, `1` 或者 `n` 这样的简单函数.
    由此我们给出下面的定义:
  - (i) 如果存在一个常数 `K`, 使得对
    $$ n \ge n_0 $$
    有
    $$ \mid f \mid \le K \phi $$,
    我们就记为
    $$ f = O(\phi) $$.
  - (ii) 如果当
    $$ n \to \infty $$
    时有
    $$ f / \phi \to 0 $$,
    我们就记为
    $$ f = o (\phi) $$.
  - (iii) 如果
    $$ f / \phi \to l $$,
    其中
    $$ l \ne 0 $$,
    我们就记为
    $$ f \sim l \phi $$.
    特别地,
    $$ f = O(1) $$
    表示 `f` 是有界的 (所以它要么趋向一个极限, 要么有限振荡), 而
    $$ f = o(1) $$
    则表示
    $$ f \to 0 $$.
- 于是我们有
  - $$ n = O(n^2) $$,
  - $$ 100 n^2 + 1000 n = O(n^2) $$,
  - $$ \sin n \theta \pi = O(1) $$,
  - $$ n = o(n^2) $$,
  - $$ 100 n^2 + 1000 n = o(n^3) $$,
  - $$ \sin n \theta \pi = o(n) $$,
  - $$ n + 1 \sim n $$,
  - $$ 100 n^2 + 1000 n \sim 100 n^2 $$,
  - $$ n + sin n \theta \pi \sim n $$,
  - 以及
  - $$ \frac{a_0 n^p + a_1 n^{p-1} + ... + a_p}{b_0 n^q + b_1 n^{q-1} + ... + b_q} \sim \frac{a_0}{b_0} n^{p-q} $$
  - 如果
    $$ a_0 \ne 0 $$
    且
    $$ b_0 \ne 0 $$
    的话.

---

- 这里要作一补充说明, 以防止可能出现的误解. 我们说
  $$ f = O(\phi) $$
  是表明通常所说的"
  $$ f $$
  的大小的阶并不比
  $$ \phi $$
  的阶高", 而不排除
  $$ f $$
  的阶比
  $$ \phi $$
  的阶低 (如同上面第一个关系式那样).
- 到目前为止, 我们已经定义了 (比方说)
  `"f(n) = O(1)"`, 或者 `"f(n) = o(n)"`,
  但还没有单独地定义过`"O(1)"`或者`"o(1)"`.
  - 我们可以使得定义更加灵活, 约定
    $$ O(\phi) $$
    或者
    $$ o(\phi) $$
    表示一个满足
    $$ f = O(\phi) $$
    或者
    $$ f = o(\phi) $$
    的未予指定的函数, 例如, 这样我们就可以记
  - `O(1) + O(1) = O(1) = o(n)`,
  - 它的含义是
    "如果 `f = O(1)` 且 `g = O(1)`, 那么 `f + g = O(1)`, 于是更有 `f + g = o(n)`".
    或者我们又可以记
  - $$ \sum_{r = 1}^{n} O(1) = O(n) $$,
  - 其含义为 `n` 个绝对值都小于一个常数的项之和必小于 `n` 的一个常数倍.

---

- 应该注意到, 包含 `O` 以及 `o` 的公式通常并不是可逆的.
  例如`"o(1) = O(1)"`也就是`"如果 f = o(1), 那么就有 f = O(1)"`是正确的,
  然而`"O(1) = o(1)"`却是错误的.
- 容易对我们的符号总结出像下面这样的若干个一般性质:
  - $$ O(\phi) + O(\psi) = O(\phi + \psi) $$;
  - $$ O(\phi) O(\psi) = O(\phi \psi) $$;
  - $$ O(\phi) o(\psi) = o(\phi \psi) $$;
  - 如果
    $$ f \sim \phi $$,
    那么
    $$ f + o(\phi) \sim \phi $$.
  - 这样的定理均为定义之直接推论.
- 这些定义的效用, 以及与一个连续变量的函数所对应的定义的效用,
  都将在后面的章节中变得愈加明显.

## 一个连续变量的函数之极限, 连续函数和不连续函数

- __定义 1__ 函数
  $$ \phi (x) $$
  称为当 `x` 趋向
  $$ \infty $$
  时趋向一个极限 `l`, 如果给定无论多么小的一个正数
  $$ \delta $$,
  都能选取到一个数
  $$ x_0 (\delta) $$,
  使得对于所有大于等于
  $$ x_0 (\delta) $$
  的 `x` 值,
  $$ \phi (x) $$
  与 `l` 的差都小于
  $$ \delta $$,
  也就是当
  $$ x ≥ x_0 (\delta) $$
  时有
  - $$ \mid \phi (x) - l \mid < \delta $$.
- 当定义中的情形发生时, 我们可以记为
  - $$ \lim_{x \to \infty} \phi (x) = l $$,
  - 或者当不可能出现混淆时, 就简单记为
    $$ \lim \phi (x) = l $$,
    或者写成
    $$ \phi (x) \to l $$.
  - 类似地我们有定义 `2`.

---

- __定义 2__ 函数
  $$ \phi (x) $$
  称为与 `x` 一起趋向
  $$ \infty $$,
  如果给定无论多么大的一个数
  $$ Δ $$,
  我们都能选取到一个数
  $$ x_0 (Δ) $$,
  使得当
  $$ x ≥ x_0 (Δ) $$
  时有
  - $$ \phi (x) > Δ $$.
  - 此时我们记
    $$ \phi (x) \to \infty $$.
  - 我们可以类似地定义
    $$ \phi (x) \to - \infty $$.
  - 最后我们有如下定义.

---

- __定义 3__ 如果上面两个定义中的条件都不满足, 就称
  $$ \phi (x) $$
  当 `x` 趋向
  $$ \infty $$
  时是振荡的.
  - 如果
    $$ \mid \phi (x) \mid $$
    当
    $$ x ≥ x_0 (Δ) $$
    时小于某个常数 `K`, 那么就称
    $$ \phi (x) $$
    是有限振荡的, 反之则称它是无限振荡的.

---

- 如果对于给定的无论多小的正数
  $$ \delta $$,
  我们都能选取
  $$ y_0 (\delta) $$,
  使得对于所有异于零且绝对值小于等于
  $$ y_0 (\delta) $$
  的 `y` 的值,
  $$ \phi (y) $$
  与 `l` 相差都小于
  $$ \delta $$,
  那么我们就称当 `y` 趋向 `0` 时
  $$ \phi (y) $$
  趋向极限 `l`, 记为
  - $$ \lim_{y \to 0} \phi (y) = l $$.
- 同样地, 如果当
  $$ y \to +0 $$
  时有
  $$ \phi (y) \to \infty $$,
  当
  $$ y \to -0 $$
  时也有
  $$ \phi (y) \to \infty $$,
  那么我们就称当
  $$ y \to 0 $$
  时有
  $$ \phi (y) \to \infty $$.
  - 类似地我们可以定义"当
    $$ y \to 0 $$
    时有
    $$ \phi (y) \to - \infty $$
    ".
- 最后, 如果当
  $$ y \to +0 $$
  时
  $$ \phi (y) $$
  既不趋向极限, 也不趋向
  $$ \infty $$
  或者
  $$ - \infty $$,
  我们就称当
  $$ y \to +0 $$
  时
  $$ \phi (y) $$
  是振荡的, 它是有限振荡还是无限振荡则要根据具体情形来判断;
  我们还可以类似地定义当
  $$ y \to -0 $$
  时函数是振荡的.

---

- 如果对于给定的
  $$ \delta $$,
  我们总可以确定数
  $$ \varepsilon (\delta) $$,
  使得当
  $$ 0 < \mid x - a \mid ≤ \varepsilon (\delta) $$
  时有
  - $$ \mid \phi (x) - l \mid < \delta $$,
  - 那么
  - $$ \lim_{x \to a} \phi (x) = l $$.
- 限制 `x` 仅取大于 `a` 的值, 也就是用
  $$ a < x ≤ a + \varepsilon (\delta) $$
  代替
  $$ 0 < \mid x - a \mid ≤ \varepsilon (\delta) $$,
  我们就定义了"当 `x` 从右边趋向 `a` 时
  $$ \phi (x) $$
  趋向 `l`", 可以把它写成
  - $$ \lim_{x \to a+0} \phi (x) = l $$.
- 用同样的方法我们可以定义
  - $$ \lim_{x \to a-0} \phi (x) = l $$.
- 于是
  $$ \lim_{x \to a} \phi (x) = l $$
  等价于两个结论
  - $$ \lim_{x \to a+0} \phi (x) = l $$,
  - $$ \lim_{x \to a-0} \phi (x) = l $$.

---

- 读者应该仔细注意: 论及
  $$ \phi (x, y) $$
  关于两个变量 `x` 和 `y` 的连续性与分别考虑它关于每一个变量的连续性,
  其内涵要多得多.
  - 显然, 如果
    $$ \phi (x, y) $$
    关于 `x` 和 `y` 连续, 那么当对另一个变量 `y` (或者 `x`)
    指定任何一个固定的值时,
    $$ \phi (x, y) $$
    关于 `x` (或者 `y`) 是连续的.
  - 但是其逆不成立.

## 微分学和积分学中另外一些定理

- 如果
  $$ f'(x) $$
  和
  $$ \phi ' (x) $$
  是连续的, 那么
  - $$
      \int_{a}^{b} f(x) \phi ' (x) dx =
      f(b) \phi (b) - f(a) \phi (a) -
      \int_{a}^{b} f'(x) \phi (x) dx
    $$.
  - 此公式称为定积分的`分部积分`公式.

## 对数函数, 指数函数以及三角函数的一般理论

> 本章内容移步:
  [复分析: 可视化方法](https://book.douban.com/subject/35316347/)
