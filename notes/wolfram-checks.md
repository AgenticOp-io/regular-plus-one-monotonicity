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


Query: simplify (2/7)*(7/5)
[Input interpretation]
simplify | 2/7 × 7/5
[Result]
2/5
[Quotient and Remainder]
2 = (0) × 5 + 2
[Decimal form]
0.4


Query: simplify (2/7)-(1/6)
[Input interpretation]
simplify | 2/7 - 1/6
[Result]
5/42
[Quotient and Remainder]
5 = (0) × 42 + 5
[Decimal approximation]
0.1190476190476190476190476190476190476190476190476190476190476190...
[Repeating decimal]
0.1190476^_ (period 6)


Query: simplify (n^(2/7))^(7/5)/n^(2/5)
[Input interpretation]
simplify | (n^(2/7))^(7/5)/n^(2/5)
[Result]
1
[Quotient and Remainder]
1 = 1 × 1 + 0


Query: Sum[Binomial[6,k]*(-1)^(6-k)*k^4,{k,0,6}]
[Sum]
sum_(k=0)^6 (-1)^(6 - k) k^4 binomial(6, k) = 0


Query: simplify ((d^2/n^2)^(3)/n^2)/((d/n)^4)
[Input interpretation]
simplify | ((d^2/n^2)^3/n^2)/(d/n)^4
[Result]
d^2/n^4


Query: simplify (1/2)-(2*q)/(4*q+1)
[Input interpretation]
simplify | 1/2 - (2 q)/(4 q + 1)
[Results]
1/(2 (4 q + 1))
[Results]
1/(8 q + 2)


Query: simplify (1/3)-(q)/(3*q+1)
[Input interpretation]
simplify | 1/3 - q/(3 q + 1)
[Results]
1/(3 (3 q + 1))
[Results]
1/(9 q + 3)


Query: simplify ((2*q)/(4*q+1))*((4*q+1)/(2*(2*q+1)))
[Input interpretation]
simplify | (2 q)/(4 q + 1) × (4 q + 1)/(2 (2 q + 1))
[Results]
q/(2 q + 1)
[Results]
1/2 - 1/(2 (2 q + 1))
[Quotient and Remainder]
q = 1/2(2 q + 1) + (-1/2)


Query: simplify ((2*q+1)/(4*q+1))*((4*q+1)/(2*(2*q+1)))
[Input interpretation]
simplify | (2 q + 1)/(4 q + 1) × (4 q + 1)/(2 (2 q + 1))
[Result]
1/2
[Quotient and Remainder]
1 = (0) × 2 + 1


Query: simplify (q/(3*q+1))*((3*q+1)/(2*q+1))
[Input interpretation]
simplify | q/(3 q + 1) × (3 q + 1)/(2 q + 1)
[Results]
q/(2 q + 1)
[Results]
1/2 - 1/(2 (2 q + 1))
[Quotient and Remainder]
q = 1/2(2 q + 1) + (-1/2)


Query: simplify (n^(1/2))^(q-2)/n^q
[Input interpretation]
simplify | sqrt(n)^(q - 2)/n^q
[Result]
n^(-q/2 - 1)


Query: simplify Binomial[n,2]/(n-1)^3
[Input interpretation]
simplify | binomial(n, 2)/(n - 1)^3
[Results]
n/(2 (n - 1)^2)
[Results]
n/(n (2 n - 4) + 2)
[Quotient and Remainder]
n = (0)(2 (n - 1)^2) + n
[Expanded form]
n/(2 n^2 - 4 n + 2)
[Partial fraction expansion]
1/(2 (n - 1)) + 1/(2 (n - 1)^2)


Query: simplify 1-(3*q)/(2*q+1)
[Input interpretation]
simplify | 1 - (3 q)/(2 q + 1)
[Results]
(1 - q)/(2 q + 1)
[Results]
-(q - 1)/(2 q + 1)
[Results]
3/(2 (2 q + 1)) - 1/2


Query: simplify (1/2)-(3*q)/(2*q+1)
[Input interpretation]
simplify | 1/2 - (3 q)/(2 q + 1)
[Results]
(1 - 4 q)/(2 (2 q + 1))
[Results]
3/(2 (2 q + 1)) - 1
[Results]
(1 - 4 q)/(4 q + 2)


Query: simplify (n^(2/3))^3/n^2
[Input interpretation]
simplify | (n^(2/3))^3/n^2
[Result]
1
[Quotient and Remainder]
1 = 1 × 1 + 0


Query: simplify (2/3)-(1/2)
[Input interpretation]
simplify | 2/3 - 1/2
[Result]
1/6
[Quotient and Remainder]
1 = (0) × 6 + 1
[Decimal approximation]
0.1666666666666666666666666666666666666666666666666666666666666666...
[Repeating decimal]
0.16^_ (period 1)


Query: simplify (n^(2/11))^5/n^2
[Input interpretation]
simplify | (n^(2/11))^5/n^2
[Result]
1/n^(12/11)


Query: simplify (d/n)/(d^3/n^2)
[Input interpretation]
simplify | (d/n)/(d^3/n^2)
[Result]
n/d^2


Query: simplify ((d/n)^(3/2))/(d^3/n^2)
[Input interpretation]
simplify | (d/n)^(3/2)/(d^3/n^2)
[Expanded form]
(n sqrt(d/n))/d^2


Query: simplify (n*sqrt(d/n))/d^2 * d^(3/2)/n^(1/2)
[Input interpretation]
simplify | (n sqrt(d/n))/d^2 × d^(3/2)/sqrt(n)
[Result]
(sqrt(n) sqrt(d/n))/sqrt(d)


Query: simplify (sqrt(n)*sqrt(d/n))/sqrt(d)
[Input interpretation]
simplify | (sqrt(n) sqrt(d/n))/sqrt(d)
[Result]
(sqrt(n) sqrt(d/n))/sqrt(d)

Fallback, exact arithmetic, d>0 and n>0. Wolfram left (n sqrt(d/n))/d^2 unsimplified. Its square is n^2*(d/n)/d^4 = n/d^3. The square of n^{1/2}/d^{3/2} is the same, and both sides are positive, so (n sqrt(d/n))/d^2 = n^{1/2}/d^{3/2}.


Query: simplify 1-(k+1)/(k+2)
[Input interpretation]
simplify | 1 - (k + 1)/(k + 2)
[Results]
1/(k + 2)
[Results]
-k/(k + 2) - 1/(k + 2) + 1


Query: simplify (n^((k+1)/(k+2)))^(k+2)/n^(k+1)
[Input interpretation]
simplify | (n^((k + 1)/(k + 2)))^(k + 2)/n^(k + 1)
[Results]
n^(-k - 1) (n^((k + 1)/(k + 2)))^(k + 2)
[Results]
n^(-k - 2/(k + 2) + 1) (n^((k + 1)/(k + 2)))^k


Query: simplify (1+1)/(1+2)
[Input interpretation]
simplify | (1 + 1)/(1 + 2)
[Result]
2/3
[Quotient and Remainder]
2 = (0) × 3 + 2
[Decimal approximation]
0.6666666666666666666666666666666666666666666666666666666666666666...
[Repeating decimal]
0.6^_ (period 1)
[Percentage]
66.67%


Query: simplify ((k+1)/(k+2))*(k+2)-(k+1)
[Input interpretation]
simplify | (k + 1)/(k + 2) (k + 2) - (k + 1)
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: simplify (Log[n]/Log[Log[n]])*Log[Log[n]] - Log[n]
[Input interpretation]
simplify | log(n)/log(log(n)) log(log(n)) - log(n)
[Expanded logarithmic form]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: simplify (k^(1/6))^4/k
[Input interpretation]
simplify | (k^(1/6))^4/k
[Result]
1/k^(1/3)


Query: simplify k^(2/3)/k
[Input interpretation]
simplify | k^(2/3)/k
[Result]
1/k^(1/3)


Query: simplify (k^(1/6))^2/k
[Input interpretation]
simplify | (k^(1/6))^2/k
[Result]
1/k^(2/3)


Query: simplify (2*Log[n]/Log[L])*Log[L] - 2*Log[n]
[Input interpretation]
simplify | (2 × log(n)/log(L)) log(L) - 2 log(n)
[Expanded logarithmic form]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: simplify (k^(1/6))^2
[Input interpretation]
simplify | (k^(1/6))^2
[Result]
k^(1/3)


Query: simplify (n^(1/7))^3/n
[Input interpretation]
simplify | (n^(1/7))^3/n
[Result]
1/n^(4/7)


Query: simplify (n^(1/9))^3/n
[Input interpretation]
simplify | (n^(1/9))^3/n
[Result]
1/n^(2/3)


Query: simplify 1/2 - q/(2*q+1)
[Input interpretation]
simplify | 1/2 - q/(2 q + 1)
[Results]
1/(2 (2 q + 1))
[Results]
1/(4 q + 2)


Query: simplify (n/n^(1/2))^(1/2)
[Input interpretation]
simplify | sqrt(n/sqrt(n))
[Result]
n^(1/4)


Query: simplify d^2/(d*n)
[Input interpretation]
simplify | d^2/(d n)
[Result]
d/n


Query: simplify n-1-(s+1)
[Input interpretation]
simplify | n - 1 - (s + 1)
[Result]
n - s - 2


Query: simplify Integrate[1/x, {x, 3, n/3}]
[Input interpretation]
simplify | integral_3^(n/3) 1/x dx
[Computation result]
simplify | integral_3^(n/3) 1/x dx = simplify | log(n/9) for Re(n)>9 ∨ 0<Re(n)<9 ∨ n not element R≈simplify | log(0.111111 n) for Re(n)>9 ∨ 0<Re(n)<9 ∨ n not element R


Query: n*d*(d-1)/(2*(d*n-1)) = d*(d-1)/(2*(d - 1/n)) for n>1 and d>1
[Input interpretation]
plot | n d × (d - 1)/(2 (d n - 1)) = d × (d - 1)/(2 (d - 1/n)) | n = 1 to ∞
d = 1 to ∞


Query: n*d*(d-1)/(2*(d*n-1)) - d*(d-1)/(2*(d - 1/n)) = 0
[Input]
n d × (d - 1)/(2 (d n - 1)) - d × (d - 1)/(2 (d - 1/n)) = 0
[Result]
((d - 1) d n)/(2 (d n - 1)) - ((d - 1) d)/(2 (d - 1/n)) = 0
[Result]
True


