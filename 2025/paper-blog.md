---
title: 阅读 Paper & Blog
description: 欲渡黄河冰塞川, 将登太行雪满山. 闲来垂钓碧溪上, 忽复乘舟梦日边.
date: 2024-01-28
---

### Device-Independent-Quantum-Randomness-Enhanced Zero-Knowledge Proof

- [Device-Independent-Quantum-Randomness-Enhanced Zero-Knowledge Proof](https://arxiv.org/abs/2111.06717)
  - Submitted on 12 Nov 2021


### Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer

- [Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer](https://arxiv.org/abs/quant-ph/9508027)

### Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention
### DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

### DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

- [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300)

```
we notice that starting from a code training model
is a better choice compared to a general LLM.

Furthermore, we observe the math training also
improves model capability, indicating it does
not only enhance the model's mathematical abilities
but also amplify general reasoning capabilities.
```

```
Although training on arXiv papers is common, especially in
many math-related papers, it brings no notable improvements
on all mathematical benchmarks adopted in this paper.
```

#### Math Pre-Training

```
To filter out low-quality mathematical content,
we rank the collected pages according to their
scores predicted by the fastText model,
and only preserve the top-ranking ones.
```

> Mathematical Problem Solving with Tool Use
  这段写得很简陋~

#### Supervised Fine-Tuning

```
The total number of training examples is 776K.

Training examples are randomly concatenated until
reaching a maximum context length of 4K tokens.
```

#### Reinforcement Learning

> 正文开始~

```
As the value function employed in PPO is typically
another model of comparable size to the policy model,
it brings a substantial memory and computational burden.
Additionally, during RL training, the value function is
treated as a baseline in the calculation of the advantage
for variance reduction. While in the LLM context,
usually only the last token is assigned a reward score
by the reward model, which may complicate the training
of a value function that is accurate at each token.
```

#### Discussion, Conclusion, and Limitation
