# Wolfram checks (v2.0)

One identity per query. App id never written here.
New identities for `v2/paper/main.tex` append below.


Query: (L^2/2)/(L^4/4) = 2/L^2
[Input]
(L^2/2)/(L^4/4) = 2/L^2
[Solution]
L!=0


Query: assuming L>0, (L^2/2)/(L^4/4) = 2/L^2
[Input]
{L>0, (L^2/2)/(L^4/4) = 2/L^2}


Query: FullSimplify[(L^2/2)/(L^4/4) - 2/L^2]
[Input interpretation]
simplify | (L^2/2)/(L^4/4) - 2/L^2
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Dn/2 - K01 + Dn/2 - K02 - (K12 - K012) = Dn - K01 - K02 - K12 + K012
[error]
no result


Query: Simplify[(Dn/2 - K01 + Dn/2 - K02 - (K12 - K012)) - (Dn - K01 - K02 - K12 + K012)]
[error]
no result


Query: Simplify[(s - a + s - b - (c - d)) - (2 s - a - b - c + d)]
[Input interpretation]
simplify | (s - a + s - b - (c - d)) - (2 s - a - b - c + d)
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(L n/2)*(L/(n-1)) - n L^2/(2(n-1))]
[Input interpretation]
simplify | (L × n/2) × L/(n - 1) - n × L^2/(2 (n - 1))
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Series[(L^2 n (n-1-L)/(2 (n-1)^2) - (L-2) L^2 /(2 n)) / (n L^2 /(2 (n-1)))^2, {n, Infinity, 1}]
[Input interpretation]
series | (L^2 n × (n - 1 - L)/(2 (n - 1)^2) - (L - 2) × L^2/(2 n))/(n × L^2/(2 (n - 1)))^2 | point | n = ∞
order | n^1
[Series expansion at n = ∞]
2/L^2 + O((1/n)^1)
(Taylor series)
(converges everywhere away from origin)
[Series representation at n = ∞]
(-2 (L - 2) n^3 + 4 (L - 2) n^2 + (2 - 4 L) n + 2)/L^2


Query: Simplify[n L^2/(2(n-1)) - n L^3/(2(n-1)^2) - n L^2 (n-1-L)/(2(n-1)^2)]
[Input interpretation]
simplify | n × L^2/(2 (n - 1)) - n × L^3/(2 (n - 1)^2) - n L^2 × (n - 1 - L)/(2 (n - 1)^2)
[Results]
0
[Results]
-(L^2 n^2)/(2 n^2 - 4 n + 2) + (L^2 n)/(2 n^2 - 4 n + 2) + (L^2 n)/(2 (n - 1))


Query: With[{M = L n - 2 t, M2 = n L (L-1) - 4 t (L-1), phi = L^2 - 4 L + 2 - 2 (L-1) M2/M, Wsum = 2 t (L-1)^2 / M^2, mom = 1 - M2^2/M^3 - M2/M^2 - Wsum, q = (L^2/M) mom (1 - phi/M), p = L/(n-1)}, Series[q/p - 1, {n, Infinity, 2}]]
[error]
no result


Query: Series[L (n-1)/(L n - 2 t) - 1 - 2 t/(L n), {n, Infinity, 1}]
[Input interpretation]
series | L × (n - 1)/(L n - 2 t) - 1 - 2 × t/(L n) | point | n = ∞
order | n^1
[Series expansion at n = ∞]
-1/n + O((1/n)^2)
(Laurent series)
(converges when 2 abs(t/(L n))<1)
[Series representation at n = ∞]
-(n (L^2 - 4 n t^2))/(L (L - 2 n t))

Fallback for the signed principal term after a t-matching host
(Wolfram With[] Series of the full q/p returned no result).
Exact Fraction arithmetic in v2/scripts/_signed_main.py:
empty host recovers the checked series (-L^2+L-1)/n^2;
unsigned L(n-1)/(Ln-2t)-1 = 2t/(Ln)-1/n+O(1/n^2) as above;
signed q/p-1-2t/(Ln) has d*n^2 bounded in L,t for
(L,t,n) in {(4,2,800),(4,2,3200),(4,8,3200),(4,16,3200),(4,16,12800),
(10,2,800),(10,2,3200),(10,16,12800),(10,100,3200),(10,100,12800)},
so the residual is O((L^2+t)/n^2). The leading signed relative error
is 2t/(Ln), the same stub-total shift as the unsigned ratio.


