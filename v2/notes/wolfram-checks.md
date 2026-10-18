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


Query: Simplify[(n^(1/3))*(n^(1/3))^2/n]
[Input interpretation]
simplify | n^(1/3) × (n^(1/3))^2/n
[Result]
1
[Quotient and Remainder]
1 = 1 × 1 + 0


Query: Limit[(n-1-2*n^(1/4))/Sqrt[n], n->Infinity]
[Limit]
lim_(n->∞) (n - 1 - 2 n^(1/4))/sqrt(n) = ∞


Query: Assuming[ell>=1 && ell (s+ell)^2/n -> 0, Limit[(s+ell)/Sqrt[n], n->Infinity]]
[Input interpretation]
Assuming[ell>=1 ∧ ell × (s + ell)^2/n implies 0, lim_(n->∞) (s + ell)/sqrt(n)]
[Result]
0


Query: Simplify[ell*((n^(2/5))/(Log[n]))^2/n] /. ell -> n^(1/5)
[error]
no result


Query: Assuming[n>1 && s>0 && ell>0, (ell (s+ell)^2)/n == o(1) && ell==1 && Simplify[s^2/n]]
[error]
no result


Query: Assuming[D>1 && D/n -> 0, Limit[1/(6 D^3) + D/n, n->Infinity]]
[Input]
Assuming[D>1 ∧ D/n implies 0, lim_(n->∞)(1/(6 D^3) + D/n)]
[Result]
1/(6 D^3)


Query: Limit[n^(2/3)/Sqrt[n], n->Infinity]
[Limit]
lim_(n->∞) n^(2/3)/sqrt(n) = ∞


Query: Limit[1/(6 n) + n^(2/3)/n, n->Infinity]
[Limit]
lim_(n->∞)(1/(6 n) + n^(2/3)/n) = 0


Query: Limit[1/(6 (n^(2/3))^3) + n^(2/3)/n, n->Infinity]
[Limit]
lim_(n->∞)(1/(6 (n^(2/3))^3) + n^(2/3)/n) = 0


Query: Limit[(n^(1/3))^2/n, n->Infinity]
[Limit]
lim_(n->∞) (n^(1/3))^2/n = 0


Query: Assuming[ell>=1, Limit[ell (n^(1/4))^2 / n, n->Infinity]]
[Input interpretation]
Assuming[ell>=1, lim_(n->∞) ell × (n^(1/4))^2/n]
[Result]
0


Query: Simplify[(n/2)-1 - ((n/2)-1)]
[Input interpretation]
simplify | n/2 - 1 - (n/2 - 1)
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Assuming[D>=n/2, D-1 >= n/2-1]
[Input]
Assuming[D>=n/2, D - 1>=n/2 - 1]
[Result]
D - 1>=n/2 - 1
[Geometric figure of boundary]
line
[Alternate forms]
2 D>=n
[Alternate forms]
D>=n/2
[Alternate forms]
D - 1>=(n - 2)/2
[Solution]
n<=2 D
[Interval notation]
(-∞, 2 D]
[Integer solution]
D = m_1 + m_2 + m_3 - m_4, n = m_1 + 2 m_2 - 2 m_4 - m_5, m_5 element Z, m_5>=0, m_4 element Z, m_4>=0, m_3 element Z, m_3>=0, m_2 element Z, m_2>=0, m_1 element Z, m_1>=0


Query: Assuming[n>2, (1/n)/(1/2)^2 == 4/n]
[Input]
Assuming[n>2, (1/n)/(1/2)^2 = 4/n]
[Result]
True


Query: Limit[(n^(2/3)-1)/Sqrt[n], n->Infinity]
[Limit]
lim_(n->∞) (n^(2/3) - 1)/sqrt(n) = ∞


Query: Simplify[(n/2)-2]
[Input interpretation]
simplify | n/2 - 2
[Result]
(n - 4)/2


Query: Limit[(n/2-2)/Sqrt[n], n->Infinity]
[Limit]
lim_(n->∞) (n/2 - 2)/sqrt(n) = ∞


Query: Limit[(Sqrt[n]*Log[n]-2)/Sqrt[n], n->Infinity]
[Limit]
lim_(n->∞) (sqrt(n) log(n) - 2)/sqrt(n) = ∞


Query: Limit[2*Sqrt[n]*Log[n]/n, n->Infinity]
[Limit]
lim_(n->∞) (2 sqrt(n) log(n))/n = 0


Query: Limit[10000000/(Sqrt[n]*Log[n]), n->Infinity]
[Limit]
lim_(n->∞) 10000000/(sqrt(n) log(n)) = 0


Query: Simplify[n*D - D^2 - D*(n - D)]
[Input interpretation]
simplify | n D - D^2 - D (n - D)
[Result]
0


Query: Simplify[D*(n - D)/(2*D^2) - (n - D)/(2*D)]
[Input interpretation]
simplify | D × (n - D)/(2 D^2) - (n - D)/(2 D)
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(8/3)*n^(1/2)*n/(n/4)^2 - (128/3)*n^(-1/2)]
[Input interpretation]
simplify | 8/3 sqrt(n) × n/(n/4)^2 - 128/3 n^(-1/2)
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Assuming[D > L > 0 && n > 0, FullSimplify[(D*n/2)*Log[D/(D - L)] - (L*n/2)*Log[L/(D - L)] - (D*n/2)*Log[D] + (L*n/2)*Log[L] + ((D - L)*n/2)*Log[D - L]]]
[error]
no result


Query: FullSimplify[d*Log[d/(d - l)] - l*Log[l/(d - l)] - d*Log[d] + l*Log[l] + (d - l)*Log[d - l]]
[Input interpretation]
simplify | d log(d/(d - l)) - l log(l/(d - l)) - d log(d) + l log(l) + (d - l) log(d - l)
[Results]
d (log(d/(d - l)) - log(d)) + (d - l) log(d - l) + l (log(l) - log(l/(d - l)))
[Results]
(d - l) log(d - l) + d (log(-d/l) - log((l - d)/l)) - l (log(-d/l) + log(l/d) - log((l - d)/l)) - d log(d) + l log(l)
[Expanded logarithmic form]
0
[Alternate form assuming d>0, l>0, and d - l>0]
-d log(d) + log((d/(d - l))^d) + (d - l) log(d - l) - l log(l/(d - l)) + log(l^l)


Query: Assuming[d > l > 0, FullSimplify[d*Log[d/(d - l)] - l*Log[l/(d - l)] - d*Log[d] + l*Log[l] + (d - l)*Log[d - l]]]
[error]
no result


Query: Simplify[(d^d/(d - l)^d)*((d - l)^l/l^l)*(1/d^d)*l^l*(d - l)^(d - l)]
[Input interpretation]
simplify | d^d/(d - l)^d × (d - l)^l/l^l × 1/d^d l^l (d - l)^(d - l)
[Result]
1
[Quotient and Remainder]
1 = 1 × 1 + 0


Query: Simplify[-d*((l/d)*Log[l/d] + ((d - l)/d)*Log[(d - l)/d]) - (d*Log[d] - l*Log[l] - (d - l)*Log[d - l])]
[Input interpretation]
simplify | -d (l/d log(l/d) + (d - l)/d log((d - l)/d)) - (d log(d) - l log(l) - (d - l) log(d - l))
[Result]
(d - l) log(d - l) + l (log(l) - log(l/d)) + (l - d) log(1 - l/d) - d log(d)
[Expanded logarithmic form]
0
[Alternate form assuming d>0, l>0, and d - l>0]
-log(d^d) + (d - l) log(d - l) - (d - l) log((d - l)/d) + l log(l) - l log(l/d)


Query: Simplify[(d/l)^l*((d/(d - l))^(d - l))*(d^(-d))*l^l*(d - l)^(d - l)]
[Input interpretation]
simplify | (d/l)^l (d/(d - l))^(d - l) d^(-d) l^l (d - l)^(d - l)
[Result]
d^(-d) l^l (d - l)^(d - l) (-d/l)^(d - l) (d/l)^l ((l - d)/l)^(l - d)


Query: Simplify[(d^l/l^l)*(d^(d - l)/(d - l)^(d - l))*d^(-d)*l^l*(d - l)^(d - l)]
[Input interpretation]
simplify | d^l/l^l × d^(d - l)/(d - l)^(d - l) d^(-d) l^l (d - l)^(d - l)
[Result]
1
[Quotient and Remainder]
1 = 1 × 1 + 0


Query: Simplify[(n - 1)/D + 1/D + (n - D)/D^2 - n/D - (n - D)/D^2]
[Input interpretation]
simplify | (n - 1)/D + 1/D + (n - D)/D^2 - n/D - (n - D)/D^2
[Result]
0


Query: Simplify[16*n^(1/2)*n/(n/4)^3 - 1024*n^(-3/2)]
[Input interpretation]
simplify | 16 sqrt(n) × n/(n/4)^3 - 1024 n^(-3/2)
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[1/(1/2)^4 - 16]
[Input interpretation]
simplify | 1/(1/2)^4 - 16
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[10*6/(10*6 + 60*4) - 1/5]
[Input interpretation]
simplify | 10 × 6/(10 × 6 + 60 × 4) - 1/5
[Results]
1/5 - 1/5
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[6/(300/70) - 7/5]
[Input interpretation]
simplify | 6/(300/70) - 7/5
[Results]
7/5 - 7/5
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[4/(300/70) - 14/15]
[Input interpretation]
simplify | 4/(300/70) - 14/15
[Results]
14/15 - 14/15
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[D - (D + 1)/2 + 1 - (D + 1)/2]
[Input interpretation]
simplify | D - (D + 1)/2 + 1 - (D + 1)/2
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[Binomial[6, 3]/2 - 10]
[Input interpretation]
simplify | binomial(6, 3)/2 - 10
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(6 - 1)!/2 - 60]
[Input interpretation]
simplify | 1/2 (6 - 1)! - 60
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[300/70 - 30/7]
[Input interpretation]
simplify | 300/70 - 30/7
[Results]
30/7 - 30/7
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[10*6 + 60*4 - 300]
[Input interpretation]
simplify | 10 × 6 + 60 × 4 - 300
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[Binomial[6, 2] - 6 - 9]
[Input interpretation]
simplify | binomial(6, 2) - 6 - 9
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[D*s - s*(s - 1) - s*(D - s + 1)]
[Input interpretation]
simplify | D s - s (s - 1) - s (D - s + 1)
[Result]
0


