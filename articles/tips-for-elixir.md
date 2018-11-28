---
title: Elixir tips
description: Elixir is awesome
date: 2018-09-13
---

### Awesome Sites

* [Elixir School](https://elixirschool.com)
* [HexDocs Elixir](https://hexdocs.pm/elixir/Kernel.html)
* [The Erlang Runtime System](https://happi.github.io/theBeamBook)

### Awesome Projects

* [EventBus](https://github.com/otobus/event_bus)
* [rustler: Safe Rust bridge for creating Erlang NIF functions](https://github.com/hansihe/rustler)
* [distillery: Simplify deployments in Elixir with OTP releases!](https://github.com/bitwalker/distillery)
* [elixirscript: Converts Elixir to JavaScript](https://github.com/elixirscript/elixirscript)

### Awesome Blogs

* [Understanding elixir macros](https://hackernoon.com/understanding-elixir-macros-3464e141434c)

### Small Projects

* [Merkle Tree implementation in pure Elixir](https://github.com/yosriady/merkle_tree)
* [multiformats/ex_multihash](https://github.com/multiformats/ex_multihash)

### Small Erlang Projects

* [Distributed key generation - pairing based cryptography](https://github.com/helium/erlang-dkg)

### Elixir

* structure
  - ebin: compiled bytecode
  - lib: code (`.ex`)
  - test: (`.exs`)
  - `.ex` to be compiled, `.exs` for scripting

* atom
  - once atom is created, it's never reclaimed

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

* function: `named` vs `anonymous`
  - anonymous must be invoked with a dot `.`
  - anonymous functions cannot have optional arguments

* `Error`, `Throw`, `Exit` and `try` `catch` `rescue` `after` `else`

### mix and OTP

* `mix`: like `npm` to `node`, `gradle` to `java`
* `otp`: like `?` to `rust`

* Process
  - `not` OS process
  - isolated
  - `link`:
  - `task`:
  - `agent`:

* `Application` and `Project`
  - `Project` is managed by `mix`
  - `Application` is from `OTP`
