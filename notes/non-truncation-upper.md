# Non-truncation two-vertex upper — RESOLVED

## Method

Last-layer Bernstein (`thm:path-upper-chernoff`):
1. Condition on \(K\) and on multiplicities \(M(w)\) of clean length-\(2\ell-2\)
   paths avoiding \(Z=N_K(y)\cup\{y\}\).
2. The final \(F\setminus K\) cut edges into \(N_K(y)\) are independent Bernoullis.
3. Coarse \(\ell_\infty\) bound on \(M\) from Thm U at error \((\log n/\delta)^{1/4}\).
4. One-vertex mass \(S\) at Chernoff scale from `lem:one-vertex-chernoff`.
5. Conditional variance \(O(\mu^2/(d\delta))\); jump \(O(\mu/(d\delta))\).
6. Bernstein at deviation \(\lambda\mu\) costs \(\exp(-\Omega(d\log n))\).
7. Dirty paths (visit \(Z\) early) cost relative \(O(d\log n/n)=o(\lambda)\).

## Why \(L^2\) failed but Bernstein works

Global \(\mathrm{Var}(Y)=O(\lambda\mu^2)\) ⇒ relative SD \(\sqrt{\lambda}\).
Conditional last-layer \(\mathrm{Var}=O(\mu^2/(d\delta))\) ⇒ Bernstein is
exp-sharp at relative \(\sqrt{\log n/\delta}\).

## Consequence

Hypothesis P closed → `thm:quant-third-global` unconditional → **global rate 1/3**.
