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
