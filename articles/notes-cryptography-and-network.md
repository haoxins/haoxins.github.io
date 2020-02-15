---
title: Cryptography is fun
description: We can do something
date: 2019-06-30
---

* TLS
  - https://tls13.ulfheim.net

* PKCS (Public Key Cryptography Standards)
  - https://en.wikipedia.org/wiki/PKCS

*
  - https://webauthn.guide

### Stream ciphers

* Stream ciphers (making OTP practical)
  - Bad news (OTP): perfect-secrecy -> key-len >= msg-len
  - Stream ciphers cannot have perfect secrecy
  - no integrity: modifications to ciphertext are undetected and
  -   have predictable impact on plaintext
  - Two time pad is insecure, never use stream cipher key more than once
  - secure PRG -> semantically secure stream cipher
  - Impl: `Salsa20`

* PRP, PRF, PRG
  - a secure PRG is unpredictable
  - also, an unpredictable PRG is secure
  - Pseudo Random Function (PRF) defined over (K, X, Y): F: K*X -> Y
    * such that exists efficient algorithm to evaluate F(k, x)
  - Pseudo Random Permutation (PRP) defined over (K, X): E: K*X -> X
    * Exists efficient deterministic algorithm to evaluate E(k, x)
    * The function E(k, ⋅) is one-to-one
    * Exists efficient inversion algorithm D(k, x)
  - A PRP is a PRF where X=Y and is efficiently invertible
  - Let F: K * {0, 1}n -> {0, 1}n be a secure PRF
    * Then the following G: K -> {0, 1}nt is a secure PRG:
    * G(k) = F(k, 0) || F(k, 1) || ⋯ || F(k, t-1)

* [Why do stream ciphers use a nonce ?](https://crypto.stackexchange.com/questions/30818/why-do-stream-ciphers-use-a-nonce)

### Block ciphers

* 2000: NIST adopts Rijndael as AES to replace DES
* PRPs and PRFs: a useful abstraction of block ciphers
* AES
  - ECB mode is not semanAcally secure
  - neither mode ensures data integrity
* CPA security for nonce-based encrypAon
  - System should be secure when nonces are chosen adversarially
* Tweakable block ciphers
  - Use tweakable encryption when you need many independent PRPs from one key
* Format-preserving encryption

### MAC

* Def: MAC I = (S, V) defined over (K, M, T) is a pair of algs:
  – S(k, m) outputs t in T
  – V(k, m, t) outputs `yes` or `no`

### Auth encryption (introduced in 2000)

* An authenticated encryption system (E, D) is a cipher where
  - as usual: E: K * M * N -> C
  - but D: K * C * N -> M & {⊥}
  - (⊥ -> ciphertext is rejected)
* Encrypt-then-MAC: always provides A.E.
* MAC-then-encrypt: may be insecure against CCA attacks

### Public encryption

* one-time security -> many-time security (CPA)

### Security

* semantically secure:
  - only negligible information about the plaintext
  - can be feasibly extracted from the ciphertext
* Chosen ciphertext security
* CPA security cannot guarantee secrecy under active attacks
* Authenticated encryption -> `CCA security` (chosen-ciphertext attack)
* integrity -> `MAC`
* integrity, confidentiality -> `authenticated encryption`

### 相关比较

* `对称密码`:
  - 共享密钥 `加&解` 密
* `公钥密码`:
  - 公钥加密, 私钥解密
  - 公钥, 需要认证 (中间人攻击)
* `消息认证码(MAC)`
  - 共享密钥 -> `MAC`
  - `不可` 防止否认
* `数字签名`:
  - 私钥生成签名
  - 公钥验证签名
  - 公钥, 需要认证 (中间人攻击)
  - `可` 防止否认

### RSA

* 公钥: `E`, `N`
* 私钥: `D`, `N`
* 加密: 密文 = 明文 ** E % N
* 解密: 明文 = 密文 ** D % N

### Diffie-Hellman

* Public numbers: G, P, G ** A % P (Alice), G ** B % P (Bob)
  - A (Alice), B (Bob) are private numbers
* session key

```
session key = G ** (A * B) % P
            = (G ** A % P) ** B % P (Bob)
            = (G ** B % P) ** A % P (Alice)
```

### AES, SHA, MAC

* AES: `Rijndael` (2000)
* SHA-3: `Keccak` (2012)

* HASH
  - no key
  - `integrity`
* MAC
  - HMAC (hash MAC)
  - share key
  - `integrity`, `auth`
  - 攻击: `重放攻击`
* digital signature
  - public key
  - `integrity`, `auth`, `deny`
  - 攻击: `中间人攻击`

### (公钥)证书

* 公钥基础设施 (PKI) = 用户 (user) + 认证机构 (CA) + 仓库 (Repo)
* 证书 至少包含: `public key`, `机构签名`
* 证书信任链

## Network

### HTTP/3

* TLS 1.3+
* 0-RTT or 1-RTT
* Early data
* Connection Id
  - Independent streams
* QPACK
* Connection -> Secure Connection -> Streams
* Stream
  - 单向
  - 双向
  - Flow control
  - Back pressure
  - Frames
* Frame
  - Headers frame
  - Data frame
  - Goaway frame
  - Other frame
  - Priority
* Alt-Svc
* UDP todo
  - 操作系统, 内核优化
  - 硬件加速
