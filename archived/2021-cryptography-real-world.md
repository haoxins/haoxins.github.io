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
* Because of this, and the fact that `SHA-2` is vulnerable
  to *length-extension attacks*, NIST decided in 2007 to
  organize an open competition for a new standard: `SHA-3`.
* `SHA-3` is a cryptographic algorithm
  built on top of a *permutation*.
* `SHA-3` is based on a particular *permutation* called
  `keccak-f` that takes an input and returns
  an output of the same size.

* Cryptographic protocols often necessitate this
  type of primitives but do not want to be
  constrained by the *fixed sizes* of
  a hash function's digest.
* For this reason, the `SHA-3` standard introduced
  a more versatile primitive called an
  *extendable output function* or `XOF`.
* This section introduces the two standardized XOFs:
  - `SHAKE` and `cSHAKE`.
* **`SHAKE`**, specified in *FIPS 202* along with `SHA-3`,
  can be seen as a hash function that returns
  an output of *an arbitrary length*.
* **`cSHAKE`** is pretty much exactly like `SHAKE`,
  except that it also takes a *customization string*.
* **`TupleHash`**, which is based on `cSHAKE` and
  specified in the same standard as `cSHAKE`.
* **`TupleHash`** is an interesting function
  that allows one to hash a *tuple*.

```zsh
echo -n "Alice""Bob""100""15" | openssl dgst -sha3-256
# vs
echo -n "Alice""Bob""1001""5" | openssl dgst -sha3-256
# This is what TupleHash solves.
```

* If an attacker retrieves hashed passwords,
  a brute force attack or an exhaustive search
  can be undertaken. This would test each
  attempt against the whole database.
  - This issue has been commonly solved by using *salts*,
    which in some sense is like using a
    per-user customization string with `cSHAKE`.
  - It effectively creates a different
    hash function for every user.
* Hash functions are supposed to be as fast.
  Attackers can leverage this to brute force
  (many, many passwords per second).
  - This issue is solved with *password hashes*,
    which are designed to be slow.
  - The current state-of-the-art
    choice for this is *Argon2*.

