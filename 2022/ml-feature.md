---
title: 特征工程 & Interpretable
description: 雁来音信无凭, 路遥归梦难成. 离恨恰如春草, 更行更远还生.
date: 2021-09-20
---

- [特征工程的艺术: 通用技巧与实用案例](https://www.ituring.com.cn/book/2817)
  - [特征工程的艺术](https://book.douban.com/subject/35902261/)

```
对于回归问题, 误差可以用差来测量, 但这样负的误差会和正的误差抵消,
所以有必要取误差的绝对值. 不过, 绝对值不是连续可导的,
所以我们通常使用误差的平方, 即均方误差 (MSE).
为了让度量与原始信号有同样的单位, 你可以求出均方误差的平方根, 得到 RMSE.
还有一些不太常用的误差度量方式, 例如,
你可以不使用平方, 转而使用另一种指数, 或者使用负的误差代替正的误差.

请注意, 如果直接使用误差作为 ML 算法 (例如, 训练一个神经网络) 优化过程的一部分,
那么连续可导的要求就是非常重要的. 你还可以在执行算法时使用一种度量,
在评价结果时使用另一种度量, 并看一下它们是否与基本目的 (效用度量) 相符合.

最后, 上面讨论的度量方式都使用均值, 都试图总结出模型行为最有代表性的方面,
但无法体现结果中的方差 (variance). 这个话题在 ML 中已经得到了非常深人的研究,
就是偏差
(bias: 学习了错误的事情; 由于模型局限性而产生的误差)
与方差
(variance: 学习了分散的点; 由于有限的数据抽样以及不同样本生成的不同模型而产生的误差)
的均衡问题.
```

```
识别异常值要比删除它们更重要, 因为如果数据中有很多异常值,
就表示这可能是一种非正态的"肥尾"分布.
你收到的异常值还可能是一种削波数据或失真数据
(即所谓的删失数据, censored data).

你可以在异常值上训练一个独立模型, 因为它们有时候会表现出一种所谓的王者效应
(king effect), 即分布中的前几个代表与其余实例在行为上截然不同.

对于 FE, 我们可以使用异常值检测在训练数据上学习一个模型,
再使用这个模型找出不正常的实例及其特征值. 一般来说,
异常值检测技术可以是监督的, 也可以是无监督的. 在 FE 中,
花费额外精力来标注异常值是不太可行的, 所以我们重点关注无监督技术.
主要的技术包括聚类, 密度估计和单类别 SVM. 在进行无监督异常值检测时,
可以使用诊断技术和调节技术:
诊断技术用于找出异常值,
调节技术用来使 ML 模型在存在异常值时具有稳健性.
```

- __使用典型值进行替换__.
  - 如果你没有某个值的任何有关信息, 那么当这个值缺失时,
    就不应该用一个能被 ML 算法选择出来作为强烈信号的值来填充它.
  - 对于这种缺失数据, 你可以让 ML 算法尽可能地忽略这个特征.
  - 要完成这个任务, 应该用均值 (如果具有多个异常值, 就使用中位数)
    或最常见的值 (众数) 来替换它, 使其尽量平淡无奇.
  - 这种方法尽管非常简单, 但仍然远远好于让这个值为 `0`,
    就像很多 ML 工具箱中那样.
  - 同样, 如果数据中有很多自然产生的 `0`, 你应该仔细地研究一下,
    看看这些 `0` 能否构成一个独立的现象.
  - 例如, 添加一个表示这个值是否为 `0` 的指示特征.

- __仿射变换__ 是一种线性变换,
  是通过将源平面上的三个点映射到目标平面上的三个点来定义的.
  - 从数学上说, 它的定义方式是乘以一个 `2 × 2` 矩阵再加上一个 `2 × 1` 向量.
  - 它包括平移, 缩放和旋转, 这些是我们要使用的一个仿射变换子集.

- 如果不考虑特征的可解释性, 就可以使用最新的技术从核变换生成一些随机特征.
  特别地, 从对核函数的傅里叶分解中随机选择正弦波是对核函数一个有效,
  基于特征的近似.
- 核方法的基础是一项重大理论成果, 称为 __Mercer__ 定理,
  即对于任意定义了对象间一种度量方式 (对称且半正定) 的函数 `K`,
  都存在一个 `φ`, 使得 `K` 可以用 `φ` 的内积来表示.
- 相关文献提出了多种核, 包括`线性核`, `多项式核`, `Fisher 核`,
  `径向基函数 (RBF) 核`, `图核`, `字符串核`等, 它们的应用非常广泛.

---

- 如果你在处理一个距离对于模型非常重要的问题,
  就可以考虑选择一些特殊元素计算距离, 得到距离的上下文,
  从而将领域知识加入问题中.

```
在处理时间戳数据时, 我们可以做出一个关键假设,
即存在一个具有有限"记忆"的基本数据生成过程.
也就是说, 这个过程仅仅依赖于几个过去的状态.
这种过程称为马尔可夫过程,
过去状态的数量称为该马尔可夫过程的阶.

这种非完整记忆有助于缓解特征爆炸问题, 在以建模为目的时,
也是对现实的一种简化.

在对时间序列进行 FE 时, 马尔可夫假设可以有两种应用:
集成以前的目标值 (或目标类别), 称为马尔可夫特征;
集成过去的特征值, 称为延迟特征.
```

```
当特征值中的可变性非常高的时候, 直接使用延迟特征或其差分是有问题的.
对这种数据的一种改进方法是通过滑动窗口来实现时间平滑.

例如, 使用窗口中值的中位数或平均数替换特征值.
在我们的例子中, 将使用一个容量为 3 的窗口.
请注意, 我们会丢失两个年份, 因为在这两个年份上无法计算平均数.

有多种方法可以测量窗口中的平均数, 常用的方法包括算术均值,
加权平均 (对与当前值更接近的延迟给予更大权重)
和指数平均 (其中的"记忆"平均数被更新为当前值与前一个"记忆"的加权和).

你还可以聚合不同容量的窗口以得到数据的一个时间剖面, 也就是说,
使用若干个在不同时间跨度上平滑的特征来代替平滑特征.

窗口中值的均值是一个描述性统计量. 其他选择还包括标准差,
以及描述窗口中数据与正态分布有多相似的度量方式 (峰度和偏度).
在本节中, 这些描述性特征称为关键特征.
在计算均值时, 你应该注意 Slutsky-Yule 效应:
在完全随机的数据上进行平均时, 会得到一条正弦曲线.
这有可能误导 ML, 使它认为数据中有一些波动, 而这些波动实际上并不存在.
```

- __协方差__ 是两个随机变量之间线性相关性的测量方式, 定义为:
  - $$ Cov (X, Y) = E \left [ (X - μ_X) (Y - μ_Y) \right ] $$
- 如果两个变量是独立的, 那么协方差为 `0`;
  如果不是独立的, 那么通过协方差可以知道,
  当一个变量增大时另一个变量是否也随之增大,
  但变化的数量级是不稳定的
  (取决于随机变量的实际值).
  - 你还可以用协方差除以它们的标准差, 得到`相关系数`.
- 对于 TSA, 这两个变量就是有延迟的同一变量.
  因此, 自相关系数测量的就是相隔一定时间距离
  (延迟) 的两个实例之间的相关性.
  - 它提供了对生成时间序列数据的概率模型的深刻理解,
    其形状可以表明时间序列的本质.
- 需要注意的是, 很多过程具有同样的自相关, 这意味着有很多错误的相关性:
  - 如果两个不相关的变量
    $$ Y_t $$
    和
    $$ X_t $$
    的自相关参数非常相似, 那么即使
    $$ X_t $$
    没有解释能力, 普通回归也会表示出很强的相关性:
  - 如果
    $$ X_t $$
    和
    $$ Y_t $$
    都按照一个固定的总体水平进行变动,
    那么回归就会错误地表示出很强的相关性.
- 从 `FE` 的角度看, 如果一个不相关特征的成长过程与目标变量很相似,
  那么它就会得到一个非常高的特征效用分数, 即使这两个变量是不相关的.
  - 因此, 它对于 `ML` 算法是没有意义的.

------------------

- [Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/)
  - A Guide for Making Black Box Models Explainable.

## Interpretability

- **Feature summary statistic**: Many interpretation methods
  provide summary statistics for each feature. Some methods
  return a single number per feature, such as feature importance,
  or a more complex result, such as the pairwise
  feature interaction strengths, which consist of
  a number for each feature pair.
- **Feature summary visualization**: Most of the feature
  summary statistics can also be visualized. Some feature
  summaries are actually only meaningful if they are
  visualized and a table would be a wrong choice.
  - The partial dependence of a feature is such a case.
    **Partial dependence** plots are curves that show a
    feature and the average predicted outcome.
- **Model internals** (e.g. learned weights): The
  interpretation of intrinsically interpretable models
  falls into this category. Examples are the weights in
  linear models or the learned tree structure
  (the features and thresholds used for the splits)
  of decision trees.
- **Data point**: This category includes all methods that
  return data points (already existent or newly created)
  to make a model interpretable. One method is called
  **counterfactual explanations**.
  - To explain the prediction of a data instance,
    the method finds a similar data point by changing
    some of the features for which the predicted outcome
    changes in a relevant way (e.g. a flip in the predicted class).
  - Another example is the identification of prototypes of
    predicted classes. To be useful, interpretation methods that
    output new data points require that the data points
    themselves can be interpreted. This works well for
    images and texts, but is less useful for
    tabular data with hundreds of features.
- **Intrinsically interpretable model**: One solution to
  interpreting black box models is to approximate them
  (either globally or locally) with an interpretable model.
  The interpretable model itself is interpreted by
  looking at internal model parameters or
  feature summary statistics.

### Algorithm Transparency

- Algorithm transparency is about how the algorithm
  learns a model from the data and what kind
  of relationships it can learn.
- Algorithm transparency only requires knowledge of
  the algorithm and not of the data or learned model.
  - This book focuses on model interpretability and
    not algorithm transparency.

### Model Interpretability

- This level of interpretability is about understanding
  how the model makes decisions, based on a holistic view
  of its features and each of the learned components
  such as weights, other parameters, and structures.
  - Global model interpretability is very
    difficult to achieve in practice.
  - I argue that you cannot really imagine a linear model
    with 5 features, because it would mean drawing the
    estimated hyperplane mentally in a `5-dimensional` space.
  - Usually, when people try to comprehend a model,
    they consider only parts of it,
    such as the weights in linear models.

- While **global** model interpretability is usually out of reach,
  there is a good chance of understanding at least
  some models on a modular level.
  - Not all models are interpretable at a parameter level.
- If you look at an individual prediction, the behavior of
  the otherwise complex model might behave more pleasantly.
  **Locally**, the prediction might only depend linearly
  or monotonically on some features, rather than having
  a complex dependence on them.
  - Local explanations can therefore be more accurate
    than global explanations.
- Model predictions for multiple instances can be explained
  either with global model interpretation methods
  (on a modular level) or with
  explanations of individual instances.

### Properties of Explanations

- Properties of Explanation Methods
  - **Expressive Power** is the "language" or structure of
    the explanations the method is able to generate.
  - An explanation method could generate `IF-THEN` rules,
    decision trees, a weighted sum,
    natural language or something else.
  - **Translucency** describes how much the explanation method
    relies on looking into the machine learning model,
    like its parameters.
  - The advantage of high translucency is that the method can
    rely on more information to generate explanations.
  - The advantage of low translucency is that the explanation
    method is more portable.
  - **Portability** describes the range of machine learning
    models with which the explanation method can be used.
  - Methods with a low translucency have a higher portability
    because they treat the machine learning model as a black box.
  - **Algorithmic Complexity** describes the computational
    complexity of the method that generates the explanation.

- Properties of Individual Explanations
  - **Accuracy**: How well does an explanation predict unseen data?
  - **Fidelity**: How well does the explanation approximate the
    prediction of the black box model?
  - High fidelity is one of the most important properties of
    an explanation, because an explanation with low fidelity
    is useless to explain the machine learning model.
  - Accuracy and fidelity are closely related. If the black
    box model has high accuracy and the explanation
    has high fidelity, the explanation also has high accuracy.
  - **Consistency**: How much does an explanation differ
    between models that have been trained on the same task
    and that produce similar predictions?
  - High consistency is desirable if the models really
    rely on similar relationships.
  - **Stability**: How similar are the explanations for
    similar instances?
  - While consistency compares explanations between models,
    stability compares explanations between similar
    instances for a fixed model.
  - High stability is always desirable.
  - **Comprehensibility**: How well do humans understand
    the explanations?
  - **Certainty**: Does the explanation reflect the
    certainty of the machine learning model?
  - **Degree of Importance**: How well does the explanation
    reflect the importance of features or
    parts of the explanation?
  - **Novelty**: Does the explanation reflect whether a
    data instance to be explained comes from a "new"
    region far removed from the distribution
    of training data?
  - The concept of novelty is related to the concept
    of certainty. The higher the novelty, the more
    likely it is that the model will have low
    certainty due to lack of data.
  - **Representativeness**: How many instances does
    an explanation cover?

## Interpretable Models

- A model with monotonicity constraints ensures that the
  relationship between a feature and the target outcome
  always goes in the same direction over the
  entire range of the feature:
  - An increase in the feature value either always leads
    to an increase or always to a decrease
    in the target outcome.
- Some models can automatically include interactions
  between features to predict the target outcome.
  You can include interactions in any type of model
  by manually creating interaction features.
  - Interactions can improve predictive performance,
    but too many or too complex interactions
    can hurt interpretability.

### Linear Regression

- The interpretation of the features in the linear
  regression model can be automated by using
  following text templates.
  - Interpretation of a `Numerical Feature`
  - An increase of feature
    $$ x_k $$
    by one unit increases the prediction for `y` by
    $$ β_k $$
    units when all other feature values remain fixed.
  - Interpretation of a `Categorical Feature`
  - Changing feature
    $$ x_k $$
    from the reference category to the other category
    increases the prediction for `y` by
    $$ β_k $$
    when all other features remain fixed.

- The importance of a feature in a linear regression
  model can be measured by the absolute
  value of its `t-statistic`.

### Logistic Regression

- A solution for classification is logistic regression.
  Instead of fitting a straight line or hyperplane,
  the logistic regression model uses the logistic
  function to squeeze the output of
  a linear equation between `0` and `1`.

- These are the interpretations for the logistic regression
  model with different feature types:
  - `Numerical feature`:
  - If you increase the value of feature
    $$ x_j $$
    by one unit, the estimated odds change by a factor of
    $$ exp(β_j) $$.
  - `Binary categorical feature`:
  - One of the two values of the feature is the reference
    category (in some languages, the one encoded in `0`).
    Changing the feature
    $$ x_j $$
    from the reference category to the other category
    changes the estimated odds by a factor of
    $$ exp(β_j) $$.
  - `Categorical feature with more than two categories`:
  - One solution to deal with multiple categories is
    `one-hot-encoding`, meaning that each category has
    its own column.
  - You only need `L-1` columns for a categorical feature
    with `L` categories, otherwise it is over-parameterized.
  - The `L-th` category is then the reference category.
    You can use any other encoding that can be used in
    linear regression. The interpretation for each category
    then is equivalent to the interpretation of binary features.
  - Intercept
    $$ β_0 $$:
  - When all numerical features are zero and the categorical
    features are at the reference category, the estimated odds are
    $$ exp(β_0) $$.
  - The interpretation of the intercept weight is usually not relevant.

### GLM, GAM and more

------------------

- [人工智能](https://book.douban.com/subject/36093845/)
  - 一般
  - 纯粹是冲着 __姚期智__ 三个字买的~

```
综上, 我们可以看出, 在温度足够高的情况下, 每一个状态都有可能被访问;
而当温度逐渐降低, 能够被访问到的状态将逐渐收敛到几个能量最小的状态中,
从而找到局部最优解.

在模拟退火算法中, 依概率收敛到能量最小状态需要三个条件:
一是初始温度必须足够高;
二是每个温度下, 状态的交换必须足够充分;
三是温度的下降必须足够缓慢.

组合优化问题和退火过程可以做如下类比,
从中我们可以理解模拟退火算法与物理退火过程的关系, 见下表.

            模拟退火算法与物理退火过程的关系
              物理退火过程            模拟退火算法
  对象       物理系统的某一状态      组合优化问题的某一个解
  评估       状态的能量             解的评估函数值
  目标       能量最低的状态          优化问题的最优解
  控制变量    温度                  搜索控制参数 T
```

- 估价函数一般由两部分组成:
  - 一部分是对该节点收益的估计,
  - 另一部分是这个估计的风险 (即, 对这个估计有多不确定).
- 前一部分通常是通过按照某种策略多次采样来计算得到的 (因此叫做蒙特卡罗方法),
  后一部分通常用模拟或采样的次数来衡量, 模拟或采样的次数越多, 风险就越小.
  - 当我们选择动作的时候, 自然想要选择收益高的, 但对于高收益高风险的动作,
    我们也要避免. 我们扩张一个节点的目的当然是为了降低对估计的不确定程度.
  - 但是对于同样不确定估计准确程度的低收益节点和高收益节点,
    我们通常也偏好于先降低高收益高风险节点的不确定性.
- 因此, MCTS 不同的变种主要都是在设计估价函数,
  即设法权衡"收益"和"风险"这两者的关系.
  下面介绍 MCTS 的一种实现方法, 称为 UCT
  (upper confidence bounds applied for trees).
  - 它为每个节点 `x` 记录两个变量 `U(x)` 和 `N(x)`, 其中 `N(x)`
    表示访问该节点的次数, `U(x)` 表示这 `N(x)` 次访问中所记录的收益的总和.
- UCT 包含 `4` 个主要阶段:
  - __选择__: 从根节点开始, 不断选择某个子节点.
  - 选择的逻辑是, 每次挑选 `UCB1(x)` 最大的一个子节点 `x`,
    直到选择到一个未经访问的节点 `u`.
  - 令 `C` 是某个常数, `UCB1(x)` 定义如下:
  - $$ UCB1(x) = \frac{U(x)}{N(x)} + C \times \sqrt{\frac{\log N(Parent(x))}{N(x)}} $$
  - __扩展__: 将选择阶段得到的节点 `u` 新建出来, 变为已访问节点.
  - __模拟__: 从状态 `u` 开始, 双方均使用随机策略直到游戏结束, 获得收益 `A`.
  - __更新__: 将 `u` 到根路径上的所有节点的 `U` 和 `N` 进行更新.
  - 即对于 `u` 到根路径上的所有点 `x`, 令
    $$ U(x) += A $$,
    $$ N(x) += 1 $$.
  - UCT 不断重复上述 `4` 个过程,
    最后输出根节点访问次数最多的子节点对应的动作作为智能体在当前状态下的动作.
- 这个算法的分析比较复杂, 下面简单介绍一下算法各个部分的含义, 以及这么设计的理由.
- 首先是 `UCB1` 的式子,这个式子借鉴自 UCB (upper confidence bound) 算法.
  - 它由两部分相加组成, 第一部分即多次访问该节点的平均收益, 代表对当前节点收益的估计.
  - 第二部分则对应了该估计的风险, 可以当作对"探索行为"的奖励:
    `x` 被访问得越多, 则这一部分的值越小.
  - 其中 `C` 只是一个常数, 而分子中 `log` 的那一项保证了每个节点都会被访问无数次.
  - 因为如果一直不访问某个节点 `x`, 那么第二部分将趋于无穷.
- 如果一个动作目前的平均收益越高, 不确定性越高, UCT 就越倾向于选择这个动作来探索.
  因此可以认为, UCT 每次会贪心地选取一个"上限最高"的动作. 不严谨地说,
  随着选择一个动作的次数变多, 它的平均收益的估计会越来越准, 而不确定性会迅速变小.
  - 如果在这种情况下, 一个动作依然以一个相当高的频率被选择,
    那么在某种程度上说明这个动作的平均收益很高 (因为此时不确定性对估价的贡献很小).
  - 这样一来, 最后选择根节点被访问次数最多的子节点可以理解为选择了收益高且风险小的一个动作.
  - 事实上也有一些 MCTS 的变种是直接挑选平均收益最高的子节点作为所选的策略的,
    这两者在分析上有细微的差别, 这里不做展开.

```
GBDT 是当前除深度神经网络外使用最广泛的机器学习模型之一.
目前使用最广泛的 GBDT 的高效开源实现包括 XGBoost, LightGBM 和 CatBoost.
其中 XGBoost 开源于 2015 年, 利用二阶导数信息进行更快速的迭代,
并支持快速和分布式训练大规模数据.
LightGBM 开源于 2017 年, 相比于 XGBoost 更加注重速度和内存使用的优化,
因此训练速度更快.
CatBoost 开源于 2017 年, 它修改了传统的梯度提升过程, 进一步控制了过拟合.
此外, CatBoost 还利用标签信息将离散型变量编码为数值型变量,
并自动对多个特征进行组合得到新的交叉特征.
例如, 对于一个有 m 种取值的离散型特征, 可以用 m 个取值为 0/1 的数值特征来表示,
如果一个数据的该离散型特征取值情况为第 k 种, 则对应的数值特征的第 k 个取值为 1,
其余取值全部为 0. 这种编码方式称为独热编码 (one-hot encoding).
此外, 还有一些基于数据标签的编码方式, CatBoost 非常好地支持了这种编码.
因此在不进行额外特征工程的情况下, CatBoost 往往能取得相对准确的预测结果.
以上提到的正则项, 每个叶子的样本数下限以及随机采样等都可以在以上的开源版本中进行选择和设定.
```

- 分类结果混淆矩阵

```
真实情况      预测结果
        正例        反例
正例    TP (真正例)  FN (假反例)

反例    FP (假正例)  TN (真反例)
```

- 查准率 `P` 与查全率 `R` 分别定义为
  - $$ P = \frac{TP}{TP + FP} $$
  - $$ R = \frac{TP}{TP + FN} $$

---

$$
F1 = \frac{2 \times P \times R}{P + R} =
\frac{2 \times TP}{样例总数 + TP - TN}
$$

- 在一些应用中, 对查准率和查全率的重视程度有所不同.
  - 例如在商品推荐系统中, 为了尽可能少打扰用户,
    更希望推荐内容确是用户感兴趣的, 此时查准率更重要;
  - 而在逃犯信息检索系统中, 更希望尽可能少漏掉逃犯, 此时查全率更重要.
- `F1` 度量的一般形式 --
  $$ F_β $$,
  能让我们表达出对`查准率`/`查全率`的不同偏好, 它定义为
  - $$ F_β = \frac{(1 + β^2) \times P \times R}{(β^2 \times P) + R} $$
  - 其中 `β > 0` 度量了查全率对查准率的相对重要性.
  - `β = 1` 时退化为标准的 `F1`;
  - `β > 1` 时查全率有更大影响;
  - `B < 1` 时查准率有更大影响.

---

- 在介绍完具体例子之后, 现在给出普适的马尔可夫决策过程的严格定义.
- 定义 __马尔可夫决策过程__:
  - 考虑离散的时间序列, `t = 0, 1, 2, ...`.
    一个离散时间马尔可夫决策过程由以下部分组成:
  - __系统状态__:
    $$ S = \{ 1, 2, ..., N \} $$
    表示整个系统的状态空间, 即所有可能状态的合集;
    $$ s(t) \in S $$
    表示在 `t` 时刻系统所处状态.
  - __控制动作__: 在状态
    $$ s(t) = i, i \in S $$
    下, 系统的动作集合用
    $$ A(i) $$
    表示; 每个时刻 `t`, 系统会从中选择一个动作
    $$ a(t) = a, a \in A(i) $$.
  - __转移概率__: 在状态 `i` 和动作 `a` 下, 系统以概率
    $$ P_{ij}(a) $$
    从状态 `i` 跳转到状态 `j`, 即
    $$ P_{ij}(a) = Pr \{ s(t + 1) = j \mid s(t) = i, a(t) = a \} $$.
    通过用策略 `π` 来表示系统的控制选择策略, 即以
    $$ π(i, a) = Pr \{ a(t) = a \mid s(t) = i \} $$
    表示在状态 `i` 下选择控制动作 `a` 的概率, 可以便利地将整体的转移概率记为
  - $$
    P(\pi) =
    \begin{bmatrix}
    P_{11}(\pi) & \cdots & P_{1N}(\pi) \\
    \vdots      & \vdots & \vdots      \\
    \cdots      & \cdots & P_{NN}(\pi)
    \end{bmatrix}
    $$,
  - 这里
    $$ P_{ij}(\pi) = \sum_{a} \pi (i, a) P_{ij} (a) $$.
  - __奖励函数__: 在状态 `s(t)` 与动作 `a(t)` 下, 系统获得一个奖励
    $$ r(s(t), a(t)) $$.
  - __折扣系数__:
    $$ 0 < \gamma < 1 $$
    表示系统对下一时刻奖励延迟性的期望值.
- 在马尔可夫决策过程中, 系统的目标是选择一个控制策略
  $$ π^{*} $$,
  最大化下述折扣奖励:
  - $$
    J^{*} = \underset{\pi}{max} \mathbb{E} \{
    \sum_{t = 0}^{\infty} \gamma^{t} r(s(t), a(t)) \mid s(0), π \}
    $$

------------------

- https://www.coursera.org/specializations/machine-learning-introduction
  - https://www.coursera.org/learn/machine-learning
  - https://www.coursera.org/account/accomplishments/certificate/THGATFHMCZ8T
  - https://www.coursera.org/learn/advanced-learning-algorithms
  - https://www.coursera.org/account/accomplishments/certificate/AVLQL2HQ9XTV
  - https://www.coursera.org/learn/unsupervised-learning-recommenders-reinforcement-learning
  - https://www.coursera.org/account/accomplishments/certificate/3F9VKTLHP3ZJ
  - https://www.coursera.org/account/accomplishments/specialization/certificate/JZHGFEKRQ7RX
  - 一般般, 不推荐

- [XGBoost](https://github.com/dmlc/xgboost)

------------------

- [Machine Learning Engineering in Action](https://book.douban.com/subject/35568115/)
  - __不推荐__

> Nothing is more demoralizing than building an ML
  solution that solves the wrong problem.

```
不仅仅是 ML 项目, 一些工程项目,
从一开始, 便偏离了实际的解决问题的目标,
而是为了引入看似炫酷的技术和四不像的架构模式!

越是欠缺实战, 没有目标的所谓技术领导者,
越是期望在一开始就设计一个完美的系统.

而真正的务实派, 在早期阶段, 首先侧重于:
1. 找准目标, 最关键的目标
2. 技术上, 避免方向性的错误

实现阶段, 及时的反馈和调整. 同时:
1. 对于系统的薄弱环节和未来改进重点逐步了然于胸

对于业界成熟的架构模式, 设计思想:
1. 你是首先找到了自己真正面对的问题, 所拥有的资源 (技术, 人员), 要达到的合理的目标
2. 还是逃避现实, 跳过上一步, 想通过所谓的 "X 模式在 Y 公司的实践" 来一蹴而就

借鉴和模仿是有云泥之别的
```

> No one thinks that code quality matters until
  it's 4 a.m. on a Saturday, you're 18 hours into
  debugging a failure, and you still
  haven't fixed the bug.

```
近年来, 经历了一些让人啼笑皆非的判断代码质量的标准, 比如:
1. 只看 Unit Test 覆盖率
2. 用什么编程语言写的
3. 有没有名义上遵循某个架构模式, 比如: DDD

代码或者项目质量其实是一个难以准确衡量的东西, 但截至 2022 年,
我们至少可以肯定:
1. 人的判断比机器更准确
2. 最有愿望提升项目质量的人一定是那个一直在开发这个项目的人

所以, 尊重人是最重要的! 而不是防备人! (你也防不住!)

程序员修炼之道 (第2版) 对此也有一些讨论
```

> If you can't justify the benefits of your project
  being in production, don't expect it to
  remain there for very long.

```
The worst reason for getting an ML project
cancelled or abandoned is budget.
```

- [MLflow](https://github.com/mlflow/mlflow)
  - 现在在用的是 [Kubeflow](https://github.com/kubeflow/kubeflow)
  - 未来更看好 [Ray](https://github.com/ray-project/ray)

- Artifact management
- Feature stores
- Prediction serving architecture
