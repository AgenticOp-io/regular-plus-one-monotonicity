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


Query: simplify (n^(4/13))^(13/10) / n^(2/5)
[Input interpretation]
simplify | (n^(4/13))^(13/10)/n^(2/5)
[Result]
1
[Quotient and Remainder]
1 = 1 × 1 + 0


Query: simplify (log(n))^(-(5/13)*(13/10)) * (log(n))^(1/2)
[Input interpretation]
simplify | log^(-5/13 × 13/10)(n) sqrt(log(n))
[Expanded logarithmic form]
1
[Quotient and Remainder]
1 = 1 × 1 + 0


Query: simplify d^(1/2)*d^(2/3)/n
[Input interpretation]
simplify | sqrt(d) × d^(2/3)/n
[Result]
d^(7/6)/n


Query: simplify (n^(1/8))^8/n
[Input interpretation]
simplify | (n^(1/8))^8/n
[Result]
1
[Quotient and Remainder]
1 = 1 × 1 + 0


Query: simplify (n^(2/7))^8/n
[Input interpretation]
simplify | (n^(2/7))^8/n
[Result]
n^(9/7)


Query: simplify n/(n^(2/7))^2
[Input interpretation]
simplify | n/(n^(2/7))^2
[Result]
n^(3/7)


Query: simplify (4/13)-(2/7)
[Input interpretation]
simplify | 4/13 - 2/7
[Result]
2/91
[Quotient and Remainder]
2 = (0) × 91 + 2
[Decimal approximation]
0.0219780219780219780219780219780219780219780219780219780219780219...
[Repeating decimal]
0.021978^_ (period 6)


Query: simplify (2/7)-(1/8)
[Input interpretation]
simplify | 2/7 - 1/8
[Result]
9/56
[Quotient and Remainder]
9 = (0) × 56 + 9
[Decimal approximation]
0.1607142857142857142857142857142857142857142857142857142857142857...
[Repeating decimal]
0.160714285^_ (period 6)
[Percent decrease]
2/7 - 1/8 = 9/56 is 43.75% smaller than 2/7.


Query: simplify Integrate[x^(-11/10), {x, D, Infinity}] for D>0
[Input interpretation]
simplify | integral_D^∞ x^(-11/10) dx | assuming D>0
[Computation result]
simplify | integral_D^∞ x^(-11/10) dx | assuming D>0 = {10/D^(1/10), D}
[Result]
10/D^(1/10)


Query: simplify (n^(1/6))^6/n
[Input interpretation]
simplify | (n^(1/6))^6/n
[Result]
1
[Quotient and Remainder]
1 = 1 × 1 + 0


Query: simplify -4+2*(6/5)
[Input interpretation]
simplify | -4 + 2 × 6/5
[Result]
-8/5
[Quotient and Remainder]
-8 = (-1) × 5 + (-3)
[Decimal form]
-1.6


Query: simplify -6+4*(6/5)
[Input interpretation]
simplify | -6 + 4 × 6/5
[Result]
-6/5
[Quotient and Remainder]
-6 = (-1) × 5 + (-1)
[Decimal form]
-1.2


Query: simplify Integrate[x^(-6/5), {x, D, Infinity}] for D>0
[Input interpretation]
simplify | integral_D^∞ x^(-6/5) dx | assuming D>0
[Computation result]
simplify | integral_D^∞ x^(-6/5) dx | assuming D>0 = {5/D^(1/5), D}
[Result]
5/D^(1/5)


Query: simplify 1-4+6-3
[Input interpretation]
simplify | 1 - 4 + 6 - 3
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: simplify 6-12+6
[Input interpretation]
simplify | 6 - 12 + 6
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Rerun of the identities used by the current theorems. Each result below matches the manuscript.

Query: simplify (2/7)*(7/6)
[Result]
1/3

Query: simplify (3/7)*(7/6)
[Result]
1/2

Query: simplify (4/13)*(13/10)
[Result]
2/5

Query: simplify (5/13)*(13/10)
[Result]
1/2

Query: simplify (1/6)-(1/10)
[Result]
1/15

Query: simplify (2/7)-(1/6)
[Result]
5/42

Query: simplify (n^(2/7))^(7/6)/n^(1/3)
[Result]
1

Query: simplify (n^(1/6))^12/n/((n^(1/6))^6)
[Input interpretation]
simplify | ((n^(1/6))^12/n)/(n^(1/6))^6
[Result]
1
[Quotient and Remainder]
1 = 1 × 1 + 0


Query: simplify (2/5)*(5/6)
[Input interpretation]
simplify | 2/5 × 5/6
[Result]
1/3
[Quotient and Remainder]
1 = (0) × 3 + 1
[Decimal approximation]
0.3333333333333333333333333333333333333333333333333333333333333333...
[Repeating decimal]
0.3^_ (period 1)


