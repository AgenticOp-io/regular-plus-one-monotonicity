# r14w2: diamond / C4 terms in c0(j,k,D), w=0, j,k>=2
Scripts: v2/scripts/r14w2_mc.py (MC), r14w2_poly.py (c0 polynomials; imports r12w3_exact.c0). Output: r14w2_poly_out.txt.

## Re-derivation (agrees with r12w2/r12w3; no change)
- N2 = sum over directed edges of F(t), t = #common nbrs of uv. F is a polynomial in t of degree <=j, so Newton-expand F = F0 + F1 (t)_1 + F2 (t)_2/2 + ...;
  (t)_3 etc. have expectation O(n^-3) per directed edge, i.e. beyond relative n^-2. So only E(t)_1 (needs r1) and E(t)_2 matter.
- Diamonds: ordered distinct common nbrs (w1,w2) of directed uv: (D-1)(D-2) choices in N(u); w1~v prob (D-1)^2/(nD) [w1 has D-1 free stubs, v has D-1],
  w2~v prob (D-1)(D-2)/(nD) [v has one stub fewer]. E(t)_2 = (D-1)^4 (D-2)^2/(nD)^2. (r11w3's ((D-1)^3/(nD))^2 was wrong.)
- C4 analogue = the "pairs" term in N1 (v outside {u}+L adjacent to two of them), plus eL (edges inside L). No C4 enters N2 at this order.
  pairs = j(D-j)(D-1)^2/(nD) [u-leaf common nbr] + C(j,2)(D-1)^3/(nD) [leaf-leaf common nbr]. Same stub counting; the leaf-leaf term has (D-1)^3, not (D-1)^2 (a vertex has D stubs, one used by leaf1 -> D-1 for leaf2).
  eL = C(j,2)(D-1)^2/(nD). N1 uses sum_v s_v = (j+1)D-2j-2eL exactly.

## MC (exact uniform simple D-regular, pairing + rejection; r14w2_mc.py; L averaged over all j-subsets of N(u))
 D=4,j=3: sum C(s_v,2)*n: n=32 29.00+-.31, n=64 26.97+-.39, n=128 26.60+-.51; pred 27.00  (ratio 1.074, .999, .985)
 D=3,j=2: n=32 5.72+-.10, n=64 5.31+-.13, n=128 5.72+-.19; pred 5.333  (ratio 1.073, .995, 1.072; n=128 is a 2-sigma fluctuation)
 sum_v s_v (eL term): D=4,j=3 pred/MC 9.578/9.536(n32), 9.789/9.791(n64), 9.8945/9.893(n128); D=3,j=2 4.9167/4.9116, 4.9583/4.9603, 4.9792/4.9775: agree within ~1-2 SE.
 sum_dir (t)_2 / pred (new): D=4: 1.13+-.08 (n32), 1.06+-.11 (n64), 0.90+-.25 (n128); consistent with 1 (rare event, large noise at big n). Earlier r12w2: 1.415,1.186,1.063 (n=16,32,64) ~ 1+4/n; old formula off by ~2.2x.
 So the C4/pairs/eL terms hold at leading order; E(t)_2 formula confirmed (MC noise-limited at the 10% level at n=64; the stub count itself is exact-combinatorial).

## Final c0(j,k,D), y=1/D (n^0 and n^-1 coefficients of the relative error vanish identically; error = c0/n^2 + ...)
 (2,2): 124y^2 - 92y + 25/2        (3,1): 249y^2/2 - 89y + 25/2     (3,2): 224y^2 - 144y + 18
 (3,3): 741y^2/2 - 213y + 49/2     (4,1): 222y^2 - 136y + 18        (4,2): 366y^2 - 208y + 49/2
 (4,3): 570y^2 - 296y + 32         (4,4): 840y^2 - 400y + 81/2
 Constant term (j+k+1)^2/2 in every case. (Equivalent to r12w3 forms, e.g. (2,2) = (25D^2-184D+248)/(2D^2).)
 Check vs r7+r13 data fits (deg 3, nmin 20; formula/fit): (2,2) D=5,6,7: -.94/-.94 .61/.61 1.89/1.89; (3,2): -1.84/-1.84 .22/.22 2.00/2.00;
 (3,3): -3.28/-3.29 -.71/-.73 1.63/1.61; (4,2): -2.46/-2.47 0/-.02 2.26/2.23; (4,4): -5.90/-5.94 -2.83/-2.92 .50/.36. D=8,9 not converged (see r13w3).

## Proved vs formula-only
- Proved (derivation + MC): CM leading counts for diamonds E(t)_2, eL, pairs, C4; simple-vs-CM conditioning changes them by 1+O(1/n) (sketch, r12w2; relies on Janson/McKay-type results, citations not checked).
- Algebra (exact, sympy): the polynomial-in-1/D forms, vanishing of n^0, n^-1 terms, and the limit (j+k+1)^2/2 for each listed (j,k).
- Formula-only / assumed: r1=3(D-1)/D (numerically confirmed D=4 to 5 digits in r13w3, not derived); error terms uniform in D; general-(j,k) closed form (only j<=4 computed, pattern c0 = (j+k+1)^2/2 + O(1/D) is a conjecture); (3,3),(4,k) at D>=8 unconfirmed by data. The (D-1)^3 term in (t)_3 and higher differences F3+ are dropped by an order-counting argument, not tested numerically.
