# Conjecture U — obstruction and unlock path

## Truncation barrier (Lemma 7.1 method)

BIM Claim 7.2 defines heavy vertices \(B\) at threshold \((1+\gamma)\) above the
two-vertex lower bound with error \(\lambda\), and gets
\[
|B|\le O\Bigl(\frac{\lambda n}{\gamma}\Bigr).
\]
Needing \(|B|=O(\eta n)\) for the neighbourhood truncation forces \(\lambda=O(\eta\gamma)\).
Needing the non-truncated path bound at relative error \(O(\eta)\) forces \(\gamma=O(\eta)\).
Combining: \(\lambda=O(\eta^2)\), hence
\[
\eta=\Omega(\sqrt{\lambda}).
\]
With Theorem 6.1 at \(\lambda=(\log n/\delta)^{1/4}\) this yields exactly
\(\eta=\Omega((\log n/\delta)^{1/8})\) — BIM's schedule. **No re-tuning of
\((\gamma,\eta)\) beats \(1/8\) inside this truncation architecture.**

## Why Theorem 6.1 stops at \(1/4\)

Lemma 6.15 (property I6) uses test sets of size \(\ge\mu n\) with \(\mu=\Theta(\lambda)\),
and requires \(\lambda^2\mu\delta\ge C\log n\), i.e. \(\lambda^3\delta=\Omega(\log n)\),
hence \(\lambda=\Omega((\log n/\delta)^{1/4})\) when this exceeds the Chernoff degree
floor \(\sqrt{\log n/\delta}\).

## Unlock A — Conjecture U / rate \(1/5\)

Replace the truncation proof of two-vertex upper bounds (Lemma 7.1) by a method
that achieves error \(O(\lambda)=O((\log n/\delta)^{1/4})\):
Kim–Vu on the path polynomial, Freedman exploration, or second-moment on
\((X_y)_{y}\).

## Unlock B — Hypothesis P / rate \(1/3\)

Strengthen I6 to hold for all \(|U|,|V|\ge n/(\log n)^{C}\) (or \(\ge c n\)).
Then Lemma 6.15 only needs \(\lambda^2\delta=\Omega(\mathrm{polylog}\,n)\), allowing
\(\lambda=\Theta\sqrt{\log n/\delta}\). Theorem 6.1 would then give lower path
bounds at Chernoff-degree scale. Combined with Unlock A (upper at the same scale),
Hypothesis P holds and B2 yields global rate \(1/3\).

## Status

| Goal | Blocker | Status |
|---|---|---|
| Rate \(1/5\) for \(d\ge n^{\tau}\) | — | **proved** (Thm quant-fifth) |
| Rate \(1/5\) for all \(d\ge C\log n\) | Truncation barrier | Conjecture U |
| Rate \(1/3\) for all \(d\ge C\log n\) | I6 set-size + truncation | Hypothesis P |
| Chernoff \(1/2\) | Process architecture | Conjecture Q |