Query: Simplify[4!*3!/2 + 3*3*2 - 90]
[Input interpretation]
simplify | 4! × (3!)/2 + 3 × 3 × 2 - 90
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[90/42 - 15/7]
[Input interpretation]
simplify | 90/42 - 15/7
[Results]
15/7 - 15/7
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[Binomial[8, 4]/2 - 35]
[Input interpretation]
simplify | binomial(8, 4)/2 - 35
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(9091/1610)/(198572/36225) - 409095/397144]
[Input interpretation]
simplify | (9091/1610)/(198572/36225) - 409095/397144
[Results]
409095/397144 - 409095/397144
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[1806808/371712775 * 200 - 1]
[Input interpretation]
simplify | 1806808/371712775 × 200 - 1
[Result]
-414047/14868511
[Quotient and Remainder]
-414047 = (0) × 14868511 + (-414047)
[Decimal approximation]
-0.027847240386074974151749290833493683395734784740718152611246680...


Query: Assuming[L>2, Limit[n^2*((L*n/2)*((L*n/2)-1)*((L*n/2)-2)/6)*(L/(n-1)*((L*(n-4)+2)/((n-2)*(n-3)))*(L^2/(L*n-4)*(1-(L-1)^2*(L*n-8)^2/(L*n-4)^3-(L-1)*(L*n-8)/(L*n-4)^2-4*(L-1)^2/(L*n-4)^2)*(1-(L^2-4*L+2-2*(L-1)^2*(L*n-8)/(L*n-4))/(L*n-4)))-3*(L/(n-1))^2*((L*(n-4)+2)/((n-2)*(n-3)))+2*(L/(n-1))^3)+L^8/48, n->Infinity]]
[error]
no result


Query: Limit[n^2*(L^2/(L*n-4)*(1-(L-1)^2*(L*n-8)^2/(L*n-4)^3-(L-1)*(L*n-8)/(L*n-4)^2-4*(L-1)^2/(L*n-4)^2)*(1-(L^2-4*L+2-2*(L-1)^2*(L*n-8)/(L*n-4))/(L*n-4))-L/(n-1)), n->Infinity]
[Limit]
lim_(n->∞) n^2 ((L^2 (1 - ((L - 1)^2 (L n - 8)^2)/(L n - 4)^3 - ((L - 1) (L n - 8))/(L n - 4)^2 - (4 (L - 1)^2)/(L n - 4)^2) (1 - (L^2 - 4 L + 2 - (2 (L - 1)^2 (L n - 8))/(L n - 4))/(L n - 4)))/(L n - 4) - L/(n - 1)) = 4
[Series expansion at n = ∞]
4 + (-L^3 + L^2 - 5 L + 8/L + 20)/n + (-48/L^2 - 17 L + 216/L - 40)/n^2 + (-768/L^3 + 1824/L^2 + 47 L - 368/L - 224)/n^3 - (L^5 - 448 L^4 + 1792 L^3 + 2752 L^2 - 12928 L + 6528)/(L^4 n^4) + O((1/n)^5)
(Laurent series)


Query: Limit[n^5/L^5*(L/(n-1)*((L*(n-4)+2)/((n-2)*(n-3)))*(L^2/(L*n-4)*(1-(L-1)^2*(L*n-8)^2/(L*n-4)^3-(L-1)*(L*n-8)/(L*n-4)^2-4*(L-1)^2/(L*n-4)^2)*(1-(L^2-4*L+2-2*(L-1)^2*(L*n-8)/(L*n-4))/(L*n-4))-L/(n-1))-2*(L/(n-1))^2*(((L*(n-4)+2)/((n-2)*(n-3)))-L/(n-1))), n->Infinity]
[error]
no result


Query: Simplify[(L*n/2)^3/6 * L^5/n^5 - L^8/(48*n^2)]
[Input interpretation]
simplify | (1/6 (L × n/2)^3) × L^5/n^5 - L^8/(48 n^2)
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[4*L*(L^2-5*L+2) - L*(L^4 - L^3 + 5*L^2 - 20*L - 8) + L*(L^4 - L^3 + L^2 - 16)]
[Input interpretation]
simplify | 4 L (L^2 - 5 L + 2) - L (L^4 - L^3 + 5 L^2 - 20 L - 8) + L (L^4 - L^3 + L^2 - 16)
[Result]
0


Query: Limit[n^5*(L/(n-1)*((L*(n-4)+2)/((n-2)*(n-3)))*(4/n^2)-2*(L/(n-1))^2*(((L*(n-4)+2)/((n-2)*(n-3)))-L/(n-1)))-4*L*(L^2-5*L+2), n->Infinity]
[Limit]
lim_(n->∞)(n^5 ((L (L (n - 4) + 2) 4)/((n - 1) ((n - 2) (n - 3)) n^2) - 2 (L/(n - 1))^2 ((L (n - 4) + 2)/((n - 2) (n - 3)) - L/(n - 1))) - 4 L (L^2 - 5 L + 2)) = 0
[Series expansion at n = ∞]
(4 L (8 L^2 - 31 L + 12))/n + (8 L (20 L^2 - 66 L + 25))/n^2 + (8 L (81 L^2 - 241 L + 90))/n^3 + (4 L (585 L^2 - 1627 L + 602))/n^4 + (12 L (658 L^2 - 1751 L + 644))/n^5 + O((1/n)^6)
(Laurent series)


Query: Limit[n*(n^2*(L^2/(L*n-4)*(1-(L-1)^2*(L*n-8)^2/(L*n-4)^3-(L-1)*(L*n-8)/(L*n-4)^2-4*(L-1)^2/(L*n-4)^2)*(1-(L^2-4*L+2-2*(L-1)^2*(L*n-8)/(L*n-4))/(L*n-4))-L/(n-1))-4)-(-L^3+L^2-5*L+20+8/L), n->Infinity]
[error]
no result


Query: Limit[(n*(n^2*(L^2/(L*n-4)*(1-(L-1)^2*(L*n-8)^2/(L*n-4)^3-(L-1)*(L*n-8)/(L*n-4)^2-4*(L-1)^2/(L*n-4)^2)*(1-(L^2-4*L+2-2*(L-1)^2*(L*n-8)/(L*n-4))/(L*n-4))-L/(n-1))-4))/L^3, n->Infinity]
[error]
no result


Query: Simplify[(L^8/(48*n^2))/(L^3/n) - L^5/(48*n)]
[Input interpretation]
simplify | (L^8/(48 n^2))/(L^3/n) - L^5/(48 n)
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Series[L/(n-1)*(L*(n-4)+2)/((n-2)*(n-3)), {n, Infinity, 2}]
[Input interpretation]
series | L/(n - 1) × (L (n - 4) + 2)/((n - 2) (n - 3)) | point | n = ∞
order | n^2
[Series expansion at n = ∞]
L^2/n^2 + (2 L (L + 1))/n^3 + O((1/n)^4)
(Laurent series)
(converges when abs(n)>3)
[Series representation at n = ∞]
(L n^2 (L (4 n - 1) - 2 n))/((n - 1) (2 n - 1) (3 n - 1))


Query: Limit[n^2*L/(n-1)*(L*(n-4)+2)/((n-2)*(n-3)) - L^2, n->Infinity]
[Limit]
lim_(n->∞)((n^2 L (L (n - 4) + 2))/((n - 1) ((n - 2) (n - 3))) - L^2) = 0
[Series expansion at n = ∞]
(2 L (L + 1))/n + (L (L + 12))/n^2 - (10 ((L - 5) L))/n^3 - (L (59 L - 180))/n^4 - (14 (L (17 L - 43)))/n^5 + O((1/n)^6)
(Laurent series)


Query: Simplify[(L^6/n^2)/(L^3/n) - L^3/n]
[Input interpretation]
simplify | (L^6/n^2)/(L^3/n) - L^3/n
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Fallback: the limit identifying the coefficient of 1/n in n^2(q3-p)-4 returned no result. Exact rational arithmetic for
n*(n^2*(q3-p)-4) - (-L^3+L^2-5*L+20+8/L),
with q3 the signed principal term after a 2-matching (including the summand 4(L-1)^2/(Ln-4)^2),
equals -6445528431584584717/30799677832475266995 at (L,n)=(5,400)
and -26692586805897374537317/510146877521279604067995 at (5,1600).
Both are O(1/n). The coefficient of L^3 in n^2(q3-p)-4 is therefore the one used for the L^8 mass.


Query: Simplify[L^3/4 - L*(L^2 - 2*L + 2)/4 - L*(L-1)/2]
[Input interpretation]
simplify | L^3/4 - L (1/4 (L^2 - 2 L + 2)) - L × (L - 1)/2
[Result]
0


Query: Limit[n*((L*n/2)*Log(1+(L/(n-1))*(2*Exp((2*L-1)/n)-1))-L^2/2-L^2*(3*L-1)/(2*n))-L^3/4, n->Infinity]
[Limit]
(insufficient time to determine limit)

Fallback: that limit returned no value. The same combination is the logarithm in the binomial-leftover proposition of the companion paper. Its series at n=∞, computed symbolically with L held as an indeterminate, is L^3/(4n) + L^3(2L+6)/(12n^2) through order 1/n^2. The Bernoulli stub
m(m-1)/(Ln) - N_adj α^2/L,
with α = u/(1+u), u=(L/(n-1))(2e^{(2L-1)/n}-1), m=(Ln/2)α and N_adj=n L(L-1)/2, has series -L(L^2-2L+2)/(4n) through order 1/n. Adding the two leading coefficients is the identity Wolfram returned as 0 above, and the sum is L(L-1)/(2n). High precision of n times (origin + binomial + stub - L(L-1)/(2n)) equals about -1.037 at (L,n)=(5,400) and about -0.249 at (5,1600), consistent with an O(L^4/n^2) remainder.

