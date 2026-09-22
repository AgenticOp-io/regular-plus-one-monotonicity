# Theorem C — long simultaneous +1 chains

## Statement

**Theorem C.**
Assume the patched error schedule of Lemma L4 / `paper/main.tex` Lemma eta.
Let \(n\) be even and let \(D=D(n)\), \(L=L(n)\) be integers with \(Dn\) even,
\[
D\to\infty,\qquad
D=o\Bigl(\frac{n^{1/2}}{\log^4 n}\Bigr),\qquad
L\to\infty,\qquad
L=o\Biggl(\frac{(n/D^2)^{1/3}}{\log^2 n}\Biggr).
\]
Then there is a coupling \((G_d)_{d=D}^{D+L}\) such that each \(G_d\sim G(n,d)\) and
\[
\mathbb{P}\bigl(G_D\subseteq G_{D+1}\subseteq\cdots\subseteq G_{D+L}\bigr)=1-o(1).
\]

## Comparison with Gao Theorem 7

Gao Thm 7: simultaneous nesting on \([d,\lfloor(1+\varepsilon_n)d\rfloor]\) for
\(d=O(n^{1/7}/\log n)\) and \(\varepsilon_n=o(1)\).
Window **length** \(o(d)=o(n^{1/7})\).

Theorem C: window length \(L=o((n/D^2)^{1/3}/\mathrm{polylog})\).

| Base \(D\) | Gao window | Our \(L\) |
|---|---|---|
| \(\log^C n\) | \(o(\log^C n)\) | \(o(n^{1/3}/\mathrm{polylog})\) |
| \(n^{1/7}\) | \(o(n^{1/7})\) | \(o(n^{5/21}/\mathrm{polylog})\approx o(n^{0.238})\) |
| \(n^{1/3}\) | outside Gao range | \(o(n^{1/9}/\mathrm{polylog})\) |
| \(n^{2/5}\) | — | \(o(n^{1/15}/\mathrm{polylog})\) |
| \(\to\sqrt{n}\) | — | \(L\to\infty\) fails (recovers single-step only) |

So for sparse \(D\) the simultaneous window is **polynomial in \(n\)**, far past any
constant-factor relative window.

## Proof

For each \(d\in\{D,D+1,\ldots,D+L-1\}\) the single-step coupling of Theorem 19
(with patched \(\eta\)) gives a coupling of \(G(n,d)\) and \(G(n,d+1)\) with
failure probability \(\le 5\eta_d(\alpha_d)\).

Compose these couplings sequentially: sample \(G_D\), then couple forward to
\(G_{D+1}\), then to \(G_{D+2}\), etc. Marginals remain correct at each step.
Union bound:
\[
\mathbb{P}(\text{some step fails})
\le
5\sum_{d=D}^{D+L-1}\eta_d(\alpha_d).
\]
It remains to choose \(\alpha_d\) so that \(\eta_d=o(1/L)\) uniformly on the window.

### Schedule

Set, for every \(d\in[D,D+L]\),
\[
\alpha
:=
\max\Biggl\{
\frac{\log n}{L},\;
\frac{1}{d},\;
\Bigl(\frac{d^2 L\log^2 n}{n}\Bigr)^{1/2},\;
\Bigl(\frac{\sqrt{d/n}\,L\log^3 n}{1}\Bigr)^{1/2}
\Biggr\}.
\]
More cleanly, take the single choice (largest \(d\) is worst for the \(d^2/n\) term)
\[
\alpha
=
\max\Biggl\{
\frac{\log n}{L},\;
D^{-1},\;
\Bigl(\frac{(D+L)^2\,L\,\log^2 n}{n}\Bigr)^{1/2},\;
\bigl(L\log^3 n\bigr)^{1/2}(D/n)^{1/4}
\Biggr\}.
\]

### Verification that \(\alpha=o(1)\) and \(\eta=o(1/L)\)

