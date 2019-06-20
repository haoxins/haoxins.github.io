---
title: Tech notes
description: just notes
date: 2019-06-18
---

## Cryptography

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
