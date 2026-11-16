# r6: R2* on n^{1/3} < L < n^{1/2}

Status: **NOT PROVED.** Blocker pinpointed to one estimate (B*). main.tex not edited.
Legend: [P] proved, [N] numerical, [C] conjecture/heuristic.

## Plan
1. Restate R2*: log E[y^T] = sum_k w^k kappa_k/k!, w=y-1, T=|F1∩F2|; need kappa1..3 exact (done r2/r4) and tail sum o(1).
2. Reduce the tail to one cumulant estimate with explicit constants.
3. Test whether any available tool (switching, McKay avoidance) gives that estimate beyond n^{1/3}.
4. State the blocking estimate precisely.

## 1. Explicit tail reduction [P, arithmetic checked in v2/scripts/r6_tail_arith.py]
(B*)  |kappa_k| <= C^k k! L^{k+1}/n^{k-1} for all k>=4, L<=n/4.
Given (B*) and r := C w L/n <= 1/2:
  |sum_{k>=4} w^k kappa_k/k!| <= sum_{k>=4} (Cw)^k L^{k+1}/n^{k-1} <= 2 (Cw)^4 L^5/n^3.
So the tail is o(1) iff L^5/n^3 -> 0, i.e. L = o(n^{3/5}); in particular on all of L = o(n^{1/2}).
With Theorem A (r4: t3 <= (L)_3/(n-2L-12)^3, kappa3 = O(L^4/n^2+L^6/n^3)) the k<=3 terms are
o(1) exactly for L=o(n^{1/2}). Hence **R2* on L=o(n^{1/2}) <=> (B*) up to the constants** [P, conditional on B*].
(B*) is needed for all k>=4; no cheaper crude bound for large k is available, see 3.

## 2. What cannot work [P/argument, from r4 Sec.2, r5 Sec.2]
Switching bounds p_S<= (n-4|S_i|-4L)^{-|S|}: relative error O(|S|L/n) = O(L^3/n) at |S|~L^2.
It is one-sided, product-over-edges, and cannot see the connected part of log p_S, which is n^{-(k-1)} for a k-cluster.
So n^{1/3} is the hard limit of every product-form (switching/avoidance) argument. [P]

## 3. The single blocking estimate
(B*) is equivalent to a cluster expansion of p_S = P_nu(S⊂F):
  log p_S = |S| log(L/(n-1)) + sum_{connected clusters C⊂S} phi_C,  |phi_C| <= (c/n)^{|C|-1} L^{?}.
Needed, concretely for k=4: two-sided asymptotics of p_S for all 4-edge S (path P5, star K1,4 [fixed by regularity],
C4, triangle+pendant, 2-path+edge, matching 4K2...) to relative accuracy o(L^-2 n^{-1}) — i.e. exact
second/third-order terms in the matching-avoidance count of a *regular host*, whose structure dependence enters only via
triangle (Theorem A) and 4-cycle counts. Theorem A-type switching gives only an upper bound with error O(L/n) per edge,
too weak by the factor n/L^... (kappa4/E(T)_4 ~ (Ln)^{-3}).  [C: nothing found false]

## 4. Partial positive result to carry (does not remove the condition)
- k=3 term o(1) iff L=o(n^{1/2}) [P, r4]. n^{1/2} is intrinsic to the STATEMENT of R2* (kappa3 -> 5c^4 at L=c n^{1/2}) [N, r4w1_k3_at_sqrt.py].
- Past n^{1/3} the second-moment can only be obtained by the cancellation route (r2_worker2: L^4/n^2 coefficient cancels) — needs (B*) as well.

## 5. Next step (concrete)
Prove (B*) at k=4 only by exact computation of p_S for the 4-edge classes via the sparse McKay disjoint-matching count with
explicit second-order term; verify against exact enumeration at n=8,10 (D_L enumeration, scripts r4w1_switch_check.py infrastructure).
Not done in this round.
