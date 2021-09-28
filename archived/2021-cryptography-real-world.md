---
title: Real-World Cryptography
description: 白露横江, 水光接天. 纵一苇之所如, 凌万顷之茫然.
date: 2021-09-10
---

* [Real-World Cryptography](https://book.douban.com/subject/34615742/)
  - https://www.manning.com/books/real-world-cryptography

## Introduction

> The slightest mistake could be deadly.

* While a typical cryptography book usually
  starts with the discovery of cryptography
  and takes you through its history, I think
  that it makes little sense for me to
  kick off things that way. I want to
  *tell you about the practical*.

* **Kerckhoff's principle**:
  - *Only the key is kept secret*

* **Asymmetric cryptography**:
  - *Two keys are better than one*
  - *key exchange*: Diffie-Hellman (**DH**)
  - DH: `man-in-the-middle`

* **RSA** contains two different primitives:
  - a public key encryption algorithm
    (or asymmetric encryption)
  - and a (digital) signature scheme.

* Three different asymmetric primitives:
  - Key exchange with Diffie-Hellman
  - Asymmetric encryption
  - Digital signatures with RSA

* Another way of dividing cryptography can be
  - *Math-based constructions*
  - These rely on mathematical problems like
    factoring numbers.
  - *Heuristic-based constructions*
  - These rely on observations and statistical
    analysis by cryptanalysts.
  - AES for symmetric encryption is an
    example of such a construction.
* *Symmetric* constructions are most often
  based on *heuristics*, while most *asymmetric*
  constructions are based on *mathematical* problems.

* **Confidentiality**
  - It's about masking and protecting some
    information from the wrong eyes.
  - For example, encryption masks
    the messages in transit.
* **Authentication**
  - It's about identifying who we are talking to.
  - For example, this can be helpful in making
    sure that messages we receive
    indeed come from Alice.

## Hash functions

* *second pre-image resistance*

> There are other ways to encode binary data
  for human consumption, but the two most
  widely used encodings are
  **hexadecimal** and **base64**.

## Message authentication codes

## Authenticated encryption

## Key exchanges

## Asymmetric encryption and hybrid encryption

## Signatures and zero-knowledge proofs

## Randomness and secrets

## Secure transport

## End-to-end encryption

## User authentication

## Crypto as in cryptocurrency?

## Hardware cryptography

## Post-quantum cryptography

## Is this it? Next-generation cryptography

## When and where cryptography fails