Query: simplify (3/5)*(5/6)
[Input interpretation]
simplify | 3/5 × 5/6
[Result]
1/2
[Quotient and Remainder]
1 = (0) × 2 + 1
[Decimal form]
0.5


Query: simplify (2/5)-(2/7)
[Input interpretation]
simplify | 2/5 - 2/7
[Result]
4/35
[Quotient and Remainder]
4 = (0) × 35 + 4
[Decimal approximation]
0.1142857142857142857142857142857142857142857142857142857142857142...
[Repeating decimal]
0.1142857^_ (period 6)


Query: simplify (n^(2/5))^(5/6)/n^(1/3)
[Input interpretation]
simplify | (n^(2/5))^(5/6)/n^(1/3)
[Result]
1
[Quotient and Remainder]
1 = 1 × 1 + 0


Query: simplify (n^(1/2))^3/n^2
[Input interpretation]
simplify | sqrt(n)^3/n^2
[Result]
1/sqrt(n)


Query: simplify (d^4/n^2)/(d*n)
[Input interpretation]
simplify | (d^4/n^2)/(d n)
[Result]
d^3/n^3


Query: simplify (d^3/n)/(d*n)
[Input interpretation]
simplify | (d^3/n)/(d n)
[Result]
d^2/n^2


Query: simplify (d^2/n)/(d*n)
[Input interpretation]
simplify | (d^2/n)/(d n)
[Result]
d/n^2


Query: simplify n*(d/n^2)
[Input interpretation]
simplify | n × d/n^2
[Result]
d/n


Query: simplify (d^4/n^3)/(d/n)
[Input interpretation]
simplify | (d^4/n^3)/(d/n)
[Result]
d^3/n^2


Query: simplify sqrt(n/d)*d^2/n^2
[Input interpretation]
simplify | sqrt(n/d) × d^2/n^2
[Result]
1/(n/d)^(3/2)


Query: simplify sqrt(n/d)*d^2/n^2 - (d/n)^(3/2) for d>0 and n>0
[Input interpretation]
simplify | {sqrt(n/d) × d^2/n^2 - (d/n)^(3/2) d>0, n>0}
[Results]
{d^2 n^2 (sqrt(n/d) - n sqrt(d/n))>0, n>0}
[Results]
{(d (d sqrt(n/d) - n^2 (d/n)^(3/2)))/n^2>0, n>0}
[Results]
{-(d (n^2 (d/n)^(3/2) - d sqrt(n/d)))/n^2>0, n>0}
[Expanded form]
{(d^2 sqrt(n/d))/n^2 - (d^2 sqrt(d/n))/n>0, n>0}


Query: simplify (d/n)^(3/2)/(d/n) for d>0 and n>0
[Input interpretation]
simplify | {(d/n)^(3/2)/(d/n) d>0, n>0}
[Expanded form]
{d sqrt(d/n)>0, n>0}


Query: sqrt(n/d)*d^2/n^2 == (d/n)^(3/2) for d>0, n>0
[Input]
{sqrt(n/d) × d^2/n^2 = (d/n)^(3/2) d>0, n>0}
[Alternate forms]
{1/(n/d)^(3/2) = d (d/n)^(3/2)>0, n>0}
[Alternate forms]
{d sqrt(n/d) = (d/n)^(3/2) n^2 ∧ d (d/n)^(3/2)>0, n>0}
[Expanded form]
{(d^2 sqrt(n/d))/n^2 = (d^2 sqrt(d/n))/n>0, n>0}
[Alternate form assuming d and n are positive]
{(d/n)^(3/2) = d^(5/2)/n^(3/2)>0, n>0}
[Solution]
d = 1, n>0
[Integer solutions]
d = 1, n = 1
[Integer solutions]
d = 1, n = 2
[Integer solutions]
d = 1, n = 3
[Integer solutions]
d = 1, n = 4
[Integer solutions]
d = 1, n = 5


Query: (d/n)^(3/2)/(d/n) == sqrt(d/n) for d>0, n>0
[Input]
{(d/n)^(3/2)/(d/n) = sqrt(d/n) d>0, n>0}
[Solution]
d = 1, n>0
[Integer solutions]
d = 1, n = 1
[Integer solutions]
d = 1, n = 2
[Integer solutions]
d = 1, n = 3
[Integer solutions]
d = 1, n = 4
[Integer solutions]
d = 1, n = 5


Query: FullSimplify[Sqrt[n/d]*d^2/n^2 - (d/n)^(3/2), Assumptions -> d>0 && n>0]
[error]
no result


