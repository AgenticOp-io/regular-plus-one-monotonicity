# +1 attack: framework, proved lemmas, open estimates

## Target

**Conjecture (+1).** Let \(n\) be even and \(3\le d\le n-4\). There exists a coupling of
\(G\sim G(n,d)\) and \(H\sim G(n,d+1)\) with \(\mathbb{P}(G\subset H)=1-o(1)\).

## Strategy (HLMPW / Gao line)

Construct \(H\) as an edge-disjoint union
\[
H \;=\; G \;\cup\; M,
\]
where \(G\sim G(n,d)\) and \(M\) is a perfect matching on the complement edges, then show
that the law of \(H\) is contiguous to (or within \(o(1)\) total variation of) \(G(n,d+1)\).

Equivalently, prove
\[
\mathrm{d_{TV}}\bigl(G(n,d)\oplus G(n,1),\; G(n,d+1)\bigr)=o(1). \tag{★}
\]
Strassen / coupling theorems then upgrade TV proximity + absolute continuity features
into an inclusion coupling (as in Isaev–McKay–Southwell–Zhukovskii / HLMPW).

---

## Lemma A — Configuration model nesting (PROVED)

Let \(n,d\) be such that the configuration model \(\mathcal{C}(n,d)\) is defined
(\(dn\) even). Realize \(\mathcal{C}(n,d+1)\) by adding one extra stub per vertex to a
configuration of \(\mathcal{C}(n,d)\) and pairing the new stubs among themselves as a
random perfect matching on stubs (then projecting).

More formally: sample a random pairing of \(dn\) stubs; independently sample a random
perfect matching on a fresh set of \(n\) stubs (one per vertex). The union is a
configuration of degree \(d+1\).

**Claim.** Writing \(G^\mathrm{conf}\) and \(H^\mathrm{conf}\) for the (possibly multi) graphs
obtained, we have \(G^\mathrm{conf}\subset H^\mathrm{conf}\) always.

**Proof.** Immediate from construction: every pair in the first pairing remains in the union. ∎

**Gap to the conjecture.** Simple-graph conditioning and contiguity of the configuration
model to \(G(n,d)\) are classical for \(d=n^{o(1)}\), but the **extra matching** is a matching
in the stub world, not a uniform perfect matching in the complement of the simple graph
\(G(n,d)\). Passing from (★-conf) to (★) is the analytic work.

---

## Lemma B — Simple-graph obstruction is sparse (PROVED for \(d=o(n^{1/3})\))

In the configuration model \(\mathcal{C}(n,d)\) with \(d=o(n^{1/3})\), the probability of being
simple is \(\exp\bigl(-\frac{d^2-1}{4}+o(1)\bigr)\) (Bollobás / Wormald), and
\(G(n,d)\) is contiguous to the conditioned simple configuration.

**Consequence.** Any coupling event that holds whp for configurations and is decreasing
under deleting loops/multiedges transfers to \(G(n,d)\) in this range — the classical
window where HLMPW already has \(+1\). Our novelty must live **outside** \(d=o(n^{1/3})\),
or else improve constants/errors inside it.

---

## Lemma C — Exact inclusion iff a 1-factor in the complement (PROVED)

Fix a \(d\)-regular graph \(G\) on even \(n\). The following are equivalent:

1. There exists a \((d+1)\)-regular \(H\supset G\).
2. The complement \(\overline{G}=K_n-G\) contains a perfect matching.
3. \(\overline{G}\) satisfies Tutte’s condition.

**Proof.** (1)⇒(2): \(H\setminus G\) is 1-regular, hence a perfect matching.  
(2)⇒(1): \(H:=G\cup M\) is \((d+1)\)-regular if \(M\subset E(\overline{G})\).  
(2)⇔(3): Tutte. ∎

**Corollary (necessary condition for a coupling).**  
Any coupling with \(G\subset H\) always must have \(M:=H\setminus G\) a perfect matching in
\(\overline{G}\). So the only possible couplings are of the form \(H=G\cup M\) with
\(M\in\mathcal{M}(\overline{G})\).

---

## Lemma D — Uniform \(H\) forces a reweighted matching (PROVED)

Let \(\mu_d\) be the law of \(G(n,d)\). Suppose we sample \(G\sim\mu_d\) and then sample a
perfect matching \(M\) in \(\overline{G}\) from a distribution \(\nu_G\). Set \(H=G\cup M\).

