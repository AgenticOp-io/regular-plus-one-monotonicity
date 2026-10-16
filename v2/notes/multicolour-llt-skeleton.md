# Multi-colour local limit theorem: skeleton (UNPROVED)

Status: workshop note. Nothing here is a theorem. No conjecture changes
status. The goal is a rigorous version of Remark no-l2n in
`v2/paper/main.tex`, which would reduce Conjecture factor-moment at linear
\(L\) to one explicit constant.

Screen: `approach_screen.py` has no entry for this approach. The closest
blocked entry, config-second-moment (configuration-model second moment at
half degree), is a different method: here the host is \(K_n\) and no pairing
model is used.

## 1. Exact representation

Let \(G\) be \(D\)-regular and let \(F_1,F_2\) be \(L\)-factors of \(G\).
Each pair \(jk\) of \(K_n\) is in exactly one of five states:

| state | in \(G\) | in \(F_1\) | in \(F_2\) |
|---|---|---|---|
| 11 | 1 | 1 | 1 |
| 10 | 1 | 1 | 0 |
| 01 | 1 | 0 | 1 |
| 00 | 1 | 0 | 0 |
| out | 0 | 0 | 0 |

So \(|\mathcal T_D|\,\EE[Z_L^2]=N_3\), the number of such colourings with
every vertex having \(G\)-degree \(D\), \(F_1\)-degree \(L\) and
\(F_2\)-degree \(L\). Similarly \(|\mathcal T_D|\EE Z_L=N_2\) (four states),
and \(|\mathcal T_D|=N_1\) (two states). Then
\[
\frac{\EE[Z_L^2]}{(\EE Z_L)^2}=\frac{N_3N_1}{N_2^2}.
\]
The overlap \(|F_1\cap F_2|\) is summed inside \(N_3\); no overlap average is
needed. This is the point of the approach.

Coefficient extraction:
\[
N_3=[z^Dx^Ly^L]\prod_{j<k}\bigl(1+z_jz_k(1+x_jx_k)(1+y_jy_k)\bigr),
\]
with \(z^D=\prod_jz_j^D\) and so on. Put \(z_j=re^{i\theta_j}\),
\(x_j=se^{i\phi_j}\), \(y_j=se^{i\psi_j}\). Then
\[
N_3=\frac{\prod_{j<k}(1+r^2(1+s^2)^2)}{r^{Dn}s^{2Ln}}
\,(2\pi)^{-3n}\int_{(-\pi,\pi]^{3n}}
\prod_{j<k}\chi(u_{jk})\,e^{-i\sum_j(D\theta_j+L\phi_j+L\psi_j)}\,d\Theta,
\]
where \(u_{jk}=(\theta_j+\theta_k,\phi_j+\phi_k,\psi_j+\psi_k)\) and \(\chi\)
is the characteristic function of the state vector
\(S=(1_G,1_{F_1},1_{F_2})\) under the product pair law
\(\pi\propto(\text{out}:1,\ 00:r^2,\ 10,01:r^2s^2,\ 11:r^2s^4)\).

## 2. Saddle point

All prescribed degrees are equal, so a uniform tilt \((r,s)\) solves the
saddle equations exactly, with \(\EE_\pi S=(\lambda,a,a)\),
\(\lambda=D/(n-1)\) and \(a=L/(n-1)\). There is no \(\boldsymbol\delta\) term
and no Theorem 1.3-type correction \(\boldsymbol\gamma\). This is simpler than
the containment ratio in Lemma containment-ratio, where \(U=F_1\cup F_2\) is
irregular.

The resulting \(\pi\) is the law of Lemma two-factor-identities: given
\(G\), membership in \(F_1\) and \(F_2\) is independent with probability
\(a/\lambda\) each.

## 3. Dominant points

\(|\chi(u)|=1\) iff \(\langle u,S\rangle\) is constant mod \(2\pi\) on the
support of \(\pi\). The support differences \((1,0,0),(0,1,0),(0,0,1)\) span
\(\mathbb Z^3\), so this happens iff \(u\in2\pi\mathbb Z^3\).
Requiring \(u_{jk}\in2\pi\mathbb Z^3\) for all pairs, with \(n\ge3\), gives
\(2\theta_j\equiv0\) and \(\theta_j\equiv\theta_k\) mod \(2\pi\), and the
same for \(\phi\) and \(\psi\). So there are exactly \(2^3=8\) dominant
points (each family shifted by \(0\) or \(\pi\) at every vertex), using
\(Dn\) and \(Ln\) even. Similarly \(N_2\) has \(4\) and \(N_1\) has \(2\).
The parity factors cancel in the ratio: \(8\cdot2/4^2=1\).

## 4. Near-saddle expansion (formal)