A separate numeric check of the conditional logarithm: with (L,t,Q,ru,rv,Nu,Nv,dW)=(5,10,3,1,0,4,0,0), n(n log(q/p) - log((L-ru)(L-rv)/L^2) - 2t/(Ln) - c1) equals about -16.75, -16.68, -16.67 at n=400,1600,6400, where c1=(Nu+Nv-ru rv-ru-rv)/L. The coefficient of 1/n is stable and the next term is O(1/n).


Query: Simplify[L^3*(a-1)^2/(4*a^2) - L*(a-1)*(L^2*a - L^2 - 2*L*a + 2*L - 2*a)/(4*a^2) - L*(a-1)*(L*a - L + a)/(2*a^2)]
[Input interpretation]
simplify | L^3 × (a - 1)^2/(4 a^2) - L (a - 1) × (L^2 a - L^2 - 2 L a + 2 L - 2 a)/(4 a^2) - L (a - 1) × (L a - L + a)/(2 a^2)
[Result]
0


Query: Simplify[-(a-1)*(-L^3*a-L^3-L^2*a+L^2+4*L*a*k-2*a*k)/(2*a^2) - L^2*(a-1)*(L*a+L+a-1)/(2*a^2) + (2*L-1)*(a-1)*k/a]
[Input interpretation]
simplify | -((a - 1) (-L^3 a - L^3 - L^2 a + L^2 + 4 L a k - 2 a k)/(2 a^2)) - L^2 (a - 1) × (L a + L + a - 1)/(2 a^2) + (2 L - 1) (a - 1) × k/a


Query: Simplify[-(a-1)*(-a*L^3-L^3-a*L^2+L^2+4*a*L*k-2*a*k) - L^2*(a-1)*(a*L+L+a-1) - 2*a*(2*L-1)*(a-1)*k]
[Input interpretation]
simplify | -((a - 1) (-a L^3 - L^3 - a L^2 + L^2 + 4 a L k - 2 a k)) - L^2 (a - 1) (a L + L + a - 1) - 2 a (2 L - 1) (a - 1) k


Query: Simplify[-(a-1)*(-a*L^3-L^3-a*L^2+L^2+4*a*L*k-2*a*k) - L^2*(a-1)*(a*L+L+a-1) + 2*a*(2*L-1)*(a-1)*k]
[Input interpretation]
simplify | -((a - 1) (-a L^3 - L^3 - a L^2 + L^2 + 4 a L k - 2 a k)) - L^2 (a - 1) (a L + L + a - 1) + 2 a (2 L - 1) (a - 1) k

Fallback: the three Simplify queries above returned an input interpretation and no result pod. The first of them is the coefficient identity with denominators retained. The second clears the denominator 2 a^2 but carries the wrong sign on the last summand; its expansion is 4 a k (1-a)(2 L-1), not the identity. The third is the corrected numerator
-(a-1)*(-a L^3 - L^3 - a L^2 + L^2 + 4 a L k - 2 a k) - L^2 (a-1)(a L + L + a - 1) + 2 a (2 L - 1)(a-1) k.
Exact expansion in Q[a,L,k] is the zero polynomial. That is the coefficient of 1/n in the linear-density origin leftover.

The averaged logarithm uses the Result 0 identity above. Its series, with a and L held fixed, is L(a-1)(L(a-1)+a)/(2 a^2 n) + O(L^4/n^2). At a=1/3 and L=6, n times the exact combination (origin at the fitted slope, binomial generating function, and Bernoulli stub) equals about 68.572 at n=2400 and about 66.303 at n=20000, against the predicted value 66. The gap shrinks proportionally to 1/n.

At density 1/3 the origin leftover through order 1/n^2 is
(-4 L^3 + 2 L^2 + 4 L k - 2 k)/n + (-91 L^4/6 + L^3 + 16 L^2 k + 5 L^2 - 2 L k - 2 k^2 - 3 k)/n^2.
The coefficient of 1/n matches the displayed formula, and the coefficient of 1/n^2 is quadratic in k and of degree 4 in L. With k=2 L^2, n^2 times the remainder after the 1/n terms, divided by L^4, stays near 8.5 at a=1/3 and near 3.5 at a=1/2 as n/L^2 grows.


Query: Simplify[4*(Log[4]-1) - 1]
[Input interpretation]
simplify | 4 (log(4) - 1) - 1
[Result]
log(256) - 5
[Expanded logarithmic form]
-5 + 8 log(2)
[Quotient and Remainder]
4 (log(4) - 1) - 1 = (0) × 1 + (4 (log(4) - 1) - 1)
[Decimal approximation]
0.5451774444795624753378569716654125446040010748820420329654400759...
[Property]
-1 + 4 (-1 + log(4)) is a transcendental number
[Expanded form]
4 log(4) - 5


Query: 256 > Exp[5]
[Input]
256>exp(5)
[Result]
True


Query: Limit[L^2*(1/L - (1 - Exp[-1/L])), L -> Infinity]
[Limit]
lim_(L->∞) L^2 (1/L - (1 - exp(-1/L))) = 1/2
[Series expansion at L = ∞]
1/2 - 1/(6 L) + 1/(24 L^2) - 1/(120 L^3) + 1/(720 L^4) + O((1/L)^5)
(Laurent series)


Query: Log[3/2] - 1/3 > 0
[Input]
log(3/2) - 1/3>0
[Result]
True


Query: ForAll[x, 0 < x <= 1/2, -Log[1 - x] - x <= x^2]
[Input]
for all _(x, 0<x<=1/2)-log(1 - x) - x<=x^2


Query: Minimize[{-Log[1 - x] - x - x^2, 0 <= x <= 1/2}, x]
[Input interpretation]
minimize | function | -log(1 - x) - x - x^2
domain | 0<=x<=1/2 | for | x
[Global minimum]
min{-log(1 - x) - x - x^2|0<=x<=1/2} = log(2) - 3/4 at x = 1/2


Query: Maximize[{-Log[1 - x] - x - x^2, 0 <= x <= 1/2}, x]
[Input interpretation]
maximize | function | -log(1 - x) - x - x^2
domain | 0<=x<=1/2 | for | x
[Global maximum]
max{-log(1 - x) - x - x^2|0<=x<=1/2} = 0 at x = 0


Query: (n*L^2*(1-4/(n-1)) + L*n + (L*n)^2/(n-1)^2)/(n-2)^2 - L^2/(n-1)^2 - ((n-4)*L^2 + n*L)/(n-2)^2 = 0 for n>2
[Input interpretation]
manipulate | plot | (n L^2 (1 - 4/(n - 1)) + L n + (L n)^2/(n - 1)^2)/(n - 2)^2 - L^2/(n - 1)^2 - ((n - 4) L^2 + n L)/(n - 2)^2 = 0
varying n from >2


Query: Assuming[n>2 && L>0, FullSimplify[(n*L^2*(1-4/(n-1)) + L*n + (L*n)^2/(n-1)^2)/(n-2)^2 - L^2/(n-1)^2 - ((n-4)*L^2 + n*L)/(n-2)^2]]
[error]
no result


Query: Assuming[n>1 && L>0, FullSimplify[-(L^2*n)/(2*(n-1)^2) + L^2/(2*n) + L^2*(2*n-1)/(2*n*(n-1)^2)]]
[error]
no result


Query: Assuming[n>4 && L>0, FullSimplify[(n-1)*L^2 - 2*L^2 + n*L - L^2 - ((n-4)*L^2 + n*L)]]
[error]
no result

Sympy fallback. The two formulas for the square trace of an L-regular host,
(n*L^2*(1-4/(n-1)) + L*n + (L*n)^2/(n-1)^2)/(n-2)^2
and
L^2/(n-1)^2 + ((n-4)*L^2 + n*L)/(n-2)^2,
have difference whose numerator is the zero polynomial. Wolfram returned no
result pod on FullSimplify of that difference.


Query: simplify (n-1)*L^2 - 3*L^2 + n*L - (n-4)*L^2 - n*L
[Input interpretation]
simplify | (n - 1) L^2 - 3 L^2 + n L - (n - 4) L^2 - n L
[Result]
0


Query: simplify -(L^2*n)/(2*(n-1)^2) + L^2/(2*n)
[Input interpretation]
simplify | -(L^2 n)/(2 (n - 1)^2) + L^2/(2 n)
[Results]
(L^2 (1 - 2 n))/(2 (n - 1)^2 n)
[Results]
(L^2 (1 - 2 n))/(2 (n - 1)^2 n)
[Results]
-(L^2 (2 n - 1))/(2 (n - 1)^2 n)


Query: Limit[n^2*((L^2/(n-1)^2 + ((n-4)*L^2 + n*L)/(n-2)^2) - L^2/n^2), n->Infinity]
[Limit]
lim_(n->∞) n^2 ((L^2/(n - 1)^2 + ((n - 4) L^2 + n L)/(n - 2)^2) - L^2/n^2) = L (1 + L) ∞
[Series expansion at n = ∞]
L (L + 1) n + 4 L - (2 ((L - 6) L))/n + ((32 - 13 L) L)/n^2 + (4 (20 - 11 L) L)/n^3 + O((1/n)^4)
(Laurent series)


