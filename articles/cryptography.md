---
title: Cryptography
description: 月出于东山之上, 徘徊于斗牛之间. 白露横江, 水光接天. 纵一苇之所如, 凌万顷之茫然.
date: 2021-03-22
---

* 完整性 Integrity
* 机密性 Confidentiality
* 可用性 Availability

### Cryptanalysis

* The ciphertext-only attack
  - The baseline attack when designing cryptosystem
* The known-plaintext attack
* The chosen-plaintext attack
  - The difference from the known-plaintext attack is that
  - the attackers are the ones choosing the plaintext

```
Perfect Secrecy == One-Time Pad
  - Claude Shannon
```

* Computational security relies on two assumptions
  - First, the attackers are computationally limited
  - Second, the cryptosystem relies on mathematical problems
  - that are assumed to be difficult to solve

* Side-Channel Attack

### Symmetric

### DH（Diffie-Hellman Key Exchange Algorithm）

------------------

# Timeline

------------------

## 2021

* [A Mathematical Theory of Communication (1948)](https://en.wikipedia.org/wiki/A_Mathematical_Theory_of_Communication)

* [BLS Signatures v4](https://tools.ietf.org/html/draft-irtf-cfrg-bls-signature-04)
  - Dan Boneh, 第一作者, 就是 Coursera 上 Cryptography 的授课老师
  - https://github.com/w3f/bls

* [Things that use Ed25519](https://ianix.com/pub/ed25519-deployment.html)
