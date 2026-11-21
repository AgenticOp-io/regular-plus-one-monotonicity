# r33: residual step 2 (lem:avoid-G-host)

## Verdict
**Not proved, and not provable in the stated form.** Hypothesis hyp:s3-avoid-G (Var_g Z <= eps_n (E_g Z)^2
uniformly on the window W_{eta_n}) is false in regime (B). This is r15w1's result; r33 re-checked the
arithmetic and found nothing to overturn it. No new proof or new counterexample was produced.

## What is established (by whom)
- r15w1 (pairing level, exact numerics): for host degrees g = delta + y with s2^2 = mean y^2,
  log(E Z^2/(E Z)^2) ~ K = n (delta-m)^2 s2^4 / (2 m^2 delta^3). Exact pairing values grow linearly in n
  (delta=40, m=6, t=3: 3.99, 7.98, 15.98, 31.97 for n=200..1600); regular host stays ~0.013.
- r33 script `v2/scripts/r33_K_formula.py`: K matches the recorded exact values within 2-5% at n=200
  (3.99 vs 4.06, 29.96 vs 31.36, 24.2 vs 25.35). In regime (B) with s2^2 ~ delta (typical G(n,p)-type
  degrees) K/delta^2 -> infinity (1e3 at n=1e6, 1e7 at n=1e12, with d=n^{1/4}). So K exceeds the
  simple-graph transfer cost exp(O(delta^2)), and the pairing blow-up should survive transfer.
- r16w2: conditioning on assortativity Lambda removes ~97% of K but the conditioned ratio still grows
  linearly in n (0.074, 0.136, 0.241 at n=100, 200, 400). Only t=2,3 trusted.

## Not proved / not checked
- The simple-graph disproof is conditional on McKay's estimate as quoted in main.tex and on r4w2 Thm 5.
  No simple-graph computation was run here or in r15w1.
- The residual growth after conditioning on Lambda is numerical, mechanism a guess.
- A variance blow-up does NOT show Z/E Z fails to -> 1 in probability: the second moment may be dominated
  by a rare overlap. So the weak-law form of step 2 is neither proved nor refuted.

## Precise remaining question
Is Z/E[Z | G, deg R = g] -> 1 in probability for g in the window? Variance/second-moment routes cannot
prove it (K -> infinity). Possible routes: small-subgraph conditioning (cycle counts, cf. r16w1 Ursell
scripts), or a truncated second moment plus a separate argument excluding the heavy overlap, neither done.
Without it, residual-moment-bim stays open in degree-conditioned form.
