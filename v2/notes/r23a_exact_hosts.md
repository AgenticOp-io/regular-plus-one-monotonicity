# r23a: which hosts (<=4 edges) have exactly computable P(H in G) from D-regularity alone
G uniform simple D-regular on [n], m=nD/2, nD even, n>=D+1. P(H)=P(H subset G)=g(H)/g(0). Q(H)=P(H) * prod_v (D-h_v)!/D! * (N-1)!!/(N-2|H|-1)!! (r17a/r22b).
Scripts: v2/scripts/r23a_counts.py (formulas + brute force), r23a_check.py (vs exact DP), r23a_ursell.py, r23a_f1.py. All below VERIFIED.

## Principle (proved)
Let c(H)=#copies of H in G. S_n acts transitively on copies of H in K_n, so P(H)=E[c(H)]/#copies_K_n(H), where #copies = n^(v)/|Aut H| (falling factorial n^(v) over v=|V(H)|).
Hence P(H) is EXACT (closed form) whenever c(H) is a deterministic function of (n,D), and is an explicit affine function of E[t], E[q] when c(H) is affine in
t=#triangles, q=#4-cycles of G (copies as subgraphs, not induced).

## A. Exactly determined by (n,D) alone  (PROVED)
- Edge: P=D/(n-1).   Every star K_{1,k} (k<=D): c=n C(D,k), P=C(D,k)/C(n-1,k).   [r22b for k=2]
- 2K2: c = C(m,2) - n C(D,2) (all edge pairs minus adjacent pairs), so  P(2K2) = [C(nD/2,2) - n C(D,2)] / (3 C(n,4)).  NEW.
- Exact star Q-ratio: Q(K_{1,k})/Q(0) = prod_{i=1..k}(nD-2i+1) / (D^k (n-1)(n-2)...(n-k))   (k=1,2 agree with r22b).
- Disjoint unions of >=2 stars other than 2K2 are NOT determined by symmetry alone: already P3+K2, 3K2 need t (below).

## B. Affine in t only (3-edge hosts)  (PROVED, brute-force verified)
Counting identities (m=nD/2):  K3: t.  P4 = m(D-1)^2 - 3t  (edge as middle, subtract closed ones).  P3+K2 = n C(D,2)(m-3D+2) + 3t  (edges missing the 3 vertices; sum of [u~w] over cherries = 3t).
3K2 = C(m,3) - K13 - P3K2 - P4 - K3.
=> P(P4)= [m(D-1)^2 - 3E t]/(n(n-1)(n-2)(n-3)/2), etc. So ALL 3-edge hosts reduce to the single number E t = C(n,3) P(K3): this is exactly the r2(D) gap. No more info than E t is hidden at 3 edges.

## C. Affine in (t,q) (4-edge hosts)  (PROVED by counting; brute-force verified on random regular graphs n=10..12, D=3,4; and against exact DP n=9..14)
K14 = nC(D,4);  chair = nD(D-1)C(D-1,2) - 6(D-2)t;  P5 = nC(D,2)(D-1)^2 - 4q - 3(2D-3)t;  C4=q;  paw = 3(D-2)t;
K13+K2 = nC(D,3)(m-4D+3)+3(D-2)t;  P4+K2 = P4(m-4D+3)+4q+6(D-2)t;  K3+K2 = t(m-3D+3);
4K2 = [3K2 (m-6D+3) + P4K2]/4;  P3+P3 and P3+2K2 from (total C(m,4)) and (cherry-weighted total) linear equations (see formulas()).
Bug found/fixed on the way: the chord sum for P4+K2 is 4q+6(D-2)t, not 12(D-2)t (reversal symmetry).
DP check (r23a_check.py D n): D=3 n=10,14 and D=4 n=9: all 19 host probabilities predicted from E t, E q alone match the exact DP, 0 mismatches (Fractions).
=> every <=4-edge host probability, hence log p_U, hence the 4th Ursell u_T of ANY 4-edge T, is an explicit function of (n, D, E t, E q). R2*(k=4) is therefore a statement about E t and E q only.

## D. Consequence for R2*(k=4) (reduction PROVED; the asymptotic input is NOT)
Write E t = (D-1)^3/6 (1+e1/n+e2/n^2+..), E q = (D-1)^4/8 (1+f1/n+f2/n^2+..). Plugging into u_T = sum_{U<=T}(-1)^{4-|U|} log P(U) (r23a_ursell.py, mpmath, n up to 1e7, D=3..6):
- C4:  n*u = f1 - 2 (+O(1/n)) for every D=3..6.  So u_C4=O(n^-2) <=> f1=2 exactly.  (Coefficient of e1: O(n^-2).)
- P5, paw, chair: u = O(n^-2) whenever e1,f1=O(1); for D=3: n^2 u_P5 -> -1/9 + e1/3 - 2 f1/3; n^2 u_paw -> -37/9 + 4e1/3 ; n^2 u_chair -> -5/9 (no dependence on e1,f1 at this order). (D=4..6 values in r23a_ursell run; same structure.)
- e2,f2 enter only at n^-3.
Numerics (exact DP, n*(E q/((D-1)^4/8)-1)): D=3: 2.52,2.35,2.26,2.21,2.17,2.15 for n=10..30; Richardson -> 1.99. D=4 -> 1.97. So f1=2 is numerically right.
E t: e1 -> 1.99 for D=3 (Richardson), D=4 ~2.2 at n<=22 (unconverged).
**So R2*(k=4, all non-star connected T) <=> (E t = (D-1)^3/6 (1+O(1/n)),  E q = (D-1)^4/8 (1+2/n+O(n^-2))) for fixed D.**  The O(1/n) for E t and the first-order constant f1=2 for E q are the whole content (the P5/paw/chair n^-2 rates need only boundedness of e1,f1).

## E. Honest gaps
- Not proved: E q = (D-1)^4/8 (1+2/n+O(n^-2)) and E t = (D-1)^3/6(1+O(1/n)). Known literature (McKay-Wormald-Wysocka short cycles) gives relative error O(1/n) for cycle counts, which gives the E t statement but NOT the exact f1=2 (that needs a first-order-corrected cycle-count expansion). I did not search the literature this round.
- D growing (L=D up to n^{1/2}): all identities in A-C are exact for any D; only E t, E q asymptotics are needed, now with D-uniform error control.
- The pairing-part claim (n^-3 for non-star) is taken from r16w1/r20a, not re-proved. Here I used u_T of log p_U directly, which is exact and does not need it; the Q/pairing split was not used.
- Stars: u of log p_U for stars is exactly computable (C(D,j)/C(n-1,j)) but contains the O(1) saturation term log C(D,j), consistent with "only stars violate n^-2".
- Only fixed D=3..6 in numerics for the Ursell expansion; n<=30 DP.
