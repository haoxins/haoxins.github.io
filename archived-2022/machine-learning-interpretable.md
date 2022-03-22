---
title: Interpretable Machine Learning
description: 维摩一室虽多病, 亦要天花作道场
date: 2021-09-20
---

* [Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/)
  - A Guide for Making Black Box Models Explainable.

## Interpretability

* **Feature summary statistic**: Many interpretation methods
  provide summary statistics for each feature. Some methods
  return a single number per feature, such as feature importance,
  or a more complex result, such as the pairwise
  feature interaction strengths, which consist of
  a number for each feature pair.
* **Feature summary visualization**: Most of the feature
  summary statistics can also be visualized. Some feature
  summaries are actually only meaningful if they are
  visualized and a table would be a wrong choice.
  - The partial dependence of a feature is such a case.
    **Partial dependence** plots are curves that show a
    feature and the average predicted outcome.
* **Model internals** (e.g. learned weights): The
  interpretation of intrinsically interpretable models
  falls into this category. Examples are the weights in
  linear models or the learned tree structure
  (the features and thresholds used for the splits)
  of decision trees.
* **Data point**: This category includes all methods that
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
* **Intrinsically interpretable model**: One solution to
  interpreting black box models is to approximate them
  (either globally or locally) with an interpretable model.
  The interpretable model itself is interpreted by
  looking at internal model parameters or
  feature summary statistics.

### Algorithm Transparency

* Algorithm transparency is about how the algorithm
  learns a model from the data and what kind
  of relationships it can learn.
* Algorithm transparency only requires knowledge of
  the algorithm and not of the data or learned model.
  - This book focuses on model interpretability and
    not algorithm transparency.

### Model Interpretability

* This level of interpretability is about understanding
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

* While **global** model interpretability is usually out of reach,
  there is a good chance of understanding at least
  some models on a modular level.
  - Not all models are interpretable at a parameter level.
* If you look at an individual prediction, the behavior of
  the otherwise complex model might behave more pleasantly.
  **Locally**, the prediction might only depend linearly
  or monotonically on some features, rather than having
  a complex dependence on them.
  - Local explanations can therefore be more accurate
    than global explanations.
* Model predictions for multiple instances can be explained
  either with global model interpretation methods
  (on a modular level) or with
  explanations of individual instances.

