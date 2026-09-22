# Beating \(1/17\): rates \(1/9\) and \(1/3\)

## Exponent orientation (corrected)

For \(0<x<1\), larger \(\beta\) in \(\varepsilon\ge x^{\beta}\) is **better** (smaller lower bound).
Chernoff \(\beta=1/2\) beats \(1/3\) beats \(1/9\) beats \(1/17\).

## Rate \(1/9\) (proved)

BIM hierarchy forces \(C_0=\omega(1/\varepsilon)\) only as a convenient nesting of constants.
Theorem 4.1 (switching) uses an **absolute** large \(C_0\). Instantiating B2 with
absolute \(C_0\) and \(\mu=\Theta(\varepsilon)\) yields
\[
\Bigl(\frac{\log n}{\varepsilon d}\Bigr)^{1/8}=O(\varepsilon)
\quad\Longleftrightarrow\quad
\varepsilon=\Omega\Bigl(\Bigl(\frac{\log n}{d}\Bigr)^{1/9}\Bigr).
\]
This **beats** \(1/17\) (which came from unnecessarily taking \(C_0=\Theta(1/\varepsilon)\)).

Verification that absolute \(C_0\) is compatible with Theorem 2.4 / 4.1:
- \(\eta=C_0(\log n/(\varepsilon d))^{1/8}=O(\varepsilon)\) at the \(1/9\) threshold
- \(\eta d=\Omega(\varepsilon d)=\Omega(d^{8/9}(\log n)^{1/9})\to\infty\)
- \(\eta^2\delta=\Omega(\varepsilon^2\cdot\varepsilon d)=\Omega(\varepsilon^3 d)=\Omega(d^{2/3}(\log n)^{1/3})\gg\log n\)

## Rate \(1/3\) (architectural optimum of this process)

Switching (Theorem 4.1) needs only \(\eta^2\delta\ge C\log n\), i.e.
\[
\eta=\Omega\Bigl(\sqrt{\frac{\log n}{\delta}}\Bigr)=\Omega\Bigl(\sqrt{\frac{n\log n}{m}}\Bigr).
\]
If path counts C2–C3 hold at this scale (call this **Hypothesis P**), set
\[
\eta_m=C\max\Bigl\{\frac{\mu}{\log n},\sqrt{\frac{n\log n}{m}}\Bigr\}
\]
in B2. Absolute \(C\), \(\mu=\Theta(\varepsilon)\):
\[
\sqrt{\frac{\log n}{\varepsilon d}}=O(\varepsilon)
\quad\Longleftrightarrow\quad
\varepsilon=\Omega\Bigl(\Bigl(\frac{\log n}{d}\Bigr)^{1/3}\Bigr).
\]
Moreover \(\eta^2\delta=\Theta(\log n)\) sits exactly on the switching threshold.

**This is optimal for the BIM deletion-process + B2 architecture:**
B2 demands \(\eta=O(\varepsilon)\) at \(R\sim\varepsilon dn\), while switching demands
\(\eta=\Omega(\sqrt{\log n/(\varepsilon d)})\), forcing \(\varepsilon=\Omega((\log n/d)^{1/3})\).

Chernoff \(\varepsilon\asymp\sqrt{(\log n)/d}\) is **impossible** in this architecture
without changing B2 / the coupling to \(G^*\) (e.g. process Conjecture 1.3).

## Hypothesis P — why it is plausible

BIM already get path-count relative error \(O(1/\ell)\) with
\(\ell=\Omega(\log n/\log(\delta d))\) (discussion before their Theorem 2.4).
At rate \(1/3\), \(\delta\asymp\varepsilon d\asymp d^{2/3}(\log n)^{1/3}\to\infty\), so
\(\ell\to\infty\) and \(1/\ell=o\bigl(\sqrt{\log n/\delta}\bigr)\) in wide ranges.
Full verification = re-checking §§5–7 with \(\eta=\Theta(\sqrt{\log n/\delta})\).

## Dense GIM (supplementary)

Gao–Isaev–McKay embedding (arXiv:1906.02886, Thm 2.6): for
\(n-d\gg\xi d\gg n/\log n\), sandwich at \(\xi\).
For \(d=\Theta(n)\) this gives \(\xi=\omega(1/\log n)\), which is **worse** than
rate \(1/9\) (\((\log n/n)^{1/9}=n^{-1/9+o(1)}\ll 1/\log n\)).
So GIM dense does not beat our \(1/9\) in the dense regime; keep as alternate proof.

## Claim ladder

| Rate | Status |
|---|---|
| \(1/17\) | superseded |
| **\(1/9\)** | **proved** (absolute \(C_0\) + BIM Thm 2.4) |
| **\(1/3\)** | **conditional on Hypothesis P** |
| \(1/2\) Chernoff | requires new architecture (Conjecture Q) |