Query: Simplify[(L-1)(L n - 4 t) - (n L (L-1) - 4 t (L-1))]
[Input interpretation]
simplify | (L - 1) (L n - 4 t) - (n L (L - 1) - 4 t (L - 1))
[Result]
0


Query: Simplify[(n D/2)(n D/2 - 1)/2 - n D (D-1)/4 - n D (n D - 4 D + 2)/8]
[Input interpretation]
simplify | (n × D/2) (1/2 (n × D/2 - 1)) - n (1/4 × (d(D - 1))/(dD)) - n (1/8 × (d(n D - 4 D + 2))/(dD))
[Results]
D ((D n^2)/8 - n/4) + (1/4 - n/8) n
[Results]
(D^2/8 - 1/8) n^2 + (1/4 - D/4) n
[Results]
n ((D^2/8 - 1/8) n - D/4 + 1/4)
[Expanded form]
(D^2 n^2)/8 - (D n)/4 - n^2/8 + n/4


Query: Simplify[(n L/2)*(n L/2 - 1)/2 - n*L*(L-1)/4 - n*L*(n*L - 4*L + 2)/8]
[Input interpretation]
simplify | (n × L/2) (1/2 (n × L/2 - 1)) - n L × (L - 1)/4 - n L (1/8 (n L - 4 L + 2))
[Results]
1/4 L (L - 1) n
[Results]
(L^2 n)/4 - (L n)/4
[Results]
L ((L n)/4 - n/4)


Query: Simplify[(n L/2)*(n L/2 - 1)/2 - n*L*(L-1)/4 - n*L^2*(n-2)/8]
[Input interpretation]
simplify | (n × L/2) (1/2 (n × L/2 - 1)) - n L × (L - 1)/4 - n L^2 × (n - 2)/8
[Result]
0


Query: Series[1 - L/(n-1) + n/((n-1)(1+e)), {n, Infinity, 0}]
[Input interpretation]
series | 1 - L/(n - 1) + n/((n - 1) (1 + e)) | point | n = ∞
order | n^0
[Series expansion at n = ∞]
(1 + 1/(1 + e)) + O((1/n)^1)
(Taylor series)
(converges when e L + L = 1 ∨ 1/abs(n)<1)
[Series representation at n = ∞]
(L n + e (L n + n - 1) + n - 2)/((1 + e) (n - 1))


Query: Simplify[L/(n-1) * n/((1+e) L) - n/((n-1)(1+e))]
[Input interpretation]
simplify | L/(n - 1) × n/((1 + e) L) - n/((n - 1) (1 + e))
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[1 + 1/(1+e) - (2+e)/(1+e)]
[Input interpretation]
simplify | 1 + 1/(1 + e) - (2 + e)/(1 + e)
[Results]
0
[Results]
1 - 1/(1 + e) - e/(1 + e)
[Number name]
zero


Query: Simplify[(n^2 L^2)*(L/n)^2 - L^4]
[Input interpretation]
simplify | (n^2 L^2) (L/n)^2 - L^4
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[n D^2/(2(n-1)) - (n D/2)*(D/(n-1))]
[Input interpretation]
simplify | n × D^2/(2 (n - 1)) - (n × D/2) × D/(n - 1)
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(n-1-D)*q*(1-q) /. q -> (p - D/(n-1))/(1 - D/(n-1)) ]
[error]
no result


Query: With[{pi = D/(n-1), p = (1+e)*D/n, q = (p-pi)/(1-pi)}, Series[((n-1-D)*q*(1-q))/((n-1)*p*(1-p)), {n, Infinity, 0}]]
[error]
no result


Query: Series[(1+e)*D/n - D/(n-1), {n, Infinity, 2}]
[Input interpretation]
series | (1 + e) × D/n - D/(n - 1) | point | n = ∞
order | n^2
[Series expansion at n = ∞]
(e D)/n - D/n^2 + O((1/n)^3)
(Laurent series)
(converges when D = 0 ∨ 1/abs(n)<1)
[Series representation at n = ∞]
D n (n/(n - 1) + e)


Query: assuming e>0 && D>0 && n>1, (1+e)^(D n/2) = Exp[(D n/2) Log[1+e]]
[Input]
{e>0 ∧ D>0 ∧ n>1, (1 + e)^(D × n/2) = exp((D × n/2) log(1 + e))}


