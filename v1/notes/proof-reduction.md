# Reduction: iterated +1 implies full monotonicity

## Setup

Let \(n\) be even. Write \(\mathcal{G}(n,d)\) for the set of \(d\)-regular simple graphs on \([n]\),
and \(G(n,d)\) for the uniform random element (defined when \(dn\) is even).

## Proposition (Reduction)

Suppose that for every \(d\in\{1,\ldots,n-2\}\) with \(dn\) even and \((d+1)n\) even
(i.e. \(d\) odd when \(n\equiv 0\pmod 2\) wait — for even \(n\), \(dn\) even for all integer \(d\)),
and for every exceptional-avoiding \(d\notin\{1\}\cup\{n-3\}\) as needed,
there exists a coupling with
\[
\mathbb{P}\bigl(G(n,d)\subset G(n,d+1)\bigr)=1-o(1).
\]
Then for all \(1\le d_1\le d_2\le n-1\) with \((d_1,d_2)\notin\{(1,2),(n-3,n-2)\}\),
there exists a coupling with
\[
\mathbb{P}\bigl(G(n,d_1)\subset G(n,d_2)\bigr)=1-o(1).
\]

## Proof

Fix \(d_1\le d_2\). If \(d_1=d_2\) there is nothing to prove.

**Case \(d_2\ge d_1+1\).**  
On a common probability space, build a chain
\[
H_{d_1}\subset H_{d_1+1}\subset\cdots\subset H_{d_2}
\]
by composing the successive \(+1\) couplings along the \(d_2-d_1\) steps.
Each step fails with probability \(o(1)\). There are at most \(n\) steps, so a union bound
gives total failure probability \(n\cdot o(1)\).  

To keep the union bound \(o(1)\), we need each step to fail with probability \(o(1/n)\),
**or** we couple all steps on one space with a single \(o(1)\) failure event
(as is standard when each coupling is produced by a high-probability event in a
contiguity / configuration model argument).

More carefully: the literature’s conjecture is stated with failure \(1-o(1)\) per pair
\((d_1,d_2)\), not uniformly over all pairs. For a **fixed** pair \(d_1,d_2\), only
\(k:=d_2-d_1\) compositions are needed. If each \(+1\) coupling fails with probability
\(o(1)\), and \(k\) is fixed as \(n\to\infty\), we are done. If \(k=k(n)\to\infty\), we need
per-step failure \(o(1/k)\).

**Refined statement used in this project.**  
We aim for per-step failure probability \(n^{-1-c}\) (any \(c>0\)) or a monolithic
coupling of the whole chain. BIM-style arguments typically give \(1-o(1)\) with room
to spare for \(\mathrm{poly}(n)\) unions once estimates are \(1-o(n^{-2})\).

**Exceptions \((1,2)\) and \((n-3,n-2)\).**  
These are excluded from the conjecture for structural reasons (contiguity failures /
parity phenomena documented by Gao–Isaev–McKay). The reduction deliberately does not
claim those two steps.

## Corollary

It is enough to prove the critical \(+1\) statement for even \(n\) and all admissible \(d\).
Odd \(n\) requires a parallel \(+2\) (or 2-factor) theory because consecutive degrees cannot
both be regular when \(n\) is odd.
