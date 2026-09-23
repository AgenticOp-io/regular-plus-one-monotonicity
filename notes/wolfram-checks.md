# Wolfram checks

Identities only. Queries are sent one at a time. The app id is not stored here.

## 2026-09-22

Mode ratio. Wolfram result: `1`. Also expanded as
`d^2/(d-1)^2 - 2d/(d-1)^2 + 1/(d-1)^2`, which is the same value.

```
Simplify[((d - 2)*n + n/d)/(2*(d - 1)^2*(n/(2*d)))]
```

Threshold after exponents are collected, for `n>1`. Wolfram result: `1`.

```
simplify ((n^(2/7))^(1/6) / (log(n))^(1/14) * log(n)^(1/14)) / n^(1/21) for n>1
```

A direct "is it always 1" query, before the powers were collected and without a domain, returned not always equal to 1. That does not contradict the reduced identity on `n>1`.

Series for small `u` and `u/a`. Wolfram:

```
sum_(k=1)^∞ ((-1)^k (u^k - (u/a)^k))/k
```

The first terms are `-u + u/a + u^2/2 - u^3/3`, matching the Laplace expansion with `a = (d-1)^2`.


Query: simplify (d^2/n)/((d^2/n)^(1/4))
[Input interpretation]
simplify | (d^2/n)/(d^2/n)^(1/4)
[Expanded form]
(d^2/n)^(3/4)


Query: simplify d * (d^2/n)^(1/8)
[Input interpretation]
simplify | d (d^2/n)^(1/8)
[Result]
d (d^2/n)^(1/8)


Query: simplify d*d^(1/4)/n^(1/8)
[Input interpretation]
simplify | d × d^(1/4)/n^(1/8)
[Result]
d^(5/4)/n^(1/8)


Query: solve d^(5/4) = n^(1/8) for d
[Input interpretation]
solve d^(5/4) = n^(1/8) for d
[Result]
d = n^(1/10)


Query: simplify (n^(1/10))^4 / n
[Input interpretation]
simplify | (n^(1/10))^4/n
[Result]
1/n^(3/5)
