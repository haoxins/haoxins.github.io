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

* Security properties of a hash function
  - The **first** one is *pre-image resistance*.
  - No one should be able to reverse the
    hash function in order to recover
    the input given an output.
  - But you can't hide something that is
    too small or that is predictable.
  - The **second** property is
    *second pre-image resistance*.
  - You should not be able to find a different
    input that hashes to the same digest.
  - The **third** property is *collision resistance*.
  - No one should be able to produce two different
    inputs that hash to the same output.

> in **practice** *impossible*
  but not **theoretically** *impossible*.

* There is a `minimum` output size that a hash
  function must produce in practice:
  `256 bits` (or `32 bytes`).
* For a hash function to provide all three
  security properties mentioned earlier, it needs
  to provide at least `128 bits` of security
  against all three attacks.
* If our hash function generates random outputs
  of 256 bits, the space of all outputs
  is of size $$ 2^256 $$.
* This means that collisions can be found with
  good probability after generating $$ 2^128 $$
  digests (due to the *birthday bound*).
* In order to achieve `128-bit` security at a minimum,
  a digest must not be truncated under:
  - `256 bits` for *collision resistance*
  - `128 bits` for *pre-image* and
    *second pre-image resistance*

> `CRC32` are not *cryptographic hash functions*
  but *error-detecting code functions*.

* `MD5` and `SHA-1` were shown to be broken
  in `2004` and `2016`.
* `SHA-2` is based on the `Merkle-Damgard` construction,
  while `SHA-3` is based on the `sponge` construction.
* `SHA-2` provides 4 different versions, producing
  outputs of `224`, `256`, `384`, or `512` bits.

* While there are different ways of building
  a **compression function**, `SHA-2` uses the
  `Davies-Meyer` method, which relies on a
  *block cipher*.
* The `Merkle-Damgard` construction iteratively
  applies a compression function to each block
  of the input to be hashed and the output of
  the previous compression function.
  The *final* call to the compression function
  directly returns the *digest*.

* While `SHA-2` is a perfectly fine hash function
  to use, it is *not suitable* for **hashing secrets**.
* This is because of a downside of the `Merkle-Damgard`
  construction, which makes `SHA-2` vulnerable to
  an attack (called a `length-extension attack`)
  if used to **hash secrets**.
* Because of this, and the fact that SHA-2 is vulnerable
  to *length-extension attacks*, NIST decided in 2007 to
  organize an open competition for a new standard: `SHA-3`.
* `SHA-3` is a cryptographic algorithm
  built on top of a *permutation*.

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