Query: FullSimplify[(d/n)^(3/2)/(d/n) - Sqrt[d/n], Assumptions -> d>0 && n>0]
[error]
no result

Fallback, exact rational arithmetic, after Wolfram returned no equality.
The domain clause in the preceding equality queries was parsed as an extra equation and solved only at d=1; that is not a counterexample.
For d>0 and n>0 both sides of sqrt(n/d)*d^2/n^2 = (d/n)^(3/2) are positive, and their squares are the same rational:
(n/d)*d^4/n^4 = d^3/n^3 = ((d/n)^(3/2))^2.
Likewise ((d/n)^(3/2)/(d/n))^2 = d/n = (sqrt(d/n))^2.
Checked as equal for every integer pair 1<=d<n<80.


Query: simplify (n^(1/4))/n
[Input interpretation]
simplify | n^(1/4)/n
[Result]
1/n^(3/4)


Query: simplify (n^(-3/4))^(-1/3)
[Input interpretation]
simplify | (n^(-3/4))^(-1/3)
[Result]
n^(1/4)


Query: simplify (1/4)-(1/5)
[Input interpretation]
simplify | 1/4 - 1/5
[Result]
1/20
[Quotient and Remainder]
1 = (0) × 20 + 1
[Decimal form]
0.05


Query: simplify (n^(1/4))^3/n
[Input interpretation]
simplify | (n^(1/4))^3/n
[Result]
1/n^(1/4)


Query: simplify (4/9)*(9/10)
[Input interpretation]
simplify | 4/9 × 9/10
[Result]
2/5
[Quotient and Remainder]
2 = (0) × 5 + 2
[Decimal form]
0.4


Query: simplify (5/9)*(9/10)
[Input interpretation]
simplify | 5/9 × 9/10
[Result]
1/2
[Quotient and Remainder]
1 = (0) × 2 + 1
[Decimal form]
0.5


Query: simplify (4/9)-(2/5)
[Input interpretation]
simplify | 4/9 - 2/5
[Result]
2/45
[Quotient and Remainder]
2 = (0) × 45 + 2
[Decimal approximation]
0.0444444444444444444444444444444444444444444444444444444444444444...
[Repeating decimal]
0.04^_ (period 1)


Query: simplify (n^(4/9))^(9/10)/n^(2/5)
[Input interpretation]
simplify | (n^(4/9))^(9/10)/n^(2/5)
[Result]
1
[Quotient and Remainder]
1 = 1 × 1 + 0


Query: simplify (2/5)-(1/8)
[Input interpretation]
simplify | 2/5 - 1/8
[Result]
11/40
[Quotient and Remainder]
11 = (0) × 40 + 11
[Decimal form]
0.275
[Percent decrease]
2/5 - 1/8 = 11/40 is 31.25% smaller than 2/5.


Query: simplify -3+8-6
[Input interpretation]
simplify | -3 + 8 - 6
[Result]
-1
[Quotient and Remainder]
-1 = (-1) × 1 + 0


Query: simplify (1+6*v+3*v^2)-4*(1+3*v)+6*(1+v)-3
[Input interpretation]
simplify | (1 + 6 v + 3 v^2) - 4 (1 + 3 v) + 6 (1 + v) - 3
[Result]
3 v^2


Query: simplify exp(l*k*n/2)/exp(l*n/2)^k
[Input interpretation]
simplify | exp(l k × n/2)/(exp^k(l × n/2))
[Result]
e^((k l n)/2) (e^((l n)/2))^(-k)
[Alternate form assuming k, l, and n are real]
1


Query: simplify (d^2/n^2)*(n/(2*d))
[Input interpretation]
simplify | d^2/n^2 × n/(2 d)
[Result]
d/(2 n)


Query: simplify Binomial[4,2]
[Input interpretation]
simplify | binomial(4, 2)
[Result]
6
[Quotient and Remainder]
6 = 6 × 1 + 0


Query: simplify Binomial[3,2]
[Input interpretation]
simplify | binomial(3, 2)
[Result]
3
[Quotient and Remainder]
3 = 3 × 1 + 0


Query: simplify (d^4/n^4)*(n/d)
[Input interpretation]
simplify | d^4/n^4 × n/d
[Result]
d^3/n^3


Query: simplify (d^3/n^3)/(d/n)^2
[Input interpretation]
simplify | (d^3/n^3)/(d/n)^2
[Result]
d/n


Query: simplify (n^(1/4))^2/n^2
[Input interpretation]
simplify | (n^(1/4))^2/n^2
[Result]
1/n^(3/2)


Query: simplify (n^(1/4))^(-6)
[Input interpretation]
simplify | 1/(n^(1/4))^6
[Result]
1/n^(3/2)