Then \(H\sim G(n,d+1)\) if and only if for every \((d+1)\)-regular \(H_0\),
\[
\sum_{\substack{G\subset H_0\\ G\text{ $d$-regular}}}
\mu_d(G)\,\nu_G(H_0\setminus G)
\;=\;
\mu_{d+1}(H_0).
\]
Since \(\mu_d(G)=1/|\mathcal{G}(n,d)|\) (uniform), this becomes
\[
\frac{1}{|\mathcal{G}(n,d)|}
\sum_{M\subset H_0}
\nu_{H_0\setminus M}(M)
\;=\;
\frac{1}{|\mathcal{G}(n,d+1)|},
\]
where the sum is over perfect matchings \(M\subset H_0\) such that \(H_0\setminus M\) is \(d\)-regular
(always true for any perfect matching in a \((d+1)\)-regular graph).

**Special case.** If \(\nu_G\) is **uniform** on perfect matchings of \(\overline{G}\), then
\(H\) is uniform on \(\mathcal{G}(n,d+1)\) iff every \((d+1)\)-regular graph has the same
number of \(d\)-regular spanning subgraphs obtained by deleting a perfect matching —
i.e. iff \(H_0\) has the same number of perfect matchings for all \(H_0\in\mathcal{G}(n,d+1)\),
which is **false**. So uniform \(\nu_G\) does **not** give exact uniformity.

**HLMPW insight.** One does not need exact uniformity — only \(\mathrm{d_{TV}}=o(1)\),
or contiguity for whp properties / Strassen lifting for inclusion.

---

## Lemma E — Sandwich upper bound implies abundance of matchings (PROVED)

Assume \(d\ge C\log n\) and apply BIM: whp
\[
G(n,d)\;\subset\;G\!\Bigl(n,(1+\varepsilon)\frac{d}{n}\Bigr).
\]
Equivalently, whp \(\overline{G(n,d)}\) contains \(\overline{G(n,(1+\varepsilon)d/n)}\).

For \(p=(1+\varepsilon)d/n\le 1-\delta\), the complement binomial graph is
\(G(n,1-p)\) up to loops of labeling, and for \(1-p\) above the perfect-matching threshold
(\(1-p\ge(\log n+\omega(1))/n\) is far too weak — we need the complement to be dense).

When \(d\le (1-\delta)n\), the complement of a \(d\)-regular graph is \((n-1-d)\)-regular,
hence itself in the BIM range if \(n-1-d\ge C\log n\). In particular \(\overline{G}\) is
whp Hamiltonian and matching-rich.

**Consequence.** Existence of some \(M\) is not the obstruction for \(d\) bounded away from
\(n\). The obstruction is **distributional bias** among matchings.

---

## Open Estimate (★) — Main lemma to prove

**Conjecture (TV contraction).** There exists \(\alpha>0\) such that for
\(3\le d\le n^{\alpha}\),
\[
\mathrm{d_{TV}}\bigl(G(n,d)\oplus G(n,1),\;G(n,d+1)\bigr)
\;\le\;
n^{-c}
\]
for some \(c>0\).

**Status.** HLMPW prove usable bounds for \(d\le n^{1/10}\) (and discuss \(n^{1/7-\varepsilon}\)).
**Our Stage 1 goal:** push \(\alpha\) past \(1/3\), or improve the TV error enough to iterate
through \(d\le n^{1/3+\delta}\).

### Proposed proof outline for (★)

1. **Janson orthogonal decomposition** of the perfect-matching count \(Y\) in \(G(n,d)\)
   against triangle counts (Gao; refined moments in HLMPW).
2. Show \(Y\) is concentrated enough that picking \(M\) proportional to
   \(1/\{\#\text{ matchings in }\overline{G}\}\) (the Radon–Nikodym fix for Lemma D)
   is close to picking a uniform edge-disjoint matching as in \(G(n,d)\oplus G(n,1)\).
3. Apply McKay’s enumeration of sparse graphs with given degrees inside a host graph
   to compare the number of ways to build \(H\) vs the uniform measure.
4. Extract explicit TV ≤ \(n^{-c}\).

### Immediate weakened theorem (CLAIM — proof incomplete)

**Conjecture (defective +1).** For \(d\le n^{1/3}\), there is a coupling and a graph \(F\)
with at most \(n^{o(1)}\) edges such that
\[
\mathbb{P}\bigl(G(n,d)\subset G(n,d+1)\cup F\bigr)=1-o(1).
\]
This would already be publishable if new; Kim–Vu historically used defects.

---

## What we will not claim

- Full +1 for all \(d\) (open).
- Process sandwich / Conjecture 1.3 (needs different ideas).
- That Lemma A alone proves the simple-graph conjecture.

## Next concrete math step

Formalize Step 2 of (★) as a standalone estimate:

> **Estimate F.** Let \(Y(G)\) be the number of perfect matchings in \(\overline{G}\) for
> \(G\sim G(n,d)\). Prove \(\frac{Y}{\mathbb{E}Y}=1+o(1)\) whp for \(d\le n^{1/3+\delta}\).

If Estimate F holds with strong enough error, Lemma D’s reweighting is negligible and
(★) follows from the configuration / ⊕ construction in the HLMPW range extended.