Query: Limit[n^2*((((4*n*L^2-8*L*k+Sigma)*(1-4/(n-1))+2*(n*L-k)+4*(n*L-k)^2/(n-1)^2)/(n-2)^2 - 2*(n*L^2*(1-4/(n-1))+n*L+(n*L)^2/(n-1)^2)/(n-2)^2)/4 - L^2/(2*n)), n->Infinity]
[Limit]
lim_(n->∞) n^2 (1/4 (((4 n L^2 - 8 L k + σ) (1 - 4/(n - 1)) + 2 (n L - k) + (4 (n L - k)^2)/(n - 1)^2)/(n - 2)^2 - (2 (n L^2 (1 - 4/(n - 1)) + n L + (n L)^2/(n - 1)^2))/(n - 2)^2) - L^2/(2 n)) = 1/4 (2 L^2 - 2 k (1 + 4 L) + σ)
[Series expansion at n = ∞]
1/4 (-2 k (4 L + 1) + 2 L^2 + σ) + (-2 k (L + 1) - L^2)/n + (k^2 + k (4 L - 6) - (13 L^2)/2 - 2 σ)/n^2 + (6 k^2 + 2 k (13 L - 8) - 22 L^2 - 9 σ)/n^3 + (23 k^2 + 8 k (11 L - 5) - (123 L^2)/2 - 29 σ)/n^4 + O((1/n)^5)
(Laurent series)


Query: simplify (1/(n-2))^2*(Sigma+2*e) - 8*(1/(n-2))*(1/(2*(n-1)*(n-2)))*Sigma + 16*(1/(2*(n-1)*(n-2)))^2*e^2 - (Sigma*(1-4/(n-1))+2*e+4*e^2/(n-1)^2)/(n-2)^2
[Input interpretation]
simplify | (1/(n - 2))^2 (σ + 2 e) - 8 × 1/(n - 2) × 1/(2 (n - 1) (n - 2)) σ + 16 (1/(2 (n - 1) (n - 2)))^2 e^2 - (σ (1 - 4/(n - 1)) + 2 e + 4 × e^2/(n - 1)^2)/(n - 2)^2
[Results]
0
[Results]
(4 e^2)/(n^4 - 6 n^3 + 13 n^2 - 12 n + 4) - (4 e^2)/((n^2 - 4 n + 4) (n^2 - 2 n + 1))


Query: simplify (L/ell)*(ell^2/n) - (L*ell)/n
[error]
no result


Query: simplify (L/m)*(m^2/n) - (L*m)/n
[Input interpretation]
simplify | L/m × m^2/n - (L m)/n
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Limit[(Log[n])^2/n, n -> Infinity]
[Limit]
lim_(n->∞) (log^2(n))/n = 0


Query: simplify 2*alpha - alpha/(1-alpha)
[Input interpretation]
simplify | 2 α - α/(1 - α)
[Results]
(α (1 - 2 α))/(1 - α)
[Results]
2 α + 1/(α - 1) + 1
[Results]
(α (2 α - 1))/(α - 1)


Query: Minimize 2*alpha - alpha/(1-alpha) for alpha from 0 to 1/2
[Input interpretation]
minimize | function | 2 α - α/(1 - α)
domain | 0<=α<=1 2^(-1)
[Global minima]
min{2 α - α/(1 - α)|0<=α<=1/2} = 0 at α = 0
[Global minima]
min{2 α - α/(1 - α)|0<=α<=1/2} = 0 at α = 1/2


Query: simplify 1 - (1-eta)*(1-alpha) - (alpha + eta - alpha*eta)
[Input interpretation]
simplify | 1 - (1 - η) (1 - α) - (α + η - α η)
[Result]
0


Query: simplify 1 - 4*(1/8) - 2*(1/8)
[Input interpretation]
simplify | 1 - 4 × 1/8 - 2 × 1/8
[Result]
1/4
[Quotient and Remainder]
1 = (0) × 4 + 1
[Decimal form]
0.25


Query: simplify (1 + 1/8 + 2/8)/(1/4)
[Input interpretation]
simplify | (1 + 1/8 + 2/8)/(1/4)
[Result]
11/2
[Quotient and Remainder]
11 = 5 × 2 + 1
[Decimal form]
5.5


Query: simplify 2*((11/2)*6 + 3)/(7/8)
[Input interpretation]
simplify | 2 × (11/2 × 6 + 3)/(7/8)
[Result]
576/7
[Quotient and Remainder]
576 = 82 × 7 + 2
[Decimal approximation]
82.285714285714285714285714285714285714285714285714285714285714285...
[Repeating decimal]
82.285714^_ (period 6)


Query: simplify (j/sqrt(n) + 1/sqrt(n))^2 - (j+1)^2/n
[Input interpretation]
simplify | (j/sqrt(n) + 1/sqrt(n))^2 - (j + 1)^2/n
[Expanded form]
0


Query: simplify (j/sqrt(n) + 1/sqrt(n))^2 = (j+1)^2/n
[Input interpretation]
simplify | (j/sqrt(n) + 1/sqrt(n))^2 = (j + 1)^2/n
[Expanded form]
True


Query: simplify (25079/11569230)/(4*(1024/1785375)) - 626975/663552
[Input interpretation]
simplify | (25079/11569230)/(4 × 1024/1785375) - 626975/663552
[Results]
626975/663552 - 626975/663552
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: simplify (77949/13712410)/(9*(1024/1785375)) - 3092626575/2808301568
[Input interpretation]
simplify | (77949/13712410)/(9 × 1024/1785375) - 3092626575/2808301568
[Results]
3092626575/2808301568 - 3092626575/2808301568
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: simplify 19355/3507 - 2765/501
[Input interpretation]
simplify | 19355/3507 - 2765/501
[Results]
2765/501 - 2765/501
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: simplify (200881/9056250)/(49643/2245950) - 6227311/6205375
[Input interpretation]
simplify | (200881/9056250)/(49643/2245950) - 6227311/6205375
[Results]
6227311/6205375 - 6227311/6205375
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: simplify 6227311 - 6205375 - 21936
[Input interpretation]
simplify | 6227311 - 6205375 - 21936
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: simplify ((1-a)/a)*(1/(2*a)-1) - 1/(2*a) + 1/2 + (1-a)/(2*a) - (a-1)*(2*a-1)/(2*a^2)
[Input interpretation]
simplify | (1 - a)/a (1/(2 a) - 1) - 1/(2 a) + 1/2 + (1 - a)/(2 a) - (a - 1) × (2 a - 1)/(2 a^2)
[Result]
0


Query: simplify (1-a)/a + (2*a-1)/a - 1
[Input interpretation]
simplify | (1 - a)/a + (2 a - 1)/a - 1
[Result]
0


Query: simplify -(1-a)/a + (1-2*a^2)/(2*a^2) + 1/2 + (1-a)/(2*a) - (1-a)/(2*a^2)
[Input interpretation]
simplify | -(1 - a)/a + (1 - 2 a^2)/(2 a^2) + 1/2 + (1 - a)/(2 a) - (1 - a)/(2 a^2)
[Result]
0


Query: Limit n*(2*k^2 - 4*k*n^2 + 16*k*n - 16*k + n^3 - 5*n^2 + 5*n)/(2*(n^4 - 6*n^3 + 13*n^2 - 12*n + 4)) as n->infinity
[Limit]
lim_(n->∞) (n (2 k^2 - 4 k n^2 + 16 k n - 16 k + n^3 - 5 n^2 + 5 n))/(2 (n^4 - 6 n^3 + 13 n^2 - 12 n + 4)) = 1/2
[Series expansion at n = ∞]
1/2 + (1/2 - 2 k)/n + (-4 k - 1)/n^2 + (k^2 - 6 k - 13/2)/n^3 + (6 k^2 - 8 k - 22)/n^4 + O((1/n)^5)
(Laurent series)


Query: simplify (4*a^2*k - 2*a^2 - 2*a*k + 1)/(2*a^2) - (1-2*a^2)/(2*a^2) - k*(2*a-1)/a
[Input interpretation]
simplify | (4 a^2 k - 2 a^2 - 2 a k + 1)/(2 a^2) - (1 - 2 a^2)/(2 a^2) - k × (2 a - 1)/a
[Result]
0


Query: Limit n*(-(n-1)/2)*(Log[(a*n/2 - (n-k))/((n*(n-1)/2) - (n-k)) * (1 - (a*n/2 - (n-k))/((n*(n-1)/2)-(n-k)))] + Log[(a*n/(n-1))*(1-a*n/(n-1))] - 2*Log[((a*n-1)/(n-2))*(1-(a*n-1)/(n-2))]) as n->infinity
[Limit]
(insufficient time to determine limit)

Fallback: the query above used edge count \(an/2\) in place of \(an^2/2\). The corrected width, with \(\lambda(e)=(an^2/2-e)/(\binom{n}{2}-e)\), was expanded in sympy. The constant term of \(n\) times the width is \((4a^2 k-2a^2-2ak+1)/(2a^2)\). The algebraic reduction of that coefficient is the preceding Result 0. A later sympy series of \(n\) times the three-host width, minus that coefficient, is identically \(0\).


Query: simplify -(1-a)/a + (4*a^2*(1/(2*a)) - 2*a^2 - 2*a*(1/(2*a)) + 1)/(2*a^2) + 1/2 - 1/(2*a) + (1-a)/(2*a)
[Input interpretation]
simplify | -(1 - a)/a + (4 a^2 × 1/(2 a) - 2 a^2 - 2 a × 1/(2 a) + 1)/(2 a^2) + 1/2 - 1/(2 a) + (1 - a)/(2 a)
[Result]
0


Query: Limit k*(2*a^2*k*n - 2*a*k*n + 4*a*k - 3*a*n - 2*k + 2*n)/(a*(a*n^2 + 2*k - 2*n)) as n->infinity
[Limit]
lim_(n->∞) (k (2 a^2 k n - 2 a k n + 4 a k - 3 a n - 2 k + 2 n))/(a (a n^2 + 2 k - 2 n)) = 0
[Series expansion at n = ∞]
(k (2 a^2 k - a (2 k + 3) + 2))/(a^2 n) + (2 k (4 a^2 k - 3 a (k + 1) + 2))/(a^3 n^2) - (2 (k (2 a^3 k^2 - a^2 k (2 k + 11) + a (8 k + 6) - 4)))/(a^4 n^3) - (4 (k (6 a^3 k^2 - a^2 k (5 k + 14) + 2 a (5 k + 3) - 4)))/(a^5 n^4) + (4 k (2 a^4 k^3 - a^3 k^2 (2 k + 23) + 2 a^2 k (9 k + 17) - 12 a (2 k + 1) + 8))/(a^6 n^5) + O((1/n)^6)
(Laurent series)


