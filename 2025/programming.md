---
title: 码农碎碎念
description: 寻芳不觉醉流霞, 倚树沉眠日已斜. 客散酒醒深夜后, 更持红烛赏残花.
date: 2025-02-02
---

### Posts

- [Rust 1.88](https://blog.rust-lang.org/2025/06/26/Rust-1.88.0/)

```rust
if let Channel::Stable(v) = release_info()
    && let Semver { major, minor, .. } = v
    && major == 1
    && minor == 88
{
    println!("`let_chains` was stabilized in this version");
}
```

- [PEP 750 - Template Strings](https://peps.python.org/pep-0750/)

```py
name = "World"
tmpl = t"Hello {name}"
assert tmpl.strings[0] == "Hello "
assert tmpl.interpolations[0].value == "World"
assert tmpl.interpolations[0].expression == "name"

tmpl = t"Hello {name!r}"
assert tmpl.interpolations[0].conversion == "r"

val = 42
tmpl = t"Value: {val:.2f}"
assert tmpl.interpolations[0].format_spec == ".2f"
```

- [Rust 1.85 and Rust 2024](https://blog.rust-lang.org/2025/02/20/Rust-1.85.0/)

```rust
let mut vec: Vec<String> = vec![];

let closure = async || {
  vec.push(ready(String::from("")).await);
};
```

---

- __数学的碎碎念__: 2025-02-10 凌晨, 洗澡的时候想出来的.
  - 如何通过一道简单的题目, 测试数学的思维水平?
    洗澡的时候编了一道.
  - 设一个矩阵 A, 输入向量 x, 输出向量 y, 则 y = Ax.
  - 问题: 1 给出一个矩阵倒数的定义; (此处可以提示: 取欧式距离)
    2 进一步, 分别定义: 全导数, 偏导数, 方向导数;
    3 再进一步, 给出积分的定义. (此处可提示: 沿某一曲线)
  - 缘起: 之所以有这个念头: 测试数学的思维水平.
    是因为看书临时去回顾了下一些群论的一些概念,
    想起几年前, 自己对于陪集, 正规子群, 商群等概念, 其实不是自然接纳的.
    但是现在, 基本也能自然的顺着思路独自给出来.
    并且过去并没有再次系统的看过群论的书籍资料, 仅仅偶尔接触到.

### 文章/视频

- [Terence Tao on how we measure the cosmos (part 1)](https://www.youtube.com/watch?v=YdOXS_9_P4U)
  - Part 1, 访谈的形式不错, 但是内容一般~
    亮点部分是开普勒如何根据大量数据得出开普勒定律!
  - [The cosmic distance ladder with Terence Tao (part 2)](https://www.youtube.com/watch?v=hFMaT9oRbs4)
  - Part 2, 一般
