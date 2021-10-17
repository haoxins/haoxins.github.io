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

* There are two sides to the web PKI.
  - First, browsers must trust a set of
    root public keys that we call
    *certificate authorities* (**CAs**).
    Usually, browsers will either use a
    hardcoded set of trusted public keys
    or will rely on the operating system
    to provide them.
  - Second, websites that want to use HTTPS
    must have a way to obtain a certification
    (a signature of their signing public key)
    from these CAs. In order to do this,
    a website owner must prove to a CA
    that they own a specific domain.

* More specifically, CAs do not actually
  sign public keys, but instead they sign
  **certificates** (more on this later).
* A **certificate** *contains* the
  *long-term public key*, along with some
  *additional important metadata* like
  the web page's domain name.

* The signature in the `CertificateVerify`
  message proves to the client what the
  server has so far seen. Without this
  signature, a MITM attacker could intercept
  the server's handshake messages and
  replace the ephemeral public key of the
  server contained in the ServerHello message,
  allowing the attacker to successfully
  impersonate the server.
* The authentication part of a handshake
  starts with the server sending a
  certificate chain to the client.
  The certificate chain starts with the
  leaf certificate (the certificate
  containing the website's public key
  and additional metadata like
  the domain name) and ends with a root
  certificate that is trusted by the browser.
  Each certificate contains a signature
  from the certificate above it in the chain.

* Finally, in order to officially end the
  handshake, both sides of the connection must
  send a `Finished` message as part of the
  authentication phase.
* A Finished message contains an authentication
  tag produced by HMAC, instantiated with the
  negotiated hash function for the session.
  This allows both the client and the server
  to tell the other side,
  "These are all the messages I have sent
  and received in order during this handshake."
  If the handshake is intercepted and tampered
  with by MITM attackers, this integrity check
  allows the participants to detect and
  abort the connection.

* While certificates are optional in TLS 1.3
  (you can always use plain keys),
  many applications and protocols,
  not just the web, make heavy use of them
  in order to certify additional metadata.
  Specifically, the `X.509` certificate
  standard **version 3** is used.
* The `X.509` standard uses a description
  language called **Abstract Syntax Notation One**
  to specify information contained in a certificate.
  A data structure described in **ASN.1**
  looks like this:

```
Certificate  ::=  SEQUENCE  {
    tbsCertificate      TBSCertificate,
    signatureAlgorithm  AlgorithmIdentifier,
    signatureValue      BIT STRING  }
```

* `tbsCertificate`: The to-be-signed certificate.
* `signatureAlgorithm`: The algorithm used to
  sign the certificate.
* `signatureValue`: The signature from a CA.

* **DER** is a deterministic (only one way to encode)
  binary encoding used to translate `X.509`
  certificates into bytes.
* **DER** only encodes information as
  "here is an integer" or "this is a bytearray."
  Field names described in `ASN.1`
  (like `tbsCertificate`) are lost after encoding.
* Decoding **DER** without the knowledge of the
  original `ASN.1` description of what each
  field truly means is thus pointless.
* **DER** encoding is a *difficult* protocol
  *to parse correctly*, and the complexity of
  `X.509` certificates makes for many mistakes
  to be potentially devastating. For this reason,
  I **don't recommend** any modern application
  **to use** `X.509` certificates unless it has to.

* In `TLS 1.3`, a **PSK** handshake works by having
  the client advertise in its `ClientHello` message
  that it supports a list of **PSK** identifiers.
  If the server recognizes one of the **PSK** IDs,
  it can say so in its response
  (the `ServerHello` message), and both can then
  avoid doing a key exchange (if they want to).
  By doing this, the *authentication phase* is
  *skipped*, making the `Finished` message at
  the end of the handshake important
  to prevent **MITM** attacks.

* Both the `ClientHello` and `ServerHello`
  messages have a random field, which is
  randomly generated for every new session
  (and often referred to as client
  random and server random).

* Another use case for **PSKs** is session
  resumption. Session resumption is about
  reusing secrets created from a
  previous session or connection.
* TLS 1.3 offers a way to generate a PSK
  after a handshake is successfully
  performed, which can be used in subsequent
  connections to avoid having to
  redo a full handshake.
* If the server wants to offer this feature,
  it can send a *New Session Ticket* message
  at any time during the *post-handshake* phase.

* Starting with TLS 1.3, if a server decides
  to allow it, clients have the possibility
  to send encrypted data as part of their
  first series of messages, right after the
  `ClientHello` message. This means that
  browsers do not necessarily have to wait
  until the end of the handshake to start
  sending application data to the server.
  This mechanism is called *early data* or
  **0-RTT** (for *zero round trip time*).
  It can only be used with the combination
  of a PSK as it allows derivation of
  symmetric keys during the `ClientHello` message.