Query: Limit n*k*(2*a^2*k*n - 2*a*k*n + 4*a*k - 3*a*n - 2*k + 2*n)/(a*(a*n^2 + 2*k - 2*n)) as n->infinity
[Limit]
lim_(n->∞) (n k (2 a^2 k n - 2 a k n + 4 a k - 3 a n - 2 k + 2 n))/(a (a n^2 + 2 k - 2 n)) = (k (2 - 3 a + 2 (-1 + a) a k))/a^2
[Series expansion at n = ∞]
(k (2 a^2 k - a (2 k + 3) + 2))/a^2 + (2 k (4 a^2 k - 3 a (k + 1) + 2))/(a^3 n) - (2 (k (2 a^3 k^2 - a^2 k (2 k + 11) + a (8 k + 6) - 4)))/(a^4 n^2) - (4 (k (6 a^3 k^2 - a^2 k (5 k + 14) + 2 a (5 k + 3) - 4)))/(a^5 n^3) + (4 k (2 a^4 k^3 - a^3 k^2 (2 k + 23) + 2 a^2 k (9 k + 17) - 12 a (2 k + 1) + 8))/(a^6 n^4) + O((1/n)^5)
(Laurent series)


Query: simplify k*(2 - 3*a + 2*(-1 + a)*a*k)/a^2 - k*(2*a^2*k - a*(2*k + 3) + 2)/a^2
[Input interpretation]
simplify | k × (2 - 3 a + 2 (-1 + a) a k)/a^2 - k × (2 a^2 k - a (2 k + 3) + 2)/a^2
[Result]
0


Query: simplify (a-1)*(2*a)/(2*a^2) - (a-1)*k/a - (1-a)*(k-1)/a
[Input interpretation]
simplify | (a - 1) × (2 a)/(2 a^2) - (a - 1) × k/a - (1 - a) × (k - 1)/a
[Result]
0


Query: simplify 3940070400/765747504900 - 89344/17363889
[Input interpretation]
simplify | 3940070400/765747504900 - 89344/17363889
[Results]
89344/17363889 - 89344/17363889
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: simplify 277888800/77306241600 - 2363/657366
[Input interpretation]
simplify | 277888800/77306241600 - 2363/657366
[Results]
2363/657366 - 2363/657366
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: simplify -L*(8*L^3 - 24*L^2 + 15*L - 3)/6 - (-4*L^4/3 + 4*L^3 - 5*L^2/2 + L/2)
[Input interpretation]
simplify | -L (1/6 (8 L^3 - 24 L^2 + 15 L - 3)) - (-4 × L^4/3 + 4 L^3 - 5 × L^2/2 + L/2)
[Result]
0


Query: simplify (j/n + 1/n)^2 - (j+1)^2/n^2
[Input interpretation]
simplify | (j/n + 1/n)^2 - (j + 1)^2/n^2
[Result]
0


Query: simplify (L^4/n^2)/(L^3/n) - L/n
[Input interpretation]
simplify | (L^4/n^2)/(L^3/n) - L/n
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: simplify L*(L^2+1)/(2*n) - L^3/(2*n) - L/(2*n)
[Input interpretation]
simplify | L × (L^2 + 1)/(2 n) - L^3/(2 n) - L/(2 n)
[Result]
0


Query: simplify L^2*(L^2+1)/(2*L*n) - L*(L^2+1)/(2*n)
[Input interpretation]
simplify | L^2 × (L^2 + 1)/(2 L n) - L × (L^2 + 1)/(2 n)
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: simplify (L-1)/(D-1) - L/(D-1) + 1/(D-1)
[Input interpretation]
simplify | (L - 1)/(D - 1) - L/(D - 1) + 1/(D - 1)
[Result]
0


Query: Sum[(1/3)^k/(2*k), {k, 3, Infinity}] - (Log[3/2] - 1/3 - 1/18)/2
[Input interpretation]
sum_(k=3)^∞ (1/3)^k/(2 k) - 1/2 (log(3/2) - 1/3 - 1/18)
[Result]
0


Query: simplify (n - D + j - 2) - (n/2 - 1) + (D - j + 1 - n/2)
[Input interpretation]
simplify | (n - D + j - 2) - (n/2 - 1) + (D - j + 1 - n/2)
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: simplify W*(1/c - 1/W) - (W/c - 1)
[Input interpretation]
simplify | W (1/c - 1/W) - (W/c - 1)
[Result]
0


Query: simplify (a/c - 1) - ((m/c)*(a/m - 1) + (m/c - 1))
[Input interpretation]
simplify | (a/c - 1) - (m/c (a/m - 1) + (m/c - 1))
[Result]
0


Query: expand (1+e)*(1+w)^2 - (1 + e + 2*w + 2*e*w + w^2 + e*w^2)
[Input interpretation]
expand | (1 + e) (1 + w)^2 - (1 + e + 2 w + 2 e w + w^2 + e w^2)
[Result]
0
[Expansion over finite field]
GF(2) | 0


Query: simplify (n^(-3/2))^(1/2)*(n^(-1))^(1/2) - n^(-5/4) for n>0
[Input interpretation]
simplify | sqrt(n^(-3/2)) sqrt(1/n) - n^(-5/4) | assuming n>0
[Result]
0
[Integer root]
n = 0


Query: simplify (n^(-3/2))^(1/3)*(n^(-3/2))^(2/3) - n^(-3/2) for n>0
[Input interpretation]
simplify | (n^(-3/2))^(1/3) (n^(-3/2))^(2/3) - n^(-3/2) | assuming n>0
[Result]
0
[Integer root]
n = 0


Query: simplify y*y^(q-1)*m^q/(y^q*m^q) for y>0, m>0
[Input interpretation]
simplify | y y^(q - 1) × m^q/(y^q m^q) y>0 | assuming | m>0
[Result]
y>0


Query: RSolve[{a[k+1]==4 a[k], a[0]==2}, a[k], k]
[Input interpretation]
solve a(k + 1) = 4 a(k)
a(0) = 2 for a(k)
[Input interpretation]
solve a(k + 1) = 4 a(k)
a(0) = 2 for a(k)
[Values]
k | 0 | 1 | 2 | 3 | 4
a(k) | 2 | 8 | 32 | 128 | 512


Query: simplify y^1*y^(q-1)*m^q - y^q*m^q
[Input interpretation]
simplify | y^1 y^(q - 1) m^q - y^q m^q
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Table[2*4^k, {k, 0, 4}]
[Input]
Table[2 × 4^k, {k, 0, 4}]
[Result]
{2, 8, 32, 128, 512}
[Table of values]
k | 0 | 1 | 2 | 3 | 4
2^(2 k + 1) | 2 | 8 | 32 | 128 | 512


Query: simplify (Exp[(x^K-1)/K])^K - Exp[x^K-1] for K>0, x>0
[Input interpretation]
simplify | exp^K((x^K - 1)/K) - exp(x^K - 1) K>0 | assuming | x>0
[Result]
e (e^((x^K - 1)/K))^K>K e^(x^K)
[Alternate forms]
e (e^(x^K/K - 1/K))^K>K e^(x^K)
[Alternate forms]
K e^(x^K)<e (e^(x^K/K - 1/K))^K
[Alternate form assuming K and x are positive]
(K - 1) e^(x^K)<0
[Alternate form assuming K and x are positive]
e^(x^K)>K e^(x^K)
[Alternate form assuming K and x are positive]
K<1


Query: PowerExpand[Exp[(x^K-1)/K]^K] - Exp[x^K-1]
[Input]
PowerExpand[exp^K((x^K - 1)/K)] - exp(x^K - 1)
[Result]
0


Query: simplify (1-l)*(n/2)/(l*n) - (1-l)*n/(2*l*n) + (1-l)*(n/2)^2/(l*n^2) - (1-l)/(4*l)
[Input interpretation]
simplify | (1 - l) × (n/2)/(l n) - (1 - l) × n/(2 l n) + (1 - l) × (n/2)^2/(l n^2) - (1 - l)/(4 l)
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: simplify (1-l)*(r*n/2)/(l*n) - (1-l)*r^2*n/(2*l*n) + (1-l)*(r*n/2)^2/(l*n^2) + (1-l)*r*(r-2)/(4*l)
[Input interpretation]
simplify | (1 - l) × (r × n/2)/(l n) - (1 - l) r^2 × n/(2 l n) + (1 - l) × (r × n/2)^2/(l n^2) + (1 - l) r × (r - 2)/(4 l)
[Result]
0


Query: simplify -(1-l)*r*(r-2)/(4*l) - r*(1-l)/(4*l) + (1-l)*r*(r-1)/(4*l)
[Input interpretation]
simplify | -((1 - l) (r × (r - 2)/(4 l))) - r × (1 - l)/(4 l) + (1 - l) r × (r - 1)/(4 l)
[Result]
0


Query: expand (r*n/2 - T)^2 - (r*n/2)^2 - (-r*n*T + T^2)
[Input interpretation]
expand | (r × n/2 - T)^2 - (r × n/2)^2 - (-r (n T) + T^2)
[Result]
0


Query: Sum[(3/4)*4^(-i), {i, 0, Infinity}]
[Infinite sum]
sum_(i=0)^∞ (3 4^(-i))/4 = 1
[Sum convergence]
sum_(i=0)^∞ (3 4^(-i))/4 converges
[Partial sum formula]
sum_(i=0)^n (3 4^(-i))/4 = 1 - 4^(-1 - n)


Query: N[(E^3-1)/3]
[Input]
N[1/3 (e^3 - 1)]
[Result]
6.36185
[Number name]
six point three six one eight four five six four one zero six two five five six


