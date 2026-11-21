# r43: attempt on r36 gaps 2-4 using r41's tail -- mostly NEGATIVE / reduction only

Status: **gaps 2-4 NOT closed.** One structural observation (below) and one reduction. main.tex untouched.

## Observation (proved, elementary; numerics `v2/scripts/r43_phi.py`)
r36 §1 calls Z a "monomer-dimer gas with activities |w|/n", but q_k is NOT a product over edges:
q_k = n^{-k} e^{phi(k)}, phi(k) = -sum_{i<k} ln(1-(2i+1)/n) = k^2/n + (2/3)k^3/n^2 + ... (ratio of remainder to
2k^3/(3n^2) is 0.998..1.11 for k<=n/10, checked n=1e4,1e6). So plain Kotecky-Preiss does not apply as stated: the
weight has a mean-field (all-pairs) interaction e^{k^2/n} on top of the local conflict. **r36 gap 2 as worded
(KP with absolute-value activities) is ill-posed**; this is a correction to r36 §1, not a closure.

## Reduction (sketch)
Decouple the global part: e^{k^2/n} = E_g e^{sqrt(2/n) g k}, g~N(0,1) (exact). Conditional on g the gas is product-form
with activities w_e e^{sqrt(2/n)g}/n, KP applies with |w|<=max(|x-1|,1), conflict degree <=2L+2j; ln Z_g is then a cluster
series, and ln Z = ln E_g exp(ln Z_g). Remaining: (i) the cubic remainder (2/3)k^3/n^2 with k up to ~L^2 is NOT small
(L^6/n^2), so it cannot be dropped inside Z; it must be handled cluster-wise (connected clusters have k<=order, small),
which needs a Mayer expansion for the coupled (g, edges) system -- not done; (ii) Gaussian integral over g with
signed weights needs |g|<=sqrt(n)/L control, which is where r41's tail (m_j<=CL^2) would be used -- plausible, unwritten.

## Gap 3 (error propagation): not done
The backward recursion y_j = x exp(sum_{k>j} gamma_k(y_k)) has gamma = O(L/n)-type sensitivity: d y_j/d y_k = O(L/n),
total Lipschitz constant sum_k O(L/n)=O(L^2/n)=o(1) for L=o(sqrt n) -- so a perturbation delta in each gamma_k of size
O(L^3/n^2) (r41 §4) changes y_j by O(L^4/n^2) and ln Z_j by O(L)*that: contraction is plausible (sketch, from the
recursion's form; not verified against a perturbed run). Rigor still needs the random o_v statistics.

## Gap 4: not done; no new numerics beyond r41 (kappa_k, k>=3 appear only as bounded residual ~ (x-1)^3 L^4/n^2).

Verdict: proved = phi expansion; sketched = Gaussian decoupling, contraction; open = everything else. (R2*) stays open.
