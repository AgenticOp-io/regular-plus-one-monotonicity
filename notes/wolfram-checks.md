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


Query: simplify (log(n)*sqrt(n/(2*d)))^3 / (6*(n/(2*d))^2)
[Input interpretation]
simplify | (log(n) sqrt(n/(2 d)))^3/(6 (n/(2 d))^2)
[Result]
(log^3(n))/(3 sqrt(2) sqrt(n/d))
[Expanded logarithmic form]
((n/d)^(3/2) log^3(n) d^2 sqrt(2))/(6 n^2)
[Expanded form]
(d sqrt(n/d) log^3(n))/(3 sqrt(2) n)


Query: simplify 1/(n/(2*d))
[Input interpretation]
simplify | 1/(n/(2 d))
[Result]
(2 d)/n


Query: series of 1/sqrt(1-1/(d-1)^2) at d=infinity
[Input interpretation]
series | 1/sqrt(1 - 1/(d - 1)^2) | point | d = ∞
[Series expansion at d = ∞]
1 + 1/(2 d^2) + (1/d)^3 + 15/(8 d^4) + 7/(2 d^5) + O((1/d)^6)
(Laurent series)


Query: simplify sum_{t=1}^{delta} t^2
[Input interpretation]
simplify | sum_(t=1)^δ t^2
[Results]
δ ((δ/3 + 1/2) δ + 1/6)
[Results]
1/6 δ (δ + 1) (2 δ + 1)
[Expanded form]
δ^3/3 + δ^2/2 + δ/6


Query: simplify (log(n))^4 / (n/(2*d))
[Input interpretation]
simplify | (log^4(n))/(n/(2 d))
[Expanded logarithmic form]
(2 d log^4(n))/n


Query: simplify (delta^3/3 + delta^2/2 + delta/6)/(2*k^2)
[Input interpretation]
simplify | (δ^3/3 + δ^2/2 + δ/6)/(2 k^2)
[Results]
(δ (2 δ + 1) (δ + 1))/(6 (2 k^2))
[Results]
(δ (δ + 1) (2 δ + 1))/(12 k^2)
[Results]
(δ (δ (2 δ + 3) + 1))/(12 k^2)


Query: expand (delta*(delta+1)*(2*delta+1))/(12*k^2)
[Input interpretation]
expand | (δ (δ + 1) (2 δ + 1))/(12 k^2)
[Results]
(2 δ^3 + 3 δ^2 + δ)/(12 k^2)
[Results]
δ^3/(6 k^2) + δ^2/(4 k^2) + δ/(12 k^2)
[Series expansion at k = 0]
(δ (δ + 1) (2 δ + 1))/(12 k^2)
(Laurent series)
(converges when k!=0)
[Series expansion at k = 1]
1/12 δ (δ + 1) (2 δ + 1) - 1/6 (δ (δ + 1) (2 δ + 1)) (k - 1) + 1/4 δ (δ + 1) (2 δ + 1) (k - 1)^2 + O((k - 1)^3)
(Taylor series)
(converges when abs(1 - k)<1)
[Series expansion at k = ∞]
(δ (δ + 1) (2 δ + 1))/(12 k^2)
(Laurent series)
(converges everywhere away from origin)


Query: simplify d*(log(n)/d)^(1/9)
[Input interpretation]
simplify | d (log(n)/d)^(1/9)
[Result]
d (log(n)/d)^(1/9)


Query: simplify d*d^(-1/9)*log(n)^(1/9)
[Input interpretation]
simplify | d d^(-1/9) log(n)^(1/9)
[Expanded logarithmic form]
d^(8/9) log(n)^(1/9)


Query: solve d^(11/6) = n for d
[Input interpretation]
solve d^(11/6) = n for d
[Result]
d = n^(6/11)


Query: simplify (d*log(n))^(1/2) * (d^(2/3)*(log(n))^(1/3))^2 / n
[Input interpretation]
simplify | sqrt(d log(n)) × (d^(2/3) log(n)^(1/3))^2/n
[Expanded logarithmic form]
(sqrt(d log(n)) d^((2 2)/3) log^(2/3)(n))/n
[Alternate form assuming d>=0, n>0, and log(n)>=0]
(d^(4/3) log^(2/3)(n) sqrt(log(n^d)))/n


Query: simplify (n^(1/2))^(11/6)/n
[Input interpretation]
simplify | sqrt(n)^(11/6)/n
[Result]
1/n^(1/12)


Query: simplify d^(4/3)*d^(1/2)*log(n)^(2/3)*log(n)^(1/2)/n
[Input interpretation]
simplify | d^(4/3) sqrt(d) log^(2/3)(n) × sqrt(log(n))/n
[Expanded logarithmic form]
(d^(11/6) log^(7/6)(n))/n


Query: simplify (n^(2/7))^(11/6)/n
[Input interpretation]
simplify | (n^(2/7))^(11/6)/n
[Result]
1/n^(10/21)


Query: simplify (d^(1/2)*(log(n))^(3/2))^(1/2)/(d^(1/2)*(log(n))^(1/2))
[Input interpretation]
simplify | sqrt(sqrt(d) log^(3/2)(n))/(sqrt(d) sqrt(log(n)))
[Result]
log(n)/sqrt(sqrt(d) log^(3/2)(n))


Query: simplify d^(1/4)*log(n)^(3/4)/(d^(1/2)*log(n)^(1/2))
[Input interpretation]
simplify | d^(1/4) × (log^(3/4)(n))/(sqrt(d) sqrt(log(n)))
[Result]
log(n)^(1/4)/d^(1/4)
