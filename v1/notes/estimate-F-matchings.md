# Estimate F — matching concentration in the complement (partial)

## Statement

Let \(n\) be even, \(3\le d\le (1-\delta)n\), and \(G\sim G(n,d)\).
Let \(Y(G)\) be the number of perfect matchings in \(\overline{G}=K_n-G\).

**Estimate F (open in general).**  
\[
\frac{Y(G)}{\mathbb{E} Y}=1+o(1)
\quad\text{with probability }1-o(n^{-2}).
\]

## Why this unlocks +1

By Lemma D in `proof-plus-one-attack.md`, the exact Radon–Nikodym weight to turn
\(G\cup M\) into uniform \(G(n,d+1)\) involves \(1/Y(G)\). If \(Y\) is tightly concentrated,
reweighting is negligible in total variation and
\[
G(n,d)\oplus(\text{near-uniform matching in complementary edges})
\]
is \(\mathrm{d_{TV}}\)-close to \(G(n,d+1)\).

## Partial proof in the BIM window

### Step 1 — Complement is nearly regular random

\(\overline{G}\) is exactly \((n-1-d)\)-regular. Write \(d':=n-1-d\). If
\(d'\ge C\log n\), BIM applies to \(\overline{G}\sim G(n,d')\) (same law).

### Step 2 — Sandwich the complement

BIM gives, whp,
\[
G\!\Bigl(n,(1-\varepsilon)\frac{d'}{n}\Bigr)
\;\subset\;
\overline{G}
\;\subset\;
G\!\Bigl(n,(1+\varepsilon)\frac{d'}{n}\Bigr).
\]

### Step 3 — Matching counts are monotone

If \(A\subset B\) then \(Y(A)\le Y(B)\). Hence whp
\[
Y\Bigl(G(n,(1-\varepsilon)d'/n)\Bigr)
\;\le\;
Y(\overline{G})
\;\le\;
Y\Bigl(G(n,(1+\varepsilon)d'/n)\Bigr).
\]

### Step 4 — ER matching concentration (classical)

For binomial graphs above the matching threshold, the number of perfect matchings
is known to concentrate after suitable normalization (Janson / Bollobás–McKay type
results; permanent of the biadjacency in related models).

**Gap.** Transferring sharp ER concentration through the sandwich gives
\[
Y(\overline{G}) = \exp\bigl(\tfrac12 n\log n - \tfrac12 n\log(1/(1-p)) + o(n)\bigr)
\]
style first-order asymptotics, but we need **relative** \(1+o(1)\) error, not
\(\exp(o(n))\). Sandwiching with fixed \(\varepsilon>0\) leaves a multiplicative
\(\exp(\Theta(n))\) gap between lower and upper ER counts — **too crude for Estimate F**.

### Step 5 — What would finish it

Need either:

1. BIM with \(\varepsilon=\varepsilon(n)\to 0\) fast enough that the ER matching
   expectations ratio → 1 (ties to Conjecture 1.3 / quantitative sandwich), **or**
2. Direct second-moment / orthogonal decomposition for \(Y\) on \(G(n,d')\) as in Gao–HLMPW,
   without going through ER (this is the viable path for Stage 1).

## Proposition (conditional)

**Proposition.** Assume Estimate F with error \(o(n^{-2})\) for all \(d\le n^{\alpha}\).
Assume also HLMPW’s comparison
\[
\mathrm{d_{TV}}\bigl(G(n,d)\oplus G(n,1),\,G(n,d)\oplus \nu_G\bigr)=o(1)
\]
where \(\nu_G\) is uniform on complementary perfect matchings.
Then \(\mathrm{d_{TV}}(G(n,d)\oplus G(n,1),\,G(n,d+1))=o(1)\), hence +1 monotonicity
holds for \(d\le n^{\alpha}\).

*Proof sketch.* Lemma D + Estimate F ⇒ uniform complementary matching law is
TV-close to the unique law producing exact \(G(n,d+1)\). Triangle inequality with the
assumed HLMPW comparison yields (★). Strassen-type lifting ⇒ inclusion coupling. ∎

## Immediate research task

Reproduce HLMPW’s second-moment bound on perfect matchings in \(G(n,d)\) and isolate
the exact inequality that fails for \(d>n^{1/10}\). Replace that inequality —
likely a moment comparison for triangles — with a stronger estimate.