Query: expand 2*L*(2*L-2) - 2*L*(L-2) - 2*L^2
[Input interpretation]
expand | 2 L (2 L - 2) - 2 L (L - 2) - 2 L^2
[Result]
0
[Expansion over finite field]
GF(2) | 0


Query: simplify -(1-l)*2*L^2/(4*l) + L^2*(1/l - 1)/2
[Input interpretation]
simplify | -((1 - l) (2 × L^2/(4 l))) + L^2 (1/2 (1/l - 1))
[Result]
0


Query: simplify Sum[(b-1)/2, {b, 1, L}] - L*(L-1)/4
[Input interpretation]
simplify | sum_(b=1)^L (b - 1)/2 - L × (L - 1)/4
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: simplify (D - x) - l*(n-1-x) + (1-l)*(x - xb) - (D - l*(n-1) - (1-l)*xb)
[Input interpretation]
simplify | (D - x) - l (n - 1 - x) + (1 - l) (x - x b) - (D - l (n - 1) - (1 - l) x b)
[Result]
0


Query: simplify (L*n/2)*(L^2*n)/n^3 - L^3/(2*n)
[Input interpretation]
simplify | (L × n/2) × (L^2 n)/n^3 - L^3/(2 n)
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: simplify (1-l)/l^2 - (1-l)^2/(2*l^2) - (1-l^2)/l^2 - 3*(1-l)/l + (1-l)*(1+7*l)/(2*l^2)
[Input interpretation]
simplify | (1 - l)/l^2 - (1 - l)^2/(2 l^2) - (1 - l^2)/l^2 - 3 × (1 - l)/l + (1 - l) × (1 + 7 l)/(2 l^2)
[Result]
0


Query: Simplify[Det[{{a(1-a), a^2/l - a^2, a(1-l)},{a^2/l - a^2, a(1-a), a(1-l)},{a(1-l), a(1-l), l(1-l)}}] - a^2 (1-l) (l-a)^2/l]
[Input interpretation]
simplify | left bracketing bar a (1 - a) | a^2/l - a^2 | a (1 - l)
a^2/l - a^2 | a (1 - a) | a (1 - l)
a (1 - l) | a (1 - l) | l (1 - l) right bracketing bar - a^2 (1 - l) × (l - a)^2/l


Query: Simplify[Det[{{a(1-a), a(1-l)},{a(1-l), l(1-l)}}] - a (1-l) (l-a)]
[Input interpretation]
simplify | left bracketing bar a (1 - a) | a (1 - l)
a (1 - l) | l (1 - l) right bracketing bar - a (1 - l) (l - a)


Query: Simplify[(a^2 (1-l) (l-a)^2/l) * l (1-l) - (a (1-l) (l-a))^2]
[Input interpretation]
simplify | (a^2 (1 - l) × (l - a)^2/l) l (1 - l) - (a (1 - l) (l - a))^2
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0

### Fallback (exact rational): 3x3 and 2x2 covariance determinants

Wolfram returned no result pod for Det[...] - a^2(1-l)(l-a)^2/l and Det[...] - a(1-l)(l-a). Exact Fraction arithmetic on the 9x9 grid a=i/23, l=j/11 (i,j=1..9) gave 0 at all 81 points for both differences. After multiplying by l, both differences are polynomials of degree at most 6 in a and 4 in l, so the grid proves the identities.



Query: FullSimplify[(-(a^2/l) Log[a^2/l] - 2 (a - a^2/l) Log[a - a^2/l] - (l - 2 a + a^2/l) Log[l - 2 a + a^2/l]) - l Log[l] - 2 (-a Log[a] - (l - a) Log[l - a]), 0 < a < l < 1]
[Input interpretation]
simplify | (-a^2/l log(a^2/l) - 2 (a - a^2/l) log(a - a^2/l) - (l - 2 a + a^2/l) log(l - 2 a + a^2/l)) - l log(l) - 2 (-a log(a) - (l - a) log(l - a)) | assuming | 0<a<l<1
[Result]
0


Query: FullSimplify[D[(N0 - e) (-(E0 - e)/(N0 - e) Log[(E0 - e)/(N0 - e)] - (1 - (E0 - e)/(N0 - e)) Log[1 - (E0 - e)/(N0 - e)]), e] - Log[(E0 - e)/(N0 - e)], 0 < e < E0 < N0]
[Input interpretation]
simplify | d/(d e)((N0 - e) (-(e × 0 - e)/(N0 - e) log((e × 0 - e)/(N0 - e)) - (1 - (e × 0 - e)/(N0 - e)) log(1 - (e × 0 - e)/(N0 - e)))) - log((e × 0 - e)/(N0 - e)) | assuming | 0<e<e × 0<N0
[Result]
d/(d e)(e log(e/(e - N0)) - N0 log(-N0/(e - N0))) - log(e/(e - N0))
[Alternate forms]
-log(1/(e - N0)) + d/(d e)(e log(1/(e - N0)) - N0 log(N0/(N0 - e)) + e) - 1
[Alternate forms]
-log(1/(e - N0)) + d/(d e)(e (log(1/(e - N0)) + 1) - N0 (log(-N0) - log(e - N0))) - 1
[Alternate form assuming N0>0]
-2 i π floor((arg(e - N0) + π)/(2 π)) + d/(d e)(2 i e π floor((arg(e - N0) + π)/(2 π)) - i π N0 + N0 (-log(N0)) + (N0 - e) log(e - N0) + e) + log(e - N0) - 1
[Alternate form assuming N0>0]
-2 i π floor(arg(e - N0)/(2 π) + 1/2) + d/(d e)(e (2 i π floor(arg(e - N0)/(2 π) + 1/2) - log(e - N0) + 1) - N0 (-log(e - N0) + log(N0) + i π)) + log(e - N0) - 1


Query: simplify (L*n/2)^2/(n*(n-1)/2) - L^2*n/(2*(n-1))
[Input interpretation]
simplify | (L × n/2)^2/(n × (n - 1)/2) - L^2 × n/(2 (n - 1))
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: FullSimplify[-Log[1-l] - l Log[l/(1-l)] - (-l Log[l] - (1-l) Log[1-l]), 0<l<1]
[Input interpretation]
simplify | -log(1 - l) - l log(l/(1 - l)) - (-l log(l) - (1 - l) log(1 - l)) | assuming | 0<l<1
[Result]
0


Query: FullSimplify[D[(K - y) (-((M - y)/(K - y)) Log[(M - y)/(K - y)] - ((K - M)/(K - y)) Log[(K - M)/(K - y)]), y] - Log[(M - y)/(K - y)], 0 < y < M < K]
[Input interpretation]
simplify | d/(dy)((K - y) (-(M - y)/(K - y) log((M - y)/(K - y)) - (K - M)/(K - y) log((K - M)/(K - y)))) - log((M - y)/(K - y)) | assuming | 0<y<M<K
[Result]
0


Query: simplify 8*E^2*x^2*(1/(4*E^(8/5)*x))^2 - E^(-6/5)/2
[Input interpretation]
simplify | 8 e^2 x^2 (1/(4 e^(8/5) x))^2 - e^(-6/5)/2
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: simplify D[Log[(M - y)/(K - y)], y] + (1 - (M - y)/(K - y))/(((M - y)/(K - y)) (K - y))
[Input interpretation]
simplify | d/(dy) log((M - y)/(K - y)) + (1 - (M - y)/(K - y))/((M - y)/(K - y) (K - y))
[Result]
0
[Expanded form]
y^2/((K - y)^2 (M - y)) + (2 y)/((K - y) (M - y)) - (K y)/((K - y)^2 (M - y)) - (M y)/((K - y)^2 (M - y)) - K/((K - y) (M - y)) - M/((K - y) (M - y)) + (K M)/((K - y)^2 (M - y)) + 1/(M - y)


Query: N[E^(-6/5)/2]
[Input]
N[e^(-6/5)/2]
[Result]
0.150597
[Number name]
zero point one five zero five nine seven one zero five nine five six one zero one zero seven


Query: simplify -(8 a^2 l^2 - 10 a^2 l + a^2 - 8 a l^3 + 10 a l^2 - a l - 2 l^3 + 2 l^2)/(12 a l (a - l)(l - 1)) + (-1/6 - 1/(12 l (1 - l))) + 2 (5 a^2 l - 6 a^2 - 5 a l^2 + 6 a l - l^2 + l)/(12 a (a - l)(l - 1))
[error]
no result


Query: Together[-(8 a^2 l^2 - 10 a^2 l + a^2 - 8 a l^3 + 10 a l^2 - a l - 2 l^3 + 2 l^2)/(12 a l (a - l) (l - 1)) - 1/6 - 1/(12 l (1 - l)) + 2 (5 a^2 l - 6 a^2 - 5 a l^2 + 6 a l - l^2 + l)/(12 a (a - l) (l - 1))]
[error]
no result

Fallback (exact rational arithmetic, Wolfram returned no result for the two queries above):
Identity c3 + c1 - 2 c2 = 0 with c1 = -1/6 - 1/(12 l(1-l)) and c2, c3 as in the queries.
Substituting a = t l, the cleared numerator has degree < 7 in t and in l.
Evaluated with Python Fractions on the product grid l in {9/17,...,15/17}, t in {1/19,...,7/19}: 49 points, all exactly 0.
Independent check from raw cumulant tensors (scripts/multicolour_constant.py --grid) at (a,l) = (1/10,1/2), (1/7,2/5), (1/20,3/4), (1/5,1/2): C = 0.
Also c1 = -1/6 - 1/(12 l(1-l)) symbolically (sympy), matching the McKay-Wormald constant.
Separate invariants: Delta K4 = Delta T1 = 2(1-l)/l, Delta T3 = 0 (sympy).


Query: minimize 1 - cos(x) - 2 x^2/pi^2 for -pi <= x <= pi
[Input interpretation]
minimize | function | 1 - cos(x) - 2 × x^2/π^2
domain | -π<=x<=π
[Global minima]
min{1 - cos(x) - (2 x^2)/π^2|-π<=x<=π} = 0 at x = -π
[Global minima]
min{1 - cos(x) - (2 x^2)/π^2|-π<=x<=π} = 0 at x = π


