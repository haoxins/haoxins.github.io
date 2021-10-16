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

* **TLS 1.3** optimizes this flow by attempting
  to do *both* the *negotiation* and the
  *key exchange* at the same time: the client
  speculatively chooses a key exchange algorithm
  and sends a public key in the first message
  (the `ClientHello`). If the client fails to
  predict the server's choice of key exchange
  algorithm, then the client falls back to the
  outcome of the negotiation and sends a new
  `ClientHello` containing the correct public key.

* In TLS 1.3, each session starts with an
  **ephemeral key exchange**. If a server is
  compromised at some point in time, no
  previous sessions will be impacted.
* TLS 1.3 derives different keys at
  different points in time to encrypt
  different phases with independent keys.
* To derive the different keys, TLS 1.3 uses
  HKDF with the hash function negotiated.
  - HKDF-Extract is used on the output of the
    key exchange to remove any biases,
  - while HKDF-Expand is used with different
    info parameters to derive
    the encryption keys.

* A TLS **1.3** handshake is actually split
  into three different stages
  - **Key exchange** This phase contains the
    `ClientHello` and `ServerHello` messages
    that provide some negotiation and perform
    the key exchange. All messages including
    handshake messages *after* this phase
    are *encrypted*.
  - **Server parameters** Messages in this phase
    contain additional negotiation data from
    the server. This is negotiation data that
    does not have to be contained in the first
    message of the server and that could
    benefit from being encrypted.
  - **Authentication** This phase includes
    authentication information from both
    the server and the client.

* Client authentication is often delegated to
  the application layer for the web, most
  often via a form asking you for your
  credentials. That being said, client
  authentication can also happen in TLS if
  requested by the server during the
  *server parameters* phase. When both sides
  of the connection are authenticated, we talk
  about mutually-authenticated TLS
  (sometimes abbreviated as **mTLS**).
* Client authentication is done the same way
  as server authentication. This can happen at
  any point after the authentication
  of the server (for example, during the
  handshake or in the post-handshake phase).

## End-to-end encryption

## User authentication

## Crypto as in cryptocurrency?

## Hardware cryptography

## Post-quantum cryptography

## Next-generation cryptography

## When and where cryptography fails
