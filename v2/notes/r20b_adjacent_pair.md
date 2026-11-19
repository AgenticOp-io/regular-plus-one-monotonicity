# r20b: adjacent-pair coefficient c(D) = (D-2)/D   (heuristic derivation; NOT rigorous)
Claim: log P(s|e,f) - log P(s|e) - log P(s|f) + log P(s) = (D-2)/(D n) + O(1/n^2), e=uv, f=vw.
## Derivation (Poisson first-order, N=nD, remaining degrees d=D-h, a(d)=d(d-1), S=sum a)
Lambda(H) = sum_x a_x/(2N') [loops] + S^2/(4N'^2) [double edges] + sum_{uv in H} d_u d_v/N' [remaining pair duplicates an H edge];  log Q ~ -Lambda.
Mixed 2nd difference D2 (h_v=2, h_u=h_w=1); N' dependence is O(n^-2):
- loops: D2[sum a]=a''=2 -> +1/N
- doubles: 2*S0*D2[S]/(4N^2) = (D-1)/N
- conflicts: 2(D-1)(D-2)-2(D-1)^2 = -2(D-1) -> -2(D-1)/N
D2[Lambda] = (1+(D-1)-2(D-1))/N = (2-D)/N, so D2[log] = (D-2)/(Dn).
Higher-order (non-Poisson) corrections Psi/n depend on degrees through O(1) averages, so their vertex-local mixed difference is O(n^-2) (argued, not proved).
## Proved / numeric / not checked
- Proved: nothing rigorous. Elementary identity only.
- Sanity check of the method (algebra, exact): same Lambda reproduces the exact L=1 value Delta(e)=(D-1)/(nD) (r17a).
- Numeric: D=3 only, from r17a data n*c(P3)=.505,.463,.438,.420 (n=8..14); a+b/n fit -> ~0.31 vs predicted 1/3 (no 1/n^2 term fitted; plausible, not conclusive).
- Not checked: D=4,5,6 (no exact data; DP too slow), the O(D^b/n^2) remainder, uniformity in D.
