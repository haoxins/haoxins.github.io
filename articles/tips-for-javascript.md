---
title: javascript
description: js tips
date: 2018-06-21
---

### Something new

* [BigInt](https://developers.google.com/web/updates/2018/05/bigint)
* [Typed arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays)


* TypedArray

```js
const t = new Int8Array(8)

Array.isArray(t) // false
ArrayBuffer.isView(t) // true
```

* ArrayBuffer

```js
const b = new ArrayBuffer(8)

Array.isArray(b) // false
```
### Modern JavaScript

* DataView

```js
const b = new ArrayBuffer(8)

const v1 = new DataView(b)
var v2 = new DataView(b, 4, 2)
v1.setInt8(4, 18)

v2.getInt8(0) // 18
```

### 参考链接

* [Modern JavaScript is fun](https://github.com/MylesBorins/i-love-this-pattern)
