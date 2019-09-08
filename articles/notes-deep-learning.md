---
title: Deep Learning is fun
description: We can do something
date: 2019-09-08
---

### Structuring Deep Learning Projects

* Orthogonalization
  - Happy cost function
  - Performs well in real world
* Single number evaluation metric
  - Combine metrics
* Satisficing and Optimizing metric
  - Optimizing metric: want to do as well as possible
  - Satisficing metrics: you'll be satisfice
* Train/dev/test distributions
  - Dev Test sets really come from the same distribution
  - Choose dev/test sets reflect data you expect to get in future
  - Set your test set to big enough to give high confidence in the overall performance of your system
* When to change dev/test sets and metrics
* Comparing to human-level performance
  - Whether bias avoidance tactics or variance avoidance tactics
  - Human-level error (Bias -> 0%) Training error (Variance) Dev error
* Reducing bias
  - bigger model
  - longer/better optimization algorithm
* Reducing variance
  - more data
  - regularization
* Error analysis
  - find a set of mislabeled examples
  - look at the mislabeled examples for false positives and false negatives
  - count up the number of errors that fall into various different categories

### Sequence models

* RNN
* LSTM
