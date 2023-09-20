- If `A` and `B` are `n` by `n`, so is `AB`. It contains
  $$ n^2 $$
  dot products, row of `A` times column of `B`.
  Each dot product needs `n` multiplications,
  so the computation of `AB` uses
  $$ n^3 $$
  separate multiplications.
  - For `n = 100` we multiply a million times.
  - For `n = 2` we have
    $$ n^3 = 8 $$.
- Mathematicians thought until recently that `AB`
  absolutely needed
  $$ 2^3 = 8 $$
  multiplications. Then somebody found a way to do it with `7`
  (and extra additions). By breaking `n` by `n` matrices into
  `2` by `2` blocks, this idea also reduced the count
  to multiply large matrices.
  - Instead of
    $$ n^3 $$
    multiplications the count has now dropped to
    $$ n^{2.376} $$.
  - Maybe
    $$ n^2 $$
    is possible?
  - But the algorithms are so awkward that scientific
    computing is done the regular
    $$ n^3 $$
    way.

## Vector Spaces and Subspaces

- A matrix multiplies a vector: __A__ _times_ __x__.
  - At the first level this is only numbers.
  - At the second level __Ax__ is a
    combination of column vectors.
  - The third level shows subspaces.

## Orthogonality

- The __orthogonal complement__ of a subspace __V__
  contains __every__ vector that is perpendicular to __V__.
  - This orthogonal subspace is denoted by
    $$ V^{\perp} $$.
