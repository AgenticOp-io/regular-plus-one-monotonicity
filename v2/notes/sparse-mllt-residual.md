# Sparse multi-colour LLT for residual moment

## Target

Unconstrained item (i) of Proposition residual-two-gaps at BIM length:
\(m=\Theta\sqrt{d\log n}\), host degree \(\delta=\varepsilon_0 d=\Theta(d^{2/3}(\log n)^{1/3})\),
with \(m/\sqrt\delta\to\infty\) and \(m=o(\delta)\), \(\delta=o(n)\) (in fact
\(\delta=o(n^{1/2})\) for \(d=o(n^{3/4}/\mathrm{polylog})\)).

Linear MLLT (Theorem mllt / mllt-sparse) needs \(\lambda-a\ge c\) and
\(1-\lambda\ge c\). Here \(\lambda=\delta/(n-1)\to 0\).

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

## Nearly regular unconstrained (conditional)

Proposition residual-nearly-regular-matching: if Gao Thm~6 extends to
degree sequences in an \(\varepsilon_n\)-window about \(\delta=o(n^{1/2})\), then
matching \(L^2\) holds uniformly there. Proposition residual-not-tv: literal
TV with \(\mu_\delta\) is blocked (`almost-regular-tv`).

## Blocked

- Bernoulli residual comparison (second moment)
- Free-extension flatness as residual flatness (pathwise \(N_m(R)\))
- Hybrid / sprinkle transfer
- Config second moment at linear degree
- Almost-regular TV / support-disjoint

## Checkpoint

Fixed \(m\): Theorem residual-factor-fixed (Gao/Laplace).
\(m=1\) first moment: Theorem residual-matching-mean.
Next: host-restricted residual \(L^2\), or sparse local-limit error at
\(\lambda\to0\).