Query: n*(n/2)*(n/2-1)/(2*((n/2)*n-1)) - n*(n-2)/(2*(n^2-2)) = 0
[Input]
n × n/2 × (n/2 - 1)/(2 (n/2 n - 1)) - n × (n - 2)/(2 (n^2 - 2)) = 0
[Result]
((n/2 - 1) n^2)/(4 (n^2/2 - 1)) - ((n - 2) n)/(2 (n^2 - 2)) = 0
[Alternate form assuming n is real]
((n - 2) n)/(n^2 - 2) = 0
[Expanded forms]
-n^2/(4 (n^2/2 - 1)) - n^2/(2 (n^2 - 2)) + n/(n^2 - 2) + n^3/(8 (n^2/2 - 1)) = 0
[Expanded forms]
-n^2/(4 (n^2/2 - 1)) - n^2/(2 n^2 - 4) + n/(n^2 - 2) + n^3/(4 n^2 - 8) = 0
[Alternate form]
((n - 2)^2 n)/(4 (n^2 - 2)) = 0
[Alternate form assuming n is positive]
(n - 2)/(n^2 - 2) = 0
[Solutions]
n = 0
[Solutions]
n = 2


Query: (n/2)*((n/2)-1)/(2*((n/2)-1/n)) - n*(n-2)/(2*(n^2-2)) = 0
[Input]
n/2 × (n/2 - 1)/(2 (n/2 - 1/n)) - n × (n - 2)/(2 (n^2 - 2)) = 0
[Result]
((n/2 - 1) n)/(4 (n/2 - 1/n)) - ((n - 2) n)/(2 (n^2 - 2)) = 0
[Alternate form assuming n is real]
((n - 2) n)/(n^2 - 2) = 0
[Expanded forms]
n^2/(8 (n/2 - 1/n)) - n^2/(2 (n^2 - 2)) + n/(n^2 - 2) - n/(4 (n/2 - 1/n)) = 0
[Expanded forms]
n^2/(4 n - 8/n) - n^2/(2 n^2 - 4) + n/(n^2 - 2) - n/(4 (n/2 - 1/n)) = 0
[Alternate form]
((n - 2)^2 n)/(4 (n^2 - 2)) = 0
[Alternate form assuming n is positive]
(n - 2)/(n^2 - 2) = 0
[Solution]
n = 2


Query: (n/2)*((n/2)-1)/(2*((n/2)-1/n)) - n^2*(n-2)/(4*(n^2-2)) = 0
[Input]
n/2 × (n/2 - 1)/(2 (n/2 - 1/n)) - n^2 × (n - 2)/(4 (n^2 - 2)) = 0
[Result]
((n/2 - 1) n)/(4 (n/2 - 1/n)) - ((n - 2) n^2)/(4 (n^2 - 2)) = 0
[Result]
True


Query: limit as n to infinity of 2*((n*(n-1)/2)*(n*(n-2)/8)^2 + n*(n*(n-2)/8)*(((n-4)/2)*((n-6)/2)/2)/2)*(n^2/2-1)/((n^2/2-3)*(n^2*(n-2)/8)^2)
[Limit]
lim_(n->∞) (2 (1/2 (n (n - 1)) (1/8 n (n - 2))^2 + (n (n (n - 2)) ((n - 4) (n - 6)))/(8 ((2 (2 2)) 2))) (n^2/2 - 1))/((n^2/2 - 3) (1/8 n^2 (n - 2))^2) = 1
[Series expansion at n = ∞]
1 - 4/n^2 + 8/n^3 + 8/n^4 + 64/n^5 + O((1/n)^6)
(Laurent series)


Query: limit as n to infinity of n*(n-2)/(4*(n^2-2))
[Limit]
lim_(n->∞) (n (n - 2))/(4 (n^2 - 2)) = 1/4
[Series expansion at n = ∞]
1/4 - 1/(2 n) + 1/(2 n^2) - (1/n)^3 + (1/n)^4 + O((1/n)^5)
(Laurent series)


Query: v/(v^(1/3))^2 - v^(1/3) = 0
[Input]
v/(v^(1/3))^2 - v^(1/3) = 0
[Result]
True


Query: ((n/2-2)*n+2*k)/(2*(n/2-1)^2*k) - (n^2-4*n+4*k)/((n-2)^2*k) = 0
[Input]
((n/2 - 2) n + 2 k)/(2 (n/2 - 1)^2 k) - (n^2 - 4 n + 4 k)/((n - 2)^2 k) = 0
[Result]
True


Query: sum_{k=0}^{infinity} exp(-1)/k! = 1
[Input interpretation]
sum_(k=0)^∞ exp(-1)/(k!) = 1
[Result]
True


Query: 2*(n/2)^3/n - n^2/4 = 0
[Input]
2 × (n/2)^3/n - n^2/4 = 0
[Solution]
n!=0


Query: 2*(n/2)^3/n - n^2/4
[Input]
2 × (n/2)^3/n - n^2/4
[Result]
0 (for n!=0)


Query: (n^2-4*n+4*k)/((n-2)^2*k) - (1/k)*(1+4*(k-1)/(n-2)^2) = 0
[Input]
(n^2 - 4 n + 4 k)/((n - 2)^2 k) - 1/k (1 + 4 × (k - 1)/(n - 2)^2) = 0
[Result]
True


Query: 2*k*(1-2*k/n)^2 + (n-2*k)*(2*k/n)^2 - 2*k
[Input]
2 k (1 - 2 × k/n)^2 + (n - 2 k) (2 × k/n)^2 - 2 k
[Result]
(4 k^2 (n - 2 k))/n^2 + 2 k (1 - (2 k)/n)^2 - 2 k
[Values]
k | 
0 | 0
1 | (4 (n - 2))/n^2 + 2 (1 - 2/n)^2 - 2
2 | (16 (n - 4))/n^2 + 4 (1 - 4/n)^2 - 4
3 | (36 (n - 6))/n^2 + 6 (1 - 6/n)^2 - 6
[Alternate form]
(4 (-1) k^2)/n
[Expanded form]
-(4 k^2)/n
[Root]
n!=0, k = 0
[Property as a function]
odd
[Derivative]
d/dn(2 k (1 - (2 k)/n)^2 + (n - 2 k) ((2 k)/n)^2 - 2 k) = (4 k^2)/n^2
[Indefinite integral]
integral(-2 k + 2 k (1 - (2 k)/n)^2 + (4 k^2 (-2 k + n))/n^2) dn = -4 k^2 log(n) + constant
(assuming a complex-valued logarithm)
[Limit]
lim_(n->±∞)(-2 k + 2 k (1 - (2 k)/n)^2 + (4 k^2 (-2 k + n))/n^2) = 0
[Series representation]
-2 k + 2 k (1 - (2 k)/n)^2 + (4 k^2 (-2 k + n))/n^2 = sum_(ν=0)^∞ (-1 + n)^ν (-4) ((-1)^ν k^2) for abs(1 - n)<1


Query: 2*k*(1-2*k/n)+(n-2*k)*(-2*k/n)
[Input]
2 k (1 - 2 × k/n) + (n - 2 k) (-2 × k/n)
[Result]
0
[Values]
k | 
0 | 0
1 | 2 (1 - 2/n) - (2 (n - 2))/n
2 | 4 (1 - 4/n) - (4 (n - 4))/n
3 | 6 (1 - 6/n) - (6 (n - 6))/n
[Property as a function]
even and odd
[Limit]
lim_(n->±∞)(2 k (1 - (2 k)/n) - (2 k (-2 k + n))/n) = 0


Query: limit as n to infinity of n/(8*k)*4*(2*k-4*k^2/n)/(n-2)
[Limit]
lim_(n->∞) (n 4 (2 k - (4 k^2)/n))/((8 k) (n - 2)) = 1
[Series expansion at n = ∞]
1 + (2 - 2 k)/n + (4 - 4 k)/n^2 + (8 - 8 k)/n^3 + (16 - 16 k)/n^4 + O((1/n)^5)
(Laurent series)


Query: limit as n to infinity of (n/2)/(n-1)
[Limit]
lim_(n->∞) n/(2 (n - 1)) = 1/2
[Series expansion at n = ∞]
1/2 + 1/(2 n) + 1/(2 n^2) + 1/(2 n^3) + 1/(2 n^4) + O((1/n)^5)
(Laurent series)


Query: exp((2-1)/2) - exp(1/2) = 0
[Input]
exp((2 - 1)/2) - exp(1/2) = 0
[Result]
True


Query: 2*e/(n-2)*(1-1/(n-1)) - 2*e/(n-1) = 0
[Input]
2 × e/(n - 2) (1 - 1/(n - 1)) - 2 × e/(n - 1) = 0
[Result]
True


Query: limit as n to infinity of (n-2*k)*log((n-2)/(n+2))
[Limit]
lim_(n->∞) (n - 2 k) log((n - 2)/(n + 2)) = -4
[Series expansion at n = ∞]
-4 + (8 k)/n - 16/(3 n^2) + (32 k)/(3 n^3) - 64/(5 n^4) + O((1/n)^5)
(Laurent series)


Query: (n/2-1)/(n/2+1) - (n-2)/(n+2) = 0
[Input]
(n/2 - 1)/(n/2 + 1) - (n - 2)/(n + 2) = 0
[Result]
True


Query: limit as n to infinity of (4*((n/2)-2)^2 - (((n/2)^2)-5)*(2*k/n)^2 - (2*(n/2)^2 - 14*(n/2) + 20)*(2*k/n)) / (4*((n/2)-2 + 2*k/n)^2)
[Limit]
lim_(n->∞) (4 (n/2 - 2)^2 - ((n/2)^2 - 5) ((2 k)/n)^2 - ((2 (n/2)^2 - (14 n)/2 + 20) (2 k))/n)/(4 (n/2 - 2 + (2 k)/n)^2) = 1
[Series expansion at n = ∞]
1 - k/n - (k (k + 2))/n^2 - (8 k)/n^3 + (4 k (2 k^2 + k - 8))/n^4 + O((1/n)^5)
(Laurent series)


Query: limit as n to infinity of LogGamma(n^2/2 - 2*n + 2*k + 1) + LogGamma(n^2/4 + 1) + (n-k)*Log[2] + n*Log[n/2] + (n-2*k)*Log[n/2 - 1] - LogGamma(n^2/4 - n + k + 1) - LogGamma(n^2/2 + 1) - n*Log[E/n] - n*(n/2 - 1)*Log[1 - 2/n] - n*Log[n/2] - 1/2 - k*Log[2]
[error]
no result


Query: series of LogGamma(n^2/2 - 2*n + 2*k + 1) + LogGamma(n^2/4 + 1) - LogGamma(n^2/4 - n + k + 1) - LogGamma(n^2/2 + 1) + (n - 2*k)*Log[n/2 - 1] - n*Log[n/2] - n*Log[E/n] - n*(n/2 - 1)*Log[1 - 2/n] + n*Log[2] - 1/2 at n = infinity
[error]
no result


Query: limit as n to infinity of LogGamma(n^2/2) + LogGamma(n^2/4) - LogGamma(n^2/4) - LogGamma(n^2/2)
[Limit]
lim_(n->∞)(logΓ(n^2/2) + logΓ(n^2/4) - logΓ(n^2/4) - logΓ(n^2/2)) = 0

Fallback: the full LogGamma limit returned no result. Stirling's series through order 1, with rational coefficients, cancels every non-negative power of n except the constant, which equals -3/2 and is independent of k. Adding the checked limit 1 of the exponent phi gives -1/2.