* This feature was quite controversial during
  the development of the TLS 1.3 standard
  because a passive attacker can replay an
  observed `ClientHello` followed by the
  encrypted 0-RTT data. This is why 0-RTT
  must be used only with application data
  that can be replayed safely.

* *Certificate revocation* As the name
  indicates, this allows a CA to revoke
  a certificate and warn browsers about it.
* *Certificate monitoring* This is a
  relatively new system that forces CAs
  to publicly log every certificate signed.

* **Secure Shell (SSH)**
* **Wi-Fi Protected Access (WPA)**
* **IPSec**: One of the most popular
  virtual network protocols (**VPNs**) used
  to connect different private networks together.
  It is mostly used by companies to link
  different office networks. As its name
  indicates, it acts at the IP layer and
  is often found in routers, firewalls,
  and other network appliances. Another
  popular VPN is OpenVPN, which
  makes direct use of TLS.

* **the Noise protocol framework**.
  - **Noise** is a much more modern
    *alternative* to *TLS*.

* The **Noise protocol framework** removes
  the run-time complexity of TLS by avoiding
  all negotiation in the handshake. A client
  and a server running Noise follow a
  linear protocol that does not branch.
* Contrast this to TLS, which can take many
  different paths, depending on the information
  contained in the different handshake messages.
* What Noise does is that it pushes all the
  complexity to the design phase.

* The Noise protocol framework offers different
  *handshake patterns* that you can choose from.
  Handshake patterns typically come with a name
  that indicates what is going on.
* For example, the `IK` handshake pattern
  indicates that the client's public key is sent
  as part of the handshake
  (the first I stands for immediate), and that
  the server's public key is known to the client
  in advance (the `K` stands for known).
* Once a handshake pattern is chosen, applications
  making use of it will never attempt to perform
  any of the other possible handshake patterns.
* As opposed to TLS, this makes Noise a simple
  and linear protocol in practice.

* One particularity of Noise is that it
  continuously authenticates its handshake
  transcript. To achieve this, both sides
  maintain two variables: a **hash (h)** and
  a **chaining key (ck)**. Each handshake
  message sent or received is hashed with
  the previous `h` value.
* In the Noise protocol framework, each
  side of the connection keeps track of a
  digest `h` of all messages that have been
  sent and received during the handshake.
  When a message is sent and encrypted with
  an authenticated encryption with associated
  data (AEAD) algorithm, the current `h` value
  is used as associated data in order to
  authenticate the handshake up to this point.
* At the end of each message pattern, a
  (potentially empty) payload is encrypted
  with an authenticated encryption with
  associated data (AEAD) algorithm. When this
  happens, the `h` value is authenticated by
  the associated data field of the AEAD.
  This allows Noise to continuously verify
  that both sides of the connection are
  seeing the exact same series of messages
  and in the same order.
* In addition, every time a DH key exchange
  happens (several can happen during a handshake),
  its output is fed along with the previous
  chaining key (ck) to HKDF, which derives a
  new chaining key and a new set of symmetric
  keys to use for authenticating and
  encrypting subsequent messages.

* **TLS** and **Noise**

## End-to-end encryption

* The reason why there is no true solution
  is that we are trying to bridge reality
  (real human beings) with a theoretical
  cryptographic protocol.

* The details are in `RFC 4880`, the last
  version of **OpenPGP**, and can be
  simplified to the following steps:
  - The sender creates an email. At this
    point the email's content is compressed
    before it is encrypted.
  - The OpenPGP implementation generates
    a random symmetric key and symmetrically
    encrypts the email using the symmetric key.
  - The symmetric key is asymmetrically
    encrypted to each recipient's public key.
  - All of the intended recipients' encrypted
    versions of the symmetric key are
    concatenated with the encrypted message.
    The email body is replaced with this blob
    of data and sent to all recipients.
  - To decrypt an email, a recipient uses their
    private key to decrypt the symmetric key,
    then decrypts the content of the email
    using the decrypted symmetric key.

* how do you obtain and how can you trust
  other people's public keys? The answer is
  that in **PGP**, **you build trust yourself**!
* The web of trust (WOT) is the concept that
  users can transitively trust other users
  by relying on signatures. Alice trusts Bob
  who trusts Charles. Alice can use Bob's
  signature over Charles's identity and
  public key to trust Charles as well.

