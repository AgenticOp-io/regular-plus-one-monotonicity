# v2.0 status

Bar is 2.0. v1.0 is sent.

Recorded negatives (not conjecture closes):
- Sprinkle transfer blocked (variance ratio \(\varepsilon/(1+\varepsilon)\)).
- Switch bound only \(D^{O(1)}\); iterated BFS only \(\exp(O(D\log D))\); both miss bulk.
- Switch graph on \(\Omega_2\) (\(n=6\)) is connected, but \(a\) still varies by \(15\%\).
- Near-disjoint second moment: \(K=o(D^2/\log(nD))\) contributes \(\exp(-\Theta(D^2))\) times bulk.
- Independent containment indicators would kill item (iii); dependence is necessary.
- Edge-exposure Azuma with Lipschitz \(|\Omega|\) has vanishing exponent; bound \(\to 2\).
- Item (iii) is a lower-tail of \(N\) at \(1/c_n\), not concentration about \(\mathbb{E}[N]\).
- \(\nu_D\) is \(S_n\)-invariant: edges match \(\mu_D\); higher subgraphs need flat inverse-count.
- \(d\nu_D/d\mu_D \propto \mathbb{E}[1/N\mid\mathrm{containment}]\); item (iii) iff \(\nu=\mu\).
- Triangle proxies are not \(\mathbb{E}[N_T/N]\); exact \(n=6\) has \(\nu/\mu\in[0.885,0.942]\).
- Literal peel flatnesses (\(Z_d\), \(N_m(R)\), sandwich-as-uniform) fail on six vertices.

Six conjectures still open.

Next: lower-tail of \(N\) at \(1/c_n\) using the pairwise dependence tilt,
or a new binomial coupling.