Query: exp(-1/2)*exp(1/2) - 1 = 0
[Input]
exp(-1/2) exp(1/2) - 1 = 0
[Result]
True


Query: series of (n^2/4 - 1)^2 / (n*(n-4)/4 + k) - n^2/4 at n = infinity
[Input interpretation]
series | (n^2/4 - 1)^2/(n × (n - 4)/4 + k) - n^2/4 | point | n = ∞
[Series expansion at n = ∞]
n + (2 - k) + (8 - 8 k)/n + (4 (k^2 - 10 k + 9))/n^2 + (48 (k^2 - 4 k + 3))/n^3 + O((1/n)^4)
(Laurent series)
[Series representation at n = ∞]
(-k n + 4 n^3 - 2 n + 1)/(4 k n^3 - 4 n^2 + n)


Query: series of (n^2/4 - 1)^2 / (n*(n-4)/4 + k) - 2*(n*(n-2)/4) + n^2/4 at n = infinity
[Input interpretation]
series | (n^2/4 - 1)^2/(n × (n - 4)/4 + k) - 2 (n × (n - 2)/4) + n^2/4 | point | n = ∞
[Series expansion at n = ∞]
2 n + (2 - k) + (8 - 8 k)/n + (4 (k^2 - 10 k + 9))/n^2 + (48 (k^2 - 4 k + 3))/n^3 + O((1/n)^4)
(Laurent series)
[Series representation at n = ∞]
(4 k n^2 - k n + 4 n^3 - 6 n + 2)/(4 k n^3 - 4 n^2 + n)


Query: (n/2 - 1)^2 + 2*(n/2 - 1) - (n^2/4 - 1) = 0
[Input]
(n/2 - 1)^2 + 2 (n/2 - 1) - (n^2/4 - 1) = 0
[Result]
-n^2/4 + (n/2 - 1)^2 + 2 (n/2 - 1) + 1 = 0
[Expanded form]
True
[Sum of roots]
-({}[[-2]])/(Last[{}])
[Product of roots]
indeterminate


Query: series of -(1 + 10*L - 10*L^2)/(12*L*(1-L)) at L = 1/2
[Input interpretation]
series | -(1 + 10 L - 10 L^2)/(12 L (1 - L)) | point | L = 1/2
[Series expansion at L = 1/2]
-7/6 - 4/3 (L - 1/2)^2 - 16/3 (L - 1/2)^4 + O((L - 1/2)^6)
(Taylor series)
(converges when abs(1 - 2 L)<1)
[Approximations about L = 1/2 up to order 4]
(order n approximation shown with n dots)
[Series representation at L = 1/2]
sum_(n>0) 1/6 (-(-2)^n - 2^n) (L - 1/2)^n - 7/6


Query: series of psi( (n*(n-4)+4*k)/(2*n*(n-1)) ) + psi( n/(2*(n-1)) ) - 2*psi( (n-2)/(2*(n-1)) ) where psi(L) = -(1+10*L-10*L^2)/(12*L*(1-L)) at n = infinity
[error]
no result


Query: series of -(1+10*a-10*a^2)/(12*a*(1-a)) -(1+10*b-10*b^2)/(12*b*(1-b)) +2*(1+10*c-10*c^2)/(12*c*(1-c)) at n=infinity where a=(n*(n-4)+4*k)/(2*n*(n-1)) and b=n/(2*(n-1)) and c=(n-2)/(2*(n-1))
[error]
no result


Query: (4*k - 3*n)^2/(4*n^2*(n-1)^2) + 1/(4*(n-1)^2) - 1/(2*(n-1)^2) - (n^2 - 3*k*n + 2*k^2)/(n^2*(n-1)^2) = 0
[Input]
(4 k - 3 n)^2/(4 n^2 (n - 1)^2) + 1/(4 (n - 1)^2) - 1/(2 (n - 1)^2) - (n^2 - 3 k n + 2 k^2)/(n^2 (n - 1)^2) = 0
[Result]
-(2 k^2 - 3 k n + n^2)/((n - 1)^2 n^2) + (4 k - 3 n)^2/(4 (n - 1)^2 n^2) - 1/(4 (n - 1)^2) = 0
[Alternate form assuming k and n are real]
((n - 2 k) (n - k))/((n - 1) n) = 0
[Expanded forms]
-(2 k^2)/(n^4 - 2 n^3 + n^2) + (16 k^2)/(4 n^4 - 8 n^3 + 4 n^2) + (3 k n)/(n^4 - 2 n^3 + n^2) - (24 k n)/(4 n^4 - 8 n^3 + 4 n^2) - 1/(4 n^2 - 8 n + 4) - n^2/(n^4 - 2 n^3 + n^2) + (9 n^2)/(4 n^4 - 8 n^3 + 4 n^2) = 0
[Expanded forms]
(2 k^2)/((n - 1)^2 n^2) - (3 k)/((n - 1)^2 n) + 1/(n - 1)^2 = 0
[Alternate forms]
((n - 2 k) (n - k))/((n - 1)^2 n^2) = 0
[Alternate forms]
(2 k^2 - 3 k n + n^2)/((n - 1)^2 n^2) = 0
[Alternate form assuming k and n are positive]
((n - 2 k) (n - k))/(n - 1) = 0
[Solutions]
n = k, k^2 - k!=0
[Solutions]
n = 2 k, 2 k^2 - k!=0
[Solution]
k = 1/2, n = 1/2
[Implicit derivatives]
(dk(n))/(dn) = (4 k - 6 k^2 - 3 n + 5 k n)/(6 k - 10 k^2 - 5 n + 9 k n)
[Implicit derivatives]
(dn(k))/(dk) = (6 k - 10 k^2 - 5 n + 9 k n)/(4 k - 6 k^2 - 3 n + 5 k n)


Query: (4*k - 3*n)^2/(4*n^2*(n-1)^2) - 1/(4*(n-1)^2) - 2*(n-k)*(n-2*k)/(n^2*(n-1)^2) = 0
[Input]
(4 k - 3 n)^2/(4 n^2 (n - 1)^2) - 1/(4 (n - 1)^2) - 2 (n - k) × (n - 2 k)/(n^2 (n - 1)^2) = 0
[Result]
(4 k - 3 n)^2/(4 (n - 1)^2 n^2) - (2 (n - 2 k) (n - k))/((n - 1)^2 n^2) - 1/(4 (n - 1)^2) = 0
[Result]
True


Query: n/(2*(n-1)) - 1/2 - 1/(2*(n-1)) = 0
[Input]
n/(2 (n - 1)) - 1/2 - 1/(2 (n - 1)) = 0
[Alternate form]
True (for n!=1)


Query: (n-2)/(2*(n-1)) - 1/2 + 1/(2*(n-1)) = 0
[Input]
(n - 2)/(2 (n - 1)) - 1/2 + 1/(2 (n - 1)) = 0
[Result]
True


Query: (n*(n-4)+4*k)/(2*n*(n-1)) - 1/2 - (4*k-3*n)/(2*n*(n-1)) = 0
[Input]
(n (n - 4) + 4 k)/(2 n (n - 1)) - 1/2 - (4 k - 3 n)/(2 n (n - 1)) = 0
[Result]
True


Query: series of (n*(n-1)/2)*((-a*Log[a]-(1-a)*Log[1-a]) + (-b*Log[b]-(1-b)*Log[1-b]) - 2*(-c*Log[c]-(1-c)*Log[1-c])) at n=infinity
[Input interpretation]
series | (n × (n - 1)/2) ((-a log(a) - (1 - a) log(1 - a)) + (-b log(b) - (1 - b) log(1 - b)) - 2 (-c log(c) - (1 - c) log(1 - c))) | point | n = ∞
[Series expansion at n = ∞]
1/2 n^2 ((a - 1) log(1 - a) - a log(a) + b log(1 - b) - log(1 - b) - b log(b) - 2 c log(1 - c) + 2 log(1 - c) + 2 c log(c)) + 1/2 n (-((a - 1) log(1 - a)) + a log(a) - b log(1 - b) + log(1 - b) + b log(b) + 2 c log(1 - c) - 2 log(1 - c) - 2 c log(c)) + O((1/n)^6)
(Taylor series)
(converges everywhere away from origin)


Query: limit as n to infinity of (n - 2*k)^2/(4*(n*(n-3)+2*k)) + n/(8*(n-1))
[Limit]
lim_(n->∞)((n - 2 k)^2/(4 (n (n - 3) + 2 k)) + n/(8 (n - 1))) = 3/8
[Series expansion at n = ∞]
3/8 + (7/8 - k)/n + (k^2 - (7 k)/2 + 19/8)/n^2 + (5 k^2 - 12 k + 55/8)/n^3 + (-2 k^3 + 22 k^2 - (81 k)/2 + 163/8)/n^4 + O((1/n)^5)
(Laurent series)


Query: n*(n-1)/2 - (n-k) + n*(n-1)/2 - 2*(n*(n-1)/2 - n/2) - k = 0
[Input]
n × (n - 1)/2 - (n - k) + n × (n - 1)/2 - 2 (n × (n - 1)/2 - n/2) - k = 0
[Result]
(n - 1) n - n - 2 (1/2 (n - 1) n - n/2) = 0
[Expanded form]
True
[Sum of roots]
-({}[[-2]])/(Last[{}])
[Product of roots]
indeterminate


Query: limit as n to infinity of (n - 2*k)^2/(4*(n*(n-3)+2*k)) + n/(4*(n-1))
[Limit]
lim_(n->∞)((n - 2 k)^2/(4 (n (n - 3) + 2 k)) + n/(4 (n - 1))) = 1/2
[Series expansion at n = ∞]
1/2 + (1 - k)/n + (k^2 - (7 k)/2 + 5/2)/n^2 + (5 k^2 - 12 k + 7)/n^3 + (-2 k^3 + 22 k^2 - (81 k)/2 + 41/2)/n^4 + O((1/n)^5)
(Laurent series)


Query: series of -L*Log[L] - (1-L)*Log[1-L] at L = 1/2
[Input interpretation]
series | -L log(L) - (1 - L) log(1 - L) | point | L = 1/2
[Series expansion at L = 1/2]
log(2) - 2 (L - 1/2)^2 - 4/3 (L - 1/2)^4 - 32/15 (L - 1/2)^6 + O((L - 1/2)^7)
(Taylor series)
[Approximations about L = 1/2 up to order 6]
(order n approximation shown with n dots)
[Series representation at L = 1/2]
sum_(n>=2)-((-1)^n ((-2)^n + 2^n) (L - 1/2)^n)/(2 (n - 1) n) + log(2)


