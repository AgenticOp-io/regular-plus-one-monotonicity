"""Leading 1/n coefficient of kappa_4(X)/24 for multi-colour LLT.

X = -1/6 sum_P kappa^(3)(u_P). For mean-zero X,
kappa_4(X) = E[X^4] - 3 (E[X^2])^2.

Uses the large-n adjacent-pair expansion with gamma_share ~ 1/n,
calibrated so that Var(X) -> (1/36)(6 T3 + 18 T1).
"""

from __future__ import annotations

import itertools
import sys
from fractions import Fraction

import sympy as sp

from scripts.multicolour_constant import laws
from scripts.next_order_sparse import sigma_and_cumulants, _matchings, wick_ee


def T_pieces(sig, kappa, m):
    S = sp.simplify(sig.inv())
    R = range(m)
    k3 = {t: kappa[t] for t in itertools.product(R, repeat=3)}
    T3 = sum(
        k3[t1] * k3[t2] * S[t1[0], t2[0]] * S[t1[1], t2[1]] * S[t1[2], t2[2]]
        for t1 in itertools.product(R, repeat=3)
        for t2 in itertools.product(R, repeat=3)
    )
    w = [sum(k3[x, y, z] * S[x, y] for x in R for y in R) for z in R]
    T1 = sum(w[x] * S[x, y] * w[y] for x in R for y in R)
    return sp.simplify(T3), sp.simplify(T1), S, k3