Query: Series[Log[(1+e)*D/n] + Log[n/D], {n, Infinity, 1}]
[Input interpretation]
series | log((1 + e) × D/n) + log(n/D) | point | n = ∞
order | n^1
[Series expansion at n = ∞]
log(((1 + e) D)/n) + log(n/D)


Reference prop:jensen-inverse — that lives in PlusOneV1, cited in text as
Proposition jensen-inverse of the companion. OK as prose name.

Also record variance ratio series:
Query: Series[sprinkle/binom variance ratio]
[Series expansion at n = ∞]
e/(1 + e) + O((1/n)^1)


Query: Simplify[Log[(1+e)*D/n] + Log[n/D] - Log[1+e]]
[Expanded logarithmic form]
0


Query: Simplify[((1+e)*D/n - D/(n-1))/(1 - D/(n-1)) - ((1+e)*D*(n-1) - D*n)/((n - D)*n )]
[Input interpretation]
simplify | ((1 + e) × D/n - D/(n - 1))/(1 - D/(n - 1)) - ((1 + e) D (n - 1) - D n)/((n - D) n)


Query: Series[((n-1-D)*((1+e)*D/n - D/(n-1))/(1-D/(n-1))*(1-((1+e)*D/n - D/(n-1))/(1-D/(n-1))))/((n-1)*(1+e)*D/n*(1-(1+e)*D/n)), {n, Infinity, 0}]
[Input interpretation]
series | ((n - 1 - D) × ((1 + e) × D/n - D/(n - 1))/(1 - D/(n - 1)) (1 - ((1 + e) × D/n - D/(n - 1))/(1 - D/(n - 1))))/((n - 1) (1 + e) × D/n (1 - (1 + e) × D/n)) | point | n = ∞
order | n^0
[Series expansion at n = ∞]
e/(1 + e) + O((1/n)^1)
(Taylor series)
(converges when abs((D + 1)/n)<1)
[Series representation at n = ∞]
(e (n - 1) + n)/((1 + e) (D n + n - 1))


Query: Simplify[e/(1+e) - e/(1+e)]
[Input interpretation]
simplify | e/(1 + e) - e/(1 + e)
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[1/(1+(1+e)^3) * ((1+e)*D/n)^3 / (D/(n-1))^3]
[Input interpretation]
simplify | 1/(1 + (1 + e)^3) × ((1 + e) × D/n)^3/(D/(n - 1))^3
[Results]
((1 + e)^3 (n - 1)^3)/(((2 + e) (1 + e + e^2)) n^3)
[Results]
((1 + e)^3 (n - 1)^3)/((1 + (1 + e)^3) n^3)
[Results]
((1 + e)^3 (n - 1)^3)/((2 + 3 e + 3 e^2 + e^3) n^3)
[Quotient and Remainder]
(1 + e)^3 (n - 1)^3 = (1/(1 + (1 + e)^3) + (3 e)/(1 + (1 + e)^3) + (3 e^2)/(1 + (1 + e)^3) + e^3/(1 + (1 + e)^3))((1 + (1 + e)^3) n^3) + ((-3 - 9 e - 9 e^2 - 3 e^3) n^2 + (3 + 9 e + 9 e^2 + 3 e^3) n - e^3 - 3 e^2 - 3 e - 1)
[Quotient and Remainder]
quotient | 1/(1 + (1 + e)^3) + (3 e)/(1 + (1 + e)^3) + (3 e^2)/(1 + (1 + e)^3) + e^3/(1 + (1 + e)^3)
remainder | (-3 - 9 e - 9 e^2 - 3 e^3) n^2 + (3 + 9 e + 9 e^2 + 3 e^3) n - e^3 - 3 e^2 - 3 e - 1


Query: With[{pi=D/(n-1),p=(1+e)*D/n}, Series[(p*pi)/(pi+(1-pi)*p)/pi, {n,Infinity,1}]]
[error]
no result


Query: With[{pi=D/(n-1),p=(1+e)*D/n}, Series[((p*pi)/(pi+(1-pi)*p))^3 / pi^3, {n,Infinity,0}]]
[error]
no result


Query: assuming e>0 && D>0 && n>D+1, Simplify[((p*pi)/(pi+(1-pi)*p))/pi /. {pi->D/(n-1), p->(1+e)*D/n}]
[error]
no result