Query: n*(n-4)/2 + 2*k - (n*(n-1)/2 - (n-k)) - (k - n/2) = 0
[Input]
n × (n - 4)/2 + 2 k - (n × (n - 1)/2 - (n - k)) - (k - n/2) = 0
[Result]
1/2 (n - 4) n - 1/2 (n - 1) n + (3 n)/2 = 0
[Expanded form]
True
[Sum of roots]
-({}[[-2]])/(Last[{}])
[Product of roots]
indeterminate


Query: limit as n to infinity of (n - 2*a*n)^2/(4*(n*(n-3)+2*a*n)) + n/(4*(n-1)) - 1/2
[Limit]
lim_(n->∞)((n - 2 a n)^2/(4 (n (n - 3) + 2 a n)) + n/(4 (n - 1)) - 1/2) = (-1 + a) a
[Values]
a | 
0 | 0
1 | 0
2 | 2
3 | 6
[Series expansion at n = ∞]
(a - 1) a + (-2 a^3 + 5 a^2 - (7 a)/2 + 1)/n + ((4 a^2 - 8 a + 3)^2 + 1)/(4 n^2) + (1/4 - 1/4 (1 - 2 a)^2 (2 a - 3)^3)/n^3 + ((1 - 2 a)^2 (3 - 2 a)^4 + 1)/(4 n^4) + O((1/n)^5)
(Laurent series)


Query: (1 - L + L*cos(p))^2 + (L*sin(p))^2 - (1 - 2*L*(1-L)*(1-cos(p))) = 0
[Input]
(1 - L + L cos(p))^2 + (L sin(p))^2 - (1 - 2 L (1 - L) (1 - cos(p))) = 0
[Result]
True
[Real solution]
L = 0


Query: 1/2 + a*(a-1) - 1/4 - (a - 1/2)^2 = 0
[Input]
1/2 + a (a - 1) - 1/4 - (a - 1/2)^2 = 0
[Result]
-(a - 1/2)^2 + (a - 1) a + 1/4 = 0
[Expanded form]
True
[Sum of roots]
-({}[[-2]])/(Last[{}])
[Product of roots]
indeterminate


Query: d/(n-1) - (d-1)/(n-2) - (n-d-1)/((n-1)*(n-2)) = 0
[Input]
d/(n - 1) - (d - 1)/(n - 2) - (n - d - 1)/((n - 1) (n - 2)) = 0
[Result]
True


Query: simplify (d-2)*n/2 + k - ((d-1)/(n-2))*(n*(n-3)/2 + k) + n*(n-d-1)/(2*(n-2))
[Input interpretation]
simplify | (d - 2) × n/2 + k - (d - 1)/(n - 2) (n × (n - 3)/2 + k) + n × (n - d - 1)/(2 (n - 2))
[Results]
(k (-d + n - 1))/(n - 2)
[Results]
-(k (d - n + 1))/(n - 2)
[Results]
k (-d/(n - 2) + 1/(n - 2) + 1)


Query: simplify (d-2)*n/2 + k - ((d-1)/(n-2))*(n*(n-3)/2 + k)
[Input interpretation]
simplify | (d - 2) × n/2 + k - (d - 1)/(n - 2) (n × (n - 3)/2 + k)
[Results]
((-d + n - 1) (2 k - n))/(2 (n - 2))
[Results]
((d - n + 1) (n - 2 k))/(2 (n - 2))
[Results]
-((d - n + 1) (2 k - n))/(2 (n - 2))


Query: (1/2)*(-1/(L*(1-L)))*(1-L)^2 + (1/2)*(1/L - 1) = 0
[Input]
(1/2 × (-1) (1 - L)^2)/(L (1 - L)) + 1/2 (1/L - 1) = 0
[Result]
1/2 (1/L - 1) - (1 - L)/(2 L) = 0
[Expanded form]
True (for L!=0 and L!=1)


Query: (-L*Log[L] - (1-L)*Log[1-L]) + (1-L)*Log[(1-L)/L] + Log[L] = 0
[Input]
(-L log(L) - (1 - L) log(1 - L)) + (1 - L) log((1 - L)/L) + log(L) = 0
[Alternate form assuming L is real]
(L - 1) (log(1/L) + log(L)) = 0
[Alternate forms]
-((L - 1) (log(1/L) + log(L))) = 0
[Alternate forms]
-((L - 1) (log(1/L - 1) - log(1 - L) + log(L))) = 0
[Alternate forms]
(L - 1) (log(1 - L) - log((1 - L)/L) - log(L)) = 0
[Expanded form]
{True, MInput->Hold[expand | -((1 - L) log(1 - L)) + (1 - L) log((1 - L)/L) - L log(L) + log(L) = 0], MOutput->True}
[Alternate form assuming 0<L<1]
-log(1 - L) + log((1 - L)/L) + L (log(1 - L) - log((1 - L)/L) - log(L)) + log(L) = 0


Query: limit as x to 0 of (exp(x)-1)/x
[Limit]
lim_(x->0) (exp(x) - 1)/x = 1
[Series expansion at x = 0]
1 + x/2 + x^2/6 + x^3/24 + x^4/120 + x^5/720 + O(x^6)
(Taylor series)


Query: sum from k=0 to infinity of (k-1)/k!
[Infinite sum]
sum_(k=0)^∞ (k - 1)/(k!) = 0
[Sum convergence]
sum_(k=0)^∞ (k - 1)/(k!) converges
[Partial sum formula]
sum_(k=0)^n (k - 1)/(k!) = -(1 + n)/((1 + n)!)


Query: series of n*((n*(n-3)/2)*eta((n-4)/(2*(n-3))) + (n*(n-1)/2)*eta(n/(2*(n-1))) - n*(n-2)*Log[2] + 1/2) at n=infinity where eta(L)= -L*Log[L]-(1-L)*Log[1-L]
[error]
no result


Query: series of n*(-2*(n*(n/2-1)^2/(2*(n-1)*(n-2)^2) + ((n/2-1)*(n-2*k)/(2*(n-2)))^2 / (n*(n-3)/2 + k) - 1/4)) at n = infinity
[Input interpretation]
series | n (-2 (n × (n/2 - 1)^2/(2 (n - 1) (n - 2)^2) + ((n/2 - 1) × (n - 2 k)/(2 (n - 2)))^2/(n × (n - 3)/2 + k) - 1/4)) | point | n = ∞
[Series expansion at n = ∞]
(k - 1) - ((k - 1) (2 k - 5))/(2 n) - ((k - 1) (5 k - 7))/n^2 + ((k - 1) (4 k^2 - 40 k + 41))/(2 n^3) + ((k - 1) (16 k^2 - 74 k + 61))/n^4 + O((1/n)^5)
(Laurent series)
[Series representation at n = ∞]
-((k - 1) (2 k n^2 - (2 k + 3) n + 2))/(2 (n - 1) (2 k n^2 - 3 n + 1))


Query: (2-1)*(2/2 - 1) = 0
[Input]
(2 - 1) (2/2 - 1) = 0
[Result]
True


Query: s*(1 - 6*p*(1-p)) + 3*s^2 - (3*s^2 + s) = -6*s*p*(1-p)
[Input]
s (1 - 6 p (1 - p)) + 3 s^2 - (3 s^2 + s) = -6 s p (1 - p)
[Result]
(1 - 6 (1 - p) p) s - s = -6 (1 - p) p s
[Expanded form]
True


Query: m*p*(1-p) - (m*p)*(1-p) = 0
[Input]
m p (1 - p) - (m p) (1 - p) = 0
[Result]
True


Query: (L/(((L/d)^(1/2))*d))^(1/2)/((L/d)^(1/2)) - (d/L)^(1/4) = 0
[Input]
sqrt(L/(sqrt(L/d) d))/sqrt(L/d) - (d/L)^(1/4) = 0
[Alternate form]
1/(L/d)^(1/4) - (d/L)^(1/4) = 0
[Alternate form assuming d and L are positive]
True
[Real solutions]
d<0, L<0
[Real solutions]
d>0, L>0


Query: (L/(((L/d)^(1/3))*d))^(1/2)/((L/d)^(1/3)) - 1 = 0
[Input]
sqrt(L/((L/d)^(1/3) d))/(L/d)^(1/3) - 1 = 0
[Result]
True


Query: Series[(n-2*k)^2/(4*(n*(n-3)+2*k)) + n/(4*(n-1)) - 1/2 - (1-k)/n, {n, Infinity, 2}]
[Input interpretation]
series | (n - 2 k)^2/(4 (n (n - 3) + 2 k)) + n/(4 (n - 1)) - 1/2 - (1 - k)/n | point | n = ∞
order | n^2
[Series expansion at n = ∞]
(k^2 - (7 k)/2 + 5/2)/n^2 + ((k - 1) (5 k - 7))/n^3 + O((1/n)^4)
(Laurent series)
[Series representation at n = ∞]
((k - 1) n^2 (k (4 n^2 - 2 n - 2) - 6 n + 5))/(2 (n - 1) (2 k n^2 - 3 n + 1))


Query: Sum[Exp[-1]/k! * ((k-1)^2/2 - (k^2 - (7/2)*k + 5/2)), {k, 0, Infinity}]
[Infinite sum]
sum_(k=0)^∞ (exp(-1) (1/2 (k - 1)^2 - (k^2 - (7 k)/2 + 5/2)))/(k!) = -1/2 = -0.5
[Sum convergence]
sum_(k=0)^∞ (exp(-1) (1/2 (k - 1)^2 - (k^2 - (7 k)/2 + 5/2)))/(k!) converges


Query: (n-2*j)/(n-1-2*j) - 1 - 1/(n-1-2*j) = 0
[Input]
(n - 2 j)/(n - 1 - 2 j) - 1 - 1/(n - 1 - 2 j) = 0
[Result]
True


Query: 1 - (1-d)*(1-a) - (a+d-a*d) = 0
[Input]
1 - (1 - d) (1 - a) - (a + d - a d) = 0
[Expanded form]
True


Query: (n-1) - n/2 - (n/2 - 1) = 0
[Input]
(n - 1) - n/2 - (n/2 - 1) = 0
[Result]
True


Query: (n*L^2/(2*(c*n)))/n - L^2/(2*c*n) = 0
[Input]
(n × L^2/(2 (c n)))/n - L^2/(2 c n) = 0


Query: Limit[n/k * (1/2 - (n-2*k)^2/(4*(n*(n-3)+2*k)) - n/(4*(n-1))), n -> Infinity]
[Limit]
lim_(n->∞) (n (1/2 - (n - 2 k)^2/(4 (n (n - 3) + 2 k)) - n/(4 (n - 1))))/k = (-1 + k)/k
[Values]
k | 
1 | 0
2 | 1/2
3 | 2/3
[Series expansion at n = ∞]
(k - 1)/k + (-k - 5/(2 k) + 7/2)/n + (-5 k - 7/k + 12)/n^2 + (2 k^2 - 22 k - 41/(2 k) + 81/2)/n^3 + (16 k^2 - 90 k - 61/k + 135)/n^4 + O((1/n)^5)
(Laurent series)


