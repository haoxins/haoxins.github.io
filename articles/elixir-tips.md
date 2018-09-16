---
title: Elixir tips
description: Elixir is awesome
date: 2018-09-13
---

### Awesome Sites

* [Elixir School](https://elixirschool.com)
* [HexDocs Elixir](https://hexdocs.pm/elixir/Kernel.html)

### Awesome Blogs

* [Understanding elixir macros](https://hackernoon.com/understanding-elixir-macros-3464e141434c)

### 101

* structure
  - ebin: compiled bytecode
  - lib: code (`.ex`)
  - test: (`.exs`)
  - `.ex` to be compiled, `.exs` for scripting

* `quote` & `unquote`
  - `quoted expressions`

* Elixir AST
  - `Script` -> `Elixir AST` -> `Expand Macros` -> `Erlang AST` -> `...`

* 3 Element Tuples
  - `foo` -> `{:foo, [], Elixir}`
  - `2 + 3` -> `{:+, [context: Elixir, import: Kernel], [2, 5]}`

* quote
  - `quote do: 2 + 3` -> `{:+, [context: Elixir, import: Kernel], [2, 3]}`

* unquote
  - `unquote do: {:+, [context: Elixir, import: Kernel], [2, 3]}` -> `2 + 3`

* `do:` vs `do/end`
  - one-lines vs multiple lines
