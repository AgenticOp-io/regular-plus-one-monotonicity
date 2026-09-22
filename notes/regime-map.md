# Regime map: \(G(n,d_1)\subseteq G(n,d_2)\) whp

Source synthesis: Gao–Isaev–McKay conjecture; Behague–Ilʼkovič–Montgomery (BIM) 2025;
Hollom–Lichev–Mond–Portier–Wang (HLMPW) 2025.

Excluded exceptional pairs in the conjecture: \((d_1,d_2)\in\{(1,2),(n-3,n-2)\}\).
Always require \(d_1 n\) and \(d_2 n\) even.

## Known regimes (DONE)

| Regime | Citation | Notes |
|---|---|---|
| \(d_1=1\), \(d_2\in[3,n-1]\) | HLMPW / earlier | Perfect matchings into denser regular |
| \(\omega((\log n)^7)=d_1\le n^{1/7}/\log n\), any \(d_2\ge d_1\) | Gao + HLMPW Thm 1.2 | Even \(n\), \(d_2=\omega(1)\) |
| \(\omega(1)=d_1\le n^{1/3}\), \(d_2=d_1+1\) | Gao / HLMPW list | True +1 in sparse–medium |
| \(d_2\ge c\,d_1\) with \(c>1\), \((\log n)^4\le c d_1\le d_2\le n-(\log n)^4\) | GIM sandwich era | Constant-factor gap |
| \(\min\{d_1,d_2-d_1\}=\omega(n/\log n)\) | GIM / HLMPW list | Very dense increments |
| \(d_1=\omega(\log n)\), \(d_2-d_1=\Omega(d_1)\) | **BIM 2025 immediate corollary** | Via sandwich transit through ER |

## Open / attack surface (TODO)

| Cell | Why hard | Our plan |
|---|---|---|
| \(d_2=d_1+1\) for \(n^{1/3}\ll d\ll n/\mathrm{polylog}\) | Matching variance / TV error accumulation | Stage 1–2 attack |
| \(d_2=d_1+1\) for dense \(d=\Theta(n)\) | Different switching geometry | After medium regime |
| Odd \(n\) (no perfect matching; steps of size 2) | Need \(d\mapsto d+2\) or near-factors | Later |
| Full decomposition \(G(n,d)\approx G(n,d_1)\oplus G(n,d-d_1)\) | Contiguity, not just inclusion | Parallel track |

## First new target (Stage 1)

**Target A (preferred).** Extend exact +1 beyond \(n^{1/3}\):
\[
\omega(1)=d\le n^{1/3+\delta}
\quad\Longrightarrow\quad
\exists\text{ coupling }G(n,d)\subset G(n,d+1)\text{ whp.}
\]

**Target B (fallback).** Constant-power increment in a new window:
\[
d\le n^{a},\quad
G(n,d)\subset G(n,d+\lfloor d^{b}\rfloor)\text{ whp}
\]
for some \(0<b<1\) not implied by BIM’s \(\Omega(d)\) gap.

**Target C (technique paper).** Sharper
\[
\mathrm{d_{TV}}\bigl(G(n,d)\oplus G(n,1),\,G(n,d+1)\bigr)
\]
with explicit \(o(1)\) usable for iteration past \(n^{1/10}\).