* PGP did try another way to solve the issue
  of *discovering public keys*:
  **key registries**. The concept is pretty
  simple: publish your PGP public key and
  associated signatures from others that
  attest to your identity on some public
  list so that people can find it.
* In practice, this doesn't work as anyone
  can publish a key and associated signature
  purportedly matching your email.

* more and more real-world cryptography
  applications are aiming at
  **replacing PGP** and solving its
  usability problems.
* **If not PGP, then what?**
* **Secure messaging**: A modern look at
  end-to-end encryption with **Signal**

* In the Signal mobile application, a
  fingerprint between Alice and Bob
  is computed by:
  - Hashing Alice's identity key prefixed
    by her username (a phone number in Signal)
    and interpreting a truncation of
    that digest as a series of numbers
  - Doing the same for Bob
  - Displaying the concatenation of the two
    series of numbers to the user

* **X3DH**: the Signal protocol's handshake
* Signal's key exchange, **X3DH**, combines three
  (or more) DH key exchanges into one.
* The three different types of DH keys that Signal uses:
  - *Identity keys* These are the long-term keys that
    represent the users. You can imagine that if
    Signal only used identity keys, then the scheme
    would be fairly similar to PGP, and there would
    be no forward secrecy.
  - *One-time prekeys* In order to add forward
    secrecy to the key exchange, even when the
    recipient of a new conversation is not online,
    Signal has users upload multiple single-use
    public keys. They are simply ephemeral keys
    that are uploaded in advance and are
    deleted after being used.
  - *Signed prekeys* We could stop here, but
    there's one edge case missing. Because the
    one-time prekeys that a user uploads can,
    at some point, be depleted, users also have
    to upload a medium-term public key that
    they sign: a signed prekey. This way, if no
    more one-time prekeys are available on the
    server under your username, someone can still
    use your signed prekey to add forward secrecy
    up to the last time you changed your
    signed prekey. This also means that you have
    to periodically rotate your signed prekey.
* Signal's flow starts with a user registering
  with a number of public keys. If Alice wants
  to talk to Bob, she first retrieves Bob's
  public keys (called a prekey bundle), then
  she performs an X3DH key exchange with these
  keys and creates an initial message using
  the output of the key exchange. After receipt
  of the message, Bob can perform the same on his
  side to initialize and continue the conversation.

* https://signal.org/docs/specifications/x3dh/

* **Double Ratchet**: Signal's *post-handshake* protocol

* https://signal.org/docs/

* The state of end-to-end encryption

* Signal has open sourced a lot of its code, but it
  lacks documentation and can be hard to use correctly.
* On the other hand, you might have better luck using
  a decentralized open source solution like **Matrix**,
  which might prove easier to integrate with.
  This is what the French government has done.

* Other protocols, like **Matrix**, attempt to
  standardize federated protocols for end-to-end
  encrypted messaging. Federated protocols are
  open protocols that anyone can interoperate
  with (as opposed to centralized protocols
  that are limited to a single application).

## User authentication

* You should think of **authentication** as
  a term used in cryptography to convey
  *two different concepts* depending
  on the context:
  - **Message/payload authentication** You're
    proving that a message is genuine and
    hasn't been modified since its creation.
  - **Origin/entity/identity authentication**
    You're proving that an entity really is
    who they say they are.

* **Authentication** is about proving that
  something is what it is supposed to be,
  and that *something* can be *a person*,
  *a message*, or *something else*.

* *User authentication*, or how machines
  authenticate humans
* *User-aided authentication*, or how humans
  can help machines authenticate one another

* In this book, I talk about *origin authentication*
  in three types of scenarios.
  - User authentication happens when a
    device authenticates a human being.
  - Machine authentication happens when a
    machine authenticates another machine.
  - User-aided authentication happens when a
    human is involved in a machine
    authenticating another machine.

* Today, two protocols are the main competitors
  when it comes to setting up SSO:
  - *Security Assertion Markup Language 2.0 (SAML)*
    A protocol using the
    *Extensible Markup Language (XML)* encoding.
  - *OpenID Connect (OIDC)* An extension to the
    *OAuth 2.0 (RFC 6749)* authorization protocol
    using the JavaScript Object Notation
    (JSON) encoding.
  - https://openid.net

* Cryptographic protocols called asymmetric
  (or augmented) password-authenticated key exchanges
  (PAKEs) attempt to provide user authentication
  without having users ever communicate their
  passwords directly to the server. This contrasts
  with symmetric or balanced PAKEs protocols,
  where both sides know the password.

