---
title: Paper & Blog - 信息, 量子
description: 欲渡黄河冰塞川, 将登太行雪满山. 闲来垂钓碧溪上, 忽复乘舟梦日边.
date: 2024-01-28
---

- [Device-Independent-Quantum-Randomness-Enhanced Zero-Knowledge Proof](https://arxiv.org/abs/2111.06717)
  - Submitted on 12 Nov 2021

```

```

---

- [A High-Level Technical Overview of Fully Homomorphic Encryption](https://www.jeremykun.com/2024/05/04/fhe-overview/)
  - [Learning with errors](https://en.wikipedia.org/wiki/Learning_with_errors)
  - [Ring learning with errors](https://en.wikipedia.org/wiki/Ring_learning_with_errors)

```
Adding ciphertexts gives you an encryption of
the sum of the underlying plaintexts.
Multiplying two ciphertexts gives you encryption of
the product of the underlying plaintexts.
```

```
If you did a naive circuit decomposition without anything else,
running FHE on the CPU is at least a million times slower
than the corresponding unencrypted program.
```

```
The special keys need only be generated and sent once
and can be used for all future computations,
but they can easily be gigabytes in size.
In one example FHE scheme with lightweight keys,
a ciphertext encrypting a single integer is on the order of 25 KB,
and the special keys are about 0.5 GB.
In others, 16,000 or more integers are packed into
a single ciphertext of similar size,
but the keys can be 10s of GiBs.
```

```
All modern FHE schemes encrypt their data using
effectively the same cryptographic foundation:
a noisy dot product.
```

```
A question that puzzled me when I first studied LWE is
why we can't simply ignore the least significant bits
of a ciphertext to "bypass" the noise.
The reason is that the noise can be negative.
Adding negative noise changes the higher order bits of
an integer by the arithmetic "wrapping around."
It "tampers" with the highest order bits,
but still allows you to remove it by
rounding up in the decryption process.
I enshrined this mistake in my first broken LWE
implementation by masking and shifting
during decryption instead of rounding.
```

```
The cryptographic guarantee is that, given a large sample
of encryptions of a message with the same secret key,
one cannot learn the secret key or the underlying message
with any nontrivial probability above random guessing.
```

```
The main advantage to using RLWE over LWE is that you can
pack many messages into a single polynomial,
and the homomorphic operations you do apply to all the messages.
It's the same sort of advantage as SIMD,
but there are more restrictions on what SIMD operations
are available on these packed messages
that I'll discuss in later sections.
```

```
So nearly all of the complexity in FHE is based around how
to avoid noise growth or how to reduce noise mid-program.
The latter is called bootstrapping, which deserves some
special attention. The idea of bootstrapping is trippy.
Its technical details are beyond the scope of this article,
but I can summarize the main idea:
you can homomorphically decrypt an FHE ciphertext and
re-encrypt it under a new secret key without ever seeing
the underlying message. In doing so, the noise of the
resulting ciphertext is "reset" to a smaller value.
But to make it work, the user has to provide the server
with a special encryption of the user's secret key, which
adds an extra security assumption called circular security,
or key-dependent message security. With bootstrapping,
you can extend an FHE program indefinitely.
The downside is that bootstrapping can be expensive,
taking milliseconds in some schemes and
seconds to minutes in others.
```

```
If you don't want to do bootstrapping, then you are
left with putting a hard limit on noise growth.
This is often called leveled homomorphic encryption
because the noise growth is discretized into levels,
and programs are prohibited from exceeding the max level.
These two techniques roughly split the FHE community in half.
```

> These two techniques roughly split the FHE community in half.

> 嗯, 确实蛮 High-Level 的~ (No details)
