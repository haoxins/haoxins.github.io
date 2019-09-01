---
title: 常见的开发环境配置需求
description: not, not, not 生产环境 ~
date: 2018-03-23
---

### Config files

* [amix/vimrc](https://github.com/amix/vimrc)

### Dev tools

* [nghttp2](https://github.com/nghttp2/nghttp2) `brew install nghttp2`

### Local https

```bash
openssl genrsa -des3 -out root_ca_dev.key 2048
# pass phrase: 123456 :)

openssl req -x509 -new -nodes -key root_ca_dev.key -sha256 -days 2048 -out root_ca_dev.pem

# Mac: Open Keychain Access -> System: Certificates ->
# Add Item: Import file -> Always Trust

touch server.csr.cnf

touch v3.ext

openssl req -new -sha256 -nodes -out server.csr -newkey rsa:2048 -keyout server.key -config <( cat server.csr.cnf )

openssl x509 -req -in server.csr -CA root_ca_dev.pem -CAkey root_ca_dev.key -CAcreateserial -out server.crt -days 2048 -sha256 -extfile v3.ext

# DONE ! try it !
node app.js

# https://localhost:3000
```

* file: `server.csr.cnf`

```
[req]
default_bits = 2048
prompt = no
default_md = sha256
distinguished_name = dn

[dn]
C=CN
ST=shanghai
L=shanghai
O=hx
OU=hx
emailAddress=haoxins@icloud.com
CN = localhost
```

* file: `v3.ext`

```
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = localhost
```

* file: `app.js`

```js
const https = require('https')
const fs = require('fs')

const options = {
  key: fs.readFileSync('dir/server.key'),
  cert: fs.readFileSync('dir/server.crt')
}

https.createServer(options, (req, res) => {
  res.writeHead(200)
  res.end('ok')
}).listen(3000)
```

* [参考文章](https://medium.freecodecamp.org/how-to-get-https-working-on-your-local-development-environment-in-5-minutes-7af615770eec)
