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

* The **handshake** is, at its *core*, simply a
  *key exchange*. The handshake ends up with the
  two participants agreeing on
  a set of *symmetric keys*.
* The **post-handshake** phase is purely about
  encrypting messages between participants.
  This phase uses an *authenticated encryption*
  algorithm and the set of keys produced
  at the end of the *handshake*.

* The handshake itself has four aspects:
  - **Negotiation** TLS is highly configurable.
    Both a client and a server can be configured to
    negotiate a range of TLS versions as well as
    a menu of acceptable cryptographic algorithms.
    The negotiation phase of the handshake aims at
    finding common ground between the client's and
    the server's configurations in order to
    securely connect the two peers.
  - **Key exchange** The whole point of the handshake
    is to perform a key exchange between two
    participants. Which key exchange algorithm to use?
    This is one of the things decided as part of the
    `client/server` negotiation process.
  - **Authentication** As you learned on key exchanges,
    it is trivial for **MITM** attackers to impersonate
    any side of a key exchange. Due to this, key exchanges
    must be authenticated. Your browser must have a way
    to ensure that it is talking to `google.com`,
    for example, and not your internet service provider
    (ISP).
  - **Session resumption** As browsers often connect
    to the same websites again and again, key exchanges
    can be costly and can slow down a user's experience.
    For this reason, mechanisms to fast-track secure
    sessions without redoing a key exchange
    are integrated into TLS.

> - In *March 2021*, the IETF published *RFC 8996*:
    **Deprecating TLS 1.0 and TLS 1.1**, effectively
    making the deprecation official.

* The `ClientHello` contains a range of
  supported SSL and TLS versions, a suite of
  cryptographic algorithms that the client is
  willing to use, and some more information that
  could be relevant for the rest of the
  handshake or for the application. The suite of
  cryptographic algorithms include
  - One or more key exchange algorithms (RFC 7919)
  - Two (for different parts of the handshake)
    or more digital signature algorithms
  - One or more hash functions to be used
    with HMAC and HKDF
  - One or more authenticated encryption algorithms
* The server then responds with a `ServerHello`
  message, which contains one of each type of
  cryptographic algorithm, cherry-picked from the
  client's selection.

## End-to-end encryption

## User authentication

## Crypto as in cryptocurrency?

## Hardware cryptography

## Post-quantum cryptography

## Next-generation cryptography

## When and where cryptography fails