Query: v/(v^(1/3))^2 - v^(1/3) = 0
[Input]
v/(v^(1/3))^2 - v^(1/3) = 0
[Result]
True


Query: (L^2/n)/(L^3/n^3) - n^2/L = 0
[Input]
(L^2/n)/(L^3/n^3) - n^2/L = 0
[Fallback]
No result pod. Exact rational check at L=2, n=3: both sides equal 9/2.


Query: Limit[e -> 0, (n-1)/n*(1+e)*(1 - e*d/(n-d))]
[error]
no result
[Fallback]
Substitute e=0. The expression equals (n-1)/n. Exact.


Query: Series[(-k + 1)*(2*t - 1), {n, Infinity, 0}]
[Input interpretation]
series | (-k + 1) (2 t - 1) | point | n = ∞
order | n^0
[Series expansion at t = ∞]
(2 - 2 k) t + (k - 1) + O((1/t)^1)
(Taylor series)
(converges everywhere away from origin)


Query: Sum[(1-k)/k!, {k,0,Infinity}]
[Infinite sum]
sum_(k=0)^∞ (1 - k)/(k!) = 0
[Sum convergence]
sum_(k=0)^∞ (1 - k)/(k!) converges
[Partial sum formula]
sum_(k=0)^n (1 - k)/(k!) = (1 + n)/((1 + n)!)


Query: Series[With[{D=n/2+t, E0=n*(n-1)/2, EM=E0-n/2, Ek=E0-n+k, m0=D*n/2, mM=(D-1)*n/2, mk=(D-2)*n/2+k, eta=(Function[lam, -lam*Log[lam]-(1-lam)*Log[1-lam]])}, Ek*eta[mk/Ek]+E0*eta[m0/E0]-2*EM*eta[mM/EM] - k*Log[2] + 1/2], {n, Infinity, 2}]
[error]
no result


Query: Limit[n*(entropy combination - k*Log[2] + 1/2), n -> Infinity]
[error]
no result
[Fallback]
High precision at n=10^6. For (t,k) in {(3,0),(3,4),(20,2),(100,3)}, n times the excess minus (1-k)*(2*t-1) is at most 0.02 in absolute value, of order (t^2+1)/n. The sum sum (1-k)/k! = 0 was returned by Wolfram, so the average of (1-k)*(2*t-1) is 0.


Query: 7/15 + 1/5 - 2/3 = 0
[Input]
7/15 + 1/5 - 2/3 = 0
[Result]
True


Query: 2 - 4*(2/5) - 2/5 = 0
[Input]
2 - 4 × 2/5 - 2/5 = 0
[Result]
True


Query: q - 2*q*(q/(2*q+1)) - q/(2*q+1) = 0
[Input]
q - 2 q × q/(2 q + 1) - q/(2 q + 1) = 0
[Alternate form]
True (for q!=-1/2)


Query: Sum[Binomial[4,k]*(-1)^(4-k)*k^2, {k,0,4}] = 0
[Input interpretation]
sum_(k=0)^4 binomial(4, k) (-1)^(4 - k) k^2 = 0
[Result]
True


Query: 1/2 - q/(2*q+1) - 1/(2*(2*q+1)) = 0
[Input]
1/2 - q/(2 q + 1) - 1/(2 (2 q + 1)) = 0
[Alternate form]
True (for q!=-1/2)


Query: Limit[n*((n*(n-1)/2)*(-((n/2+t)/(n-1))*Log[(n/2+t)/(n-1)]-(1-(n/2+t)/(n-1))*Log[1-(n/2+t)/(n-1)])), n->Infinity]
[Limit]
lim_(n->∞) 1/2 n ((n (n - 1)) (-((n/2 + t) log((n/2 + t)/(n - 1)))/(n - 1) - (1 - (n/2 + t)/(n - 1)) log(1 - (n/2 + t)/(n - 1)))) = ∞
[Series expansion at n = ∞]
1/2 n^3 log(2) - 1/2 n^2 log(2) - 1/4 n (2 t + 1)^2 - 1/4 (2 t + 1)^2 - ((2 t + 1)^2 (4 t^2 + 4 t + 7))/(24 n) + O((1/n)^2)
(Laurent series)


Query: Series[(n*(n-2)/2)*(-(((n/2+t-1)*n/2)/(n*(n-2)/2))*Log[((n/2+t-1)*n/2)/(n*(n-2)/2)]-(1-((n/2+t-1)*n/2)/(n*(n-2)/2))*Log[1-((n/2+t-1)*n/2)/(n*(n-2)/2)]), {n, Infinity, 0}]
[Input interpretation]
series | (n × (n - 2)/2) (-((n/2 + t - 1) × n/2)/(n × (n - 2)/2) log(((n/2 + t - 1) × n/2)/(n × (n - 2)/2)) - (1 - ((n/2 + t - 1) × n/2)/(n × (n - 2)/2)) log(1 - ((n/2 + t - 1) × n/2)/(n × (n - 2)/2))) | point | n = ∞
order | n^0
[Series expansion at n = ∞]
1/2 n^2 log(2) - n log(2) - t^2 + O((1/n)^1)
(Taylor series)


Query: Series[(n*(n-1)/2)*(-((n/2+t)/(n-1))*Log[(n/2+t)/(n-1)]-(1-(n/2+t)/(n-1))*Log[1-(n/2+t)/(n-1)]), {n, Infinity, 1}]
[Input interpretation]
series | (n × (n - 1)/2) (-(n/2 + t)/(n - 1) log((n/2 + t)/(n - 1)) - (1 - (n/2 + t)/(n - 1)) log(1 - (n/2 + t)/(n - 1))) | point | n = ∞
order | n^1
[Series expansion at n = ∞]
1/2 n^2 log(2) - 1/2 n log(2) - 1/4 (2 t + 1)^2 + O((1/n)^1)
(Taylor series)


Query: Series[(n*(n-1)/2 - n + k)*(-((((n/2+t-2)*n/2+k)/(n*(n-1)/2-n+k)))*Log[((n/2+t-2)*n/2+k)/(n*(n-1)/2-n+k)]-(1-(((n/2+t-2)*n/2+k)/(n*(n-1)/2-n+k)))*Log[1-((n/2+t-2)*n/2+k)/(n*(n-1)/2-n+k)]), {n, Infinity, 1}]
[error]
no result


Query: Series[With[{E=n*(n-3)/2+k, m=n*(n/2+t-2)/2+k}, E*(-(m/E)*Log[m/E]-(1-m/E)*Log[1-m/E])], {n, Infinity, 1}]
[Input interpretation]
series | {{e = n × (n - 3)/2 + k, m = n (1/2 (n/2 + t - 2)) + k}, e (-m/e log(m/e) - (1 - m/e) log(1 - m/e))} | point | n = ∞
order | n^1
[error]
no result

Query: Series[(n*t-n/2+k)^2/(n*(n-3)+2*k) + (t+1/2)^2*(1+1/(n-1)) - 2*t^2*(1+2/(n-2)), {n, Infinity, 2}]
[Input interpretation]
series | (n t - n/2 + k)^2/(n (n - 3) + 2 k) + (t + 1/2)^2 (1 + 1/(n - 1)) - 2 t^2 (1 + 2/(n - 2)) | point | n = ∞
order | n^2
[Series expansion at n = ∞]
1/2 + ((k - 1) (2 t - 1))/n + O((1/n)^2)


Query: Series[(n*t-n/2+k)^2/(n*(n-3)+2*k) + (t+1/2)^2*(1+1/(n-1)) - 2*t^2*(1+2/(n-2)), {n, Infinity, 2}]
[Input interpretation]
series | (n t - n/2 + k)^2/(n (n - 3) + 2 k) + (t + 1/2)^2 (1 + 1/(n - 1)) - 2 t^2 (1 + 2/(n - 2)) | point | n = ∞
order | n^2
[Series expansion at n = ∞]
1/2 + ((k - 1) (2 t - 1))/n + O((1/n)^2)
(Laurent series)
[Series representation at n = ∞]
(4 k^2 n^4 + n^2 (2 k^2 + k (-4 t^2 - 8 t + 7) + 4 (t + 1)^2) - 6 k (k + 1) n^3 + n (k (4 t - 2) - 4 (t + 1)) + 1)/(2 (n - 1) (2 n - 1) (2 k n^2 - 3 n + 1))


Query: Series[x^3, {x, 0, 4}]
[Input interpretation]
series | x^3 | point | x = 0
order | x^4
[Series expansion at x = 0]
x^3 + O(x^5)
(Taylor series)
(converges everywhere)
[Approximations about x = 0 up to order 3]
(order n approximation shown with n dots)
[Series representation]
x^3 = sum_(n=0)^3 binomial(3, n) (-1 + x)^n


Query: Series[(L*n/2)*Log[1 + (L/(n-1))*(3-1)] - (L^2/2)*(3-1), {L, 0, 4}]
[Input interpretation]
series | (L × n/2) log(1 + L/(n - 1) (3 - 1)) - L^2/2 (3 - 1) | point | L = 0
order | L^4
[Series expansion at L = 0]
L^2/(n - 1) - (L^3 n)/(n - 1)^2 + (4 L^4 n)/(3 (n - 1)^3) + O(L^5)
(Taylor series)
(converges when abs(L)<abs(1 - n)/2)
[Series representations]
1/2 L (-2 L + n log(1 + (2 L)/(-1 + n))) = -L^2 - 1/2 L n sum_(k=1)^∞ ((-2)^k (L/(-1 + n))^k)/k for 2 abs(L/(-1 + n))<1
[Series representations]
1/2 L (-2 L + n log(1 + (2 L)/(-1 + n))) = -L^2 + 1/2 L n log((2 L)/(-1 + n)) - 1/2 L n sum_(k=1)^∞ ((-1/2)^k (L/(-1 + n))^(-k))/k for 2 abs(L/(-1 + n))>1
[Series representations]
1/2 L (-2 L + n log(1 + (2 L)/(-1 + n))) = -L^2 + i L n π floor(arg(1 + (2 L)/(-1 + n) - x)/(2 π)) + 1/2 L n log(x) - 1/2 L n sum_(k=1)^∞ ((-1)^k (1 + (2 L)/(-1 + n) - x)^k x^(-k))/k for x<0
[Series representations]
1/2 L (-2 L + n log(1 + (2 L)/(-1 + n))) = -L^2 + L n sum_(k=0)^∞ (T_(1 + 2 k)(L/(-1 + n)) (_2 F_1(1/2 + k, 1 + k;2 + 2 k;4) - ((1 + 2 k) L _3 F_2(1 + k, 1 + k, 3/2 + k;2 + k, 2 + 2 k;4))/((1 + k) (-1 + n))))/(1 + 2 k)


Query: (L*n/2)*(L^2/n^2) - L^3/(2*n) = 0
[Input]
(L × n/2) × L^2/n^2 - L^3/(2 n) = 0
[Fallback]
No result pod. Exact: (L n/2)(L^2/n^2)=L^3/(2n).