* In the summer of 2019, the Crypto Forum Research
  Group (CFRG) of the IETF started a PAKE selection
  process with the goal to pick one algorithm to
  standardize for each category of PAKEs:
  *symmetric/balanced* and *asymmetric/augmented*.
* In March 2020, the CFRG announced the end of the
  PAKE selection process, selecting
  - **CPace** The recommended *symmetric/balanced*
    PAKE.
  - **OPAQUE** The recommended *asymmetric/augmented*
    PAKE.

* *oblivious pseudorandom function* (**OPRF**).
  - The term *oblivious* in cryptography generally
    refers to protocols where one party computes a
    cryptographic operation without knowing the
    input provided by another party.

* Here is how an **OPRF** works at a high level:
  - Alice wants to compute a PRF over an input
    but wants the input to remain secret.
    She "blinds" her input with a random value
    (called a blinding factor) and sends this to Bob.
  - Bob runs the OPRFs on this blinded value
    with his secret key, but the output is still
    blinded so it's useless for Bob.
    Bob then sends this back to Alice.
  - Alice finally "unblinds" the result using the
    same blinding factor she previously
    used to obtain the real output.
* An oblivious PRF (OPRF) is a construction that
  allows one party to compute a PRF over the input
  of another party without learning that input.
  To do this, Alice first generates a random
  blinding factor, then blinds her input with that
  before sending it to Bob. Bob uses his secret key
  to compute the PRF over the blinded value, then
  sends the blinded output to Alice who can
  unblind it. The result does not depend on the
  value of the blinding factor.

* https://github.com/cfrg/draft-irtf-cfrg-opaque
* https://cfrg.github.io/draft-irtf-cfrg-opaque/draft-irtf-cfrg-opaque.html
* https://datatracker.ietf.org/doc/draft-irtf-cfrg-opaque/

* To register to a server using **OPAQUE**,
  Alice generates a long-term key pair
  and sends her public key to the server,
  which stores it and associates it with
  Alice's identity. She then uses the **OPRF**
  protocol to obtain a strong symmetric
  key from her password and sends an encrypted
  backup of her key pair to the server.
  To log in, she obtains her encrypted key
  pair from the server, then performs the **OPRF**
  protocol with her password to obtain a symmetric
  key capable of decrypting her key pair. All
  that's left is to perform a mutually
  authenticated key exchange
  (or possibly sign a challenge) with this key.
* Passwords are a handy way to authenticate
  users as they live in someone's head and can
  be used on any device. On the other hand,
  users have trouble creating strong passwords,
  and because users tend to reuse passwords
  across websites, password breaches can be
  damaging. SSO allows you to connect to many
  services using one (or a few) service(s),
  while asymmetric (or augmented)
  password-authenticated key exchanges allow
  you to authenticate without the server ever
  learning your real password.

* A *one-time password* (**OTP**) algorithm
  allows you to create as many one-time
  passwords as you want from a symmetric
  key and some additional data. The additional
  data is different, depending on the
  OTP algorithm.

* There are two main schemes that one can
  use to produce OTPs:
  - The HMAC-based one-time password (**HOTP**)
    algorithm, standardized in `RFC 4226`,
    which is an OTP algorithm where the
    additional data is a counter.
  - The time-based one-time password (**TOTP**)
    algorithm, standardized in `RFC 6238`,
    which is an OTP algorithm where the
    additional data is the time.

* Most applications nowadays use **TOTP**
  because *HOTP* requires both the client
  and the server to store a state (a counter).
* Storing a state can lead to issues if
  one side falls out of synchrony and
  cannot produce (or validate)
  legitimate OTPs anymore.

* In most cases, this is how TOTP works:
  - When registering, the service communicates
    a symmetric key to the user
    (perhaps using a QR code). The user then
    adds this key to a TOTP application.
  - When logging in, the user can use the
    TOTP application to compute a one-time
    password. This is done by computing
    `HMAC(symmetric_key, time)`, where time
    represents the current time
    (rounded to the minute in order to make
    a one-time password valid for 60 seconds). Then
  - (a) The TOTP application displays to the
    user the derived one-time password, truncated
    and in a human-readable base (for example,
    reduced to 6 characters in base 10
    to make it all digits).
  - (b) The user either copies or types the
    one-time password into the relevant application.
  - (c) The application retrieves the user's
    associated symmetric key and computes the
    one-time password in the same way as the
    user did. If the result matches the received
    one-time password, the user is
    successfully authenticated.

## Crypto as in cryptocurrency?

## Hardware cryptography

## Post-quantum cryptography

## Next-generation cryptography

## When and where cryptography fails