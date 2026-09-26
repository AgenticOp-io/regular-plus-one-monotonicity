# v2.0 status

Bar is 2.0. v1.0 is sent.

Recorded negatives (not conjecture closes):
- Sprinkle transfer blocked (variance ratio \(\varepsilon/(1+\varepsilon)\)).
- Switch bound only \(D^{O(1)}\); iterated BFS only \(\exp(O(D\log D))\); both miss bulk.
- Near-disjoint second moment: \(K=o(D^2/\log(nD))\) contributes \(\exp(-\Theta(D^2))\) times bulk.
- Independent containment indicators would kill item (iii); dependence is necessary.
- Item (iii) is a lower-tail of \(N\) at \(1/c_n\), not concentration about \(\mathbb{E}[N]\).
- \(\nu_D\) is \(S_n\)-invariant: edges match \(\mu_D\); higher subgraphs need flat inverse-count.
- \(d\nu_D/d\mu_D \propto \mathbb{E}[1/N\mid\mathrm{containment}]\); item (iii) iff \(\nu=\mu\).
- Triangle: unconditional first moment matches \(\mu_D\); conditional proxy
  \(\bigl((1+\varepsilon)/(2+\varepsilon)\bigr)^3\pi^3\); neither is \(\mathbb{E}[N_T/N]\).
- Exact \(n=6\), \(D=2\): \(\mathbb{E}[1/N\mid C_6]/\mathbb{E}[1/N\mid C_3\cup C_3]\in[1.07,1.16]\);
  triangle \(\nu/\mu\in[0.885,0.942]\).
- Literal peel \(Z_d\) flatness fails on \(K_6\) at \((d,m)=(1,1)\).
- Literal \(N_1\) residual flatness fails on \(7080/16588\) multi-matching hosts.
- Sandwich posterior is not the first peel flatness.

Six conjectures still open.

Next object needs a lower-tail bound for \(N\) at \(1/c_n\), or a new binomial
coupling — not moments about \(\mathbb{E}[N]\), not near-disjoint factors, not switches.