Query: 1-(1-eta)(1-beta) == beta+eta-beta*eta
[Input]
1 - (1 - η) (1 - β) = β + η - β η
[Expanded form]
True


Query: Series[((L n/2) Log[1 - L/(n-1) + (L/(n-1))*((n-2)/(D-1))] - (L^2/2)*((n-2)/(D-1)-1)) /. D->delta n, {n, Infinity, 1}]
[error]
no result


Query: Series[(L n/2) Log[1 - L/(n-1) + (L/(n-1))*((n-2)/(n/2-1))] - (L^2/2)*((n-2)/(n/2-1)-1), {n, Infinity, 1}]
[Input interpretation]
series | (L × n/2) log(1 - L/(n - 1) + L/(n - 1) × (n - 2)/(n/2 - 1)) - L^2/2 ((n - 2)/(n/2 - 1) - 1) | point | n = ∞
order | n^1
[Series expansion at n = ∞]
-((L - 2) L^2)/(4 n) + O((1/n)^2)
(Laurent series)
(converges when (1/abs(n)<1 ∨ (abs(n) = 1 ∧ Boole[1/n = 1]<1)) ∧ (abs((1 - L)/n)<1 ∨ (abs((1 - L)/n) = 1 ∧ Boole[(L + n - 1)/n = 0]<1)))
[Series representation at n = ∞]
(L (log((-L n + n - 1)/(n - 1)) - L n))/(2 n)


Query: With[{E0=n(n-1)/2, m0=(n/2)*n/2, s=L n/2, eta[x_]:=-x Log[x]-(1-x)Log[1-x], f[e_]:=(E0-e) eta[(m0-e)/(E0-e)], lam=(n/2-1)/(n-2)}, Series[f[2s]+f[0]-2 f[s] + (L^2/2)(1/lam-1), {n,Infinity,1}]]
[error]
no result


Query: eta[x_]:=-x Log[x]-(1-x)Log[1-x]; f[e_,E,m]:=(E-e) eta[(m-e)/(E-e)]; D[f[e,E,m],{e,2}] /. e->0
[error]
no result


Query: Simplify[D[(E-e)*(-((m-e)/(E-e))*Log[(m-e)/(E-e)]-(1-(m-e)/(E-e))*Log[1-(m-e)/(E-e)]), {e, 2}] /. e->0]
[error]
no result


Query: n^(1/2) / (n^(1/2))^(3/2) == n^(-1/4)
[Input]
sqrt(n)/sqrt(n)^(3/2) = n^(-1/4)
[Result]
True


Query: (L^2 (d+L)^2)/(L n) - L (d+L)^2/n == 0
[Input]
(L^2 (d + L)^2)/(L n) - L × (d + L)^2/n = 0


Query: simplify L^2*(d+L)^2/(L*n) - L*(d+L)^2/n
[Input interpretation]
simplify | L^2 × (d + L)^2/(L n) - L × (d + L)^2/n
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: (n^(1/4))^4 == n
[Input]
(n^(1/4))^4 = n
[Result]
True


Query: q - 2 q (q/(2 q+1)) == q/(2 q+1)
[Input]
q - 2 q × q/(2 q + 1) = q/(2 q + 1)
[Alternate form]
True (for q!=-1/2)


Query: Limit[ -((L-2) L^2)/4 / L^3, L->Infinity] == -1/4
[Input]
lim_(L->∞) (-1/4 ((L - 2) L^2))/L^3 = -1/4
[Result]
True


Query: Series[(L n/2) Log[1 - L/(n-1) + (L/(n-1))*((n-2)/(n/2-1))] - (L^2/2)*((n-2)/(n/2-1)-1), {n, Infinity, 2}]
[Input interpretation]
series | (L × n/2) log(1 - L/(n - 1) + L/(n - 1) × (n - 2)/(n/2 - 1)) - L^2/2 ((n - 2)/(n/2 - 1) - 1) | point | n = ∞
order | n^2
[Series expansion at n = ∞]
-((L - 2) L^2)/(4 n) + (L^2 (L^2 - 3 L + 3))/(6 n^2) + O((1/n)^3)
(Laurent series)
(converges when (1/abs(n)<1 ∨ (abs(n) = 1 ∧ Boole[1/n = 1]<1)) ∧ (abs((1 - L)/n)<1 ∨ (abs((1 - L)/n) = 1 ∧ Boole[(L + n - 1)/n = 0]<1)))
[Series representation at n = ∞]
(L (log((-L n + n - 1)/(n - 1)) - L n))/(2 n)


Query: Series[(L n/2) Log[1 - L/(n-1) + (L/(n-1))*((n-2)/(n/2-1))] - (L^2/2)*((n-2)/(n/2-1)-1), {n, Infinity, 3}]
[Input interpretation]
series | (L × n/2) log(1 - L/(n - 1) + L/(n - 1) × (n - 2)/(n/2 - 1)) - L^2/2 ((n - 2)/(n/2 - 1) - 1) | point | n = ∞
order | n^3
[Series expansion at n = ∞]
-((L - 2) L^2)/(4 n) + (L^2 (L^2 - 3 L + 3))/(6 n^2) - (L^2 (L^3 - 4 L^2 + 6 L - 4))/(8 n^3) + O((1/n)^4)
(Laurent series)
(converges when (1/abs(n)<1 ∨ (abs(n) = 1 ∧ Boole[1/n = 1]<1)) ∧ (abs((1 - L)/n)<1 ∨ (abs((1 - L)/n) = 1 ∧ Boole[(L + n - 1)/n = 0]<1)))
[Series representation at n = ∞]
(L (log((-L n + n - 1)/(n - 1)) - L n))/(2 n)


Query: (n^(1/4))^(-3) == (n^(1/4))/n
[Input]
1/(n^(1/4))^3 = n^(1/4)/n
[Result]
True


Query: Series[1/2 + t/(n-2), {n, Infinity, 1}]
[Input interpretation]
series | 1/2 + t/(n - 2) | point | n = ∞
order | n^1
[Series expansion at n = ∞]
1/2 + O((1/n)^1)
(Taylor series)
(converges when abs(n)>2)
[Series representation at n = ∞]
(2 n (t - 1) + 1)/(2 - 4 n)


Query: (2/5)*(5/3) == 2/3
[Input]
2/5 × 5/3 = 2/3
[Result]
True


Query: Series[1/(2*(1/2 + t/(n-2))) - 1, {n, Infinity, 1}]
[Input interpretation]
series | 1/(2 (1/2 + t/(n - 2))) - 1 | point | n = ∞
order | n^1
[Series expansion at n = ∞]
-(2 t)/n + O((1/n)^2)
(Laurent series)
(converges when abs((2 - 2 t)/n)<1)
[Series representation at n = ∞]
-(2 n t)/(2 n (t - 1) + 1)


Query: Binomial(n,2)*(m/(n-1))^2 == n*m^2/(2*(n-1))
[Input]
binomial(n, 2) (m/(n - 1))^2 = n × m^2/(2 (n - 1))
[Result]
True


Query: Simplify[D[p^(-x), {x, 2}] / (p^(-x)*(Log[p])^2)]
[Input interpretation]
simplify | ((d^2 p^(-x))/(dx^2))/(p^(-x) log^2(p))
[Result]
1
[Quotient and Remainder]
1 = 1 × 1 + 0


Query: (d * (log(n)/d)^(1/2))^(-1/2) == d^(-1/4)*(log(n))^(-1/4)
[Input]
(d sqrt(log(n)/d))^(-1/2) = d^(-1/4) log^(-1/4)(n)
[Alternate form]
sqrt(d sqrt(log(n)/d)) = d^(1/4) log(n)^(1/4)
[Expanded form]
(sqrt(log(n)/d) sqrt(d sqrt(log(n)/d)))/log(n) = 1/(d^(1/4) log(n)^(1/4))
[Alternate form assuming d and n are positive]
True
[Real solution]
d>0, n>1
[Implicit derivatives]
(dd(n))/(dn) = -d/(n log(n))
[Implicit derivatives]
(dn(d))/(dd) = -(n log(n))/d


Query: Limit[n/(n-1), n->Infinity] == 1
[Input]
lim_(n->∞) n/(n - 1) = 1
[Result]
True


Query: (L*n)^3 / n^4 == L^3 / n
[Input]
(L n)^3/n^4 = L^3/n


Query: Simplify[(L*n)^3/n^4 - L^3/n] == 0
[Input interpretation]
simplify | (L n)^3/n^4 - L^3/n = 0
[Result]
True


Query: n*((n-1)/2 - d/2)*m^2/(n-1-d)^2 == n*m^2/(2*(n-1-d))
[Input]
n ((n - 1)/2 - d/2) × m^2/(n - 1 - d)^2 = n × m^2/(2 (n - 1 - d))
[Result]
True


Query: (D*n/2)*(D^2/n^2) == D^3/(2*n)
[Input]
(D × n/2) × D^2/n^2 = D^3/(2 n)


Query: Simplify[(D*n/2)*(D^2/n^2) - D^3/(2*n)] == 0
[Input interpretation]
simplify | (D × n/2) × D^2/n^2 - D^3/(2 n) = 0
[Result]
True


