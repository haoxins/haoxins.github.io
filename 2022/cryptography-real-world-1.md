---
title: Real-World Cryptography (上)
description: 白露横江, 水光接天. 纵一苇之所如, 凌万顷之茫然.
date: 2021-09-10
---

* [Real-World Cryptography](https://book.douban.com/subject/34615742/)
  - https://www.manning.com/books/real-world-cryptography

## Introduction

> The slightest mistake could be deadly.

```
While a typical cryptography book usually
starts with the discovery of cryptography
and takes you through its history, I think
that it makes little sense for me to
kick off things that way.

I want to tell you about the practical.
```

* Kerckhoff's principle:
  - Only the key is kept secret

* **Asymmetric cryptography**:
  - Two keys are better than one
  - key exchange: Diffie-Hellman (**DH**)
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
  - __Math-based constructions__
  - These rely on mathematical problems like
    factoring numbers.
  - __Heuristic-based constructions__
  - These rely on observations and statistical
    analysis by cryptanalysts.
  - AES for symmetric encryption is an
    example of such a construction.
* Symmetric constructions are most often
  based on heuristics, while most asymmetric
  constructions are based on mathematical problems.

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

> There are other ways to encode binary data
  for human consumption, but the two most
  widely used encodings are
  **hexadecimal** and **base64**.

* Security properties of a hash function
  - The **first** one is `pre-image resistance`.
  - No one should be able to reverse the
    hash function in order to recover
    the input given an output.
  - But you can't hide something that is
    too small or that is predictable.
  - The **second** property is
    `second pre-image resistance`.
  - You should not be able to find a different
    input that hashes to the same digest.
  - The **third** property is `collision resistance`.
  - No one should be able to produce two different
    inputs that hash to the same output.

> in practice impossible
  but not theoretically impossible.

* There is a `minimum` output size that a hash
  function must produce in practice:
  `256 bits` (or `32 bytes`).
* For a hash function to provide all three
  security properties mentioned earlier, it needs
  to provide at least `128 bits` of security
  against all three attacks.
* If our hash function generates random outputs of
  `256` bits, the space of all outputs is of size
  $$ 2^{256} $$.
* This means that collisions can be found with
  good probability after generating
  $$ 2^{128} $$
  digests (due to the `birthday bound`).
* In order to achieve `128-bit` security at a minimum,
  a digest must not be truncated under:
  - `256 bits` for __collision resistance__
  - `128 bits` for __pre-image__ and
    __second pre-image resistance__

> `CRC32` are __not__ cryptographic hash functions
  __but__ `error-detecting` code functions.

* `MD5` and `SHA-1` were shown to be __broken__
  in 2004 and 2016.
* `SHA-2` is based on the `Merkle-Damgard` construction,
  while `SHA-3` is based on the `sponge` construction.
* `SHA-2` provides `4` different versions, producing
  outputs of `224`, `256`, `384`, or `512` bits.

* While there are different ways of building
  a compression function, `SHA-2` uses the
  `Davies-Meyer` method, which relies on a
  block cipher.
* The `Merkle-Damgard` construction iteratively
  applies a compression function to each block
  of the input to be hashed and the output of
  the previous compression function.
  - The final call to the compression function
    directly returns the digest.

* While `SHA-2` is a perfectly fine hash function
  to use, it is **not** suitable for **hashing secrets**.
  - This is because of a downside of the `Merkle-Damgard`
    construction, which makes `SHA-2` vulnerable to
    an attack (called a `length-extension attack`)
    if used to hash secrets.
* Because of this, and the fact that `SHA-2` is vulnerable
  to `length-extension attacks`, NIST decided in 2007 to
  organize an open competition for a new standard:
  - `SHA-3`.
* `SHA-3` is a cryptographic algorithm
  built on top of a permutation.
  - `SHA-3` is based on a particular permutation called
    `keccak-f` that takes an input and returns
    an output of the same size.

---

* Cryptographic protocols often necessitate this
  type of primitives but do not want to be
  constrained by the fixed sizes of
  a hash function's digest.
  - For this reason, the `SHA-3` standard introduced
    a more versatile primitive called an
    `extendable output function` or __XOF__.
* This section introduces the two standardized XOFs:
  - `SHAKE` and `cSHAKE`.
* **`SHAKE`**, specified in FIPS 202 along with `SHA-3`,
  can be seen as a hash function that returns
  an output of an arbitrary length.
* **`cSHAKE`** is pretty much exactly like `SHAKE`,
  except that it also takes a customization string.
* **`TupleHash`**, which is based on `cSHAKE` and
  specified in the same standard as `cSHAKE`.
* **`TupleHash`** is an interesting function
  that allows one to hash a tuple.

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
  - This issue has been commonly solved by using
    **salts**, which in some sense is like using
    a per-user customization string with `cSHAKE`.
  - It effectively creates a different
    hash function for every user.
* Hash functions are supposed to be as fast.
  Attackers can leverage this to brute force
  (many, many passwords per second).
  - This issue is solved with **password hashes**,
    which are designed to be slow.
  - The current state-of-the-art
    choice for this is `Argon2`.

* [RFC 9106](https://datatracker.ietf.org/doc/rfc9106/)
  - Argon2 Memory-Hard Function for
    Password Hashing and Proof-of-Work Applications

## Message authentication codes

* Mix a `hash` function with a `secret` key and
  you obtain something called a
  `message authentication code` (**MAC**),
  a cryptographic primitive to
  protect the **integrity** of data.

* **`HMAC`** is a message authentication code
  that uses a hash function at its core.
  - It is compatible with different hash functions,
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
  on a `never-seen-before` message by themselves.

* If you are trying to authenticate __structures__,
  make sure to __serialize__ them before
  authenticating them with a `MAC`;
  - otherwise, __forgery might be trivial__.

* Remember, finding a collision for a
  `hash function` means finding two different
  inputs `X` and `Y` such that `HASH(X) = HASH(Y)`.
* We can extend this definition to `MACs` by
  defining a collision when `MAC(k, X) = MAC(k, Y)`
  for inputs `X` and `Y`.

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

> The pseudorandom function (PRF)

* Many major applications use a `MAC` with a
  random key in place of the noncryptographic
  hash function.
  - This is the case for many programming languages
    (like Rust, Python).
* They all make use of `SipHash`, a poorly-named
  `MAC` optimized for short authentication tags,
  with a random key generated at the start of the program.

* The most widely used `MAC` is __HMAC__ (for `hash-based MAC`),
  invented in 1996, and specified in `RFC 2104`.
  - It first creates two keys from the main key.
  - It then concatenates a key, `k1`,
    with the message and hashes it.
  - The result is concatenated with a key, `k2`,
    and hashed one more time.
  - This produces the final authentication tag.

> Because `HMAC` is customizable, the size of its
  authentication tag is dictated by the
  hash function used.

* `KMAC` is simply a wrapper around `cSHAKE`.
  To use a key, it encodes (in a unambiguous way)
  the `key`, the `input`, and the `output length`
  as the input to cSHAKE.

* `SHA-2` has an `annoying peculiarity`:
  - From a digest over an input, one can compute
    the digest of an input and more.
* This **vulnerability** allows one to continue
  hashing from a given digest, like the
  operation was not finished.
  - **length-extension attack**
  - one **should never** hash secrets with `SHA-2`

## Authenticated encryption

* The Advanced Encryption Standard (**AES**) block cipher

> `Bit security` is an upper bound

* The interface of `AES` for encryption:
  - The algorithm takes a `variable-length key`.
  - It also takes a plaintext of exactly `128` bits.
  - It outputs a ciphertext of exactly `128` bits.
  - Because `AES` encrypts a `fixed-size` plaintext,
    we call it a **block cipher**.

* In technical terms, a block cipher
  with a key is a **permutation**:
  - it maps all the possible plaintexts to
    all the possible ciphertexts.
  - Changing the `key` changes that `mapping`.
  - A permutation is also `reversible`.

* **AES**, which behave like permutations
  and are randomized by a key.
  - We say that they are
    `pseudorandom permutations` (**PRPs**).

* When entering the `AES` algorithm,
  a plaintext of `16 bytes` gets transformed
  into a `4-by-4` matrix.
  - This state is then encrypted and finally
    transformed into a `16-byte` ciphertext.
* `AES` iterates a **round function** over
  a state in order to encrypt it.
* The `round function` takes several
  arguments including a secret key.
  - Each call to the round function
    transforms the state further, eventually
    producing the ciphertext.
  - Each `round` uses a different round key,
    which is derived from the main symmetric key
    (key schedule).
* This allows the __slightest change__ in the bits
  of the symmetric key to give a
  __completely different__ encryption
  (a principle called __`diffusion`__).

> The slightest change in the plaintext also
  returns a completely different ciphertext.
  This principle is called the **avalanche effect**.

---

* There are several ways to specify how to
  choose these padding bytes, but the most important
  aspect of padding is that it must be __reversible__.
  - Once we decrypt ciphertext, we should be able
    to remove the padding to retrieve
    the original unpadded message.

* `PKCS#7` padding specifies one rule:
  - the value of each padding byte must be
    set to the length of the required padding.
* What if the plaintext is already `16` bytes?
  - Then we add a full block of padding
    set to the value `16`.
* To remove the padding, you can easily check
  the value of the last byte of plaintext and
  interpret it as the length of padding to remove.

* The electronic codebook (__ECB__) mode of operation.
  - As you learned, encryption is deterministic,
    and so encrypting the same block of plaintext
    twice leads to the same ciphertext.
  - This means that by encrypting each block
    individually, the resulting ciphertext
    might have __repeating patterns__.
  - The famous ECB penguin is an encryption
    of an image of a penguin using the
    electronic codebook (__ECB__) mode of operation.
  - As ECB does not hide __repeating patterns__,
    one can guess just by looking at the
    ciphertext what was originally encrypted.

* To encrypt more than `128` bits of plaintext safely,
  better modes of operation exist that
  `"randomize"` the encryption.
* One of the most popular modes of operation for
  AES is `cipher block chaining` (**CBC**).
* **CBC** works for any deterministic block cipher
  (not just AES) by taking an additional value
  called an `initialization vector` (**IV**)
  to randomize the encryption.
  - Because of this, the `IV` is the length of
    the block size (`16` bytes for AES) and
    must be __random__ and __unpredictable__.
  - To decrypt with the CBC mode of operation,
    reverse the operations.
  - As the `IV` is needed, it must be transmitted
    in clear text along with the ciphertext.

> When an `IV` repeats or is __predictable__,
  the encryption becomes __deterministic__ again,
  and a number of clever attacks become possible.

* We then apply the `MAC` after padding the plaintext
  and encrypting it over __both__ the ciphertext
  and the `IV`; otherwise, an attacker can still modify
  the `IV` without being caught.
  - This construction is called `Encrypt-then-MAC`.
  - The alternatives (like `MAC-then-Encrypt`) can
    sometimes lead to clever attacks and are
    thus **avoided** in practice.
  - In addition, it is best practice to use
    different keys for `AES` and `HMAC`.

* All-in-one constructions: Authenticated encryption
  - `AES-GCM`
  - `ChaCha20-Poly1305`

* The `AES-GCM` __AEAD__ (`authenticated encryption with associated data`)
  - It was designed for high performance by taking advantage of
    hardware support for AES and by using a MAC (`GMAC`)
    that can be implemented efficiently.
- `AES-GCM` combines the `Counter` (`CTR`) mode of operation
  with the `GMAC` message authentication code.
- `AES-CTR` uses `AES` to encrypt a nonce concatenated
  with a number instead of the plaintext.
  - The nonce of `AES-GCM` is sometimes
    referred to as an `IV`.
  - The nonce in `AES-CTR` is `96` bits (`12` bytes)
    and takes most of the `16` bytes to be encrypted.
  - The `32` bits (`4` bytes) left serves as a counter,
    starting from `1` and incremented for each block
    encryption until it reaches its maximum value.
  - This means that, at most, `4,294,967,295` blocks
    of `128` bits can be encrypted with the
    same nonce (so less than `69` GBs).

* An interesting aspect of `CTR` mode:
  - __no padding is required__.
* We say that it turns a block cipher (`AES`)
  into a stream cipher.
  - It encrypts the plaintext byte by byte.

* By default, encryption __doesn't__ hides
  the length of what you are encrypting.
  - Because of this, the use of compression before
    encryption can lead to attacks if an attacker
    can influence parts of what is being encrypted.

* `GMAC` is effectively the encryption of the
  `GHASH` output with `AES-CTR` (and a different key).
  - Again, the __nonce must be unique__.

* `AES-GCM` works by using `AES-CTR` with a
  symmetric key `K` to encrypt the plaintext
  and by using `GMAC` to authenticate the
  associated data and the ciphertext using
  an authentication key `H`.

---

* `ChaCha20-Poly1305`
  - It is the combination of two algorithms:
    the `ChaCha20` stream cipher and the
    `Poly1305` MAC.
  - In 2013, Google standardized the
    `ChaCha20-Poly1305` __AEAD__ in order to make
    use of it in Android mobile phones
    relying on low-end processors.
  - Nowadays, it is widely adopted by internet
    protocols like OpenSSH, TLS, and Noise.
  - `ChaCha20` is a modification of
    the `Salsa20` stream cipher
- `ChaCha20` works by taking a symmetric key
  and a unique nonce. It then generates a
  keystream that is `XORed` with the plaintext
  (or ciphertext) to produce the ciphertext
  (or plaintext).
  - The encryption is `length-preserving` as
    the ciphertext and the plaintext are
    of the same length.
  - While allowing a large number of messages
    to be encrypted under a single key, other
    standards like `XChaCha20-Poly1305`
    are available.

* `Poly1305` is a `MAC` created via the
  Wegman-Carter technique, much like the
  `GMAC` we previously talked about.
* Eventually, we can use `ChaCha20` and a
  counter set to `0` to generate a keystream
  and derive the 16-byte `r` and 16-byte `s`
  values we need for `Poly1305`.

* `ChaCha20-Poly1305` works by using `ChaCha20`
  to encrypt the plaintext and to derive the
  keys required by the `Poly1305` MAC.
  - `Poly1305` is then used to authenticate the
    ciphertext as well as the associated data.

## Key exchanges

> A key exchange between two participants allows
  them to agree on a secret key, while a
  `man-in-the-middle` (**MITM**) adversary can't derive
  the same secret key from passively
  observing the key exchange.

* The key exchange is **unauthenticated**!
  - An unauthenticated key exchange is vulnerable
    to an active `MITM` attacker.
  - Indeed, the attacker can simply impersonate
    both sides of the connection and perform
    two separate key exchanges.

> By the way, when both sides are __authenticated__,
  we call that a `mutually authenticated key exchange`.

* While key exchanges are useful, they do not
  scale well in all scenarios without their
  sister primitive:
  - the digital signature.

> `X25519` key exchange algorithm

---

* The `Diffie-Hellman` (**DH**) key exchange

* **Group theory**
  - The DH key exchange is built on top of
    a field of mathematics called group theory,
    which is the base of most public key
    cryptography today.
  - Note that DH works in a `multiplicative` group:
    a group where the `multiplication` is used
    as the defined binary operation.

* The four properties of a **group**:
  `closure`, `associativity`, `identity` element,
  and `inverse` element.
  - __Closure__: Operating on two elements results
    in another element of the same set.
  - __Associativity__: Operating on several elements
    at a time can be done in any order.
  - __Identity element__: Operating with this element
    does not change the result of the other operand.
  - __Inverse element__: Existing as an inverse to
    all group elements.

> To speed things up, most cryptographic libraries
  will instead look for pseudo-primes (numbers that
  have a high probability of being primes).

* `DH` uses the modular multiplication as
  a special operation.
  - $$ 3 × 2 = 6 $$
  - $$ 3 × 2 \mod 5 = 1 $$
  - $$ 3^{-1} \mod 5 = 2 $$

> When the context is clear, the modulus part
  is often left out from equations.

* We now have a group, which includes the set
  of strictly positive integers `1, 2, ..., p - 1`
  for `p` a prime number, along with
  modular multiplication.
* The group we formed also happens to be two things:
  - __Commutative__: The order of operations doesn't matter.
    A group that has this property is
    often called a `Galois` group.
  - __A finite field__: A `Galois` group that has more
    properties, as well as an additional operation.

* `DH` defined over this type of group is sometimes
  called `Finite Field Diffie-Hellman` (**FFDH**).
* A `subgroup` is just a group contained inside
  your original group.
  - That is, it's a subset of the group elements.
  - Operating on elements of the subgroup results in
    another subgroup element,
  - and every subgroup element has an inverse
    in the subgroup, etc.
* A `cyclic subgroup` is a subgroup that can be
  generated from a single generator (or base).
* A generator generates a `cyclic subgroup` by
  multiplying itself over and over.
* For example, the generator `4` defines a subgroup
  consisting of the numbers `1` and `4`:
  - `4 mod 5 = 4`
  - `4 × 4 mod 5 = 1`
  - `4 × 4 × 4 mod 5 = 4`
  - `4 × 4 × 4 × 4 mod 5 = 1`

* It happens that when our modulus is __prime__,
  every element of our group is a generator
  of a subgroup.
  - These different subgroups can have
    different sizes, which we call __orders__.

---

* A group is a set of numbers with a binary
  operation that respects some properties
  - closure,
  - associativity,
  - identity element,
  - inverse element.
* DH works in the `Galois` group
  (a group with `commutativity`), formed by
  the set of strictly positive numbers up to
  a prime number (not included) and the
  modular multiplication.
  - In a `DH` group, every element is a
    generator of a subgroup.

* The security of the `DH` key exchange relies
  on the __discrete logarithm problem__ in a group,
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

---

* The `Elliptic Curve Diffie-Hellman` (**ECDH**) key exchange
  - Compared to the recommended `2,048-bit` parameters in **DH**,
    parameters of `256 bits` were possible with the
    elliptic curve variant of the algorithm.
  - elliptic curves are just curves!

* The **short Weierstrass equation**
  - $$ y^2 = x^3 + ax + b \, (Where \, 4a^3 + 27b^2 \neq 0) $$

* Groups over elliptic curves are often
  defined as `additive groups`.
* `Elliptic curve cryptography` (**ECC**), in practice,
  is mostly specified with elliptic curves in
  coordinates modulo a large prime number `p`.

* The group we formed on top of elliptic curves
  __differs__ with the group we formed with the
  strictly positive integers modulo a prime number.
  - Due to some of these differences, the strongest
    attacks known against `DH` (known as
    index calculus or number field sieve attacks)
    do not work well on the elliptic curve groups.
  - This is the main reason why parameters for `ECDH`
    can be __much lower than__ the parameters for `DH`
    at the same level of security.
* Nowadays, most of the curves in use come from
  a couple standards, and most applications have
  fixated on two curves:
  - **P-256**
  - and **Curve25519**.
* `RFC 7748`, "Elliptic Curves for Security,"
  which was published in 2016, specifies two curves:
  - **Curve25519**
  - and **Curve448**.
* The combination of `ECDH` with **Curve25519**
  is often dubbed **X25519**.

> A small subgroup attack impacts `DH` groups
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
  a `prime-order group`.
  - The curve has two subgroups:
  - a small subgroup of size `8` and a large subgroup
    used for `ECDH`.
  - On top of that, the original design did not
    prescribe validating received points,
    and libraries, in turn, did not implement
    these checks.
  - This led to issues being found in different types
    of protocols that were making use of
    the primitive in more exotic ways.

## Asymmetric encryption and hybrid encryption

* In reality, asymmetric encryption is quite
  limited due to the restricted length
  of messages it can encrypt.

* Today, `RSA` is often not the preferred way
  of doing a key exchange, and it is being used
  less and less in protocols **in favor of**
  **Elliptic Curve Diffie-Hellman** (`ECDH`).

* In practice, asymmetric encryption can only
  encrypt messages up to a certain length.

* **ECIES**
  - The main standard to perform hybrid encryption
    with `Elliptic Curve Diffie-Hellman` (**ECDH**)

* Nowadays, most protocols and applications that
  use `RSA` either still implement the insecure
  `PKCS#1` v1.5 or `OAEP`.
  - On the other hand, more and more protocols
    are moving away from `RSA` encryption
    **in favor of** `Elliptic Curve Diffie-Hellman`
    (**ECDH**) for both key exchanges
    and hybrid encryption.

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
  - Anybody can verify your signature on a message.

* A signature scheme typically consists of
  __three__ different algorithms:
  - A `key pair generation algorithm` that
    a signer uses to create a new private
    and public key (the public key can
    then be shared with anyone).
  - A `signing algorithm` that takes a
    private key and a message to
    produce a signature.
  - A `verifying algorithm` that takes a
    public key, a message, and a signature
    and returns a success or error message.

* What are signatures good for? They are good for
  authenticating the origin of a message
  as well as the integrity of a message:
  - **Origin**:
  - If my signature is on it, it came from me.
  - **Integrity**:
  - If someone modifies the message, it voids the signature.

* Key exchanges didn't fully solve the problem
  of setting up a secure connection between two
  participants as an active `man-in-the-middle` (__MITM__)
  attacker can trivially impersonate both sides of a
  key exchange.
  - This is where signatures enter the ring.

* **Public key infrastructures**
  - `Transitivity of trust` allows you to scale trust
    in systems in extreme ways.

* **Zero-knowledge proofs** (ZKPs):
  - The origin of signatures
* **Schnorr identification protocol**:
  - An **interactive** zero-knowledge proof

* So-called interactive ZKP systems that
  follow a three-movement pattern
  (`commitment`, `challenge`, and `proof`)
  are often referred to as `Sigma` protocols.

---

* The `Schnorr identification protocol` is an
  **interactive** ZKP that is complete
  (Peggy can prove she knows some witness),
  sound (Peggy cannot prove anything if she
  doesn't know the witness), and zero-knowledge
  (Victor learns nothing about the witness).
  - Peggy: I'll prove that I know `x` in
    $$ Y = g^{x} \mod p $$
  - Peggy: Here's a `commitment` of a
    random value
    $$ R = g^k $$
  - Victor: Here's a random challenge `c`
  - Peggy: Here's a `hidden witness`
    $$ s = k + c \times x $$
  - Victor: Indeed,
    $$ g^s = Y^{c} \times R $$

> Signatures as `non-interactive` zero-knowledge proofs

* In 1986, Amos Fiat and Adi Shamir published a
  technique that allowed one to easily convert
  an `interactive` ZKP into a `non-interactive` ZKP.
* The trick they introduced (referred to as the Fiat-Shamir
  heuristic or Fiat-Shamir transformation) was to
  make the prover compute the challenge themselves,
  in a way they can't control.
* Compute the challenge as a hash of all the messages
  sent and received as part of the protocol up to
  that point (which we call the `transcript`).
* If we assume that the hash function gives outputs
  that are indistinguishable from truly-random numbers
  (in other words, it looks random), then it can
  successfully simulate the role of the verifier.
* Digital signatures are just non-interactive ZKPs.
  - Applying the Fiat-Shamir transform to the
    Schnorr identification protocol, we obtain the
    Schnorr signature scheme.

---

* **Schnorr signature**
  - Commitment:
    $$ R = g^k $$
  - "Random" challenge:
    $$ c = HASH(R, msg) $$
  - Hidden witness:
    $$ s = k + c \times x $$

* A Schnorr signature is essentially two values,
  `R` and `s`, where `R` is a commitment to some
  secret random value (which is often called a
  `nonce` as it needs to be unique per signature),
  and `s` is a value computed with the help of
  the commitment `R`, the private key
  (the witness `x`), and a message.

---

* RSA `PKCS#1` v1.5:
  - A **bad** standard
* RSA for encryption was loosely standardized
  in the `PKCS#1` v1.5 document.
  - The same document contained a specification
    for signing with RSA (without a security proof).
* RSA was then standardized again in the
  `PKCS#1` v2 document with a better construction
  (called `RSA-OAEP`).
  - The same happened for RSA signatures with `RSA-PSS`
    being standardized in the same document
    (with a security proof).
* `RSA-PSS`: A **better** standard
  - `RSA-PSS` was standardized in the updated
    `PKCS#1` v2.1 and included a proof of security.
  - (1) Encode the message using the
    `PSS` encoding algorithm
  - (2) Sign the encoded message using RSA
    (as was done in the `PKCS#1` v1.5 standard)
  - `PSS` (for Probabilistic Signature Scheme) is
    provably secure, meaning that no one should be
    able to forge a signature without
    knowledge of the private key.

---

* The Elliptic Curve Digital Signature Algorithm
  (**ECDSA**)
  - An elliptic curve variant of DSA that was itself
    invented only to circumvent patents
    in Schnorr signatures.
  - Unfortunately, ECDSA, like DSA, does not come with
    a proof of security, __while Schnorr signatures did__.
  - The private key is a large number
    `x` generated randomly.
  - The public key is obtained by viewing `x` as
    an index in a group created by a generator
    (called base point in elliptic curve cryptography).

* The elliptic curves that tend to be used with
  **ECDSA** are pretty much the same curves that
  are popular with the Elliptic Curve Diffie-Hellman
  (**ECDH**) algorithm with one notable exception:
  - **Secp256k1**.
* **Secp256k1** is a type of elliptic curve called
  a Koblitz curve. A Koblitz curve is just an
  elliptic curve with some constraints in its
  parameters that allow implementations to
  optimize some operations on the curve.

---

* The Edwards-curve Digital Signature Algorithm
  (**EdDSA**)
  - EdDSA is actually based on Schnorr signatures
  - One particularity of EdDSA is that the scheme
    does not require new randomness for
    every signing operation.
  - EdDSA produces signatures deterministically.
  - EdDSA is on track to be included in NIST's
    upcoming update for its `FIPS 186-5` standard
    (still a draft as of early 2021).
  - In practice, EdDSA is mostly instantiated with
    the `Edwards25519` curve and the combo is called
    `Ed25519` (whereas EdDSA with `Edwards448`
    is shortened as `Ed448`).
  - Key generation with EdDSA is a bit different
    from other existing schemes. Instead of generating
    a signing key directly, EdDSA generates a secret
    key that is then used to derive the actual
    signing key and another key that
    we call the nonce key.
  - __That nonce key is important!__ It is the one used
    to deterministically generate the
    required per signature nonce.
  - To sign, EdDSA first deterministically generates
    the nonce by hashing the nonce key with the
    message to sign. After that, a process similar
    to Schnorr signatures follows.

* EdDSA key generation produces a secret key
  that is then used to derive two other keys.
  - The first derived key is the actual signing
    key and can thus be used to derive
    the public key;
  - the other derived key is the nonce key,
    used to deterministically derive the nonce
    during signing operations.
* EdDSA signatures are then like Schnorr
  signatures with the exception that the nonce
  is generated deterministically from the nonce
  key and the message, and the public key of the
  signer is included as part of the challenge.

---

* The **most widely used** instantiation of
  EdDSA, Ed25519, is defined with the
  `Edwards25519` curve and the
  `SHA-512` as a hash function.

* Substitution attacks on signatures
  - Substitution attacks, also referred to as
    duplicate signature key selection (DSKS),
    are possible on both RSA `PKCS#1` v1.5
    and `RSA-PSS`.

## Randomness and secrets

* That being said, all of these factors impact the
  end result so much that a slight imprecision in
  the knowledge of the initial conditions would mess
  with our predictions.
  - The extreme sensitivity of an outcome to its
    initial conditions is known as **chaos theory**,
    and it is the reason why things like the weather
    are hard to predict accurately past
    a certain number of days.

* These hardware random number generators are often
  called true random number generators (TRNGs) as
  they make use of external unpredictable physical
  phenomena like thermal noise to extract randomness.
  - Randomness extractors must clean and gather several
    sources of noise together before it can be used for
    cryptographic applications.
* Extracting randomness from noise is a process that
  can be __slow__. For some applications that might need
  lots of random numbers quickly, it can become a
  bottleneck.

* pseudorandom number generator (**PRNG**)

* Obtaining unpredictable randomness is somewhat of a
  slow process. This is sometimes due to a source of
  entropy being slow to produce noise.
  - As a result, OSs often optimize their
    production of random numbers by using
    pseudorandom number generators (**PRNGs**).
* A pseudorandom number generator (PRNG) generates a
  sequence of random numbers based on a seed. Using the
  same seed makes the PRNG produce the same sequence
  of random numbers.
  - It should be impossible to recover the state using
    knowledge of the random outputs.
  - It follows that it should also be impossible from
    observing the produced random numbers alone to
    predict future random numbers or to
    recover previously generated random numbers.

* Cryptographically secure PRNGs usually tend
  to exhibit the following properties:
  - **Deterministic**: Using the same seed twice
    produces the same sequence of random numbers.
    This is why the construction is called
    pseudorandom, and this is what allows a
    PRNG to be extremely fast.
  - **Indistinguishable from random**: In practice,
    you should not be able to distinguish between a
    PRNG outputting a random number from a set of
    possible numbers and a little fairy impartially
    choosing a random number from the same set.
  - Consequently, observing the random numbers
    generated alone shouldn't allow anyone to
    recover the internal state of the PRNG.

* A PRNG has `forward` secrecy if compromise of
  a state does not allow recovering previously
  generated random numbers.
* A PRNG has `backward` secrecy if compromise of
  a state does not allow predicting future random
  numbers generated by the PRNG.
  - This is true only once new entropy is produced
    and injected in the update function
    after the compromise.

---

* Most (if not all) cryptographic applications do
  not use random numbers directly extracted from
  noise, but instead use them to seed a PRNG in
  an initial step and then switch to generating
  random numbers from the PRNG when needed.
* Today, PRNGs are mostly heuristic-based
  constructions. This is because constructions
  based on hard mathematical problems
  (like the discrete logarithm) are too
  slow to be practical.
* To be secure, a PRNG must be seeded with an
  unpredictable secret. More accurately, we say
  that the PRNG takes a key of `n` bytes sampled
  uniformly at random.
  - This means that we should pick the key
    randomly from the set of all possible
    `n-byte` strings, where each byte string
    has the same chance of being picked.

* Actually, because AES is hardware-supported on
  most machines, it is customary to see `AES-CTR`
  being used to produce random numbers.
  - The symmetric key becomes the seed, and the
    ciphertexts become the random numbers.
* In practice, there is a bit more complexity
  added to these constructions in order to provide
  forward and backward secrecy.
* Generating random numbers on a system usually
  means that entropy was mixed together from
  different noise sources and used to
  seed a `long-term` **PRNG**.

* In `2021`, Linux uses a PRNG that's based on the
  `ChaCha20` stream cipher. In addition, the random
  number generator interface exposed to developers
  will be different depending on the OS.
  - For example, on Linux, one can read bytes from
    the `/dev/urandom`.
  - One problem with `/dev/urandom` is that it might
    not provide enough entropy
    (its numbers won't be random enough)
    if used too early after booting the device.
* I recommend that you use `getrandom` if it is
  available on your system. The following listing
  shows how one can securely use getrandom in C:

```c
#include <sys/random.h>

uint8_t secret[16];
int len = getrandom(secret, sizeof(secret), 0);

if (len != sizeof(secret)) {
  abort();
}
```

> It might be easy to forget that `getrandom`
  only returns up to `256` bytes per call,
  for example. For this reason, you should always
  attempt to generate random numbers through the
  standard library of the programming
  language you're using.

* Make sure that you use random libraries that
  generate **cryptographically strong** random
  numbers. Usually the name of the library helps
  (for example, you can probably guess which one
  you should use between the `math/rand` and
  `crypto/rand` packages in Golang).

```
In most situations, sticking to what the
programming language's standard library or
what a good cryptography library
provides should be enough.
```

* It is good to keep in mind the following
  edge cases should you run into them:
  - **Forking processes**: When using a userland
    PRNG (some applications with extremely high
    performance requirements might have no
    other choice), it is important to keep in mind
    that a program that forks will produce a new
    child process that will have the same PRNG
    state as its parent.
  - Consequently, both PRNGs will produce the
    same sequence of random numbers from there on.
  - **Virtual machines (VMs)**: Cloning of PRNG state
    can also become a problem when using the OS PRNG.
    Think about VMs. If the entire state of a VM is
    saved and then started several times from this
    point on, every instance might produce the exact
    same sequence of random numbers.
  - This is sometimes fixed by hypervisors and OSs,
    but it is good to look into what the hypervisor
    you're using is doing before running applications
    that request random numbers in VMs.
  - **Early boot entropy**: While OSs should have no
    trouble gathering entropy in user-operated devices
    due to the noise produced by the user's interactions
    with the device, embedded devices and headless
    systems have more challenges to overcome in order to
    produce good entropy at boot time.
  - History has shown that some devices tend to boot in
    a similar fashion and end up amassing the same
    initial noise from the system, leading to the same
    seed being used for their internal PRNGs and the
    same series of random numbers being generated.

* **Public randomness**
  - `One-to-many`:
  - You want to produce randomness for others.
  - `Many-to-many`:
  - A set of participants want to produce
    randomness together.

---

* A `verifiable random function` (**VRF**) generates
  verifiable randomness via public key cryptography.
  - To generate a random number, simply use a
    signature scheme which produces unique signatures
    (like **BLS**) to sign a seed, then hash the
    signature to produce the public random number.
  - To validate the resulting randomness, make sure that
    the hash of the signature is indeed the random number
    and verify the signature over the seed.

* One popular decentralized randomness beacon is
  called drand and is run in concert by several
  organizations and universities. It is available at
  - https://leagueofentropy.com
  - **League of Entropy**:
    Decentralized Randomness Beacon

---

* Key derivation with HKDF
  - PRNGs are not the only constructions one can
    use to derive more secrets from one secret
    (in other words, to stretch a key).
  - Deriving several secrets from one secret is
    actually such a frequent pattern in
    cryptography that this concept has its
    own name: `key derivation`.

* A key derivation function (**KDF**) is like
  a PRNG in many ways, except for a number of
  subtleties as noted in the following list.
  - __A KDF__ does not necessarily expect a uniformly
    random secret (as long as it has enough entropy).
  - This makes a KDF useful for deriving secrets
    from key exchange output, which produce high
    entropy but biased results.
  - The resulting secrets are, in turn, uniformly random,
    so you can use these in constructions that expect
    uniformly random keys.
  - __A KDF__ is generally used in protocols that
    require participants to rederive the same keys
    several times.
  - In this sense, a KDF is expected to be
    deterministic, while PRNGs sometimes
    provide backward secrecy by frequently
    reseeding themselves with more entropy.
  - __A KDF__ is usually not designed to produce
    a __LOT__ of random numbers. Instead, it is normally
    used to derive a limited number of keys.

* A key derivation function (KDF) and a PRNG
  are two similar constructions.
  - The main differences are that a KDF does
    __not__ expect a fully uniformly random secret as
    input (as long as it has enough entropy) and is
    usually __not__ used to generate too much output.

* The most popular KDF is the HMAC-based
  key derivation function (HKDF). HKDF is a
  light KDF built on top of HMAC and defined
  in `RFC 5869`.
  - For this reason, one can use HKDF with
    different hash functions, although,
    it is most commonly used with `SHA-2`.
- HKDF is specified as two different functions:
  - **HKDF-Extract**: Removes biases from a
    secret input, producing a uniformly random secret.
  - **HKDF-Expand**: Produces an arbitrary length
    and uniformly random output.
  - Like PRNGs, it expects a uniformly random secret
    as `input` and `is`, thus, usually ran after
    HKDF-Extract.

* HKDF-Extract is the __first__ function specified by HKDF.
  It takes an optional salt that is used as the key
  in HMAC and the input secret that might be
  nonuniformly random.
  - Using different salts with the same input
    secret produces different outputs.

* HKDF-Expand is the __second__ function specified
  by HKDF. It takes an optional `info` byte string
  and an `input` secret that needs to be
  uniformly random.
  - Using different `info` byte strings with the
    same `input` secret produces different outputs.
  - The length of the output is controlled
    by a `length` argument.

* HKDF does not expect the `salt` to be a secret;
  it can be known to everyone, including adversaries.
  - Instead of a hash function, HKDF-Extract uses a MAC
    (specifically HMAC), which coincidentally has an
    interface that accepts two arguments.

* HKDF is limited by the size of the hash function
  you use; more precisely, if you use `SHA-512`
  (which produces outputs of `512` bits) with HKDF,
  you are limited to `512 × 255` bits = `16,320` bytes
  of output for a given key and an info byte string.

* Calling HKDF or HKDF-Expand several times with
  the same arguments, except for the output length,
  produces the same output truncated to the different
  length requested.
  - This property is called **related outputs** and can,
    in rare scenarios, surprise protocol designers.
  - It is good to keep this in mind.

* The extended output functions (`XOFs`)
  (SHAKE and cSHAKE) can be used as a KDF
  as well! __Remember__, a XOF
  - Does not expect a uniformly random input
  - Can produce a practically infinitely
    large uniformly random output

* most serious applications employ
  two defense-in-depth techniques:
  - **Key rotation**: By associating an expiration date
    to a key (usually a public key) and by replacing
    your key with a new key periodically, you can "heal"
    from an eventual compromise.
  - The shorter the expiration date and rotation frequency,
    the faster you can replace a key that might be
    known to an attacker.
  - **Key revocation**: Key rotation is not always
    enough, and you might want to cancel a key
    as soon as you hear it has been compromised.
  - For this reason, some systems allow you to ask
    if a key has been revoked before making use of it.

* **Secret splitting** allows you to break a secret
  into multiple parts that can be shared among
  a set of participants.
  - Here, a secret can be anything you want:
  - a symmetric key,
  - a signing private key, and so on.
* Given a key and a number of shares `n`, the
  **Shamir's Secret Sharing** scheme creates `n`
  partial keys of the same size
  as the original key.
* The **Shamir's Secret Sharing** scheme used to
  split a secret in `n` partial keys requires all
  of the `n` partial keys to reconstruct
  the original key.
* The idea behind the **Shamir's Secret Sharing**
  scheme is to see a polynomial defining a curve
  as the secret and random points on the curve as
  partial keys.
  - To recover a polynomial of degree
    `n` that defines a curve, one needs to know
    `n + 1` points on the curve.
  - For example,
    $$ f(x) = 3x + 5 $$
    is of degree `1`, so you need any two points
    `(x, f(x))` to recover the polynomial, and
    $$ f(x) = 5x^2 + 2x + 3 $$
    is of degree `2`, so you need any three points
    to recover the polynomial.

* To avoid this single point of failure issue, there
  exist several cryptographic techniques that can be
  useful in different scenarios.
  - Imagine a protocol that accepts a financial
    transaction only if it has been signed by Alice.
    In order to reduce the impact of an attack on
    Alice, we can, instead, change the protocol to
    accept (on the same transaction) a number `n`
    of signatures from `n` different public keys,
    including Alice's.
  - An attacker would have to compromise all `n`
    signatures in order to forge a valid transaction!
  - Such systems are called **multi-signature**
    (often shortened as **multi-sig**) and are widely
    adopted in the cryptocurrency space.
  - Some signature schemes (like the **BLS**
    signature scheme) can compress several
    signatures down to a single one.
  - This is called **signature aggregation**.
  - Some multi-signature schemes go even further
    in the compression by allowing the `n` public keys
    to be aggregated into a single public key.
  - This technique is called distributed key generation (`DKG`)
    and is part of a field of cryptography called
    **secure multi-party computation**.
  - DKG lets `n` participants collaboratively
    compute a public key without ever having the
    associated private key in the clear during the
    process (unlike SSS, there is no dealer).
  - If participants want to sign a message, they can
    then collaboratively create a signature using each
    participant's private shares, which can be verified
    using the public key they previously created.
  - __Again__, the private key __never__ exists
    physically, preventing the single point of
    failure problem SSS has.