Query: Series[ ((1+e)*D/n) / (D/(n-1) + (1-D/(n-1))*(1+e)*D/n) * (n-1)/D , {n, Infinity, 0}]
[Input interpretation]
series | ((1 + e) × D/n)/(D/(n - 1) + (1 - D/(n - 1)) (1 + e) × D/n) × (n - 1)/D | point | n = ∞
order | n^0
[Series expansion at n = ∞]
((1 + e) n)/(e D + 2 D) + ((1 + e) (e D + D - e - 3))/((2 + e)^2 D) + O((1/n)^1)
(Taylor series)
[Series representation at n = ∞]
-((1 + e) (n - 1)^2)/(D n (D n + e (D n + n - 1) + n - 2))


Query: Simplify[ ((1+e)*D/n) / (D/(n-1) + (1-D/(n-1))*(1+e)*D/n) * (n-1)/D ]
[Input interpretation]
simplify | ((1 + e) × D/n)/(D/(n - 1) + (1 - D/(n - 1)) (1 + e) × D/n) × (n - 1)/D


Query: Limit[((1+e)*a) / (a*n/(n-1) + (1 - a*n/(n-1))*(1+e)*a) * (n-1)/(a*n), n->Infinity]
[Limit]
lim_(n->∞) (((1 + e) a) (n - 1))/(((a n)/(n - 1) + (1 - (a n)/(n - 1)) (1 + e) a) (a n)) = -(1 + e)/(a (-2 + a + (-1 + a) e))
[Values]
a | 
1 | 1 + e
2 | -(1 + e)/(2 e)
3 | (1 + e)/(-3 - 6 e)
[Series expansion at n = ∞]
(1 + e)/(a - (1 + e) (a - 1) a) + ((1 + e) (2 (1 + e) a - e - 3))/(a (e a + a - e - 2)^2 n) - ((1 + e) (e a + a - 1)^2)/(a (e a + a - e - 2)^3 n^2) + ((1 + e)^2 (e a + a - 1)^2)/(a (e a + a - e - 2)^4 n^3) - ((1 + e)^3 (e a + a - 1)^2)/(a (e a + a - e - 2)^5 n^4) + O((1/n)^5)
(Laurent series)


Query: Simplify[((1+e)*a) / (a*n/(n-1) + (1-a*n/(n-1))*(1+e)*a) * (n-1)/(a*n)]
[Input interpretation]
simplify | ((1 + e) a)/(a × n/(n - 1) + (1 - a × n/(n - 1)) (1 + e) a) × (n - 1)/(a n)


Query: rational fallback: p/(pi+(1-pi)p) -> (1+e)/(2+e) (D=o(n), D->inf)
[fallback]
Wolfram Limit/With Series returned no usable sparse result; exact Fraction arithmetic:
e=1/100 target=0.5024875622
  n=10000 D=100 p/denom=0.5050002525 err=2.513e-03
  n=100000 D=500 p/denom=0.5037507109 err=1.263e-03
  n=1000000 D=2000 p/denom=0.5029928077 err=5.052e-04
e=1/10 target=0.5238095238
  n=10000 D=100 p/denom=0.5265428050 err=2.733e-03
  n=100000 D=500 p/denom=0.5251825147 err=1.373e-03
  n=1000000 D=2000 p/denom=0.5243586027 err=5.491e-04
e=1 target=0.6666666667
  n=10000 D=100 p/denom=0.6711188670 err=4.452e-03
  n=100000 D=500 p/denom=0.6688941063 err=2.227e-03
  n=1000000 D=2000 p/denom=0.6675565204 err=8.899e-04


Query: Simplify[((1+e)/(2+e))^3 - 1]
[Input interpretation]
simplify | ((1 + e)/(2 + e))^3 - 1
[Results]
-(7 + 9 e + 3 e^2)/(2 + e)^3
[Results]
(1 + e)^3/(2 + e)^3 - 1
[Results]
-1/(2 + e)^3 + 3/(2 + e)^2 - 3/(2 + e)
[Decimal approximation]
-0.510587251584480249735819007021469549731604050398220985586287065...
[Property]
-1 + (1 + e)^3/(2 + e)^3 is a transcendental number


