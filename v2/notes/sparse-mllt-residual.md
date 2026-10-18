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

## Blocked

- Bernoulli residual comparison
- Free-extension flatness as residual flatness
- Hybrid / sprinkle transfer
- Config second moment at linear degree

## Checkpoint

Fixed \(m\): Theorem residual-factor-fixed (Gao/Laplace).
Next identity: leading \(\Delta\operatorname{Re}h\) for the sparse pair law
\(\pi_m\) as \(\lambda\to 0\) with \(a/\lambda\to 0\) and \(a\sqrt{n/\lambda}\to\infty\).