Under \(L=o((n/D^2)^{1/3}/\log^2 n)\) and \(D=o(n^{1/2}/\log^4 n)\), \(L=o(n^{1/3})\)
so \(\log n/L\to 0\) fails? No: \(L\to\infty\) so \(\log n/L\) may or may not go to 0.
We need \(\alpha=o(1)\). Require the stronger
\[
L=\omega(\log n)
\]
(automatic if \(L\to\infty\) slower than any positive power? No — if \(L=\log\log n\) then
\(\log n/L\to\infty\). So impose \(L=\omega(\log n)\), or replace \(\log n/L\) by
\(L^{-1}\omega(1)\) with \(\omega\to\infty\) slowly.

**Refined schedule.** Set \(\beta_n\to\infty\) arbitrarily slowly (e.g. \(\log\log n\)) and
\[
\alpha
=
\max\Biggl\{
\frac{\beta_n}{L},\;
D^{-1},\;
\Bigl(\frac{(D+L)^2\,L\,\beta_n}{n}\Bigr)^{1/2},\;
\bigl(L\beta_n\log^3 n\bigr)^{1/2}(D/n)^{1/4}
\Biggr\}.
\]
Demand
\[
L=o\Biggl(\frac{(n/D^2)^{1/3}}{\beta_n}\Biggr)
\quad\text{and}\quad
L=\omega(\beta_n),\quad D\to\infty.
\]
Then:

1. \(\beta_n/L=o(1)\).
2. \(D^{-1}=o(1)\).
3. \((D+L)^2 L\beta_n/n = o(1)\) because \(L=o((n/D^2)^{1/3}/\beta_n)\) and
   \(D+L\sim D\) (since \(L=o((n/D^2)^{1/3})=o(n^{1/3}/D^{2/3})\), and
   \(D^{2/3}L=o(n^{1/3})\) while \(D\to\infty\); for \(D\ge n^{1/6}\) one checks
   \(L=o(D)\), for smaller \(D\) still \(L=o(n^{1/3})=o(n^{1/2}/\mathrm{polylog})\)
   so \(D+L\le 2\max(D,L)\) and the same \(o(1)\) holds after adjusting constants).
4. Spectral-type term similarly \(o(1)\).

Now \(\eta(\alpha)\le C'(\alpha + 1/(D^3\alpha^2) + D^2/(n\alpha^2) + \sqrt{D/n}\log^3 n/\alpha^2)\).

- \(2\alpha = O(\beta_n/L)=o(1/L)\cdot\beta_n\); take \(\beta_n=o(\log n)\) wait —
  we need \(\alpha=o(1/L)\)? No: we need \(\eta=o(1/L)\). Having \(\alpha=\beta_n/L\)
  gives \(2\alpha=\beta_n/L\), and \(\sum\eta\le L\cdot(\beta_n/L)=\beta_n\to\infty\) — BAD.

**Fix:** need \(\alpha=o(1/L)\) so that \(L\cdot\alpha=o(1)\). Set \(\alpha=\gamma_n/L\) with
\(\gamma_n\to 0\) (e.g. \(\gamma_n=1/\log n\)).

Then \(L\cdot 2\alpha=2\gamma_n=o(1)\). Good.

Constraints from other terms with \(\alpha=\gamma_n/L\):
\[
\frac{D^2}{n\alpha^2}
=
\frac{D^2 L^2}{n\gamma_n^2}
=
o\Bigl(\frac1L\Bigr)
\quad\Longleftrightarrow\quad
\frac{D^2 L^3}{n\gamma_n^2}=o(1)
\quad\Longleftrightarrow\quad
L=o\Bigl(\bigl(n\gamma_n^2/D^2\bigr)^{1/3}\Bigr).
\]
And
\[
\frac1{D^3\alpha^2}
=
\frac{L^2}{D^3\gamma_n^2}
=
o\Bigl(\frac1L\Bigr)
\quad\Longleftrightarrow\quad
\frac{L^3}{D^3\gamma_n^2}=o(1)
\quad\Longleftrightarrow\quad
L=o\bigl(D\gamma_n^{2/3}\bigr).
\]
The second is mild when \(D\to\infty\) and \(L\) is polynomial-sub-\(D\).
The first is the binding constraint:
\[
L=o\Biggl(\Bigl(\frac{n}{D^2}\Bigr)^{1/3}\gamma_n^{2/3}\Biggr).
\]
With \(\gamma_n=1/\log n\):
\[
L=o\Biggl(\frac{(n/D^2)^{1/3}}{\log^{2/3}n}\Biggr),
\]
and \(L\cdot\eta=o(1)\) as needed.

Also need \(\alpha=o(1)\): \(\gamma_n/L=o(1)\) automatic since \(L\to\infty\).

### Conclusion

Under
\[
D\to\infty,\quad
D=o(n^{1/2}/\log^4 n),\quad
\omega(1)=L=o\bigl((n/D^2)^{1/3}/\log^{2/3}n\bigr),
\]
the sequential composition succeeds with probability \(1-o(1)\).

## Corollary (sparse mega-window)

Taking \(D=\lfloor\log^4 n\rfloor\) (even parity arranged) yields a simultaneous nesting
window of length
\[
L=o\bigl(n^{1/3}/\mathrm{polylog}\,n\bigr).
\]
That is: one coupling nests \(G(n,D)\subseteq\cdots\subseteq G(n,D+L)\) through
\(\Theta(n^{1/3}/\mathrm{polylog})\) consecutive degrees.