Query: Simplify[60+10-70]
[Input interpretation]
simplify | 60 + 10 - 70
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[2-0]
[Input interpretation]
simplify | 2 - 0
[Result]
2
[Quotient and Remainder]
2 = 2 × 1 + 0


Query: Simplify[1/70]
[Input interpretation]
simplify | 1/70
[Result]
1/70
[Quotient and Remainder]
1 = (0) × 70 + 1
[Decimal approximation]
0.0142857142857142857142857142857142857142857142857142857142857142...
[Repeating decimal]
0.0142857^_ (period 6)
[Percentage]
1.429%


Query: Simplify[Exp[c*D*Log[D]] / Exp[e*D*n] /. {c->10, e->1/100, D->100, n->10000}]
[error]
no result


Query: assuming D>1 && n>1 && e>0, Exp[O[D]*Log[D]] mistarget
[error]
no result


Query: rational fallback: eps=(log(n)/D)^(1/3); compare (Dn/2)log(1+eps) vs 4 D log D
[fallback]
n=1000000 D=100 eps=0.516958 ln_bulk=20835365.828 ln_tree=1842.068
n=1000000 D=1000 eps=0.239951 ln_bulk=107535875.393 ln_tree=27631.021
n=1000000000 D=10000 eps=0.127493 ln_bulk=599982562457.456 ln_tree=368413.615


Query: Simplify[16588-7080]
[Input interpretation]
simplify | 16588 - 7080
[Result]
9508
[Quotient and Remainder]
9508 = 9508 × 1 + 0
[Percent decrease]
16588 - 7080 = 9508 is 42.68% smaller than 16588.


Query: Simplify[D^2 * n / (2*(n-1)) - D^2 / 2]
[Input interpretation]
simplify | D^2 × n/(2 (n - 1)) - D^2/2
[Result]
D^2/(2 (n - 1))


Query: Series[D^2 * n / (2*(n-1)), {n, Infinity, 1}]
[Input interpretation]
series | D^2 × n/(2 (n - 1)) | point | n = ∞
order | n^1
[Series expansion at n = ∞]
D^2/2 + O((1/n)^1)
(Taylor series)
(converges when D = 0 ∨ 1/abs(n)<1)
[Series representation at n = ∞]
D^2/(2 - 2 n)


Query: Simplify[D^2/2 - (D^2/10)*Log[n/D]]
[Input interpretation]
simplify | D^2/2 - D^2/10 log(n/D)
[Results]
-1/10 D^2 (log(n/D) - 5)
[Results]
D^2 (1/2 - 1/10 log(n/D))
[Expanded logarithmic form]
D^2/2 + 1/10 D^2 log(D) + -1/10 D^2 log(n)
[Alternate form assuming D!=0, n!=0, and D n>0]
1/10 D^2 log(e^5/(n/D))


Query: assuming D>1 && n>D, Simplify[(D^2)/(D^2/log(n/D))*Log[n/D]]
[error]
no result


Query: Simplify[(D*n/2)*(D/(n-1)) - D^2/2]
[Input interpretation]
simplify | (D × n/2) × D/(n - 1) - D^2/2
[Result]
D^2/(2 (n - 1))


Query: Series[(D*n/2)*(-Log[1-D/(n-1)]), {n, Infinity, 0}]
[Input interpretation]
series | (D × n/2) (-log(1 - D/(n - 1))) | point | n = ∞
order | n^0
[Series expansion at n = ∞]
D^2/2 + O((1/n)^1)
(Taylor series)
(converges when (1/abs(n)<1 ∨ (abs(n) = 1 ∧ Boole[1/n = 1]<1)) ∧ (abs((D + 1)/n)<1 ∨ (abs((D + 1)/n) = 1 ∧ Boole[(D + 1)/n = 1]<1)))
[Series representation at n = ∞]
-(D log((D n + n - 1)/(n - 1)))/(2 n)


Query: Simplify[Log[(2+e)/(1+e)] - Log[2]]
[Input interpretation]
simplify | log((2 + e)/(1 + e)) - log(2)
[Result]
log((2 + e)/(2 + 2 e))
[Expanded logarithmic form]
log(2 + e) - log(1 + e) - log(2)
[Reduced logarithmic form]
log((2 + e)/((1 + e) 2))
[Quotient and Remainder]
log((2 + e)/(1 + e)) - log(2) = (0) × 1 + (log((2 + e)/(1 + e)) - log(2))
[Decimal approximation]
-0.454964154146117054410757069251900010919681890132207767139340386...


