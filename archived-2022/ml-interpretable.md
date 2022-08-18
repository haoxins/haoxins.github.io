---
title: Interpretable & 特征工程的艺术 & Engineering
description: 雁来音信无凭, 路遥归梦难成. 离恨恰如春草, 更行更远还生.
date: 2021-09-20
---

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
就是偏差 (bias: 学习了错误的事情; 由于模型局限性而产生的误差)
与方差 (variance: 学习了分散的点; 由于有限的数据抽样以及不同样本生成的不同模型而产生的误差)
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
  特别地, 从对核函数的傅里叶分解中随机选择正弦波是对该函数一个有效,
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