Query: D[-x*Log[x]-(1-x)*Log[1-x],x] + Log[x/(1-x)]
[Input]
(d(-x log(x) - (1 - x) log(1 - x)))/(dx) + log(x/(1 - x))
[Alternate forms]
log(1/(1 - x)) + log(1 - x)
[Alternate forms]
log(1 - x) - log(x) + log(-x/(x - 1))
[Alternate form assuming x>0]
piecewise | 2 i π | arg(1 - x)>=π
0 | (otherwise)
[Alternate form assuming x>0]
2 i π floor(arg(1 - x)/(2 π) + 1/2)
[Alternative representations]
(d(-x log(x) - (1 - x) log(1 - x)))/(dx) + log(x/(1 - x)) = (d(-((1 - x) log(a) log(a, 1 - x)) - x log(a) log(a, x)))/(dx) + log(a) log(a, x/(1 - x))
[Alternative representations]
(d(-x log(x) - (1 - x) log(1 - x)))/(dx) + log(x/(1 - x)) = (d(-((1 - x) log(e, 1 - x)) - x log(e, x)))/(dx) + log(e, x/(1 - x))
[Alternative representations]
(d(-x log(x) - (1 - x) log(1 - x)))/(dx) + log(x/(1 - x)) = (d(x Li_1(1 - x) + (1 - x) Li_1(x)))/(dx) - Li_1(1 - x/(1 - x))
[Series representations]
(d(-x log(x) - (1 - x) log(1 - x)))/(dx) + log(x/(1 - x)) = d/(dx)(-x log(x) - (-1 + x) sum_(k=1)^∞ ((-1)^k (-x)^k)/k) + log(x/(1 - x)) for abs(x)<1
[Series representations]
(d(-x log(x) - (1 - x) log(1 - x)))/(dx) + log(x/(1 - x)) = d/(dx)(-x log(x) + (-1 + x) (log(-x) - sum_(k=1)^∞ ((-1)^k (-x)^(-k))/k)) + log(x/(1 - x)) for abs(x)>1
[Series representations]
(d(-x log(x) - (1 - x) log(1 - x)))/(dx) + log(x/(1 - x)) = d/(dx)( sum_(k=1)^∞ ((-1)^k ((-x)^k + (-x)^(1 + k) + (-1 + x)^k x))/k) - sum_(k=1)^∞ ((-1)^k ((1 - 2 x)/(-1 + x))^k)/k for (abs(-1 + x)<1 and abs(x)<1 and abs((1 - 2 x)/(-1 + x))<1)
[Integral representations]
(d(-x log(x) - (1 - x) log(1 - x)))/(dx) + log(x/(1 - x)) = d/(dx)( integral_1^(1 - x) (-1 + x) (1/t + x/(-1 + t + 2 x - t x)) dt) + integral_1^(x/(1 - x)) 1/t dt
[Integral representations]
(d(-x log(x) - (1 - x) log(1 - x)))/(dx) + log(x/(1 - x)) = d/(dx)(-(i (-1 + x))/(2 π) integral_(-i ∞ + γ)^(i ∞ + γ) ((-x)^(-s) Γ(-s)^2 Γ(1 + s))/Γ(1 - s) ds - x log(x)) + log(x/(1 - x)) for (-1<γ<0 and abs(arg(-x))<π)
[Integral representations]
(d(-x log(x) - (1 - x) log(1 - x)))/(dx) + log(x/(1 - x)) = (2 π d/(dx)(i/(2 π) integral_(-i ∞ + γ)^(i ∞ + γ) ((-1 + x)^(-s) (-x)^(-s) ((-1 + x)^s + (-(-1 + x)^s + (-x)^s) x) Γ(-s)^2 Γ(1 + s))/Γ(1 - s) ds) - i integral_(-i ∞ + γ)^(i ∞ + γ) (((1 - 2 x)/(-1 + x))^(-s) Γ(-s)^2 Γ(1 + s))/Γ(1 - s) ds)/(2 π) for (abs(arg(-1 + x))<π and abs(arg(-x))<π and abs(arg((1 - 2 x)/(-1 + x)))<π and -1<γ<0)


Query: Simplify[D[-x*Log[x]-(1-x)*Log[1-x],x] - Log[(1-x)/x]]
[Input interpretation]
simplify | (d(-x log(x) - (1 - x) log(1 - x)))/(dx) - log((1 - x)/x)
[Results]
-log(1/x) - log(x)
[Results]
-log(1/x - 1) + log(1 - x) - log(x)


Query: Assuming[0<x<1, Simplify[D[-x*Log[x]-(1-x)*Log[1-x],x] - Log[(1-x)/x]]]
[error]
no result


Query: Simplify[L/(n-1) + (1-L/(n-1))*(D-L)/(n-1-L) - D/(n-1)]
[Input interpretation]
simplify | L/(n - 1) + (1 - L/(n - 1)) × (D - L)/(n - 1 - L) - D/(n - 1)
[Results]
0
[Results]
-(D L)/((n - 1) (-L + n - 1)) + D/(-L + n - 1) - D/(n - 1) + L^2/((n - 1) (-L + n - 1)) + L/(n - 1) - L/(-L + n - 1)


Query: Simplify[L/(n-1) + (1 - L/(n-1))*(D-L)/(n-1-L) - D/(n-1)] == 0
[Input interpretation]
simplify | L/(n - 1) + (1 - L/(n - 1)) × (D - L)/(n - 1 - L) - D/(n - 1) = 0
[Result]
True
[Expanded form]
-(D L)/((n - 1) (-L + n - 1)) + D/(-L + n - 1) - D/(n - 1) + L^2/((n - 1) (-L + n - 1)) + L/(n - 1) - L/(-L + n - 1) = 0


Query: Simplify[(n/2-1)/(n-2)-1/2]
[Input interpretation]
simplify | (n/2 - 1)/(n - 2) - 1/2
[Results]
1/2 - 1/2
[Results]
0
[Results]
n/(2 (n - 2)) - 1/(n - 2) - 1/2


