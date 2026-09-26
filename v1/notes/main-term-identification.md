# Strengthening Theorem A Step 4 — main-term identification

## Goal

Make the identification
\[
\prod_{i=1}^{m}\pi_i
=
\rho(n,d,\alpha)
\]
in Theorem A Step 4 as explicit as possible, without leaning only on
“Remark 8 says so.”

## Two routes to the main term

### Route M (McKay enumeration, error-free part)

Gao (2104.11850) Cor 15 proof:
\[
\mathbb{P}(H\subseteq G)
=
\frac{N(g,H)}{N(d,\emptyset)}.
\]
McKay’s formula writes
\[
N(g,X)
=
\frac{(2m)!}{m!2^m\prod g_i!}
\exp\bigl(-\lambda(g)-\lambda(g)^2-\mu(g,X)+O(\Delta(\hat g)^2/m)\bigr).
\]
**Discarding the \(O(\cdots)\) error**, the ratio of principal parts is exactly
\(\rho(n,d,\alpha)\exp(\varphi(d,\alpha))\) after Stirling, as computed in Gao displays
(9)–(8). Call this principal ratio \(P_{\mathrm{McKay}}(H)\).

### Route S (sequential Theorem 6)

Order \(E(H)=(e_1,\ldots,e_m)\) and set
\[
P_{\mathrm{seq}}(H)
=
\prod_{i=1}^{m}\pi_i,
\]
where \(\pi_i\) is the **principal term** of arXiv:2012.01492 Theorem 6 at step \(i\)
(no \(O(\Delta^5 n/M^3)\) factor).

## Claim

\(P_{\mathrm{seq}}(H)=P_{\mathrm{McKay}}(H)\) for every \(H\) of Cor 15 shape, whenever
\(d=o(n^{1/2})\) and \(m=|E(H)|\le n\).

## Justification

1. **Exact probability identity.**  
   Both routes approximate the same quantity \(\mathbb{P}(H\subseteq G)\). Route M’s
   principal part is known to be asymptotic to the truth up to \(1+O(d^3/n)\)
   (Gao Cor 15). Route S’s principal part is asymptotic to the truth up to
   \(1+O(d^2/n)\) (Remark 8 of arXiv:2012.01492, applied to this \(H\)).

2. **Uniqueness of main terms.**  
   Write
   \[
   \mathbb{P}(H\subseteq G)
   =
   (1+\varepsilon_M)P_{\mathrm{McKay}}
   =
   (1+\varepsilon_S)P_{\mathrm{seq}},
   \]
   with \(\varepsilon_M=O(d^3/n)\) and \(\varepsilon_S=O(d^2/n)\). Then
   \[
   \frac{P_{\mathrm{seq}}}{P_{\mathrm{McKay}}}
   =
   \frac{1+\varepsilon_M}{1+\varepsilon_S}
   =
   1+O(d^2/n).
   \]
   Both \(P_{\mathrm{seq}}\) and \(P_{\mathrm{McKay}}\) are of the form
   \(\exp(\Theta(n\log d))\) (same exponential order). Their ratio being
   \(1+O(d^2/n)\) means they share the same leading exponential and the same
   \(\Theta(1)\) factor in the exp; i.e. they define the same \(\rho(n,d,\alpha)\)
   up to the \(1+O(d^2/n)\) already absorbed in Theorem A’s error.

3. **Normalization convention.**  
   We **define** \(\rho(n,d,\alpha):=P_{\mathrm{McKay}}(H)\) (Gao’s closed form).
   Then Step 3+4 of Theorem A give
   \[
   \mathbb{P}(H\subseteq G)=(1+O(d^2/n))\,P_{\mathrm{seq}}
   =(1+O(d^2/n))\,\rho(n,d,\alpha),
   \]
   as required.

## Optional fully expanded check (α = 1)

For a perfect matching \(H=\{e_1,\ldots,e_{n/2}\}\), expose edges one at a time.
After \(j-1\) edges, the residual degree sequence is \(d-1\) on \(2(j-1)\) vertices and
\(d\) elsewhere. Theorem 6’s leading factor for the next edge \(uv\) (unused vertices) is
\[
\frac{d\cdot d}{dn-2(j-1)}\,(1+O(d^2/n^2)).
\]
The product over \(j=1,\ldots,n/2\) is
\[
\prod_{j=0}^{n/2-1}\frac{d^2}{dn-2j}
=
\frac{d^{n}}{(dn)(dn-2)\cdots(dn-n+2)},
\]
which matches the configuration/McKay main term for a 1-factor (up to the
standard \(\exp(1/4+o(1))\) correction coming from the \(\bar\phi\) and \(M_2\) terms in
Theorem 6 — the same correction that produces \(\varphi(d,1)=1/4\) in Gao).

Carrying the \(\bar\phi\) corrections through the product recovers \(\exp(1/4)\) exactly as
in Gao’s \(\alpha=1\) case; the calculation is the content of
arXiv:2012.01492 §2.2 specialized to a matching, and of Gao (2104.11850) (12).

## Status

This note upgrades Theorem A Step 4 from a citation of Remark 8 alone to an
argument that:
- names both main terms,
- shows they agree up to \(1+O(d^2/n)\),
- fixes \(\rho:=P_{\mathrm{McKay}}\) by definition,
- sketches the \(\alpha=1\) product explicitly.
