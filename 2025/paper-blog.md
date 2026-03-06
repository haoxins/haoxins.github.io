---
title: 阅读 Paper & Blog
description: 欲渡黄河冰塞川, 将登太行雪满山. 闲来垂钓碧溪上, 忽复乘舟梦日边.
date: 2024-01-28
---

### Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention

- [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://arxiv.org/abs/2502.11089)

```
Our approach advances sparse attention
design with two key innovations:
(1) We achieve substantial speedups through
arithmetic intensity-balanced algorithm design,
with implementation optimizations for modern hardware.
(2) We enable end-to-end training, reducing pretraining
computation without sacrificing model performance.
```

```
A natural approach to efficient long-context modeling
is to take advantage of the inherent sparsity of
softmax attention, where selectively computing
critical query-key pairs can significantly reduce
computational overhead while preserving performance.

Recent advances demonstrate this potential
through diverse strategies:
KV-cache eviction methods,
blockwise KV-cache selection methods,
and sampling, clustering or
hashing-based selection methods.
```

```
To achieve more effective and efficient sparse attention,
we present NSA, a Natively trainable Sparse Attention
architecture that integrates hierarchical token modeling.

NSA reduces per-query computation by organizing
keys and values into temporal blocks and processing them
through three attention paths:
compressed coarse-grained tokens,
selectively retained fine-grained tokens, and
sliding windows for local contextual information.
```

```
NSA introduces two core innovations corresponding
to the key requirements above:
(1) Hardware-aligned system:
Optimize blockwise sparse attention for
Tensor Core utilization and memory access,
ensuring balanced arithmetic intensity.
(2) Training-aware design:
Enable stable end-to-end training through
efficient algorithms and backward operators.
```

> 1. compressed, 2. selected, 3. aligned

### DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)

```
Here we show that the reasoning abilities of LLMs can be
incentivized through pure reinforcement learning (RL),
obviating the need for human-labeled reasoning trajectories.
```

```
In parallel, a complementary line of research has
demonstrated that large language models can be effectively
augmented through chain-of-thought (CoT) prompting.
This technique, which involves either providing carefully
designed few-shot examples or using minimalistic prompts
such as "Let's think step by step", enables models to
produce intermediate reasoning steps, thereby substantially
enhancing their performance on complex tasks.
```

```
Specifically, we build upon DeepSeek-V3-Base (DeepSeek-AI)
and employ Group Relative Policy Optimization (GRPO)
as our RL framework. The reward signal is solely based
on the correctness of final predictions against
ground-truth answers, without imposing constraints on
the reasoning process itself.
Notably, we bypass the conventional supervised fine-tuning
(SFT) phase before RL training. This design choice stems
from our hypothesis that human-defined reasoning patterns
may limit model exploration, whereas unrestricted
RL training can better incentivize the emergence
of novel reasoning capabilities in LLMs.
```

#### DeepSeek-R1-Zero

```
Template for DeepSeek-R1-Zero.
prompt will be replaced with the specific
reasoning question during training.

A conversation between User and Assistant.
The user asks a question, and the Assistant solves it.
The assistant first thinks about the reasoning process
in the mind and then provides the user with the answer.
The reasoning process and answer are enclosed within
<think> ... </think> and <answer> ... </answer> tags,
respectively, i.e.,
<think> reasoning process here </think>
<answer> answer here </answer>.
User: prompt.
Assistant:
```

```
For DeepSeek-R1-Zero: our rule-based reward system
mainly consists of two types of rewards:
accuracy rewards and format rewards.
```

```
In the initial stage, we collect thousands of
cold-start data that exhibits a conversational,
human-aligned thinking process.
RL training is then applied to improve the model
performance with the conversational thinking
process and language consistency.
```

```
Even if DeepSeek-R1 achieves frontier results on
reasoning benchmarks, it still faces several
capability limitations, as outlined below:
1. Structure Output and Tool Use;
2. Token efficiency;
3. Language Mixing;
4. Prompting Engineering;
5. Software Engineering Tasks.

Beyond specific capability limitations,
the pure RL methodology itself also
presents inherent challenges:
1. Reward Hacking.

In this work, for tasks that cannot obtain a reliable signal,
DeepSeek-R1 uses human annotation to create supervised data,
and only conduct RL for hundreds of steps.
We hope in the future, a robust reward model
can be obtained to address such issues.
```

```
With the advent of pure RL methods like DeepSeek-R1,
the future holds immense potential for solving any task
that can be effectively evaluated by a verifier,
regardless of its complexity for humans.
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
