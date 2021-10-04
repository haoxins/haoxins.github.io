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