Query: With[{eta=-#*Log[#]-(1-#)*Log[1-#]&, E0=n*(n-1)/2, m0=n^2/4}, Series[(E0)*eta[m0/E0] + (E0-L*n)*eta[(m0-L*n)/(E0-L*n)] - 2*(E0-L*n/2)*eta[(m0-L*n/2)/(E0-L*n/2)] + L^2/2, {n,Infinity,1}]]
[error]
no result


Query: Series[-n/4*(1/(n-1)+(2*L-1)^2/(n-1-2*L)-2*(L-1)^2/(n-1-L))+L^2/2, {n, Infinity, 1}]
[Input interpretation]
series | -n/4 (1/(n - 1) + (2 L - 1)^2/(n - 1 - 2 L) - 2 × (L - 1)^2/(n - 1 - L)) + L^2/2 | point | n = ∞
order | n^1
[Series expansion at n = ∞]
-(L^2 (3 L - 1))/(2 n) + O((1/n)^2)
(Laurent series)
(converges when abs((L + 1)/n)<1 ∧ abs((2 L + 1)/n)<1 ∧ abs(n)>1)
[Series representation at n = ∞]
(L^2 n (2 L^2 (n - 1) n + 3 L (n - 1)^2 + n^2 + n - 1))/(2 (n - 1) (L n + n - 1) (2 L n + n - 1))


Query: Series[(n*(n-1-2*L)/2+k)*((1-2*L+2*k/n)/(2*(n-1-2*L+2*k/n)))^2, {n, Infinity, 1}]
[Input interpretation]
series | (n (1/2 (n - 1 - 2 L)) + k) ((1 - 2 L + 2 × k/n)/(2 (n - 1 - 2 L + 2 × k/n)))^2 | point | n = ∞
order | n^1
[Series expansion at n = ∞]
1/8 (1 - 2 L)^2 + O((1/n)^1)
(Taylor series)
[Series representation at n = ∞]
-(2 k n - 2 L + 1)^2/(8 (-2 k n^2 + 2 L n + n - 1))


Query: Series[(n*(n-1-2*L)/2+k)*((1-2*L+2*k/n)/(2*(n-1-2*L+2*k/n)))^2, {n, Infinity, 2}]
[Input interpretation]
series | (n (1/2 (n - 1 - 2 L)) + k) ((1 - 2 L + 2 × k/n)/(2 (n - 1 - 2 L + 2 × k/n)))^2 | point | n = ∞
order | n^2
[Series expansion at n = ∞]
1/8 (1 - 2 L)^2 + ((2 L - 1) (-4 k + 4 L^2 - 1))/(8 n) + O((1/n)^2)
(Laurent series)
[Series representation at n = ∞]
-(2 k n - 2 L + 1)^2/(8 (-2 k n^2 + 2 L n + n - 1))


Query: Series[n/4*(1/(n-1)+(2*L-1)^2/(n-1-2*L)-2*(L-1)^2/(n-1-L)) - L^2/2 + L^2*(3*L-1)/(2*n), {n, Infinity, 1}]
[Input interpretation]
series | n/4 (1/(n - 1) + (2 L - 1)^2/(n - 1 - 2 L) - 2 × (L - 1)^2/(n - 1 - L)) - L^2/2 + L^2 × (3 L - 1)/(2 n) | point | n = ∞
order | n^1
[Series expansion at n = ∞]
(L^2 (3 L - 1))/n + O((1/n)^2)
(Laurent series)
(converges when abs((L + 1)/n)<1 ∧ abs((2 L + 1)/n)<1 ∧ abs(n)>1)
[Series representation at n = ∞]
(L^2 n (6 L^3 (n - 1) n^2 + L^2 n (7 n^2 - 18 n + 11) - 6 L (n - 1)^2 - n^3 + 2 n^2 - 4 n + 2))/(2 (n - 1) (L n + n - 1) (2 L n + n - 1))


Query: Series[(L*n/2)*Log[1-L/(n-1)+2*(L/(n-1))*Exp[(2*L-1)/n]] - L^2/2 - L^2*(3*L-1)/(2*n), {n, Infinity, 1}]
[Input interpretation]
series | (L × n/2) log(1 - L/(n - 1) + 2 × L/(n - 1) exp((2 L - 1)/n)) - L^2/2 - L^2 × (3 L - 1)/(2 n) | point | n = ∞
order | n^1
[Series expansion at n = ∞]
L^3/(4 n) + O((1/n)^2)
(Laurent series)


Query: Simplify[(L^3/(4*n))/(L^3/n^3) - n^2/4] == 0
[Input interpretation]
simplify | (L^3/(4 n))/(L^3/n^3) - n^2/4 = 0
[Result]
True


Query: Simplify[n*(n-1)/2 * (1/(2*(n-1)))^2 - n/(8*(n-1))] == 0
[Input interpretation]
simplify | n × (n - 1)/2 (1/(2 (n - 1)))^2 - n/(8 (n - 1)) = 0
[Result]
True


Query: Simplify[n*(n-1-L)/2 * ((1-L)/(2*(n-1-L)))^2 - n*(L-1)^2/(8*(n-1-L))] == 0
[Input interpretation]
simplify | n (1/2 (n - 1 - L)) ((1 - L)/(2 (n - 1 - L)))^2 - n × (L - 1)^2/(8 (n - 1 - L)) = 0
[Expanded form]
True


Query: Simplify[L/(n-1)*(L-1)/(n-2) - (L/(n-1))^2]
[Input interpretation]
simplify | L/(n - 1) × (L - 1)/(n - 2) - (L/(n - 1))^2
[Results]
(L (L - n + 1))/((n - 2) (n - 1)^2)
[Results]
(L (L - n + 1))/((n - 2) (n - 1)^2)
[Results]
L^2/((n - 2) (n - 1)^2) - L/((n - 2) (n - 1))


Query: Simplify[L/(n-1)*(L*(n-4)+2)/((n-2)*(n-3)) - (L/(n-1))^2]
[Input interpretation]
simplify | L/(n - 1) × (L (n - 4) + 2)/((n - 2) (n - 3)) - (L/(n - 1))^2
[Results]
(2 L (-L + n - 1))/((n - 3) (n - 2) (n - 1)^2)
[Results]
-(2 L (L - n + 1))/((n - 3) (n - 2) (n - 1)^2)
[Results]
((2 L)/(n - 1) - (2 L^2)/(n - 1)^2)/((n - 3) (n - 2))


Query: Simplify[(n*L*(L-1)/2)*L*(L-n+1)/((n-2)*(n-1)^2) + ((L*n/2)*(L*n/2-1)/2 - n*L*(L-1)/2)*2*L*(-L+n-1)/((n-3)*(n-2)*(n-1)^2)]
[Input interpretation]
simplify | (n L × (L - 1)/2) L × (L - n + 1)/((n - 2) (n - 1)^2) + ((L × n/2) (1/2 (L × n/2 - 1)) - n L × (L - 1)/2) × 2 L × (-L + n - 1)/((n - 3) (n - 2) (n - 1)^2)


Query: Series[(n*L*(L-1)/2)*L*(L-n+1)/((n-2)*(n-1)^2) + ((L*n/2)*(L*n/2-1)/2 - n*L*(L-1)/2)*2*L*(n-1-L)/((n-3)*(n-2)*(n-1)^2), {n, Infinity, 1}]
[Input interpretation]
series | (n L × (L - 1)/2) L × (L - n + 1)/((n - 2) (n - 1)^2) + ((L × n/2) (1/2 (L × n/2 - 1)) - n L × (L - 1)/2) × 2 L × (n - 1 - L)/((n - 3) (n - 2) (n - 1)^2) | point | n = ∞
order | n^1
[Series expansion at n = ∞]
-((L - 2) L^2)/(4 n) + O((1/n)^2)
(Laurent series)
(converges when abs(n)>3)
[Series representation at n = ∞]
-((L - 2) L^2 n (L n + n - 1))/(4 (n - 1)^2 (3 n - 1))


Query: L^4/n^2 / (L^3/n) == L/n
[Input]
(L^4/n^2)/(L^3/n) = L/n


Query: Simplify[n*L*(L-1)/2 - n*Binomial[L,2]]
[Input interpretation]
simplify | n L × (L - 1)/2 - n binomial(L, 2)
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[L^4/n^2/(L^3/n) - L/n] == 0
[Input interpretation]
simplify | (L^4/n^2)/(L^3/n) - L/n = 0
[Result]
True


Query: Series[Log[Hypergeometric2F1[-L*n/2, -L*n/2, -n*(n-1)/2, 1-2]] - (L*n/2)*Log[1+L/(n-1)], {n, Infinity, 1}]
[Input interpretation]
series | log(2F1(-L × n/2, -L × n/2, -n × (n - 1)/2, 1 - 2)) - (L × n/2) log(1 + L/(n - 1)) | point | n = ∞
order | n^1
[Series expansion at n = ∞]
log(2F1(-(L n)/2, -(L n)/2, -1/2 (n - 1) n, -1)) + (-L^2/2 + ((L - 2) L^2)/(4 n) + O((1/n)^2))


Query: Simplify[L/(n-1)*(L*(n-4)+2)/((n-2)*(n-3)) - L^2/(n-1)^2 - 2*L*(n-1-L)/((n-3)*(n-2)*(n-1)^2)] == 0
[Input interpretation]
simplify | L/(n - 1) × (L (n - 4) + 2)/((n - 2) (n - 3)) - L^2/(n - 1)^2 - 2 L × (n - 1 - L)/((n - 3) (n - 2) (n - 1)^2) = 0
[Result]
True
[Expanded form]
(L^2 n)/((n - 3) (n - 2) (n - 1)) - (4 L^2)/((n - 3) (n - 2) (n - 1)) + (2 L^2)/((n - 3) (n - 2) (n - 1)^2) - L^2/(n - 1)^2 - (2 L n)/((n - 3) (n - 2) (n - 1)^2) + (2 L)/((n - 3) (n - 2) (n - 1)) + (2 L)/((n - 3) (n - 2) (n - 1)^2) = 0


Query: Series[(n*L*(L-1)/2)*L*(L-n+1)/((n-2)*(n-1)^2) + ((L*n/2)*(L*n/2-1)/2 - n*L*(L-1)/2)*2*L*(n-1-L)/((n-3)*(n-2)*(n-1)^2), {n, Infinity, 2}]
[Input interpretation]
series | (n L × (L - 1)/2) L × (L - n + 1)/((n - 2) (n - 1)^2) + ((L × n/2) (1/2 (L × n/2 - 1)) - n L × (L - 1)/2) × 2 L × (n - 1 - L)/((n - 3) (n - 2) (n - 1)^2) | point | n = ∞
order | n^2
[Series expansion at n = ∞]
-((L - 2) L^2)/(4 n) + ((L - 4) (L - 2) L^2)/(4 n^2) + O((1/n)^3)
(Laurent series)
(converges when abs(n)>3)
[Series representation at n = ∞]
-((L - 2) L^2 n (L n + n - 1))/(4 (n - 1)^2 (3 n - 1))


Query: Series[n*Binomial[L,3]*(L*(L-1)*(L-2)/((n-1)*(n-2)*(n-3)) - 3*L*(L-1)/((n-1)*(n-2))*L/(n-1) + 2*L^3/(n-1)^3), {n, Infinity, 3}]
[Input interpretation]
series | n binomial(L, 3) (L (L - 1) × (L - 2)/((n - 1) (n - 2) (n - 3)) - 3 L × (L - 1)/((n - 1) (n - 2)) × L/(n - 1) + 2 × L^3/(n - 1)^3) | point | n = ∞
order | n^3
[Series expansion at n = ∞]
((L - 2) (L - 1) L^2)/(3 n^2) - ((L - 2)^2 (L - 1) L^2)/n^3 + ((L - 2) (L - 1) L^2 (2 L^2 - 21 L + 25))/(3 n^4) + O((1/n)^5)
(Laurent series)
(converges when abs(n)>3)
[Series representation at n = ∞]
-((L - 2) (L - 1) L^2 n^2 ((2 L^2 + 3 L + 1) n^2 - (3 L + 2) n + 1))/(3 (n - 1)^3 (6 n^2 - 5 n + 1))


Query: Series[((L-2)*L^2)/(4*n) + ((n*L*(L-1)/2)*L*(L-n+1)/((n-2)*(n-1)^2) + ((L*n/2)*(L*n/2-1)/2 - n*L*(L-1)/2)*2*L*(n-1-L)/((n-3)*(n-2)*(n-1)^2))/(1+L/(n-1))^2, {n, Infinity, 2}]
[Input interpretation]
series | ((L - 2) L^2)/(4 n) + ((n L × (L - 1)/2) L × (L - n + 1)/((n - 2) (n - 1)^2) + ((L × n/2) (1/2 (L × n/2 - 1)) - n L × (L - 1)/2) × 2 L × (n - 1 - L)/((n - 3) (n - 2) (n - 1)^2))/(1 + L/(n - 1))^2 | point | n = ∞
order | n^2
[Series expansion at n = ∞]
((L - 2) L^2 (3 L - 4))/(4 n^2) - ((L - 2) L^2 (5 L^2 - 15 L + 13))/(4 n^3) + O((1/n)^4)
(Laurent series)
(converges when abs((1 - L)/n)<1 ∧ abs(n)>3)
[Series representation at n = ∞]
((L - 2) L^2 n^2 (L^2 n (3 n - 1) + L (-6 n^2 + 8 n - 3) + 3 n^2 - 7 n + 4))/(4 (3 n - 1) ((L - 1) n + 1)^2)


Query: Series[(L*n/2)*Log[1-L/(n-1)+(L/(n-1))*2*Exp[(2*L-1)/n]] - L^2/2 - L^2*(3*L-1)/(2*n) + (2*Exp[(2*L-1)/n]-1)^2/((1-L/(n-1)+(L/(n-1))*2*Exp[(2*L-1)/n])^2) * ((n*L*(L-1)/2)*L*(L-n+1)/((n-2)*(n-1)^2) + ((L*n/2)*(L*n/2-1)/2 - n*L*(L-1)/2)*2*L*(n-1-L)/((n-3)*(n-2)*(n-1)^2)), {n, Infinity, 1}]
[error]
no result


Query: Series[(2*Exp[(2*L-1)/n]-1)^2/(1-L/(n-1)+(L/(n-1))*2*Exp[(2*L-1)/n])^2, {n, Infinity, 1}]
[Input interpretation]
series | (2 exp((2 L - 1)/n) - 1)^2/(1 - L/(n - 1) + L/(n - 1) × 2 exp((2 L - 1)/n))^2 | point | n = ∞
order | n^1
[Series expansion at n = ∞]
1 + O((1/n)^1)
(Taylor series)


Query: Series[(2*Exp[(2*L-1)/n]-1)^2/(1-L/(n-1)+(L/(n-1))*2*Exp[(2*L-1)/n])^2, {n, Infinity, 2}]
[Input interpretation]
series | (2 exp((2 L - 1)/n) - 1)^2/(1 - L/(n - 1) + L/(n - 1) × 2 exp((2 L - 1)/n))^2 | point | n = ∞
order | n^2
[Series expansion at n = ∞]
1 + (6 L - 4)/n + O((1/n)^2)
(Laurent series)


Query: Series[(L*n/2)*Log[1-L/(n-1)+(L/(n-1))*2*Exp[(2*L-1)/n]] - L^2/2 - L^2*(3*L-1)/(2*n), {n, Infinity, 2}]
[Input interpretation]
series | (L × n/2) log(1 - L/(n - 1) + L/(n - 1) × 2 exp((2 L - 1)/n)) - L^2/2 - L^2 × (3 L - 1)/(2 n) | point | n = ∞
order | n^2
[Series expansion at n = ∞]
L^3/(4 n) + (L^3 (L + 3))/(6 n^2) + O((1/n)^3)
(Laurent series)


Query: Series[(n*L*(L-1)^2/2)*(L/(n-1)*(L-1)/(n-2)*L*(L-1)/(L*n-4) - 2*L*(L-1)/((n-1)*(n-2))*L/(n-1) - L/(n-1)*(L*(n-4)+2)/((n-2)*(n-3))*L/(n-1) + 2*L^3/(n-1)^3), {n, Infinity, 2}]
[Input interpretation]
series | (n L (1/2 (L - 1)^2)) (L/(n - 1) × (L - 1)/(n - 2) L × (L - 1)/(L n - 4) - 2 L × (L - 1)/((n - 1) (n - 2)) × L/(n - 1) - L/(n - 1) × (L (n - 4) + 2)/((n - 2) (n - 3)) × L/(n - 1) + 2 × L^3/(n - 1)^3) | point | n = ∞
order | n^2
[Series expansion at n = ∞]
((L - 1)^2 L^2)/(2 n^2) - ((L - 1)^2 L (2 L^3 - 4 L^2 + 5 L - 4))/(2 n^3) + O((1/n)^4)
(Laurent series)
(converges when 4 abs(1/(L n))<1 ∧ abs(n)>3)
[Series representation at n = ∞]
((L - 1)^2 L^3 n^2 ((3 L^2 + 2 L + 35) n^3 + (-9 L^2 + 18 L - 47) n^2 + (2 L^2 - 4 L + 13) n - 1))/(2 (n - 1)^3 (2 n - 1) (3 n - 1) (L - 4 n))


Query: Simplify[L^3/(4*n) - (L-2)*L^2/(4*n) - L^2/(2*n)] == 0
[Input interpretation]
simplify | L^3/(4 n) - (L - 2) × L^2/(4 n) - L^2/(2 n) = 0
[Expanded form]
True
