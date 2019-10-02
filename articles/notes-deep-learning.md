---
title: Deep Learning is fun
description: We can do something
date: 2019-09-08
---

## ?

[CS231n: Convolutional Neural Networks for Visual Recognition](https://github.com/cs231n/cs231n.github.io)

[Understanding Neural Networks. From neuron to RNN, CNN, and Deep Learning](https://towardsdatascience.com/understanding-neural-networks-from-neuron-to-rnn-cnn-and-deep-learning-cd88e90e0a90)

## Structuring Deep Learning Projects

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

## Train, Dev, Test sets

## Bias, Variance

## Convolutional Neural Networks (CNN)

* Example: edge detection
* Filter: choose vs learn
* Input (n*n), Filter (f*f), Output ((n-f+1)*(n-f+1))
* Padding input, make output size = input size
* Strided Convolutions:
  - Input (n*n)
  - Filter (f*f)
  - Padding (p)
  - Stride s
  - Output (((n+2p-f)/s+1)*((n+2p-f)/s+1))
* Convolutions Over Volume
* Pooling Layers
  - Max pooling
* Convolutional Implementation of Sliding Windows
* Transfer Learning
  - Download open source ways and use that as initialization for your problem
  - Add your own stuff
* One-shot Learning
  - similarity function
* Siamese Network
* Triplet Loss

* Why Convolutions
  - parameter sharing
  - sparsity of connections
* R-CNN: Regions with convolutional networks or regions with CNNs
  - region proposals by segmentation algorithm

* DNN

## Recurrent Neural Networks (RNN)

* LSTM

https://en.wikipedia.org/wiki/Backpropagation
