# Sparse multi-colour LLT for residual moment

## Target

Unconstrained item (i) of Proposition residual-two-gaps at BIM length:
\(m=\Theta\sqrt{d\log n}\), host degree \(\delta=\varepsilon_0 d=\Theta(d^{2/3}(\log n)^{1/3})\),
with \(m/\sqrt\delta\to\infty\) and \(m=o(\delta)\), \(\delta=o(n)\) (in fact
\(\delta=o(n^{1/2})\) for \(d=o(n^{3/4}/\mathrm{polylog})\)).

Linear MLLT (Theorem mllt / mllt-sparse) needs \(\lambda-a\ge c\) and
\(1-\lambda\ge c\). Here \(\lambda=\delta/(n-1)\to 0\).
Proposition mllt-vanishing-margin: at \(a=o(\lambda)\to0\) the state-pair
products that feed \(\Sigma\succeq c^3 D_a\) degrade to \(\Theta(\lambda)\)
(G-coordinate) and \(\Theta(a\lambda)\) (factor), so the sparse MLLT error
control does not transfer.

## Live route

Configuration-model / McKay enumeration of the colouring count
\(N_3 N_1/N_2^2\) at densities \(a=m/(n-1)\), \(\lambda=\delta/(n-1)\to 0\), with
\(na=\omega(\sqrt n)\) replaced by the sparse threshold where
\(\widehat\Delta^2/E=o(1)\).

Screen: `config-second-moment --degree o(sqrt(n))` is CLEAR.

## Package residues as \(\lambda\to0\) (Lemma sparse-package-residues)

With \(a=o(\lambda)\):
- \(\beta_{\mathrm{C35}}=5(1-\lambda)/(3\lambda)\) exact at \(\lambda=1/10\)
  (residue 15) and \(\lambda=1/5\) (residue \(20/3\)) via
  `scripts/beta_c35_lam.py`.
- \(\beta_{\mathrm{p64}}=(1-\lambda)/(2\lambda)\): two-point extrapolation at
  \(a\in\{\lambda/8,\lambda/16\}\) for \(\lambda\in\{1/10,1/15,1/20\}\)
  recovers the candidate (errors \(O(a/\lambda)\); e.g.\ at \(\lambda=1/10\)
  the fit gives \(b_0\sim4.457\) vs \(9/2=4.5\)).

These are the leading \(\Delta\operatorname{Re}h\) package residues for a
sparse-host expansion. They do **not** extend Theorem mllt-sparse (linear
margins still required for the local-limit error).

## Bernoulli first moment (closed)

Theorem residual-matching-mean:
\(\EE[Y(R)|G]=p^{n/2}Y(C)\). Corollary residual-first-moment: at \(m=1\) the
first-moment half of residual-to-peel-weight reduces to free complementary
matching concentration. Bernoulli *second* moment still diverges
(`bernoulli-residual-moment` BLOCK at every \(d=o(n)\)).

## Nearly regular / constrained (partial close)

- Theorem bern-degree-uniform: Bern\(|\deg=g=\mathrm{Unif}(\Omega(C,g))\).
- Remark residual-not-unrestricted: \(\mu_\delta\) is exponentially rare in
  \(\Omega(C,\delta)\) when \(d\delta\to\infty\); wrong comparison.
- Theorem residual-matching-constrained: matching \(L^2\) on
  \(\Omega(C,\delta)\) for \(\delta(d+\delta)^2/n=o(1)\) (McKay; host \(\mu\)
  cancels in ratios). BIM range \(d=o(n^{3/8}(\log n)^{-1/3})\).
- Corollary residual-matching-window: mixture over the sharp window needs
  flat means \(\EE_g Y\).

## Blocked

- Bernoulli residual comparison (unconditional second moment)
- Free-extension flatness as residual flatness (pathwise \(N_m(R)\))
- Hybrid / sprinkle transfer
- Config second moment at linear degree
- Almost-regular TV / support-disjoint / unrestricted contiguity

## Formal BIM variance scale (Proposition bim-residual-scale)

If the five-package residue
\(\Delta\operatorname{Re}h\sim 287(1-\lambda)/(216\lambda\,na)\) persists as
\(\lambda\to0\) with \(a=o(\lambda)\), then
\[
\frac{\Var Z}{(\EE Z)^2}
\sim
\Theta\Bigl(\frac{n}{\delta m}\Bigr)
=
\Theta\Bigl(\frac{n}{d^{7/6}(\log n)^{5/6}}\Bigr),
\]
vanishing iff \(d=\omega(n^{6/7}(\log n)^{-5/7})\), and \(\to\infty\) throughout
\(d=o(n^{3/4}/\mathrm{polylog})\) (where \(\delta=o(\sqrt n)\) and \(m\le\delta\)
force \(\delta m=o(n)\)). Package evidence: Lemma sparse-package-residues
(p64, C35) plus \(\kappa_3,\kappa_4\) forms \(\propto(1-\lambda)/\lambda\).
Not a conjecture close: MLLT still needs linear margins; host is constrained.

## Package persistence ruled out at matchings

Proposition package-not-persist: at \(m=1\), unconstrained matching variance
is \(1/(6\delta^3)\to0\) for \(\delta\to\infty\), \(\delta=o(n)\), while the
formal scale \(\Theta(n/\delta)\to\infty\). The mid-window residue therefore
cannot persist at matching length; sparse-host expansions need a different
leading term (e.g.\ short-cycle / McKay type).

## Sharp rate (Conjecture residual-factor-sharp)

Target: \(\Var Z/(\EE Z)^2=O(m^2/\delta^3+\delta^2 m/n)\) for
\(m=o(\delta^{3/2})\), \(\delta=o(n^{2/5})\). Recovers matching \(1/(6\delta^3)\);
numerics at \(n=8,\delta=5\) give relvar\((m=2)/\)relvar\((m=1)\approx4\).
Proposition residual-sharp-bim: at BIM scales \(m^2/\delta^3=\Theta(1/d)\to0\),
so the sharp conjecture would close unconstrained item (i).

## Checkpoint

\(m=o(\sqrt\delta)\) on McKay scale: **closed** (Theorem residual-moment).
Gao relative error \(O(\delta^2 m/n)\) (requires \(\delta=o(n^{2/5})\), automatic
on McKay) and overlap leftover \(O(m^2/\delta)\).
BIM length \(m\gg\sqrt\delta\): Conjecture residual-moment-bim; unconstrained
half is Conjecture residual-factor-sharp; package-residue divergence is
blocked at \(m=1\).
