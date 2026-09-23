# Conjecture U — RESOLVED

## Former obstruction

BIM Lemma 7.1 truncation forces \(\eta=\Omega(\sqrt{\lambda})\). With
Theorem 6.1 at \(\lambda=(\log n/\delta)^{1/4}\) this gave only
\(\eta=(\log n/\delta)^{1/8}\).

## Resolution (via linear I6)

Theorem `thm:path-lower-chernoff` upgrades lower path error to
\(\lambda=\sqrt{\log n/\delta}\). The same truncation then yields
\[
\eta=\Omega(\sqrt{\lambda})=(\log n/\delta)^{1/4},
\]
which is Theorem `thm:U`. Global rate \(1/5\) follows
(Theorem `thm:quant-fifth`).

## Remaining for rate \(1/3\)

Need two-vertex **upper** at \(\sqrt{\log n/\delta}\) by a method that avoids
truncation. Linear-I6 expansion does **not** give this: Claim 6.4 counts a
subclass of layered paths (lower bounds only). Options: Kim–Vu on the path
polynomial, Freedman exploration, or second-moment / no-heavy-hitter control
on \((P_{x,y})_y\) given the one-vertex upper from Lemma 5.1.
