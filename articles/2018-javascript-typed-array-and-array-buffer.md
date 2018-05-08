---
title: js typed arrays
description: and array buffer, data view
date: 2018-04-19
---

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

* DataView

```js
const b = new ArrayBuffer(8)

const v1 = new DataView(b)
var v2 = new DataView(b, 4, 2)
v1.setInt8(4, 18)

v2.getInt8(0) // 18
```

### 参考链接

* [MDN - typed arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays)
