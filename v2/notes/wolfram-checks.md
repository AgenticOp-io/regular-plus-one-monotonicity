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