Query: Simplify[((D*n/2)*(D/(n-1)))/(((1+e)*D/n)*(1-D/(n-1))) * (D/n)]
[Input interpretation]
simplify | ((D × n/2) × D/(n - 1))/(((1 + e) × D/n) (1 - D/(n - 1))) × D/n
[Results]
(D^2 n)/((1 + e) 2 (-D + n - 1))
[Results]
-(D^2 n)/(2 (1 + e) (D - n + 1))
[Results]
-(D^2 n)/(2 e D + 2 D - 2 e n - 2 n + 2 e + 2)


Query: Series[((n*D/2)*(D/(n-1)))/(((1+e)*D/n)*(1-D/(n-1))), {n, Infinity, 0}]
[Input interpretation]
series | ((n × D/2) × D/(n - 1))/(((1 + e) × D/n) (1 - D/(n - 1))) | point | n = ∞
order | n^0
[Series expansion at n = ∞]
(D n)/(2 + 2 e) + (D^2 + D)/(2 + 2 e) + O((1/n)^1)
(Taylor series)
(converges when abs((D + 1)/n)<1)
[Series representation at n = ∞]
-D/(2 (1 + e) n (D n + n - 1))


Query: rational fallback: s*pi/(p*(1-pi)) ~ D*n/(2(1+e)); (1-pi)^s*(Dn)^ell for ell=D^2/(100*log(n*D))
[fallback]
n=1000000 D=100 ratio=45459136.8 ell=5.4 log_contrib=-4904.5
n=1000000 D=200 ratio=95257241.9 ell=20.9 log_contrib=-19617.5
n=10000000 D=500 ratio=2272841142.1 ell=111.9 log_contrib=-122591.4


Query: Series[(D^2/2)*Log[n/D], {n, Infinity, 0}]
[Input interpretation]
series | D^2/2 log(n/D) | point | n = ∞
order | n^0
[Series expansion at n = ∞]
1/2 D^2 log(n/D)
[Series representation at n = ∞]
1/2 D^2 log(1/(D n))


Query: Simplify[(D*n/2)*Log[2] - (D^2/2)*Log[n/D]]
[Input interpretation]
simplify | (D × n/2) log(2) - D^2/2 log(n/D)
[Result]
-1/2 D (D log(n/D) - n log(2))
[Expanded logarithmic form]
1/2 D n log(2) + 1/2 D^2 log(D) + -1/2 D^2 log(n)
[Alternate form assuming D!=0, n!=0, and D n>0]
1/2 D (n log(2) - D log(n/D))


Query: Series[(D^2 * n /(2*(n-1)))*Log[n/((1+e)*D)], {n, Infinity, 0}]
[Input interpretation]
series | (D^2 × n/(2 (n - 1))) log(n/((1 + e) D)) | point | n = ∞
order | n^0
[Series expansion at n = ∞]
1/2 D^2 log(n/(e D + D)) + O((1/n)^1)
(generalized Puiseux series)
[Series representation at n = ∞]
-(D^2 log(1/(D n + e D n)))/(2 (n - 1))


Query: Simplify[1.1511944248672998 - 1511944248672998/10000000000000000]
[Input interpretation]
simplify | 1.1511944248672998 - 1511944248672998/10000000000000000
[Result]
1.0000000000000000
[Quotient and Remainder]
1.0000000000000000 = 1 × 1 + 0.×10^-16
[Number name]
one
[Percent decrease]
1.1511944248672998 - 1511944248672998/10000000000000000 = 1.0000000000000000 is 13.13% smaller than 1.1511944248672998 = 1.1511944248672998.


Query: Series[D*n*Log[(1+e)*D/n] + D*n*Log[(2+e)/(1+e)], {n, Infinity, 0}]
[Input interpretation]
series | D n log((1 + e) × D/n) + D n log((2 + e)/(1 + e)) | point | n = ∞
order | n^0
[Series expansion at n = ∞]
D n log(((2 + e) D)/n) + O((1/n)^1)
(Puiseux series)