* [RFC 9106](https://datatracker.ietf.org/doc/rfc9106/)
  - Argon2 Memory-Hard Function for
    Password Hashing and Proof-of-Work Applications

## Message authentication codes

* Mix a *hash function* with a *secret key* and
  you obtain something called a
  *message authentication code* (**MAC**),
  a cryptographic primitive to
  protect the **integrity** of data.

* **`HMAC`** is a message authentication code
  that uses a hash function at its core.
* It is compatible with different hash functions,
  but it is mostly used in conjunction with `SHA-2`.

* 哇喔, Rust!

```rust
// sha2 = "0.9.8"
// hmac = "0.11.0"
use hmac::{Hmac, Mac, NewMac};
use sha2::Sha256;
// Note that this protocol is not perfect:
// it allows replays.
fn send_message(key: &[u8], message: &[u8]) -> Vec<u8> {
    let mut mac = Hmac::<Sha256>::new(key.into());
    mac.update(message);
    mac.finalize().into_bytes().to_vec()
}

fn receive_message(key: &[u8], message: &[u8], authentication_tag: &[u8]) -> bool {
    let mut mac = Hmac::<Sha256>::new(key.into());
    mac.update(message);
    mac.verify(&authentication_tag).is_ok()
}

fn main() {
    let key: [u8; 64] = [1; 64];
    let msg: [u8; 64] = [9; 64];
    let tag = send_message(&key, &msg);
    let ok = receive_message(&key, &msg, &tag);

    assert_eq!(ok, true)
}
```

* A `MAC` usually comes with a proof that even
  if an attacker can ask you to produce the
  authentication tags for a large number of
  arbitrary messages, the attacker should still
  not be able to forge an authentication tag
  on a never-seen-before message by themselves.

* If you are trying to authenticate *structures*,
  make sure to *serialize* them before
  authenticating them with a `MAC`; otherwise,
  forgery might be trivial.

* Remember, finding a collision for a
  *hash function* means finding two different
  inputs X and Y such that `HASH(X) = HASH(Y)`.
* We can extend this definition to `MACs` by
  defining a collision when `MAC(k, X) = MAC(k, Y)`
  for inputs X and Y.

* When verifying an authentication tag,
  the comparison between the received
  authentication tag and the one you compute
  must be done in **constant time**.
  - **timing attacks**

```go
// Constant time comparison in Golang
for i := 0; i < len(x); i++ {
  v |= x[i] ^ y[i]
}
```

* HMAC-based key derivation function (HKDF)
* The pseudorandom function (PRF)

* Many major applications use a `MAC` with a
  random key in place of the *noncryptographic*
  hash function.
* This is the case for many programming languages
  (like Rust, Python).
* They all make use of `SipHash`, a poorly-named
  `MAC` optimized for short authentication tags,
  with a random key generated
  at the start of the program.

* The most widely used `MAC` is `HMAC` (for *hash-based MAC*),
invented in 1996, and specified in `RFC 2104`.
  - It first creates two keys from the main key.
  - It then concatenates a key, `k1`,
    with the message and hashes it.
  - The result is concatenated with a key, `k2`,
    and hashed one more time.
  - This produces the final authentication tag.

> Because `HMAC` is customizable, the size of its
  *authentication tag* is dictated by the
  hash function used.

* `KMAC` is simply a wrapper around `cSHAKE`.
  To use a `key`, it encodes (in a unambiguous way)
  the *key*, the *input*, and the *output length*
  as the `input` to `cSHAKE`.

* `SHA-2` has an *annoying peculiarity*:
  - From a digest over an input, one can compute
    the digest of an input and more.
* This vulnerability allows one to continue
  hashing from a given digest, like the
  operation was not finished.
  - **length-extension attack**
  - one **should never** hash secrets with `SHA-2`

## Authenticated encryption

* The Advanced Encryption Standard (**AES**) block cipher

> *Bit security* is an *upper bound*

* The interface of `AES` for encryption:
  - The algorithm takes a *variable-length key*.
  - It also takes a *plaintext* of exactly `128` bits.
  - It outputs a *ciphertext* of exactly `128` bits.
  - Because `AES` encrypts a *fixed-size* plaintext,
    we call it a **block cipher**.

* In technical terms, a *block cipher*
  with a *key* is a **permutation**:
  - it maps all the possible *plaintexts* to
    all the possible *ciphertexts*.
  - Changing the *key* changes that *mapping*.
  - A *permutation* is also *reversible*.

* **AES**, which behave like *permutations*
  and are *randomized* by a *key*.
* We say that they are
  *pseudorandom permutations* (**PRPs**).

* When entering the `AES` algorithm,
  a plaintext of *16 bytes* gets transformed
  into a `4-by-4` matrix.
* This state is then encrypted and finally
  transformed into a `16-byte` ciphertext.
* `AES` iterates a **round function** over
  a state in order to encrypt it.
* The *round function* takes several
  arguments including a secret key.
* Each call to the *round function*
  transforms the state further, eventually
  producing the ciphertext.
* Each *round* uses a *different round key*,
  which is derived *from the main symmetric key*
  (*key schedule*).
* This allows the *slightest change* in the bits
  of the symmetric key to give a
  *completely different encryption*
  (a principle called *diffusion*).

> The *slightest change* in the plaintext also
  returns a *completely different ciphertext*.
  This principle is called the **avalanche effect**.

* There are several ways to specify how to
  choose these padding bytes, but the most important
  aspect of padding is that it must be reversible.
* Once we decrypt ciphertext, we should be able
  to remove the padding to retrieve
  the original unpadded message.

* `PKCS#7` padding specifies one rule:
  - the value of each padding byte must be
    set to the length of the required padding.
* What if the plaintext is already 16 bytes?
  - Then we add a full block of padding
    set to the value 16.
* To remove the padding, you can easily check
  the value of the last byte of plaintext and
  interpret it as the length of padding to remove.

* The electronic codebook (**ECB**) mode of operation.
  - As you learned, encryption is deterministic,
    and so encrypting the same block of plaintext
    twice leads to the same ciphertext.
  - This means that by encrypting each block
    *individually*, the resulting ciphertext
    might have *repeating patterns*.
  - The famous ECB penguin is an encryption
    of an image of a penguin using the
    electronic codebook (ECB) mode of operation.
  - As ECB does not hide repeating patterns,
    one can guess just by looking at the
    ciphertext what was originally encrypted.

* To encrypt more than 128 bits of plaintext safely,
  better modes of operation exist that
  "randomize" the encryption.
* One of the most popular modes of operation for
  AES is *cipher block chaining* (**CBC**).
* *CBC* works for any deterministic block cipher
  (not just AES) by taking an additional value
  called an *initialization vector* (**IV**)
  to randomize the encryption.
  - Because of this, the `IV` is the length of
    the block size (16 bytes for AES) and
    must be random and unpredictable.
* To decrypt with the CBC mode of operation,
  reverse the operations.
* As the `IV` is needed, it must be transmitted
  in clear text along with the ciphertext.

> When an `IV` repeats or is *predictable*,
  the encryption becomes *deterministic* again,
  and a number of clever **attacks** become possible.

* We then apply the `MAC` after *padding* the *plaintext*
  and *encrypting* it over *both* the ciphertext
  and the IV; otherwise, an attacker can still modify
  the IV without being caught.
  - This construction is called `Encrypt-then-MAC`.
  - The alternatives (like `MAC-then-Encrypt`) can
    sometimes lead to clever attacks and are
    thus **avoided** in practice.
  - In addition, it is best practice to use
    *different keys* for `AES` and `HMAC`.

* All-in-one constructions: Authenticated encryption
  - `AES-GCM`
  - `ChaCha20-Poly1305`

* The `AES-GCM` AEAD (authenticated encryption with associated data)
  - It was designed for high performance by taking advantage of
    hardware support for AES and by using a MAC (GMAC)
    that can be implemented efficiently.
  - `AES-GCM` combines the *Counter* (`CTR`) mode of operation
    with the `GMAC` message authentication code.
  - `AES-CTR` uses AES to encrypt a nonce concatenated
    with a number instead of the plaintext.
  - The *nonce* of `AES-GCM` is sometimes
    referred to as an `IV`.
  - The *nonce* in `AES-CTR` is `96` bits (`12` bytes)
    and takes *most* of the `16` bytes to be encrypted.
  - The `32` bits (`4` bytes) left serves as a counter,
    starting from `1` and incremented for each block
    encryption until it reaches its maximum value.
  - This means that, at most, `4,294,967,295` blocks
    of `128` bits can be encrypted with the
    *same nonce* (so less than `69` GBs).

* an interesting aspect of `CTR` mode:
  - no padding is required.
* We say that it turns a block cipher (`AES`)
  into a stream cipher.
* It encrypts the plaintext byte by byte.

* By default, encryption *doesn't* hides
  the length of what you are encrypting.
* Because of this, the use of compression before
  encryption can lead to attacks if an attacker
  can influence parts of what is being encrypted.

* `GMAC` is effectively the encryption of the
  `GHASH` output with `AES-CTR` (and a different key).
* Again, the nonce must be *unique*.

* `AES-GCM` works by using `AES-CTR` with a
  symmetric key *K* to encrypt the plaintext
  and by using `GMAC` to authenticate the
  *associated data* and the *ciphertext* using
  an authentication key *H*.

* `ChaCha20-Poly1305`
  - It is the combination of two algorithms:
    the `ChaCha20` stream cipher and the
    `Poly1305 MAC`.
  - In 2013, Google standardized the
    `ChaCha20-Poly1305` AEAD in order to make
    use of it in *Android* mobile phones
    relying on low-end processors.
  - Nowadays, it is widely adopted by internet
    protocols like *OpenSSH*, *TLS*, and *Noise*.
  - `ChaCha20` is a modification of
    the `Salsa20` stream cipher
  - `ChaCha20` works by taking a symmetric key
    and a unique nonce. It then generates a
    keystream that is `XORed` with the plaintext
    (or ciphertext) to produce the ciphertext
    (or plaintext).
    The encryption is *length-preserving* as
    the ciphertext and the plaintext are
    of the same length.
  - While allowing a large number of messages
    to be encrypted under a single key, other
    standards like `XChaCha20-Poly1305`
    are available.

* `Poly1305` is a `MAC` created via the
  *Wegman-Carter* technique, much like the
  `GMAC` we previously talked about.
* Eventually, we can use `ChaCha20` and a
  counter set to `0` to generate a keystream
  and derive the `16-byte` *r* and `16-byte` *s*
  values we need for `Poly1305`.

* `ChaCha20-Poly1305` works by using `ChaCha20`
  to encrypt the plaintext and to derive the
  keys required by the *Poly1305 MAC*.
* `Poly1305` is then used to authenticate the
  ciphertext as well as the associated data.

## Key exchanges

> A *key exchange* between two participants allows
  them to agree on a *secret key*, while a
  `man-in-the-middle` (**MITM**) adversary can't derive
  the same *secret key* from passively
  observing the key exchange.

* The *key exchange* is **unauthenticated**!
  - An *unauthenticated key exchange* is vulnerable
    to an active `MITM` attacker.
  - Indeed, the attacker can simply impersonate
    both sides of the connection and perform
    two separate key exchanges.

> By the way, when both sides are *authenticated*,
  we call that a *mutually authenticated key exchange*.

* While *key exchanges* are useful, they do not
  scale well in all scenarios without their
  sister primitive: the *digital signature*.

> `X25519` key exchange algorithm

* The `Diffie-Hellman` (**DH**) key exchange

* **Group theory**
  - The DH key exchange is built on top of
    a field of mathematics called *group theory*,
    which is the base of most public key
    cryptography today.
  - Note that DH works in a *multiplicative* group:
    a group where the *multiplication* is used
    as the defined binary operation.

* The four properties of a **group**:
  *closure*, *associativity*, *identity* element,
  and *inverse* element.
  - *Closure*: Operating on two elements results
    in another element of the same set.
  - *Associativity*: Operating on several elements
    at a time can be done in any order.
  - *Identity element*: Operating with this element
    does not change the result of the other operand.
  - *Inverse element*: Existing as an inverse to
    all group elements.

> To speed things up, most cryptographic libraries
  will instead look for pseudo-primes (numbers that
  have a high probability of being primes).

* `DH` uses the *modular multiplication* as
  a special operation.
  - `3×2 = 6`
  - `3×2 mod 5 = 1`
  - $$ 3^{-1} mod 5 = 2 $$

> When the context is clear, the modulus part
  is often left out from equations.

* We now have a group, which includes the set
  of strictly positive integers `1, 2, ..., p-1`
  for `p` a prime number, along with
  *modular multiplication*.
* The group we formed also happens to be two things:
  - *Commutative*: The order of operations doesn't matter.
    A group that has this property is
    often called a *Galois group*.
  - *A finite field*: A *Galois group* that has more
    properties, as well as an additional operation.

* `DH` defined over this type of group is sometimes
  called `Finite Field Diffie-Hellman` (**FFDH**).
* A *subgroup* is just a group contained inside
  your original group. That is, it's a subset of
  the group elements. Operating on elements of the
  *subgroup* results in another *subgroup* element,
  and every *subgroup* element has an *inverse*
  in the *subgroup*, etc.
* A *cyclic subgroup* is a *subgroup* that can be
  generated from a single generator (or base).
* A generator generates a *cyclic subgroup* by
  *multiplying* itself over and over.
* For example, the generator 4 defines a *subgroup*
  consisting of the numbers 1 and 4:
  - `4 mod 5 = 4`
  - `4×4 mod 5 = 1`
  - `4×4×4 mod 5 = 4`
  - `4×4×4×4 mod 5 = 1`

* It happens that when our modulus is *prime*,
  every element of our group is a generator
  of a subgroup.
* These different *subgroups* can have
  different *sizes*, which we call **orders**.

* A group is a set of numbers with a binary
  operation that respects some properties
  (*closure*, *associativity*,
  *identity element*, *inverse element*).
* DH works in the *Galois group*
  (a group with *commutativity*), formed by
  the set of strictly positive numbers up to
  a prime number (not included) and the
  *modular multiplication*.
* In a `DH` group, every element is a
  generator of a subgroup.

* The security of the `DH` key exchange relies
  on the *discrete logarithm problem* in a group,
  a problem believed to be hard to solve.

* [Diffie-Hellman key exchange](https://en.wikipedia.org/wiki/Diffie-Hellman_key_exchange)

* In general, https://www.keylength.com summarizes
  recommendations on parameter lengths for
  common cryptographic algorithms.
* Due to all of these issues, newer protocols and
  libraries have converged towards either *deprecating*
  `DH` in favor of *Elliptic Curve Diffie-Hellman*
  (**ECDH**) or using the groups defined in the better
  standard, [RFC 7919](https://www.rfc-editor.org/info/rfc7919).

* The **Elliptic Curve Diffie-Hellman** (*ECDH*) key exchange
  - Compared to the recommended `2,048-bit` parameters in **DH**,
    parameters of `256 bits` were possible with the
    elliptic curve variant of the algorithm.
  - elliptic curves are just curves!

* The **short Weierstrass equation**
  - $$ y^2 = x^3 + ax + b \, (Where \, 4a^3 + 27b^2 \neq 0) $$

* Groups over *elliptic curves* are often
  defined as additive groups.
* *Elliptic curve cryptography* (**ECC**), in practice,
  is mostly specified with *elliptic curves* in
  *coordinates modulo* a large prime number `p`.

* The group we formed on top of *elliptic curves*
  differs with the group we formed with the
  strictly positive integers modulo a prime number.
* Due to some of these differences, the strongest
  attacks known against DH (known as
  *index calculus or number field sieve attacks*)
  do not work well on the *elliptic curve* groups.
* This is the main reason why parameters for `ECDH`
  can be much lower than the parameters for `DH`
  at the same level of security.
* Nowadays, most of the curves in use come from
  a couple standards, and most applications have
  fixated on two curves: **P-256** and **Curve25519**.
* `RFC 7748`, "*Elliptic Curves for Security*,"
  which was published in 2016, specifies two
  curves: **Curve25519** and **Curve448**.
* The combination of `ECDH` with **Curve25519**
  is often dubbed **X25519**.

> A *small subgroup attack* impacts `DH` groups
  that have many subgroups. By choosing generators
  of small subgroups as public keys, an attacker
  can leak bits of someone's private key
  little by little.

* If using `ECDH`, I would advise you to use
  the **X25519** key exchange due to the quality
  of the design (which takes into account
  invalid curve attacks), the quality of available
  implementations, and the resistance against
  timing attacks by design.
* **Curve25519** has one caveat though it is not
  a *prime-order group*. The curve has two subgroups:
  a small subgroup of size 8 and a large subgroup
  used for `ECDH`. On top of that, the original
  design did not prescribe validating received
  points, and libraries, in turn, did not implement
  these checks. This led to issues being found in
  different types of protocols that were making
  use of the primitive in more exotic ways.

## Asymmetric encryption and hybrid encryption

* In reality, asymmetric encryption is quite
  *limited* due to the restricted length
  of messages it can encrypt.

* Today, `RSA` is often *not the preferred way*
  of doing a key exchange, and it is being used
  *less and less* in protocols *in favor of*
  **Elliptic Curve Diffie-Hellman** (`ECDH`).

* In practice, *asymmetric encryption* can only
  encrypt messages up to *a certain length*.

* **ECIES**
  - The main standard to perform hybrid encryption
    with *Elliptic Curve Diffie-Hellman* (**ECDH**)

* Nowadays, most protocols and applications that
  use `RSA` either still implement the insecure
  `PKCS#1` `v1.5` or `OAEP`. On the other hand,
  more and more protocols are moving away from
  `RSA` encryption **in favor of**
  *Elliptic Curve Diffie-Hellman* (**ECDH**)
  for both *key exchanges* and *hybrid encryption*.

* First, if you want to encrypt a message
  to Alice, you use an `(EC)DH`-based key
  exchange with Alice's public key and a
  key pair that you generate for the occasion
  (this is called an ephemeral key pair).
* After this, you can send the ephemeral
  public key and the ciphertext to Alice.
  Alice can use your ephemeral public key
  to perform a key exchange with
  her own key pair.

## Signatures and zero-knowledge proofs

* Only you can use your signature to sign arbitrary messages.
* Anybody can verify your signature on a message.

* A signature scheme typically consists of
  *three different algorithms*:
  - A *key pair generation algorithm* that
    a signer uses to create a new private
    and public key (the public key can
    then be shared with anyone).
  - A *signing algorithm* that takes a
    private key and a message to
    produce a signature.
  - A *verifying algorithm* that takes a
    public key, a message, and a signature
    and returns a success or error message.

* What are signatures good for? They are good for
  *authenticating the origin* of a message
  *as well as the integrity* of a message:
  - **Origin**:
  - If my signature is on it, it came from me.
  - **Integrity**:
  - If someone modifies the message, it voids the signature.

* *Key exchanges* didn't fully solve the problem
  of setting up a secure connection between two
  participants as an active **man-in-the-middle** (MITM)
  attacker can trivially impersonate both sides of a
  *key exchange*. This is where *signatures*
  enter the ring.

* **Public key infrastructures**
  - *Transitivity of trust* allows you to scale trust
    in systems in extreme ways.

* **Zero-knowledge proofs** (ZKPs):
  - The origin of signatures
* **Schnorr identification protocol**:
  - An **interactive** *zero-knowledge proof*

* So-called *interactive* ZKP systems that
  follow a three-movement pattern
  (*commitment*, *challenge*, and *proof*)
  are often referred to as *Sigma protocols*.

* The *Schnorr identification protocol* is an
  **interactive** ZKP that is complete
  (Peggy can prove she knows some witness),
  sound (Peggy cannot prove anything if she
  doesn't know the witness), and zero-knowledge
  (Victor learns nothing about the witness).
  - Peggy: I'll prove that I know `x` in $$ Y = g^{x} \mod p $$
  - Peggy: Here's a *commitment* of a
    random value $$ R = g^k $$
  - Victor: Here's a random challenge `c`
  - Peggy: Here's a *hidden witness* $$ s = k + c \times x $$
  - Victor: Indeed, $$ g^s = Y^{c} \times R $$

> - Signatures as `non-interactive` *zero-knowledge proofs*

* In 1986, Amos Fiat and Adi Shamir published a
  technique that allowed one to easily convert
  an *interactive* ZKP *into* a *non-interactive* ZKP.
* The trick they introduced (referred to as the Fiat-Shamir
  heuristic or Fiat-Shamir transformation) was to
  make the prover compute the challenge themselves,
  in a way they can't control.
* Compute the challenge as a hash of all the messages
  sent and received as part of the protocol up to
  that point (which we call the *transcript*).
* If we assume that the hash function gives outputs
  that are indistinguishable from truly-random numbers
  (in other words, it looks random), then it can
  successfully simulate the role of the verifier.
* *Digital signatures* are just *non-interactive* ZKPs.
  Applying the *Fiat-Shamir transform* to the
  *Schnorr identification protocol*, we obtain the
  *Schnorr signature scheme*.

* **Schnorr signature**
  - *Commitment*: $$ R = g^k $$
  - *"Random" challenge*: $$ c = HASH(R, msg) $$
  - *Hidden witness*: $$ s = k + c \times x $$

* A *Schnorr signature* is essentially two values,
  `R` and `s`, where `R` is a *commitment* to some
  secret random value (which is often called a
  *nonce* as it needs to be unique per signature),
  and `s` is a value computed with the help of
  the *commitment* `R`, the private key
  (the witness `x`), and a message.

## Randomness and secrets

## Secure transport

## End-to-end encryption

## User authentication

## Crypto as in cryptocurrency?

## Hardware cryptography

## Post-quantum cryptography

## Is this it? Next-generation cryptography

## When and where cryptography fails