Near \(\Theta=0\),
\(\log\chi(u)=i\langle u,\EE S\rangle-\tfrac12u^{\mathsf T}\Sigma_3u
+\sum_{\ell\ge3}\frac{i^\ell}{\ell!}\kappa_\ell^{\pi}(u)\), where
\(\kappa_\ell^\pi\) is the \(\ell\)-th cumulant tensor of \(S\).
The linear terms cancel against the degree phases. The quadratic form is
\(\tfrac12\Theta^{\mathsf T}(\Sigma_3\otimes Q(K_n))\Theta\), with determinant
\(\det(\Sigma_3)^n\det Q(K_n)^3\).
The expected analogue of Isaev–McKay Theorem 1.2 is
\[
N_m=\frac{2^m\,e^{\binom n2H(\pi_m)}}{(2\pi)^{mn/2}\det(\Sigma_m)^{n/2}\det Q(K_n)^{m/2}}
\exp\bigl(\kappa_1^{(m)}+\tfrac12\kappa_2^{(m)}+o(1)\bigr),
\]
where \(\kappa^{(m)}_r\) are the cumulants of
\(R_m(\boldsymbol Y)=\sum_{jk}\sum_{\ell=3,4}\frac{i^\ell}{\ell!}\kappa_\ell^\pi(Y_{jk})\),
with \(\boldsymbol Y\) Gaussian of covariance \((\Sigma_m\otimes Q)^{-1}\).

## 5. Consequence (conditional on 4 and 6)

In \(N_3N_1/N_2^2\):

- entropy: \(\binom n2[H_5+H(\lambda)-2H_2]=0\) (Lemma two-factor-identities);
- determinant: \(\det\Sigma_3\det\Sigma_1=(\det\Sigma_2)^2\) (same lemma), and
  the powers of \(\det Q\) are \((3+1-4)/2=0\);
- parity: \(8\cdot2/16=1\);
- what is left: \(\exp(\Delta\kappa+o(1))\), where
  \(\Delta\kappa=\Delta^{(3,1;2)}[\kappa_1+\tfrac12\kappa_2]\) is an explicit
  function \(C(\alpha,\lambda)\) at \(L=\alpha n\).

So, granted 4 and 6,
\(\EE[Z_L^2]/(\EE Z_L)^2\to e^{C(\alpha,\lambda)}\) at linear \(L\).

Next concrete step (not done): compute \(C(\alpha,\lambda)\). At leading order,
\(\kappa_1^{(m)}\) is a contraction of \(\kappa_4^\pi\) with \(\Sigma_m^{-1}\otimes\Sigma_m^{-1}\),
and \(\kappa_2^{(m)}\) is a contraction of \(\kappa_3^\pi\otimes\kappa_3^\pi\) with three
copies of \(\Sigma_m^{-1}\) (from pairs of edges sharing a vertex), plus
the corrections from the \(J\) part of \(Q(K_n)^{-1}\). Test whether
\(C\equiv0\), or \(C\to0\) as \(\alpha\to0\). The second is the heuristic form
of Conjecture factor-moment. Check by exact rational arithmetic on a grid of
\((a,\lambda)\), then by Wolfram.

## 6. Obstacles (unproved)

1. Outside region. The modulus \(|\prod\chi(u_{jk})|\) away from the 8 points
   is not a product over families. The Isaev–McKay Sections 4.2–4.3
   argument (Cheeger bound, shifted boxes) is written for scalar
   \(f_\lambda(z)=\log(1+\lambda(e^{iz}-1))\). A vector version needs:
   (i) \(|\chi(u)|\le\exp(-c\,\mathrm{dist}(u,2\pi\mathbb Z^3)^2)\), which holds
   with \(c=c(\alpha,\lambda)>0\) when every state has probability bounded
   below; and (ii) a multi-family version of the shifted-box comparison,
   because partial shifts (one family shifted on a vertex subset) give
   pair factors like \(|1-2\lambda|\), not exponentially small ones when
   \(\lambda\) is near \(0\) or \(1\).
2. Sparse colours. At \(L=n^\sigma\), \(\sigma<1\), the state 11 has
   probability \(a^2/\lambda\asymp n^{2\sigma-2}\), so \(\Sigma_3\) degenerates.
   This needs the analogue of the Isaev–McKay range
   \(\varLambda\ge Bn^{\sigma-1}\) with three families of different
   densities. Factor-moment lives at \(n^{1/2}<L=o(n)\), so this is required,
   not optional.
3. Cumulant bookkeeping. Theorem 2.4/2.5 of Isaev–McKay assume scalar
   variables \(Y_{jk}\); the vector \(Y_{jk}\in\mathbb R^3\) needs the same
   graph-counting bounds with tensor coefficients. This looks routine.

## 7. Relation to proved results

- Theorem peel-second-moment-third proves the \(P_L\) analogue for
  \(L\le n^{1/3}\) with a one-sided error \(e^{C(L^3+1)/n}\). Section 5 would
  give a two-sided constant, which is what is needed past \(n^{1/3}\).
- The \(+L^2/(2n)\) of the single determinant (v1 cubic-not-identified) is
  absorbed in \(\det(\Sigma_3\otimes Q)\). This is exact cancellation, not
  an estimate, provided 4 holds.