Query: Det[4 IdentityMatrix[6] + ConstantArray[1, {6, 6}]] - 4^5*10
[Input interpretation]
left bracketing bar (4 I_6 + ConstantArray[1, {6, 6}]) - 4^5 × 10 right bracketing bar
[Result]
-62904320


Query: Det[4 IdentityMatrix[6] + ConstantArray[1, {6, 6}]]
[Input interpretation]
left bracketing bar 4 I_6 + ConstantArray[1, {6, 6}] right bracketing bar
[Result]
10240


Query: simplify 2*(1/(n-2))*(1-1/(2n-2)) - 2/((n-2)(2n-2)) - 2/(n-1)
[Input interpretation]
simplify | 2 × 1/(n - 2) (1 - 1/(2 n - 2)) - 2/((n - 2) (2 n - 2)) - 2/(n - 1)
[Results]
0
[Results]
-2/(n - 1) - 4/((2 n - 2) (n - 2)) + 2/(n - 2)


Query: simplify (1/(n-2))*(1-1/(2n-2)) - 3/((n-2)(2n-2)) - (n-3)/((n-1)(n-2))
[Input interpretation]
simplify | 1/(n - 2) (1 - 1/(2 n - 2)) - 3/((n - 2) (2 n - 2)) - (n - 3)/((n - 1) (n - 2))
[Results]
0
[Results]
-n/((n - 2) (n - 1)) + 1/(n - 2) + 3/((n - 2) (n - 1)) - 4/((n - 2) (2 n - 2))


Query: simplify -4/((n-2)(2n-2)) + 2/((n-1)(n-2))
[Input interpretation]
simplify | -4/((n - 2) (2 n - 2)) + 2/((n - 1) (n - 2))
[Result]
0


Query: limit n(n-1)(n-2)*9*(2/(n-1))^2*((n-3)/((n-1)(n-2))) as n->infinity
[Limit]
lim_(n->∞) (n (n - 1) ((n - 2) 9 (2/(n - 1))^2 (n - 3)))/((n - 1) (n - 2)) = 36
[Series expansion at n = ∞]
36 - 36/n - 108/n^2 - 180/n^3 - 252/n^4 + O((1/n)^5)
(Laurent series)


Query: limit (n(n-1)/2)*((n-2)(n-3)/2)*9*(2/(n-1))^2*(-2/((n-1)(n-2))) as n->infinity
[Limit]
lim_(n->∞) ((n (n - 1)) ((n - 2) (n - 3)) 9 (2/(n - 1))^2 (-2))/(2 2 ((n - 1) (n - 2))) = -18
[Series expansion at n = ∞]
-18 + 18/n + 54/n^2 + 90/n^3 + 126/n^4 + O((1/n)^5)
(Laurent series)


Query: limit (n(n-1)/2)*(3/24)*(2/(n-1))^2 as n->infinity
[Limit]
lim_(n->∞) ((n (n - 1)) 3 (2/(n - 1))^2)/(2 24) = 1/4
[Series expansion at n = ∞]
1/4 + 1/(4 n) + 1/(4 n^2) + 1/(4 n^3) + 1/(4 n^4) + O((1/n)^5)
(Laurent series)


Query: limit n(n-1)(n-2)*6*((n-3)/((n-1)(n-2)))^3 as n->infinity
[Limit]
lim_(n->∞) n (n - 1) ((n - 2) 6 ((n - 3)/((n - 1) (n - 2)))^3) = 6
[Series expansion at n = ∞]
6 - 18/n - 24/n^2 + 72/n^4 + 216/n^5 + O((1/n)^6)
(Laurent series)


Query: simplify n + n(n-3) - n(n-3)/2 - n(n-1)/2
[Input interpretation]
simplify | n + n (n - 3) - n × (n - 3)/2 - n × (n - 1)/2
[Result]
0


Query: limit as n->infinity of (n(n-1)/2)(2/(n-1))^3 + n(n-1)(n-2)((n-3)/((n-1)(n-2)))^3 + (n(n-1)/2)((n-2)(n-3)/2)(-2/((n-1)(n-2)))^3
[Limit]
lim_(n->∞)(1/2 (n (n - 1)) (2/(n - 1))^3 + n (n - 1) (n - 2) ((n - 3)/((n - 1) (n - 2)))^3 + ((n (n - 1)) ((n - 2) (n - 3)) (-2/((n - 1) (n - 2)))^3)/(2 2)) = 1
[Series expansion at n = ∞]
1 + 1/n + 2/n^2 + 6/n^3 + 18/n^4 + O((1/n)^5)
(Laurent series)


Query: simplify (n(n-1)/2)(3/24)(2/(n-1))^2 - n/(4(n-1))
[Input interpretation]
simplify | (n × (n - 1)/2) × 3/24 (2/(n - 1))^2 - n/(4 (n - 1))
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: simplify 9 (2/(n-1))^2 (n(n-1)/2) - 18 n/(n-1)
[Input interpretation]
simplify | 9 (2/(n - 1))^2 (n × (n - 1)/2) - 18 × n/(n - 1)
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: 4 + 9(-1/2 + 1/40 + 1/500) + 1/5
[Input]
4 + 9 (-1/2 + 1/40 + 1/500) + 1/5
[Exact result]
-57/1000
[Decimal form]
-0.057
[Continued fraction]
- [0; 17, 1, 1, 5, 5]
[Egyptian fraction expansion]
-1 + 1/2 + 1/3 + 1/10 + 1/104 + 1/19500
[Equivalent fractions]
-57/1000 | -114/2000 | -171/3000 | -228/4000 | -285/5000 | ...
[Occurrence in convergents]
(26 π)/1433≈0, 1/17, 1/18, 2/35, 11/193, 46/807, 57/1000, 160/2807, 217/3807, ...
(simple continued fraction convergent sequence)


Query: 2 + 6(-1/2 + 1/40 + 1/500) + 4/5
[Input]
2 + 6 (-1/2 + 1/40 + 1/500) + 4/5
[Exact result]
-19/500
[Decimal form]
-0.038
[Continued fraction]
- [0; 26, 3, 6]
[Egyptian fraction expansion]
-1 + 1/2 + 1/3 + 1/8 + 1/273 + 1/273000
[Equivalent fractions]
-19/500 | -38/1000 | -57/1500 | -76/2000 | -95/2500 | ...


Query: simplify 1 + 3(-1/2 + 1/8) - (1/2)(-1/4 + h)
[Input interpretation]
simplify | 1 + 3 (-1/2 + 1/8) - 1/2 (-1/4 + h)
[Result]
-h/2


Query: simplify 2 - (8s+49)/4 + 2s + 10
[Input interpretation]
simplify | 2 - 1/4 (8 s + 49) + 2 s + 10
[Result]
-1/4


Query: simplify -1/2 + (3/2)(1/9 - h) + 1/3 - 3 h
[Input interpretation]
simplify | -1/2 + 3/2 (1/9 - h) + 1/3 - 3 h
[Result]
-(9 h)/2


Query: simplify -1/2 + 3*(1/20) + (1/2)*(1/3)
[Input interpretation]
simplify | -1/2 + 3 × 1/20 + 1/2 × 1/3
[Result]
-11/60
[Quotient and Remainder]
-11 = (0) × 60 + (-11)
[Decimal approximation]
-0.183333333333333333333333333333333333333333333333333333333333333...
[Repeating decimal]
-0.183^_ (period 1)


Query: simplify -1/2 + 1/30 + 2/20 + 1/6
[Input interpretation]
simplify | -1/2 + 1/30 + 2/20 + 1/6
[Result]
-1/5
[Quotient and Remainder]
-1 = (0) × 5 + (-1)
[Decimal form]
-0.2


Query: simplify -1 + 2*(1/5 - h) + 3/5 - 3*h
[Input interpretation]
simplify | -1 + 2 (1/5 - h) + 3/5 - 3 h
[Result]
-5 h


Query: simplify -1/2 + 3/24 + (1/2)*(1/2 - h)
[Input interpretation]
simplify | -1/2 + 3/24 + 1/2 (1/2 - h)
[Results]
-1/8 (4 h + 1)
[Results]
-h/2 - 1/8
[Results]
1/8 (-4 h - 1)


Query: simplify 1 + 11*(-1/8)
[Input interpretation]
simplify | 1 + (11 × (-1))/8
[Result]
-3/8
[Quotient and Remainder]
-3 = (0) × 8 + (-3)
[Decimal form]
-0.375


Query: Simplify[(-1/6) - 2*(-1/12)]
[Input interpretation]
simplify | -1/6 - (2 × (-1))/12
[Results]
1/6 - 1/6
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(13/24) - 2*(13/48)]
[Input interpretation]
simplify | 13/24 - 2 × 13/48
[Results]
13/24 - 13/24
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(3/8) - 2*(3/16)]
[Input interpretation]
simplify | 3/8 - 2 × 3/16
[Results]
3/8 - 3/8
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[lam/(a*(lam-a)) - 1/a]
[Input interpretation]
simplify | λ/(a (λ - a)) - 1/a
[Results]
-1/(a - λ)
[Results]
1/(λ - a)


Query: Assuming[a>0&&lam>a, Series[lam/(a*(lam-a)),{a,0,1}]]
[error]
no result


Query: Simplify[lam/(a*(lam-a)) - (1/a + 1/(lam-a))]
[Input interpretation]
simplify | λ/(a (λ - a)) - (1/a + 1/(λ - a))
[Result]
0


Query: Simplify[1/(n*a^4) /. a -> n^(-1/4)*w]
[error]
no result


Query: Simplify[1/(n*(n^(-1/4))^4)]
[Input interpretation]
simplify | 1/(n (n^(-1/4))^4)
[Result]
1
[Quotient and Remainder]
1 = 1 × 1 + 0