Query: Simplify[D*n*Log[(1+e)*D/n] + D*n*Log[(2+e)/(1+e)] - D*n*Log[D/n]]
[Input interpretation]
simplify | D n log((1 + e) × D/n) + D n log((2 + e)/(1 + e)) - D n log(D/n)
[Results]
D n (log(D/n) + log(2 + e)) - D n log(D/n)
[Results]
D n (-log(D/n) + log(((1 + e) D)/n) + log((2 + e)/(1 + e)))
[Expanded logarithmic form]
D n log(2 + e)
[Alternate form assuming D and n are real]
D n log((2 + e)/(1 + e)) + D n log(1 + e)


Query: Simplify[((1+e)*D/n)*(1 - D/(n-1) + (D/(n-1))*n/((1+e)*D)) - (2+e)*D/n]
[Input interpretation]
simplify | ((1 + e) × D/n) (1 - D/(n - 1) + D/(n - 1) × n/((1 + e) D)) - (2 + e) × D/n


Query: Series[((1+e)*D/n)*(1-D/(n-1)+(D/(n-1))*n/((1+e)*D)), {n, Infinity, 1}]
[Input interpretation]
series | ((1 + e) × D/n) (1 - D/(n - 1) + D/(n - 1) × n/((1 + e) D)) | point | n = ∞
order | n^1
[Series expansion at n = ∞]
((2 + e) D)/n + O((1/n)^2)
(Laurent series)
(converges when (1 + e) D^2 = D ∨ abs(n)>1)
[Series representation at n = ∞]
(D n (D n + e (D n + n - 1) + n - 2))/(n - 1)


Query: Series[(n*D^2*(n-1-D)/(2*(n-1)^2))*Log[n/((1+e)*D)], {n, Infinity, 0}]
[Input interpretation]
series | (n D^2 × (n - 1 - D)/(2 (n - 1)^2)) log(n/((1 + e) D)) | point | n = ∞
order | n^0
[Series expansion at n = ∞]
1/2 D^2 log(n/(e D + D)) + O((1/n)^1)
(generalized Puiseux series)
[Series representation at n = ∞]
-(D^2 (D n + n - 1) log(1/(D n + e D n)))/(2 (n - 1)^2)


Query: Simplify[((1-u)^2+2*u*(1-u)/v+u^2/v^2)/((1-u)+u/v)^2]
[Input interpretation]
simplify | ((1 - u)^2 + 2 u × (1 - u)/v + u^2/v^2)/((1 - u) + u/v)^2
[Results]
1
[Results]
u^2/(v^2 (u/v - u + 1)^2) - (2 u^2)/(v (u/v - u + 1)^2) + u^2/(u/v - u + 1)^2 + (2 u)/(v (u/v - u + 1)^2) - (2 u)/(u/v - u + 1)^2 + 1/(u/v - u + 1)^2


Query: Series[Binomial[n,2]*Log[1-(D/(n-1))^2+((D/(n-1))^2)/((1+e)*D/n)], {n, Infinity, 0}]
[Input interpretation]
series | binomial(n, 2) log(1 - (D/(n - 1))^2 + (D/(n - 1))^2/((1 + e) × D/n)) | point | n = ∞
order | n^0
[Series expansion at n = ∞]
(D n)/(2 + 2 e) - (D ((3 + 4 e + 2 e^2) D - 2 (1 + e)))/(4 (1 + e)^2) + O((1/n)^1)
(Taylor series)


Query: Simplify[((1-u)^2+2*u*(1-u)/v+u^2/v^2)-((1-u)+u/v)^2]
[Input interpretation]
simplify | ((1 - u)^2 + 2 u × (1 - u)/v + u^2/v^2) - ((1 - u) + u/v)^2
[Expanded form]
0


Query: rational fallback: (binom(n,2)-s)*log(1-pi^2+pi^2/p) ~ Dn/(2(1+e))
[fallback]
n=1000 D=20 logRV=8644.8467 target=9090.91
n=10000 D=100 logRV=443104.6772 target=454545.45
n=100000 D=200 logRV=9044655.6095 target=9090909.09


Query: Simplify[1-(1-Exp[-t])*q - ((1-q)+q*Exp[-t])]
[Input interpretation]
simplify | 1 - (1 - exp(-t)) q - ((1 - q) + q exp(-t))
[Expanded form]
0


Query: Simplify[551/1000]
[Input interpretation]
simplify | 551/1000
[Result]
551/1000
[Quotient and Remainder]
551 = (0) × 1000 + 551
[Decimal form]
0.551
[Percentage]
55.1%


