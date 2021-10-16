---
title: Real-World Cryptography (下)
description: 余音袅袅, 不绝如缕. 舞幽壑之潜蛟, 泣孤舟之嫠妇.
date: 2021-10-15
---

* [Real-World Cryptography](https://book.douban.com/subject/34615742/)
  - https://www.manning.com/books/real-world-cryptography

## Secure transport

* *Transport Layer Security* (**TLS**)
  - The most recent version of **TLS** is **TLS 1.3**,
    specified in **RFC 8446** and published in `2018`.

* TLS is split into two phases.
  - *A handshake phase* A secure communication
    is negotiated and created between
    two participants.
  - *A post-handshake phase* Communications are
    encrypted between the two participants.

* The **handshake** is, at its core, simply a
  key exchange. The handshake ends up with the
  two participants agreeing on
  a set of symmetric keys.
* The **post-handshake** phase is purely about
  encrypting messages between participants.
  This phase uses an authenticated encryption
  algorithm and the set of keys produced
  at the end of the handshake.

## End-to-end encryption

## User authentication

## Crypto as in cryptocurrency?

## Hardware cryptography

## Post-quantum cryptography

## Next-generation cryptography

## When and where cryptography fails
