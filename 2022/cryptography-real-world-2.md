---
title: Real-World Cryptography (下)
description: 余音袅袅, 不绝如缕. 舞幽壑之潜蛟, 泣孤舟之嫠妇.
date: 2021-10-15
---

* [Real-World Cryptography](https://book.douban.com/subject/34615742/)
  - https://www.manning.com/books/real-world-cryptography

## Secure transport

* Transport Layer Security (**TLS**)
  - The most recent version of TLS is TLS `1.3`,
    specified in `RFC 8446` and published in `2018`.

* TLS is split into two phases.
  - `A handshake phase` A secure communication
    is negotiated and created between
    two participants.
  - `A post-handshake phase` Communications are
    encrypted between the two participants.

* The **handshake** is, at its core, simply a
  `key exchange`.
  - The handshake ends up with the two participants
    agreeing on a set of `symmetric keys`.
* The **post-handshake** phase is purely about
  encrypting messages between participants.
  - This phase uses an authenticated encryption algorithm
    and the set of keys produced at the end of the handshake.

---

* The handshake itself has four aspects:
  - **Negotiation** TLS is highly configurable.
    Both a client and a server can be configured to
    negotiate a range of TLS versions as well as
    a menu of acceptable cryptographic algorithms.
  - The negotiation phase of the handshake aims at
    finding common ground between the client's and
    the server's configurations in order to
    securely connect the two peers.
  - **Key exchange** The whole point of the handshake is
    to perform a key exchange between two participants.
  - Which key exchange algorithm to use?
    This is one of the things decided as part of the
    `client/server` negotiation process.
  - **Authentication** As you learned on key exchanges,
    it is trivial for **MITM** attackers to impersonate
    any side of a key exchange.
  - Due to this, key exchanges must be authenticated.
    Your browser must have a way to ensure that it is
    talking to `google.com`, for example, and not your
    internet service provider (ISP).
  - **Session resumption** As browsers often connect
    to the same websites again and again, key exchanges
    can be costly and can slow down a user's experience.
  - For this reason, mechanisms to fast-track secure
    sessions without redoing a key exchange
    are integrated into TLS.

- In `March 2021`, the IETF published `RFC 8996`:
  - **Deprecating** TLS `1.0` and TLS `1.1`,
    effectively making the deprecation official.

---

* The `ClientHello` contains a range of
  supported SSL and TLS versions, a suite of
  cryptographic algorithms that the client is
  willing to use, and some more information that
  could be relevant for the rest of the
  handshake or for the application. The suite of
  cryptographic algorithms include
  - One or more key exchange algorithms (`RFC 7919`)
  - Two (for different parts of the handshake)
    or more digital signature algorithms
  - One or more hash functions to be used
    with HMAC and HKDF
  - One or more authenticated encryption algorithms
* The server then responds with a `ServerHello`
  message, which contains one of each type of
  cryptographic algorithm, cherry-picked from the
  client's selection.

---

* TLS `1.3` optimizes this flow by attempting
  to do __both__ the `negotiation` and the
  `key exchange` at the same time:
  - the client speculatively chooses a key exchange algorithm
    and sends a public key in the first message
    (the `ClientHello`).
  - If the client fails to predict the server's choice of
    key exchange algorithm, then the client falls back to
    the outcome of the negotiation and sends a new
    `ClientHello` containing the correct public key.

* In TLS `1.3`, each session starts with an
  **ephemeral key exchange**.
  - If a server is compromised at some point in time,
    no previous sessions will be impacted.
* TLS `1.3` derives different keys at
  different points in time to encrypt
  different phases with independent keys.
* To derive the different keys, TLS `1.3` uses
  HKDF with the hash function negotiated.
  - HKDF-Extract is used on the output of the
    key exchange to remove any biases,
  - while HKDF-Expand is used with different
    info parameters to derive
    the encryption keys.

---

* A TLS `1.3` handshake is actually split
  into __three__ different stages
  - **Key exchange** This phase contains the
    `ClientHello` and `ServerHello` messages
    that provide some negotiation and perform
    the key exchange.
  - All messages including handshake messages
    after this phase are encrypted.
  - **Server parameters** Messages in this phase
    contain additional negotiation data from
    the server.
  - This is negotiation data that does not have to
    be contained in the first message of the server
    and that could benefit from being encrypted.
  - **Authentication** This phase includes
    authentication information from both
    the server and the client.

---

* Client authentication is often delegated to
  the application layer for the web, most
  often via a form asking you for your
  credentials.
  - That being said, client authentication can also
    happen in TLS if requested by the server during
    the server parameters phase.
  - When both sides of the connection are authenticated,
    we talk about mutually-authenticated TLS
    (sometimes abbreviated as **mTLS**).
* Client authentication is done the same way
  as server authentication.
  - This can happen at any point after the
    authentication of the server
  - (for example, during the handshake or
    in the post-handshake phase).

---

* There are two sides to the web PKI.
  - __First__, browsers must trust a set of
    root public keys that we call
    certificate authorities (**CAs**).
  - Usually, browsers will either use a
    hardcoded set of trusted public keys
    or will rely on the operating system
    to provide them.
  - __Second__, websites that want to use HTTPS
    must have a way to obtain a certification
    (a signature of their signing public key)
    from these CAs.
  - In order to do this, a website owner must
    prove to a CA that they own a specific domain.

* More specifically, CAs do not actually
  sign public keys, but instead they sign
  certificates (more on this later).
  - A certificate contains the long-term public key,
    along with some additional important metadata
    like the web page's domain name.

* The signature in the `CertificateVerify`
  message proves to the client what the
  server has so far seen.
  - Without this signature, a MITM attacker could
    intercept the server's handshake messages and
    replace the ephemeral public key of the
    server contained in the ServerHello message,
    allowing the attacker to successfully
    impersonate the server.
* The authentication part of a handshake
  starts with the server sending a
  certificate chain to the client.
  - The certificate chain starts with the leaf certificate
    (the certificate containing the website's public key
    and additional metadata like the domain name)
    and ends with a root certificate that is
    trusted by the browser.
  - Each certificate contains a signature from the
    certificate above it in the chain.

* Finally, in order to officially end the handshake,
  both sides of the connection must send a `Finished`
  message as part of the authentication phase.
* A Finished message contains an authentication
  tag produced by HMAC, instantiated with the
  negotiated hash function for the session.
  - This allows both the client and the server
    to tell the other side,
    "These are all the messages I have sent
    and received in order during this handshake."
  - If the handshake is intercepted and tampered
    with by MITM attackers, this integrity check
    allows the participants to detect and
    abort the connection.

---

* While certificates are __optional__ in TLS `1.3`
  (you can always use plain keys),
  many applications and protocols,
  not just the web, make heavy use of them
  in order to certify additional metadata.
  - Specifically, the `X.509` certificate
    standard version `3` is used.
* The `X.509` standard uses a description language
  called **Abstract Syntax Notation One**
  to specify information contained in a certificate.
  - A data structure described in `ASN.1`
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
  - Field names described in `ASN.1`
    (like `tbsCertificate`) are lost after encoding.
* Decoding **DER** without the knowledge of the
  original `ASN.1` description of what each
  field truly means is thus pointless.
* **DER** encoding is a difficult protocol
  to parse correctly, and the complexity of
  `X.509` certificates makes for many mistakes
  to be potentially devastating.
  - For this reason, I **don't recommend** any
    modern application **to use** `X.509`
    certificates unless it has to.

---

* In TLS `1.3`, a **PSK** handshake works by having
  the client advertise in its `ClientHello` message
  that it supports a list of **PSK** identifiers.
  - If the server recognizes one of the **PSK** IDs,
    it can say so in its response
    (the `ServerHello` message),
    and both can then avoid doing a key exchange
    (if they want to).
  - By doing this, the authentication phase is
    skipped, making the `Finished` message at
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
* TLS `1.3` offers a way to generate a PSK
  after a handshake is successfully performed,
  which can be used in subsequent
  connections to avoid having to
  redo a full handshake.
* If the server wants to offer this feature,
  it can send a `New Session Ticket` message
  at any time during the post-handshake phase.

---

* Starting with TLS `1.3`, if a server decides
  to allow it, clients have the possibility
  to send encrypted data as part of their
  first series of messages, right after the
  `ClientHello` message.
  - This means that browsers do not necessarily
    have to wait until the end of the handshake
    to start sending application data to the server.
  - This mechanism is called `early data` or
    **0-RTT** (for `zero round trip time`).
  - It can only be used with the combination
    of a PSK as it allows derivation of
    symmetric keys during the `ClientHello` message.
* This feature was quite controversial during
  the development of the TLS `1.3` standard
  because a passive attacker can replay an
  observed `ClientHello` followed by the
  encrypted `0-RTT` data.
  - This is why `0-RTT` must be used only with
    application data that can be replayed safely.

---

* `Certificate revocation` As the name
  indicates, this allows a CA to revoke
  a certificate and warn browsers about it.
* `Certificate monitoring` This is a
  relatively new system that forces CAs
  to publicly log every certificate signed.

* **IPSec**: One of the most popular
  virtual network protocols (**VPNs**) used
  to connect different private networks together.
  - It is mostly used by companies to link
    different office networks.
  - As its name indicates, it acts at the IP layer
    and is often found in routers, firewalls,
    and other network appliances.
  - Another popular VPN is OpenVPN, which
    makes direct use of TLS.

* the __Noise__ protocol framework.
  - __Noise__ is a much more modern
    alternative to TLS.

* The Noise protocol framework removes
  the run-time complexity of TLS by avoiding
  all negotiation in the handshake.
  - A client and a server running Noise follow
    a linear protocol that does not branch.
  - Contrast this to TLS, which can take many
    different paths, depending on the information
    contained in the different handshake messages.
* What Noise does is that it pushes all the
  complexity to the design phase.

* The Noise protocol framework offers different
  handshake patterns that you can choose from.
  - Handshake patterns typically come with a name
    that indicates what is going on.
  - For example, the `IK` handshake pattern
    indicates that the client's public key
    is sent as part of the handshake
    (the first I stands for immediate),
    and that the server's public key is known to
    the client in advance (the `K` stands for known).
* Once a handshake pattern is chosen, applications
  making use of it will never attempt to perform
  any of the other possible handshake patterns.
  - As opposed to TLS, this makes Noise a simple
    and linear protocol in practice.

* One particularity of Noise is that it
  continuously authenticates its handshake
  transcript.
  - To achieve this, both sides maintain two variables:
  - a **hash (h)** and a **chaining key (ck)**.
  - Each handshake message sent or received is
    hashed with the previous `h` value.
* In the Noise protocol framework, each
  side of the connection keeps track of a
  digest `h` of all messages that have been
  sent and received during the handshake.
  - When a message is sent and encrypted with
    an authenticated encryption with associated
    data (AEAD) algorithm, the current `h` value
    is used as associated data in order to
    authenticate the handshake up to this point.
* At the end of each message pattern, a
  (potentially empty) payload is encrypted
  with an authenticated encryption with
  associated data (AEAD) algorithm.
  - When this happens, the `h` value is authenticated
    by the associated data field of the AEAD.
  - This allows Noise to continuously verify
    that both sides of the connection are
    seeing the exact same series of messages
    and in the same order.
* In addition, every time a DH key exchange happens
  (several can happen during a handshake),
  its output is fed along with the previous
  chaining key (ck) to HKDF, which derives a
  new chaining key and a new set of symmetric
  keys to use for authenticating and
  encrypting subsequent messages.

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
  - The email body is replaced with this blob
    of data and sent to all recipients.
  - To decrypt an email, a recipient uses their
    private key to decrypt the symmetric key,
    then decrypts the content of the email
    using the decrypted symmetric key.

* how do you obtain and how can you trust
  other people's public keys?
  - The answer is that in **PGP**,
    **you build trust yourself**!
* The web of trust (WOT) is the concept that
  users can transitively trust other users
  by relying on signatures.
  - Alice trusts Bob who trusts Charles.
  - Alice can use Bob's signature over Charles's
    identity and public key to trust Charles as well.

* PGP did try another way to solve the issue
  of discovering public keys: **key registries**.
  - The concept is pretty simple:
  - publish your PGP public key and
    associated signatures from others that
    attest to your identity on some public
    list so that people can find it.
* In practice, this doesn't work as anyone
  can publish a key and associated signature
  purportedly matching your email.

---

* more and more real-world cryptography
  applications are aiming at
  **replacing PGP** and solving its
  usability problems.
* If not PGP, then what?
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

---

* **X3DH**: the Signal protocol's handshake
* Signal's key exchange, **X3DH**, combines three
  (or more) DH key exchanges into one.
* The __three__ different types of DH keys that Signal uses:
  - `Identity keys` These are the long-term keys that
    represent the users. You can imagine that if
    Signal only used identity keys, then the scheme
    would be fairly similar to PGP, and there would
    be no forward secrecy.
  - `One-time prekeys` In order to add forward
    secrecy to the key exchange, even when the
    recipient of a new conversation is not online,
    Signal has users upload multiple single-use
    public keys.
  - They are simply ephemeral keys that are uploaded
    in advance and are deleted after being used.
  - `Signed prekeys` We could stop here, but
    there's one edge case missing. Because the
    one-time prekeys that a user uploads can,
    at some point, be depleted, users also have
    to upload a medium-term public key that
    they sign: a signed prekey.
  - This way, if no more one-time prekeys are available
    on the server under your username, someone can still
    use your signed prekey to add forward secrecy
    up to the last time you changed your signed prekey.
  - This also means that you have to
    periodically rotate your signed prekey.
* Signal's flow starts with a user registering
  with a number of public keys. If Alice wants
  to talk to Bob, she first retrieves Bob's
  public keys (called a prekey bundle), then
  she performs an X3DH key exchange with these
  keys and creates an initial message using
  the output of the key exchange.
  - After receipt of the message, Bob can perform the
    same on his side to initialize and
    continue the conversation.

* https://signal.org/docs/specifications/x3dh/

* **Double Ratchet**: Signal's post-handshake protocol

* https://signal.org/docs/

* Signal has open sourced a lot of its code, but it
  lacks documentation and can be __hard__ to use correctly.
* On the other hand, you might have better luck using
  a decentralized open source solution like **Matrix**,
  which might prove easier to integrate with.
  - This is what the French government has done.

---

* Other protocols, like **Matrix**, attempt to
  standardize federated protocols for end-to-end
  encrypted messaging.
  - Federated protocols are open protocols that
    anyone can interoperate with
    (as opposed to centralized protocols that
    are limited to a single application).

## User authentication

* You should think of **authentication** as
  a term used in cryptography to convey
  two __different__ concepts depending
  on the context:
  - **Message/payload authentication** You're
    proving that a message is genuine and
    hasn't been modified since its creation.
  - **Origin/entity/identity authentication**
    You're proving that an entity really is
    who they say they are.

* **Authentication** is about proving that
  something is what it is supposed to be,
  and that something can be a person,
  a message, or something else.

---

* `User authentication`, or how machines
  authenticate humans
* `User-aided authentication`, or how humans
  can help machines authenticate one another

* In this book, I talk about origin authentication
  in __three__ types of scenarios.
  - User authentication happens when a
    device authenticates a human being.
  - Machine authentication happens when a
    machine authenticates another machine.
  - User-aided authentication happens when a
    human is involved in a machine
    authenticating another machine.

* Today, two protocols are the main competitors
  when it comes to setting up SSO:
  - Security Assertion Markup Language 2.0 (SAML)
    A protocol using the
    Extensible Markup Language (XML) encoding.
  - OpenID Connect (OIDC) An extension to the
    OAuth 2.0 (`RFC 6749`) authorization protocol
    using the JavaScript Object Notation (JSON) encoding.
  - https://openid.net

* Cryptographic protocols called asymmetric
  (or augmented) password-authenticated key exchanges
  (PAKEs) attempt to provide user authentication
  without having users ever communicate their
  passwords directly to the server.
  - This contrasts with symmetric or balanced PAKEs protocols,
    where both sides know the password.

* In the summer of 2019, the Crypto Forum Research
  Group (CFRG) of the IETF started a PAKE selection
  process with the goal to pick one algorithm to
  standardize for each category of PAKEs:
  `symmetric/balanced` and `asymmetric/augmented`.
* In March 2020, the CFRG announced the end of the
  PAKE selection process, selecting
  - **CPace** The recommended `symmetric/balanced`
    PAKE.
  - **OPAQUE** The recommended `asymmetric/augmented`
    PAKE.

* `oblivious pseudorandom function` (**OPRF**).
  - The term oblivious in cryptography generally
    refers to protocols where one party computes a
    cryptographic operation without knowing the
    input provided by another party.

---

* Here is how an **OPRF** works at a high level:
  - Alice wants to compute a PRF over an input
    but wants the input to remain secret.
    She "blinds" her input with a random value
    (called a blinding factor) and sends this to Bob.
  - Bob runs the OPRFs on this blinded value
    with his secret key, but the output is still
    blinded so it's useless for Bob.
  - Bob then sends this back to Alice.
  - Alice finally "unblinds" the result using the
    same blinding factor she previously
    used to obtain the real output.
* An oblivious PRF (OPRF) is a construction that
  allows one party to compute a PRF over the input
  of another party without learning that input.
  - To do this, Alice first generates a random
    blinding factor, then blinds her input with that
    before sending it to Bob.
  - Bob uses his secret key to compute the PRF over
    the blinded value, then sends the blinded output
    to Alice who can unblind it.
  - The result does not depend on the
    value of the blinding factor.

* https://github.com/cfrg/draft-irtf-cfrg-opaque
* https://cfrg.github.io/draft-irtf-cfrg-opaque/draft-irtf-cfrg-opaque.html
* https://datatracker.ietf.org/doc/draft-irtf-cfrg-opaque/

* To register to a server using **OPAQUE**,
  Alice generates a long-term key pair
  and sends her public key to the server,
  which stores it and associates it with
  Alice's identity.
  - She then uses the **OPRF** protocol to
    obtain a strong symmetric key from her password
    and sends an encrypted backup of
    her key pair to the server.
  - To log in, she obtains her encrypted key
    pair from the server, then performs the **OPRF**
    protocol with her password to obtain a symmetric
    key capable of decrypting her key pair.
  - All that's left is to perform a mutually
    authenticated key exchange
    (or possibly sign a challenge) with this key.
* Passwords are a handy way to authenticate
  users as they live in someone's head and can
  be used on any device. On the other hand,
  users have trouble creating strong passwords,
  and because users tend to reuse passwords
  across websites, password breaches can be
  damaging.
  - SSO allows you to connect to many
    services using one (or a few) service(s),
    while asymmetric (or augmented)
    password-authenticated key exchanges allow
    you to authenticate without the server ever
    learning your real password.

---

* A one-time password (**OTP**) algorithm
  allows you to create as many one-time
  passwords as you want from a symmetric
  key and some additional data.
  - The additional data is different,
    depending on the `OTP` algorithm.

* There are two main schemes that one can
  use to produce OTPs:
  - The HMAC-based one-time password (**HOTP**)
    algorithm, standardized in `RFC 4226`,
    which is an `OTP` algorithm where the
    additional data is a counter.
  - The time-based one-time password (**TOTP**)
    algorithm, standardized in `RFC 6238`,
    which is an `OTP` algorithm where the
    additional data is the time.

* Most applications nowadays use **TOTP**
  because `HOTP` requires both the client
  and the server to store a state (a counter).
  - Storing a state can lead to issues if
    one side falls out of synchrony and
    cannot produce (or validate)
    legitimate OTPs anymore.

* In most cases, this is how __TOTP__ works:
  - When registering, the service communicates
    a symmetric key to the user
    (perhaps using a QR code). The user then
    adds this key to a TOTP application.
  - When logging in, the user can use the
    TOTP application to compute a one-time
    password.
  - This is done by computing
    `HMAC(symmetric_key, time)`,
    where time represents the current time
    (rounded to the minute in order to make
    a one-time password valid for `60` seconds).
    Then
  - (a) The TOTP application displays to the
    user the derived one-time password, truncated
    and in a human-readable base (for example,
    reduced to `6` characters in base `10`
    to make it all digits).
  - (b) The user either copies or types the
    one-time password into the relevant application.
  - (c) The application retrieves the user's
    associated symmetric key and computes the
    one-time password in the same way as the
    user did.
  - If the result matches the received
    one-time password, the user is
    successfully authenticated.

* One interesting standard in this space is the
  **Fast IDentity Online 2** (**FIDO2**).
  `FIDO2` is an open standard that defines how
  to use asymmetric keys to authenticate users.
  The standard specifically targets phishing
  attacks, and for this reason, `FIDO2` is made to
  work **only with hardware authenticators**.
  - Hardware authenticators are simply physical
    components that can generate and store signing
    keys and can sign arbitrary challenges.
  - **FIDO2** is split into two specifications:
  - `Client to Authenticator Protocol` (**CTAP**)
    `CTAP` specifies a protocol that roaming
    authenticators and clients can use to
    communicate with one another. Roaming
    authenticators are hardware authenticators
    that are external to your main device.
  - A client in the `CTAP` specification is
    defined as the software that wants to
    query these authenticators as part of
    an authentication protocol. Thus, a client
    can be an operating system, a native
    application like a browser, and so on.
  - `Web Authentication` (**WebAuthn**)
    `WebAuthn` is the protocol that web browsers
    and web applications can use to authenticate
    users with hardware authenticators.
  - It, thus, must be implemented by browsers to
    support authenticators. If you are building
    a web application and want to support user
    authentication via hardware authenticators,
    `WebAuthn` is what you need to use.

* To authenticate without using a password,
  applications can allow users to either use
  **symmetric keys** via **OTP-based** protocols
  or use **asymmetric keys** via the **FIDO2**
  standard.
  - FIDO2 supports different types of
    authenticators, roaming authenticators
    (via the CTAP standard) or built-in authenticators.

* User-aided authentication protocols that
  allow a human to pair two devices are modeled
  with two types of channels between the devices:
  - an insecure channel (for example,
    NFC, Bluetooth, WiFi, and so on),
    which we assume is adversary-controlled, and
  - an authenticated channel (for example, real life),
    which does not provide confidentiality but can
    be used to exchange relatively small
    amounts of information.

* The **CPace** PAKE works by having the two
  devices create a generator based on a password
  and then use it to perform as a base for the
  usual ephemeral DH key exchange.

* three techniques to pair two devices:
  - `(1)` a user can either help the devices
    obtain each other's public keys so that
    they can perform a key exchange;
  - `(2)` a user can enter the same password
    on two devices so that they can perform
    a symmetric password-authenticated
    key exchange; or
  - `(3)` a user can verify a fingerprint of
    the key exchange after the fact to
    confirm that no MITM attacker
    intercepted the pairing.

## Crypto as in cryptocurrency?

* One limitation of these **PBFT-based**
  consensus algorithms is that they all
  require a known and fixed set of
  participants.
* More problematic, past a certain number
  of participants, they start breaking
  apart: communication complexity
  increases drastically, they become
  extremely slow, electing a leader
  becomes complicated, etc.

## Next-generation cryptography

* I give you a taste of what the future of
  real-world cryptography might look like
  (perhaps in the next 10 to 20 years)
  by briefly introducing three primitives:
  - **Secure multi-party computation** (MPC)
    A subfield of cryptography that allows
    different participants to execute a
    program together without necessarily
    revealing their own input to the program.
  - **Fully homomorphic encryption** (FHE)
    The holy grail of cryptography, a
    primitive used to allow arbitrary
    computations on encrypted data.
  - **General-purpose zero-knowledge proofs**
    (ZKPs) The primitive you learned about
    that allows you to prove that you know
    something without revealing that something,
    but this time, applied more generally
    to more complex programs.

* The more the merrier:
  *Secure multi-party computation* (MPC)

* *Secure multi-party computation* (MPC) is
  a field of cryptography that came into existence
  in 1982 with the famous Millionaires' problem.
* In his 1982 paper "Protocols for Secure Computations,"
  Andrew C. Yao wrote,
  - "Two millionaires wish to know who is richer;
    however, they do not want to find out inadvertently
    any additional information about each other's wealth.
    How can they carry out such a conversation?"
  - Simply put, MPC is a way for
    *multiple participants to compute a program together*.

* MPC allows us to completely remove trusted third
  parties from a distributed computation and enables
  participants to compute the computation by themselves
  without revealing their respective inputs to one
  another. This is done through
  a cryptographic protocol.

* NIST in mid-2019 kicking off a standardization
  process for **threshold cryptography**.
* Another well-known subfield of **MPC** is the
  field of **private set intersection** (PSI),
  which poses the following problem:
  - Alice and Bob have a list of words, and they
    want to know which words (or perhaps just how many)
    they have in common without revealing their
    respective list of words.
    - One way to solve this problem is to use the
      oblivious pseudorandom function (OPFR) construction.
* **Private set intersection** (PSI) allows Alice
  to learn what words she has in common with Bob.
  - First, she blinds every word she has in her
    list and uses the OPRF protocol with Bob to
    apply a PRF using Bob's key on
    each of her words.
  - Finally, Bob sends her the PRF of his key
    with his words. Alice can then see if
    anything matches to learn what
    words they have in common.

* More generally, MPC has many different
  solutions aiming at the computation of
  arbitrary programs. General-purpose MPC
  solutions all provide different levels
  of efficiency (from hours to milliseconds)
  and types of properties.
* For example, how many dishonest participants
  can the protocol tolerate? Are participants
  malicious or just honest but curious
  (also called semi-honest, a type of participant
  in MPC protocols that is willing to execute
  the protocol correctly but might attempt to
  learn the other participants' inputs)?
* An **arithmetic circuit** is a number of
  addition or multiplication gates linking inputs
  to outputs. Notice that different inputs to the
  circuit are provided by different participants,
  but they could also be public inputs
  (known to everyone).

* The first step of a general-purpose MPC with
  secret sharing is to have participants split
  their respective secret inputs (using
  Shamir's secret sharing scheme) and distribute
  the parts to all participants.
* The second step of a general-purpose MPC with
  secret sharing is to have participants compute
  each gate in the circuit.
  - For example, a participant can compute an
    addition gate by adding the two input Shamir
    shares that they have, which produces a
    Shamir share of the output.

* The state of **MPC**
  - There's been huge progress in the last decade
    to make MPC practical. It is a field of many
    different use cases, and one should be on the
    lookout for the potential applications that can
    benefit from this newish primitive.
  - Note that, unfortunately, no real standardization
    effort exists, and while several MPC implementations
    can be considered practical for many use cases
    today, they are not easy to use.
  - Incidentally, the general-purpose MPC construction
    I explained earlier in this section is based on
    secret sharing, but there are more ways to
    construct MPC protocols.
  - A well-known alternative is called **garbled circuits**,
    which is a type of construction first proposed
    by Yao in his 1982 paper introducing MPC.
  - Another alternative is based on
    **fully homomorphic encryption**.

* **Fully homomorphic encryption** (FHE) and
  the promises of an encrypted cloud
  - This interesting concept, originally proposed
    in 1978 by Rivest, Adleman, and Dertouzos, is
    what we call fully homomorphic encryption (FHE)
    (or as it used to be called,
    the holy grail of cryptography).
  - Fully homomorphic encryption (FHE) is an
    encryption scheme that allows for arbitrary
    computations over encrypted content. Only the
    owner of the key can decrypt
    the result of the computation.

* Other types of homomorphic encryptions include
  - **Somewhat homomorphic** Which means partially
    homomorphic for one operation
    (addition or multiplication) and homomorphic
    for the other operation in limited ways.
  - For example, additions are unlimited up to a
    certain number but only a few
    multiplications can be done.
  - **Leveled homomorphic** Both addition and
    multiplication are possible up to a
    certain number of times.
  - **Fully homomorphic** Addition and multiplication
    are unlimited (it's the real deal).

* After encrypting a message with a fully
  homomorphic encryption algorithm, operating on it
  increases its noise to dangerous thresholds,
  where decryption becomes impossible.
* To eliminate the noise of the ciphertext,
  you can decrypt it. But because you don't have
  the secret key, instead you reencrypt the noisy
  ciphertext under another public key
  (called the bootstrapping key) to obtain a new
  ciphertext of a noisy ciphertext without error.
* You use the initial secret key encrypted to the
  bootstrapping key to apply the decryption
  circuit to that new ciphertext. This effectively
  decrypts the noisy ciphertext in place, removing
  the errors. There will be some amount of errors
  due to the decryption circuit.

* You could think that you're stuck, but
  **bootstrapping** unsticks you by removing the
  noise out of that ciphertext. To do that, you
  re-encrypt the noisy ciphertext under another
  public key (usually called the bootstrapping key)
  to obtain an encryption of that noisy ciphertext.
  - Notice that the new ciphertext has no noise.
* Now comes the magic: you are provided with the
  initial private key, not in cleartext, but
  encrypted under that bootstrapping key. This
  means that you can use it with a decryption
  circuit to homomorphically decrypt the inner
  noisy ciphertext.
  - If the decryption circuit produces an acceptable
    amount of noise, then it works, and you will
    end up with the result of the first homomorphic
    operation encrypted under the bootstrapping key.
* If the remaining amount of errors allows you
  to do at least one more homomorphic operation
  `(+ or ×)`, then you are gold: you have a
  fully homomorphic encryption algorithm because
  you can always, in practice, run the
  bootstrapping after or before every operation.
  - Note that you can set the bootstrapping
    key pair to be the same as the initial key pair.
  - It's a bit weird as you get some circular
    security oddity, but it seems to work and no
    security issues are known.

* **General-purpose zero-knowledge proofs** (ZKPs)

* **General-purpose ZKPs** allow a prover to convince
  a verifier about the integrity of an execution trace
  (the inputs of a program and the outputs
  obtained after its execution) while hiding some of
  the inputs or outputs involved in the computation.
  - An example of this is a prover trying to prove
    that a sudoku can be solved.

* In 2018, actors from the industry and academia
  joined together to form the ZKProof Standardization
  effort with the goal to "standardize the use of
  cryptographic zero-knowledge proofs."

* Distinctions between the different proposed
  schemes are quite important. Because it is a
  great source of confusion, here is how some
  of these schemes are divided:
  - **Zero-knowledge or not** If some of the
    information needs to remain secret from some
    of the participants, then we need
    zero-knowledgeness.
  - Note that proofs without secrets can be useful as well.
  - For example, you might want to delegate some intensive
    computation to a service that, in turn,
    has to prove to you that the result
    they provide is correct.
  - **Interactive or not** Most ZKP schemes can be
    made non-interactive, and protocol designers
    seem most interested in the non-interactive
    version of the scheme. This is because
    back-and-forth's can be time consuming
    in protocols, but also because interactivity
    is sometimes not possible.
  - So-called non-interactive proofs are often
    referred to as NIZKs for non-interactive ZKPs.
  - **Succinct proofs or not** Most of the ZKP schemes in
    the spotlight are often referred to as zk-SNARKs for
    Zero-Knowledge Succinct Non-Interactive Argument of Knowledge.
  - While the definition can vary, it focuses on the
    size of the proofs produced by such systems
    (usually in the order of hundreds of bytes), and
    the amount of time needed to verify them
    (within the range of milliseconds).
  - **zk-SNARKs** are, thus, short and easy to use to verify ZKPs.
  - Note that a scheme not being a zk-SNARK does not
    disqualify it for the real world as often different
    properties might be useful in different use cases.
  - **Transparent setup or not** Like every cryptographic
    primitive, ZKPs need a setup to agree on a set of
    parameters and common values. This is called a
    common reference string (CRS). But setups for ZKPs
    can be much more limiting or dangerous than
    initially thought.
  - There are **three** types of setup:
  - **Trusted** Means that whoever created the CRS also
    has access to secrets that allow them to forge proofs
    (hence, it's why these secrets are sometimes
    called "toxic waste").
  - This is quite an issue as we are back to having a
    trusted third party, yet schemes that exhibit this
    property are often the most efficient
    and have the shortest proof size.
  - To decrease the risk, MPC can be use to have many
    participants help create these dangerous parameters.
    If a single participant is honest and deletes their
    keys after the ceremony, the toxic waste gets flushed.
  - **Universal** A trusted setup is said to be universal if
    you can use it to prove the execution of any circuit
    (bounded by some size). Otherwise it is specific
    to a single circuit.
  - **Transparent** Fortunately for us, many schemes also
    offer transparent setups, meaning that no trusted
    third party needs to be present to create the
    parameters of the system. Transparent schemes
    are by design universal.
  - **Quantum-resistant or not** Some ZKPs make use of
    public key cryptography and advanced primitives like
    bilinear pairings, while others only rely on symmetric
    cryptography (like hash functions), which makes them
    naturally resistant to quantum computers
    (usually at the expense of much larger proofs).

* First and foremost, there are many, many zk-SNARK schemes,
  too many of them, really.
* Most build on this type of construction:
  - A proving system, allowing a prover to
    prove something to a verifier.
  - A translation or compilation of a program to
    something the proving system can prove.

* How can we prove this without giving out `f(x)`?
  The answer is in the following three tricks:
  - **Homomorphic commitments** A commitment scheme
    similar to the ones we used in other ZKPs
  - **Bilinear pairings** A mathematical construction
    that has some interesting properties;
  - The fact that different polynomials evaluate to
    different values most of the time.

* Finally, the succinctness of zk-SNARKs comes from
  the fact that two functions that differ evaluate
  to different points most of the time.
* The Schwartz-Zippel lemma says that two different
  polynomials of degree `n` can intersect in at most
  `n` points.
  - In other words, two different
    polynomials will differ in most points.