Query: Assuming[n>1, Simplify[(n/2 - n^(1/4)) / Sqrt[n]]]
[error]
no result


Query: Simplify[(n/2 - n^(1/4))/n^(1/2)]
[Input interpretation]
simplify | (n/2 - n^(1/4))/sqrt(n)
[Result]
(n^(3/4) - 2)/(2 n^(1/4))
[Expanded form]
sqrt(n)/2 - 1/n^(1/4)


Query: Limit[(n/2 - n^(1/3))/Sqrt[n], n->Infinity]
[Limit]
lim_(n->∞) (n/2 - n^(1/3))/sqrt(n) = ∞


Query: Limit[n^(1/2)/(n/2 - n^(1/3)), n->Infinity]
[Limit]
lim_(n->∞) sqrt(n)/(n/2 - n^(1/3)) = 0
[Series expansion at n = ∞]
2 sqrt(1/n) + 4 (1/n)^(7/6) + 8 (1/n)^(11/6) + 16 (1/n)^(5/2) + 32 (1/n)^(19/6) + 64 (1/n)^(23/6) + 128 (1/n)^(9/2) + O((1/n)^(31/6))
(Puiseux series)


Query: Limit[(n/2 - n^(1/4))/n^(1/2), n->Infinity]
[Limit]
lim_(n->∞) (n/2 - n^(1/4))/sqrt(n) = ∞


Query: Simplify[L^3/n^3 /. L -> n/2]
[error]
no result


Query: Simplify[(n/2)^3/n^3]
[Input interpretation]
simplify | (n/2)^3/n^3
[Result]
1/8
[Quotient and Remainder]
1 = (0) × 8 + 1


Query: Assuming[n>1, (n/2)^3/n^3 == 1/8]
[Input]
Assuming[n>1, (n/2)^3/n^3 = 1/8]
[Result]
True


Query: Limit[(n - 1 - 2*n^(1/4))/Sqrt[n], n->Infinity]
[Limit]
lim_(n->∞) (n - 1 - 2 n^(1/4))/sqrt(n) = ∞


Query: Simplify[(n^(1/3))^3/n]
[Input interpretation]
simplify | (n^(1/3))^3/n
[Result]
1
[Quotient and Remainder]
1 = 1 × 1 + 0


Query: Simplify[(n-1-d-ell) - ((n-1-ell)-d)]
[error]
no result


Query: Simplify[(n-1-d-L) - ((n-1-L)-d)] /. L -> ell
[error]
no result


Query: Simplify[d + (n - 1 - d - ell) - (n - 1 - ell)]
[error]
no result


Query: d+(n-1-d-ell)-(n-1-ell) [exact rational fallback]
[fallback]
0 for all n,d,ell



Query: Simplify[(n-2)-d - (n-2-d)]
[Input interpretation]
simplify | (n - 2) - d - (n - 2 - d)
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[n-d-(n-2-d)]
[Input interpretation]
simplify | n - d - (n - 2 - d)
[Result]
2
[Quotient and Remainder]
2 = 2 × 1 + 0


Query: Limit[(n-2-n/3)/Sqrt[n], n->Infinity]
[Limit]
lim_(n->∞) (n - 2 - n/3)/sqrt(n) = ∞


Query: Assuming[n>4, (1/n)/(1/4)^2 == 16/n]
[Input]
Assuming[n>4, (1/n)/(1/4)^2 = 16/n]
[Result]
True


Query: Assuming[n>2 && 0<c<1/2, Limit[(n-2-c*n)/Sqrt[n], n->Infinity]]
[error]
no result


Query: Limit[(n-2-n/4)/Sqrt[n], n->Infinity]
[Limit]
lim_(n->∞) (n - 2 - n/4)/sqrt(n) = ∞


Query: Simplify[(n-2)-(n/2-1)]
[Input interpretation]
simplify | (n - 2) - (n/2 - 1)
[Result]
(n - 2)/2


Query: Limit[(n/2-1)/Sqrt[n], n->Infinity]
[Limit]
lim_(n->∞) (n/2 - 1)/sqrt(n) = ∞


Query: Assuming[n>4, n-1-(n/2-1) >= n/2]
[Input]
Assuming[n>4, n - 1 - (n/2 - 1)>=n/2]
[Result]
n/2>=n/2
[Alternate form]
True
