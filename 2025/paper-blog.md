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

- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)

```
Our goal is to explore the potential of LLMs
to develop reasoning capabilities without any
supervised data, focusing on their self-evolution
through a pure RL process.
Specifically, we use DeepSeek-V3-Base as the
base model and employ GRPO as the RL framework to
improve model performance in reasoning.
```

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

```
As the reinforcement learning training process progresses,
the old reward model may not be sufficient to supervise the
current policy model. Therefore, we also explore the iterative
RL with GRPO. In iterative GRPO, we generate new training sets
for the reward model based on the sampling results from the
policy model and continually train the old reward model using
a replay mechanism that incorporates 10% of historical data.
Then, we set the reference model as the policy model,
and continually train the policy model with the new reward model.
```

#### Discussion, Conclusion, and Limitation

```
A popular yet unverified hypothesis suggests that code
training improves reasoning. We attempt to offer a partial
response to this, particularly within the mathematical domain:
code training improves models' ability to do mathematical
reasoning both with and without tool use.
```

```
Code training also improves mathematical reasoning without
tool use. Under the two-stage training setting, the initial
stage of code training already results in moderate enhancements.
It also boosts the efficiency of the subsequent math training,
eventually leading to the best performance.

However, combining code tokens and math tokens for one-stage
training compromises mathematical reasoning without tool use.
One conjecture is that DeepSeek-LLM 1.3B, due to its
limited scale, lacks the capacity to fully assimilate both
code and mathematical data simultaneously.
```

```
Perhaps counter-intuitively, according to our experiments,
arXiv papers seem ineffective in improving mathematical
reasoning. When trained on a arXiv-only corpus, both
models display no notable improvements or even
deterioration across various mathematical benchmarks
of different complexities employed in this study.
```

```
These findings indicate that RL enhances the model's
overall performance by rendering the output
distribution more robust, in other words,
it seems that the improvement is attributed to
boosting the correct response from TopK rather than
the enhancement of fundamental capabilities.
```

> the improvement is attributed to boosting the
  __correct response from TopK__ rather than the
  enhancement of fundamental capabilities.