Query: Simplify[Sqrt[d^(2/3)] / d^(1/2)]
[Input interpretation]
simplify | sqrt(d^(2/3))/sqrt(d)
[Result]
1/d^(1/6)


Query: Simplify[Sqrt[d^(2/3)]/Sqrt[d]]
[Input interpretation]
simplify | sqrt(d^(2/3))/sqrt(d)
[Result]
1/d^(1/6)


Query: Series[1/(2*a) - 3/8 + 2*a, {a, 0, 2}]
[Input interpretation]
series | 1/(2 a) - 3/8 + 2 a | point | a = 0
order | a^2
[Series expansion at a = 0]
2 a + 1/(2 a) - 3/8
(Laurent series)
(converges when a!=0)
[Approximations about a = 0 up to order 1]
(order n approximation shown with n dots)
[Series representations]
-3/8 + 1/(2 a) + 2 a = sum_(n=-∞)^∞ ( piecewise | -3/8 | n = 0
1/2 | n = -1
2 | n = 1) a^n
[Series representations]
-3/8 + 1/(2 a) + 2 a = sum_(n=-∞)^∞ ( piecewise | (-1)^n/2 | n>1
3/2 | n = 1
17/8 | n = 0) (-1 + a)^n


Query: Simplify[(3/8) - 2*(3/16) + 0]
[Input interpretation]
simplify | 3/8 - 2 × 3/16 + 0
[Results]
3/8 - 3/8
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(-3/4) - 2*(-5/8) + (-1/4)]
[Input interpretation]
simplify | -3/4 - 2 (-5/8) - 1/4
[Result]
1/4
[Quotient and Remainder]
1 = (0) × 4 + 1
[Decimal form]
0.25


Query: Simplify[(1-1/2)/(2*(1/2)) - 1/2]
[Input interpretation]
simplify | (1 - 1/2)/(2 × 1/2) - 1/2
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(1-2/5)/(2*(2/5)) - 3/4]
[Input interpretation]
simplify | (1 - 2/5)/(2 × 2/5) - 3/4
[Results]
3/4 - 3/4
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(1-1/3)/(2*(1/3)) - 1]
[Input interpretation]
simplify | (1 - 1/3)/(2 × 1/3) - 1
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(1-3/4)/(2*(3/4)) - 1/6]
[Input interpretation]
simplify | (1 - 3/4)/(2 × 3/4) - 1/6
[Results]
1/6 - 1/6
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Series[(-104*a^2+52*a-5)/(3*a*(2*a-1)), {a, 0, 2}]
[Input interpretation]
series | (-104 a^2 + 52 a - 5)/(3 a (2 a - 1)) | point | a = 0
order | a^2
[Series expansion at a = 0]
5/(3 a) - 14 + (20 a)/3 + (40 a^2)/3 + O(a^3)
(Laurent series)
(converges when 2 abs(a)<1 ∧ a!=0)
[Approximations about a = 0 up to order 2]
(order n approximation shown with n dots)
[Series representations]
(5 - 52 a + 104 a^2)/(3 a - 6 a^2) = -19 + sum_(n=1)^∞ 1/3 (-1 + a)^n (-5) ((-1)^n (-1 + 2^(1 + n)))
[Series representations]
(5 - 52 a + 104 a^2)/(3 a - 6 a^2) = sum_(n=-∞)^∞ ( piecewise | 5/3 | n = -1
(5 2^(1 + n))/3 | n>0
-14 | n = 0) a^n


Query: Limit[a*(-104*a^2+52*a-5)/(3*a*(2*a-1)), a->0]
[Limit]
lim_(a->0) (a (-104 a^2 + 52 a - 5))/(3 a (2 a - 1)) = 5/3
[Series expansion at a = 0]
5/3 - 14 a + (20 a^2)/3 + (40 a^3)/3 + (80 a^4)/3 + (160 a^5)/3 + O(a^6)
(Taylor series)


Query: Simplify[5/3 + 1/2 - 13/6]
[Input interpretation]
simplify | 5/3 + 1/2 - 13/6
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[13/6 - 5/6 - 4/3]
[Input interpretation]
simplify | 13/6 - 5/6 - 4/3
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: N[-5/6, 20]
[Input]
-5/6 | 20 digits
[Result]
-0.83333333333333333333
[Number name]
negative zero point eight three three three three three three three three three three three three three three four


Query: N[4/3, 20]
[Input]
4/3 | 20 digits
[Result]
1.3333333333333333333
[Number name]
one point three three three three three three three three three three three three three three three three


Query: Simplify[-1997/5184 - (-1997/5184)]
[Input interpretation]
simplify | -1997/5184 - -1997/5184
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(4258*(1/10)^2 - 2129*(1/10) + 262)/(216*(2*(1/10) - 1)) + 191/360]
[Input interpretation]
simplify | (4258 (1/10)^2 - 2129 × 1/10 + 262)/(216 (2 × 1/10 - 1)) + 191/360
[Results]
191/360 - 191/360
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(4258*(1/8)^2 - 2129*(1/8) + 262)/(216*(2*(1/8) - 1)) + 1997/5184]
[Input interpretation]
simplify | (4258 (1/8)^2 - 2129 × 1/8 + 262)/(216 (2 × 1/8 - 1)) + 1997/5184
[Results]
1997/5184 - 1997/5184
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Limit[a*(4258*a^2 - 2129*a + 262)/(216*a*(2*a - 1)), a->0]
[Limit]
lim_(a->0) (a (4258 a^2 - 2129 a + 262))/(216 a (2 a - 1)) = -131/108
[Series expansion at a = 0]
-131/108 + (535 a)/72 - (131 a^2)/27 - (262 a^3)/27 - (524 a^4)/27 - (1048 a^5)/27 + O(a^6)
(Taylor series)


Query: Simplify[-131/108 + 41/108 + 5/6]
[Input interpretation]
simplify | -131/108 + 41/108 + 5/6
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[13/6 - 131/108 - 103/108]
[Input interpretation]
simplify | 13/6 - 131/108 - 103/108
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(-1022*(1/10)^2+511*(1/10)-72)/(192*(2*(1/10)-1)) - 389/1920]
[Input interpretation]
simplify | (-1022 (1/10)^2 + 511 × 1/10 - 72)/(192 (2 × 1/10 - 1)) - 389/1920
[Results]
389/1920 - 389/1920
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Limit[(-1022*a^2+511*a-72)/(192*(2*a-1)), a->0]
[Limit]
lim_(a->0) (-1022 a^2 + 511 a - 72)/(192 (2 a - 1)) = 3/8
[Series expansion at a = 0]
3/8 - (367 a)/192 + (3 a^2)/2 + 3 a^3 + 6 a^4 + 12 a^5 + O(a^6)
(Taylor series)


Query: Simplify[13/6 + 3/8 - 131/108 - 287/216]
[Input interpretation]
simplify | 13/6 + 3/8 - 131/108 - 287/216
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(-1022*(1/20)^2+511*(1/20)-72)/(192*(2*(1/20)-1)) - 363/1280]
[Input interpretation]
simplify | (-1022 (1/20)^2 + 511 × 1/20 - 72)/(192 (2 × 1/20 - 1)) - 363/1280
[Results]
363/1280 - 363/1280
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(-1022*(1/8)^2+511*(1/8)-72)/(192*(2*(1/8)-1)) - 257/1536]
[Input interpretation]
simplify | (-1022 (1/8)^2 + 511 × 1/8 - 72)/(192 (2 × 1/8 - 1)) - 257/1536
[Results]
257/1536 - 257/1536
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(-1022*(1/12)^2+511*(1/12)-72)/(192*(2*(1/12)-1)) - 2629/11520]
[Input interpretation]
simplify | (-1022 (1/12)^2 + 511 × 1/12 - 72)/(192 (2 × 1/12 - 1)) - 2629/11520
[Results]
2629/11520 - 2629/11520
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[5*(1-1/3)/(3*(1/3)) - 10/3]
[Input interpretation]
simplify | 5 × (1 - 1/3)/(3 × 1/3) - 10/3
[Results]
10/3 - 10/3
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[5*(1-2/5)/(3*(2/5)) - 5/2]
[Input interpretation]
simplify | 5 × (1 - 2/5)/(3 × 2/5) - 5/2
[Results]
5/2 - 5/2
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[5*(1-2/3)/(3*(2/3)) - 5/6]
[Input interpretation]
simplify | 5 × (1 - 2/3)/(3 × 2/3) - 5/6
[Results]
5/6 - 5/6
[Results]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(1-lam)/(2*lam) + 5*(1-lam)/(3*lam) - 13*(1-lam)/(6*lam)]
[Input interpretation]
simplify | (1 - λ)/(2 λ) + 5 × (1 - λ)/(3 λ) - 13 × (1 - λ)/(6 λ)
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(1-lam)/(2*lam)+5*(1-lam)/(3*lam)+3*(1-lam)/(8*lam)-131*(1-lam)/(108*lam) - 287*(1-lam)/(216*lam)]
[Input interpretation]
simplify | (1 - λ)/(2 λ) + 5 × (1 - λ)/(3 λ) + 3 × (1 - λ)/(8 λ) - 131 × (1 - λ)/(108 λ) - 287 × (1 - λ)/(216 λ)
[Result]
0
[Quotient and Remainder]
0 = (0) × 1 + 0


Query: Simplify[(d^(2/3))*(Log[n]^(1/3))/Sqrt[n] /. d -> n^(3/4)/Log[n]^(1/2)]
[error]
no result

Query: Simplify[(d^(2/3))*(Log[n]^(1/3))/Sqrt[n] /. d -> n^(3/4)/Log[n]^(1/2)]
[error]
no result
Fallback (sympy exact): at d=n^{3/4}/log(n)^{1/2} the ratio delta/sqrt(n) simplifies to 1;
hence delta=o(n^{1/2}) throughout d=o(n^{3/4}/log(n)^{1/2}).
Likewise delta/n -> 0 throughout d=o(n^{3/2}/log(n)^{1/2}).
