---
title: 写给自己的量子课 01 - 从测量开始
description:
date: 2022-04-30
---

### 测量苹果的宽度

- 测量即是破坏
  - 实在/存在的破坏
    - 状态(信息)的破坏

### 测量一个指令的试行时间

```go
times := 1_000_000_000
start := float64(time.Now().Unix())
for i := 0; i <= times; i++ {
  // 指令
}
end := float64(time.Now().Unix())
fmt.Print((end - start) / float64(times))
```

- 本质上, 原子等微观态的测量类似

### 测量是什么?
