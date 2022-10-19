---
title: Cryptography
description: 月出于东山之上, 徘徊于斗牛之间.
date: 2021-03-22
---

* 完整性 Integrity
* 机密性 Confidentiality
* 可用性 Availability

### DH (Diffie-Hellman Key Exchange Algorithm)

* El Gamal

### Hash and Integrity

* Message Authentication Code (MAC)
* Digital Signature

### Asymmetric

* **ECC**, RSA

### Symmetric

* Block Cipher vs Stream Cipher
  - like: batch vs streaming

* Block
  - Electronic Codebook (ECB)
  - Cipher Block Chaining (CBC)
  - Cipher Feedback (CFB)
  - Output Feedback (OFB)
  - Counter (CTR) (IPSec and others)

### Cryptanalysis

* The ciphertext-only attack
  - The baseline attack when designing cryptosystem
* The known-plaintext attack
* The chosen-plaintext attack
  - The difference from the known-plaintext attack is that
    the attackers are the ones choosing the plaintext

```
Perfect Secrecy == One-Time Pad
  - Claude Shannon
```

* Computational security relies on two assumptions
  - First, the attackers are computationally limited
  - Second, the cryptosystem relies on mathematical problems
    that are assumed to be difficult to solve

* Side-Channel Attack

------------------

# Events

------------------

## 2021

* [Google - Fully Homomorphic Encryption (FHE)](https://github.com/google/fully-homomorphic-encryption)

```
About Fully Homomorphic Encryption

Fully Homomorphic Encryption (FHE) is an emerging data processing paradigm
that allows developers to perform transformations on encrypted data.
FHE can change the way computations are performed by preserving privacy end-to-end,
thereby giving users even greater confidence that their information
will remain private and secure.
```

* `SHA-1` to `SHA-2`

> 微软宣布, 从2021年5月9日起, 该公司旗下的所有主要流程与服务, 都将全面转向仅使用 SHA-2 算法.

* [A Mathematical Theory of Communication (1948)](https://en.wikipedia.org/wiki/A_Mathematical_Theory_of_Communication)

* [BLS Signatures v4](https://tools.ietf.org/html/draft-irtf-cfrg-bls-signature-04)
  - Dan Boneh, 第一作者, 就是 Coursera 上 Cryptography 的授课老师
  - https://github.com/w3f/bls

* [Things that use Ed25519](https://ianix.com/pub/ed25519-deployment.html)
