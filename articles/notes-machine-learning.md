---
title: Machine learning is fun
description: We can do something
date: 2019-06-30
---

马尔可夫假设 -> 贝叶斯网络
贝叶斯网络 vs 条件随机场
期望最大化算法
最大熵模型
最小二乘法
在线学习
EM算法

## linear-regression

### gradient descent algorithm

```
1. scale the features, for example: [-1, 1]
2. mean normalization
```

```
debugging: by plotting the cost function

if your learning rate alpha is small enough,
then J(theta) should decrease on every iteration

learning rate is too small -> slow convergence

learning rate is too large, J(theta) may not decrease
on every iteration and it may not even converge
```

```
how to choose features:

1. maybe generate new features
2. polynomial regression
```

### normal equation

* advantages
  - no need to iterate

* disadvantages
  - slow if features number is very large

### Large Scale Machine Learning

* Stochastic Gradient Descent
* Mini-Batch Gradient Descent
* Ceiling Analysis
* Online Learning

## logistic regression (classification problems)

* [Logistic regression](https://en.wikipedia.org/wiki/Logistic_regression)
* [Logistic function](https://en.wikipedia.org/wiki/Logistic_function)
* [Activation function](https://en.wikipedia.org/wiki/Activation_function)
* [Sigmoid function](https://en.wikipedia.org/wiki/Sigmoid_function)
