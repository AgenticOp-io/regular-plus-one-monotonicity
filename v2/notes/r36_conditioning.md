# r36: disjointness conditioning in (R2*) -- second-order (cluster) expansion

Status: **no L^3/n cancellation needed or true; the L^3/n term is an explicit deterministic coefficient that
matches the known kappa_2 exactly. Rigorous closure of (R2*) NOT achieved (sketch-level, gaps in §4).**
Nothing edits main.tex.

## 1. Exact one-factor identity (proved, elementary)
For M a uniform PM of K_n, F, U graphs, put w_e = x-1 on F\U, w_e = -1 on U (incl. F∩U). Then
  Z := E[x^{|M∩F|} 1{M∩U=∅}] = Σ_{S matching in F∪U} Π_{e∈S} w_e · q_{|S|},  q_k = 1/((n-1)(n-3)…(n-2k+1)).
(Expand Π_e(1+w_e 1[e∈M]).) This is a monomer–dimer gas with activities |w_e|/n and conflict degree ≤ 2L+2j.
Kotecky–Preiss converges for (|x-1|+1)(L+j)·C < n, so ln Z = Σ_k (clusters of ≤k edges), the k-th order
being O(n·L(CL/n)^{k-1}/n) = O(L^k/n^{k-1}) *per factor* (k=1: O(L); k=2: O(L^2/n); k=3: O(L^3/n^2)).

## 2. The 2nd-order term (computed; checked numerically)
With W1=Σw, Q2=Σw², P2 = Σ_v (s_v²-Σ_{e∋v}w_e²)/2, s_v=Σ_{e∋v}w_e:
  ln Z = q1 W1 + (q2-q1²)W1²/2 - q2(Q2/2+P2) + O(L³/n²).
Hafnian-DP exact vs this, n=12..20, L,j'∈{2,3}: first-order error ≈0.05–0.10, second-order error
≈1e-3 (`v2/scripts/r36_cluster2.py`). Mechanism: the s_v² pieces of (q2-q1²)W1²/2 (=s²/(2n) per factor)
and -q2P2 (=-s²/(2n)) cancel, leaving R/(4n), R=L(x-1)²+j' = O(L/n)·(1+L) per factor, so the O(L²/n)-per-factor
slack of Lemma avoid-overlap is really **O(L/n) deterministic + O(L³/n²) remainder**. For y=1 and U regular
this gives ln P(avoid U_j) = -n j'/(2(n-1)) + j'/(4n)+O(j'^3/n²) (F-independent; Tri enters only at 3rd order).

## 3. Why L^3/n is not an error but a tilt, and its coefficient (derived; checked numerically)
Dependence on the random overlap m_j=|F∩U_j| is, to the needed order, linear: ln Z_j = ln Z_j(m=0) + γ_j m_j,
γ_j ≈ -(y_j-1)/(n-1) (+O(L/n²)). Since m_j=Σ_{i<j}|M'_i∩F|, exposing M'_L,…,M'_1 *backwards* turns this into a
deterministic tilt of the activities: y_L=x, y_j = x·exp(Σ_{k>j}γ_k(y_k)), and
  ln E[x^T] = Σ_j [ln Z_j(y_j; m=0, U regular j-1) - ln Z_j(1; m=0)]
(group-1 avoid factors and P(D)^2 cancel exactly against the y=1 terms; they are F/U-independent by regularity).
Numerics at n up to 1e6, L up to 600 (`v2/scripts/r36_recursion.py`, mpmath 40 digits): prediction minus
(x-1)κ1 + (x-1)²κ2/2 with κ1=L²n/(2(n-1)), κ2=-L³/n+L²/n equals (0.88→0.99)·L⁴/n² (x=2), i.e. the L³/n and L²/n
coefficients agree exactly and the residual is O(L⁴/n²) = o(1) for L=o(n^{1/2}). So the matching-conditioning
structure reproduces C(x)=-(x-1)²/2 and no uncancelled L³/n term.

## 4. Gaps (NOT proved)
1. Linearisation in m_j needs m_j=O(L²) (up to polylog) with a tail bound under the tilted measure;
   terms dropped: q2 w²Σ_v o_v² (≤ L m/n²) and m² w²/n³. A priori m_j ≤ nL/2; need an overlap tail bound
   (e.g. via Lemma decomp-overlap moment generating function, which itself is only O(L³/n)-accurate -- circular
   unless bootstrapped: first use it to get a crude Poisson-type tail P(T>CL²)≤e^{-cL²}, then rerun).
2. Rigorous KP bound for third-and-higher clusters with signed weights (|w| activities; fine by KP absolute
   values, but constants not written), giving O(L³/n²) per factor → O(L⁴/n²) total.
3. Error propagation through the backward recursion with y_j random-free but γ_j depending on o_v statistics.
4. Only the cumulant-matching (κ_2) was checked; κ_k, k≥3 beyond the first cluster orders and the tail
   summability in (R2*) uniformly in y=λ^{-1}(1+O(L/n)) not verified (script uses x=2 only).
Verdict: proved = exact identity §1; sketched = §2–3 chain; failed to close = items 1–4, so (R2*) stays open.