def kappa4_x_coeff(sig, kappa, m):
    """Coeff of 1/n in kappa_4(X)/24.

    Leading connected 4-edge diagrams: tree of share-edges.
    Calibrate combinatorial factor so that the same machinery reproduces
    Var(X) -> T3/6 + T1/2 = (6T3+18T1)/36.
    """
    T3, T1, S, k3 = T_pieces(sig, kappa, m)
    R = range(m)

    # kappa_4 for four cubics on a fixed share-pattern via connected Wick.
    # With g_share = 1/n and #labeled ordered 4-tuples along a spanning tree
    # ~ n^2 (2n)^3 = 8 n^5, times g^6 = n^{-6}, gives 8/n.
    # The tensor contraction over connected pairings of 12 legs:
    #
    # Faster route: for Gaussian Wiener chaos of order 3,
    # kappa_4(I_3(f),...,I_3(f)) has a known expression in terms of
    # contractions of the kernel f.
    #
    # Kernel on one edge: f_P(alpha,beta,gamma) = -1/6 kappa3_{abc}
    #   * (colour embedding into u_P = Theta_j + Theta_k).
    #
    # Use Isserlis on E[X^4] with the product structure.
    #
    # Practical computation: evaluate the connected contraction
    # U = sum_{connected pairings pi of 12 legs} prod S * prod k3
    # then kappa_4(X) ~ (const / n) * U / 6^4.
    #
    # Calibrate const via Var: for r=2, ell=6,
    # Var(X) = (1/36) * (share_factor * T3_like + ...).
    # Known answer Var = T3/6 + T1/2.
    #
    # For kappa_4, use the formula for a sum of dependent mean-zero vars
    # with sparse dependence graph (line graph of K_n):
    # kappa_4(X) = sum_{connected 4-cliques in dependence} psi + ...
    #
    # Dependence: edges P,P' dependent if they share a vertex.
    # Connected 4-sets of edges of K_n: stars K_{1,4}, paths, triangles+edge, etc.

    # Enumerate isomorphism types of 4-edge connected graphs on labeled
    # vertices of K_n, weight by automorphism and gamma products.
    # For leading 1/n with S ~ O(1) or O(1/a):
    # stars at one vertex: 4 edges from one vertex to 4 others.
    # Count: n * binom(n-1,4) ~ n^5/24. Each pair of edges shares the hub,
    # so all 6 pairwise gammas are share-type ~ 1/n.
    # Wick needs 6 covs for 12 legs: (1/n)^6 * n^5 = 1/n. Yes.

    # Compute tensor for a STAR: 4 edges e_i = {0, i} for i=1..4.
    # u_{e_i} = Theta_0 + Theta_i. Cov(u_i, u_j) = Cov(Th0,Th0)+... 
    # With Cov(Theta_j, Theta_k) = S/(n-2) * (delta_{jk} - 1/(2n-2)).
    # Leading: Cov(u_i, u_i) ~ 2S/n, Cov(u_i,u_j)~ S/n for i!=j.

    g0, g = 2, 1  # scaled: actual cov = (g/n) S
    # E[prod_{i=1..4} k3(u_i)] via 12-wick with block cov
    # Then subtract disconnected for kappa_4 of four variables.
    # For identical joint law of (f1,f2,f3,f4) on a star:
    # kappa_4(f,f,f,f) = E[f^4] - 3 E[f^2]^2  (all four the same marginal)
    # but they are exchangeable not independent — use full moment-cumulant.

    # Joint cumulant kappa(f1,f2,f3,f4) for exchangeable star:
    # = E[f1 f2 f3 f4] - E[f1 f2]E[f3 f4] - E[f1 f3]E[f2 f4] - E[f1 f4]E[f2 f3]
    #   (all E[f]=0; no triple*single terms)

    def moment_f_powers(Smat, k3dict, cov_blocks):
        """E[prod_{r=1..4} k3(u^{(r)})] with Cov(u^{(r)},u^{(s)}) = cov_blocks[r,s]*S."""
        total = 0
        for cols in itertools.product(R, repeat=12):
            # cols[3*r + p] = colour of leg p of edge r
            term = 1
            for r in range(4):
                t = (cols[3 * r], cols[3 * r + 1], cols[3 * r + 2])
                term *= k3dict[t]
            # wick = sum pairings of 12 legs
            # Too slow for m=3 (3^12). Contract differently below.
            _ = term
        return None

    # Tensor contraction without enumerating colours:
    # E[k3(u)k3(v)k3(w)k3(z)] = sum_{a1..a3,...} k3[a]k3[b]k3[c]k3[d]
    #   * E[u_a1 u_a2 u_a3 v_b1 ... z_d3]
    # E[product of 12 Gaussians] = sum wick prod cov.

    def ee4(cov):
        """cov is 4x4 matrix of scalars; colour cov = cov[r,s] * S."""
        total = 0
        for t1 in itertools.product(R, repeat=3):
            for t2 in itertools.product(R, repeat=3):
                for t3 in itertools.product(R, repeat=3):
                    for t4 in itertools.product(R, repeat=3):
                        idxs = t1 + t2 + t3 + t4
                        wsum = 0
                        for pairing in _matchings(12):
                            pt = 1
                            for ia, ib in pairing:
                                ra, rb = ia // 3, ib // 3
                                pt *= cov[ra, rb] * S[idxs[ia], idxs[ib]]
                            wsum += pt
                        total += k3[t1] * k3[t2] * k3[t3] * k3[t4] * wsum
        return total

    # For m>=2 this is m^{12} * 10395 — m=2: 4096*10395 ~ 4e7, borderline
    # m=3: 531441*10395 ~ 5e9 — too slow.
    # Optimize: only m=1 exact; for m=2,3 use series substitution numeric grid.

    if m == 1:
        cov_star = sp.Matrix([[g0, g, g, g], [g, g0, g, g], [g, g, g0, g], [g, g, g, g0]])
        # Actually for star with scaled cov: diag 2, off 1
        E4 = ee4(cov_star)
        # E[f_i f_j] for i!=j: two cubics with cov off-diag g
        def ee2(c00, c01, c11):
            cov2 = sp.Matrix([[c00, c01], [c01, c11]])
            total = 0
            for t1 in itertools.product(R, repeat=3):
                for t2 in itertools.product(R, repeat=3):
                    idxs = t1 + t2
                    wsum = 0
                    for pairing in _matchings(6):
                        pt = 1
                        for ia, ib in pairing:
                            ra, rb = ia // 3, ib // 3
                            pt *= cov2[ra, rb] * S[idxs[ia], idxs[ib]]
                        wsum += pt
                    total += k3[t1] * k3[t2] * wsum
            return total

        E11 = ee2(g0, 0, 0)  # same edge — not needed for star kappa among 4 distinct
        E12 = ee2(g0, g, g0)
        # kappa(f1,f2,f3,f4) = E4 - 3 E12^2  (three pairings of four indices)
        kap4_star = E4 - 3 * E12**2
        # X = sum_P (-1/6) k3(u_P), so each f = -1/6 k3
        # kappa_4(X) includes (#stars) * kappa(f,f,f,f) + other shapes
        # #stars = n * binom(n-1,4) ~ n^5/24
        # f = -1/6 k3, so kappa(f^4) = (-1/6)^4 kap4_star = kap4_star/1296
        # Contribution ~ (n^5/24) * kap4_star/1296 * (1/n)^0 already in cov scale
        # Wait: we used g0=2,g=1 without 1/n; actual cov = (g/n)S, so
        # E4 scales as (1/n)^6, E12 as (1/n)^3, E12^2 as (1/n)^6
        # kap4_star_scaled = kap4_star / n^6
        # #stars * kap4 / 1296 = n^5/24 * kap4_star/(1296 n^6) = kap4_star/(31104 n)
        #
        # Also path diagrams etc. For m=1 at lam=1/2, k3=0 so X=0.
        return sp.simplify(kap4_star / (31104)), T3, T1

    # For general m: use that kappa_4(X)/24 ~ c(T3,T1, higher)/n
    # Classical Edgeworth: for approx normal, kappa_4 ~ O(1/n).
    # Express leading coeff via complete contractions.
    #
    # From diagrammatics matching Var X calibration:
    # Var X = (1/36)(6 T3 + 18 T1) = T3/6 + T1/2.
    # For fourth cumulant of cubic chaos, a standard formula is
    # kappa_4 = (const) * (contractions of 4 copies of k3 with 6 S).
    #
    # One main term: 9 * ||k3||_{S}^4 type.
    # Try: assume kappa_4(X) = (1/n) * Q(T3, T1, U) and fit U from series.

    # Compute U6 = full contraction of 4 k3 with 6 S (one topology)
    # Star topology in colour space: all six S connect through a hub pattern.

    # Simplified numeric: return None and use Monte-Carlo for grid in main
    return None, T3, T1


def main():
    a = sp.symbols("a", positive=True)
    lam = sp.Rational(1, 2)
    # m=1 sanity: k3=0
    states, probs = laws(a, lam)[0]
    sig, kappa = sigma_and_cumulants(states, probs, max_ell=3)
    print("m1 T", T_pieces(sig, kappa, 1)[:2])

    # Symbolic T3,T1 series — kappa4 often polynomial in these for Gaussian chaos
    for mlabel, law in zip([1, 2, 3], laws(a, lam)):
        states, probs = law
        sig, kappa = sigma_and_cumulants(states, probs, max_ell=3)
        T3, T1, S, k3 = T_pieces(sig, kappa, len(states[0]))
        print(f"m{mlabel} T3", sp.series(T3, a, 0, 2))
        print(f"m{mlabel} T1", sp.series(T1, a, 0, 2))
        # Hermite: for a pure Gaussian cubic, kappa_4(X)=0 if X is in 3rd chaos
        # and the fourth cumulant of one chaos element is  related to
        # 3! * 2^3 * ||contractions||.
        # If X is asymptotically Gaussian with rate 1/sqrt(n) corrections,
        # kappa_4(X) = O(1/n) * poly(1/a).


if __name__ == "__main__":
    main()
