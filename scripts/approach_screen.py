"""Stop a proof approach before expanding it.

Uses only obstructions already proved in v1/paper/main.tex. A block means that
approach cannot close the claim. A clear result is not a proof.

  python scripts/approach_screen.py middle
  python scripts/approach_screen.py config-second-moment --degree n/2
"""

from __future__ import annotations

import argparse
import sys

# degree regime -> (blocked_when_linear, note)
# linear means min(d, n-d) is a positive fraction of n.


def regime(degree: str) -> str:
    key = degree.strip().lower().replace(" ", "")
    aliases = {
        "n/2": "half",
        "theta(n)": "linear",
        "θ(n)": "linear",
        "o(n)": "sublinear",
        "o(sqrt(n))": "sparse",
        "o(n^(1/2))": "sparse",
    }
    if key not in aliases:
        raise SystemExit(f"unknown degree regime: {degree}")
    return aliases[key]


CHECKS = {
    "config-second-moment": {
        "half": (
            "block",
            "Proposition config-loops: at d=n/2 the configuration model has a loop with probability 1-o(1). "
            "A multigraph second moment does not transfer to the uniform simple graph.",
        ),
        "linear": (
            "block",
            "The loop expectation d(d-1)/(2(d-1/n)) tends to infinity whenever d tends to infinity. "
            "The probability statement is proved at d=n/2. Do not expand a configuration second moment in the middle band.",
        ),
        "sublinear": (
            "clear",
            "d=o(n) is outside Proposition config-loops. This screen does not prove the argument.",
        ),
        "sparse": (
            "clear",
            "d=o(sqrt(n)) is the range of the existing variance lemma. This screen does not reprove it.",
        ),
    },
    "gao-iteration": {
        "half": (
            "block",
            "Proposition linear-barrier: Gao Theorem 6 needs d=o(n). At d=n/2 the hypothesis does not start.",
        ),
        "linear": (
            "block",
            "Proposition linear-barrier: both d and n-d of order n lie outside Theorem 6.",
        ),
        "sublinear": (
            "clear",
            "d=o(n) is the hypothesis of the sublinear theorem. This screen does not reprove it.",
        ),
        "sparse": (
            "clear",
            "d=o(sqrt(n)) is inside the edge estimate. This screen does not reprove it.",
        ),
    },
    "plus-one-chain": {
        "half": (
            "block",
            "Proposition harmonic: if each step on [3,n/3] costs at least c/d, the union bound is at least c log(n/9).",
        ),
        "linear": (
            "block",
            "Proposition harmonic: a chain of one-step couplings across [3,n/3] does not tend to probability 1 when each cost is at least c/d.",
        ),
        "sublinear": (
            "clear",
            "A chain inside d=o(n) is not the harmonic obstruction. This screen does not prove the chain.",
        ),
        "sparse": (
            "clear",
            "Sparse chains are not blocked by the harmonic sum. This screen does not reprove them.",
        ),
    },
    "chebyshev-ratio": {
        "half": (
            "block",
            "Lemma ratio-error carries an O(d/n) error. At d=n/2 that term does not tend to 0, so Chebyshev from this lemma does not give a vanishing failure.",
        ),
        "linear": (
            "block",
            "The O(d/n) error in the variance lemma stays of order 1 when d is a positive fraction of n.",
        ),
        "sublinear": (
            "clear",
            "d/n tends to 0 in this regime. Whether the variance proof extends is a separate argument.",
        ),
        "sparse": (
            "clear",
            "d=o(sqrt(n)) is the stated range of the variance lemma.",
        ),
    },
    "laplace-window": {
        "half": (
            "block",
            "The overlap window needs n/(2d) to infinity. At d=n/2 that mean is 1.",
        ),
        "linear": (
            "block",
            "At d a positive fraction of n, the mean overlap n/(2d) stays constant, so the Gaussian window does not open.",
        ),
        "sublinear": (
            "clear",
            "n/(2d) tends to infinity when d=o(n). This screen does not reprove the window.",
        ),
        "sparse": (
            "clear",
            "The overlap mean tends to infinity in this regime.",
        ),
    },
    "almost-regular-tv": {
        "half": (
            "block",
            "Proposition support-disjoint: a non-regular degree sequence and the regular law have disjoint supports, so their total variation is 1. Proposition hybrid-singular is the same obstruction for the hybrid.",
        ),
        "linear": (
            "block",
            "Proposition support-disjoint does not depend on the degree. Total variation between an almost-regular graph and a regular graph is 1.",
        ),
        "sublinear": (
            "block",
            "Proposition support-disjoint does not depend on the degree. Identify the peel with a uniform regular subgraph of the binomial host instead.",
        ),
        "sparse": (
            "block",
            "Proposition support-disjoint does not depend on the degree. Identify the peel with a uniform regular subgraph of the binomial host instead.",
        ),
    },
    "bernoulli-residual-moment": {
        "half": (
            "block",
            "Proposition bernoulli-moment: the second-moment ratio on an independent Bernoulli residual is E[p^{-K}] >= p^{-EK} with EK = Theta(d log n), which diverges.",
        ),
        "linear": (
            "block",
            "Proposition bernoulli-moment: even at linear degree, p is bounded away from 1 only if the sandwich rate is bounded away from 0, and EK = Theta(d log n) still sends p^{-EK} to infinity.",
        ),
        "sublinear": (
            "block",
            "Proposition bernoulli-moment: throughout d=o(n) one has p=o(1) and EK=Theta(d log n), so p^{-EK} tends to infinity.",
        ),
        "sparse": (
            "block",
            "Proposition bernoulli-moment: the Bernoulli comparison diverges throughout d=o(n).",
        ),
    },
    "quadratic-pgf-without-leftover": {
        "half": (
            "block",
            "Proposition origin-leftover: the quadratic-times-PGF deficit is -L^3/(4n), but the origin leftover is -L^2(3L-1)/(2n)+(2L-1)k/n. Proposition binomial-leftover-average is that formal average, not the second-moment ratio. Do not treat the incomplete deficit as a variance lower bound.",
        ),
        "linear": (
            "block",
            "The half-degree leftover is proved only at D=n/2. The incomplete quadratic-times-PGF deficit is not a lower bound at any linear degree.",
        ),
        "sublinear": (
            "block",
            "Proposition origin-leftover uses the half-degree entropy. This is not an attack on a sublinear host.",
        ),
        "sparse": (
            "block",
            "The leftover expansion is a half-degree identity. It does not apply to the sparse matching expansion.",
        ),
    },
    "binomial-pgf-without-pairwise": {
        "half": (
            "block",
            "Proposition pairwise-mass: the exact pairwise mass is -L^3/(4n)+L^2/(2n). Proposition cubic-not-identified: that term cancels the binomial leftover cubic, and the remaining-degree main term is an unsigned O(L^3/n). Do not treat origin-plus-binomial as the second-moment ratio.",
        ),
        "linear": (
            "block",
            "The pairwise mass is exact at every degree. The leftover cubic that it cancels is proved only at D=n/2. Do not use a binomial PGF as a signed L^3/n rate.",
        ),
        "sublinear": (
            "block",
            "Proposition cubic-not-identified: the sequential main term is p(1+O(L/n)), so the product error is O(L^3/n). This is not a signed rate.",
        ),
        "sparse": (
            "block",
            "The binomial-versus-pairwise comparison is a half-degree generating-function identity. It is not an attack on the sparse matching expansion.",
        ),
    },
    "origin-at-typical-k": {
        "half": (
            "block",
            "Proposition typical-origin: the third-derivative remainder of the origin is O(L^3/n) uniformly in the intersection, including at the typical value Theta(L^2). This does not improve factor-third.",
        ),
        "linear": (
            "block",
            "Proposition typical-origin: evaluating the origin at the typical intersection leaves the same cubic O(L^3/n).",
        ),
        "sublinear": (
            "block",
            "Proposition typical-origin applies whenever the origin logarithm has third derivative O(n^{-4}). The cubic order does not change.",
        ),
        "sparse": (
            "block",
            "The typical-intersection rewrite is not an attack on the sparse matching expansion.",
        ),
    },
    "sn-orbit-as-iii": {
        "half": (
            "block",
            "Proposition sn-orbit: S_n makes E[1/N|containment] constant on isomorphism types. Non-isomorphic D-regular graphs are different orbits. This is not item (iii).",
        ),
        "linear": (
            "block",
            "S_n-invariance does not identify the inverse count across non-isomorphic regular graphs.",
        ),
        "sublinear": (
            "block",
            "S_n-invariance reduces selection-reduces (iii) to iso-types and does not prove it.",
        ),
        "sparse": (
            "block",
            "S_n-invariance is not a proof of selection-reduces (iii).",
        ),
    },
    "chebyshev-N-about-mean": {
        "half": (
            "block",
            "Proposition target-cn: the only possible c_n for selection-reduces (iii) is P(N>=1)/(|Omega| p^{Dn/2}). Concentration of N about E[N] would give 1/E[N], off by E[p^{-K}]=exp(Theta(Dn)), and the masses of nu_D would not sum to 1.",
        ),
        "linear": (
            "block",
            "The target inverse-count constant is not 1/E[N] at any degree. Chebyshev about the mean of N cannot prove item (iii).",
        ),
        "sublinear": (
            "block",
            "Contain-first identifies E[N] only for D=o(n^{1/3}). Even there, Chebyshev about that mean is the wrong scale for 1/N.",
        ),
        "sparse": (
            "block",
            "Chebyshev about E[N] is the wrong scale for item (iii) of selection-reduces.",
        ),
    },
    "signed-gao-matching-host": {
        "half": (
            "block",
            "Proposition signed-matching-host: after a t-matching host the signed Gao principal term is p(1+2t/(Ln)+O((L^2+t)/n^2)). At typical t=Theta(L^2) this is p(1+Theta(L/n)). The phase does not cancel the stub-total shift.",
        ),
        "linear": (
            "block",
            "The signed matching-host expansion is for G(n,L), not a linear-degree host count. The leftover relative error is still Theta(L/n) at typical prefix.",
        ),
        "sublinear": (
            "block",
            "Signed sequential Gao after a matching host leaves relative error 2t/(Ln). Product error O(L^3/n). Not a path past n^{1/3}.",
        ),
        "sparse": (
            "block",
            "L=o(n^{1/3}) is already factor-third. This signed term does not enlarge that range.",
        ),
    },
    "host-count-chebyshev": {
        "half": (
            "block",
            "Proposition host-count-second: Var N/(EN)^2 is the p^{-K01-K02}-tilt of p^{-(K12-K012)}, which equals 1 iff H intersect H' lives in G0. Chebyshev on N is not item (iii) of selection-reduces.",
        ),
        "linear": (
            "block",
            "The host-count second moment identity does not use the degree. Chebyshev on N is not a proof that 1/N is flat.",
        ),
        "sublinear": (
            "block",
            "Contain-first is only for D=o(n^{1/3}). Even in that range, Chebyshev on N is not item (iii).",
        ),
        "sparse": (
            "block",
            "Chebyshev on the binomial-host subgraph count is not the inverse-count upper bound.",
        ),
    },
    "contain-first-as-inverse": {
        "half": (
            "block",
            "Proposition jensen-inverse: E[1/N] >= 1/E[N]. Proposition contain-first flattens only the denominator for D=o(n^{1/3}). Item (iii) of selection-reduces is the matching upper bound.",
        ),
        "linear": (
            "block",
            "Proposition contain-first requires D=o(n^{1/3}), which linear degree is not. Proposition jensen-inverse blocks using a first moment in any case.",
        ),
        "sublinear": (
            "block",
            "Proposition jensen-inverse: a flat first moment of N does not flatten E[1/N].",
        ),
        "sparse": (
            "block",
            "Proposition jensen-inverse: a flat first moment of N does not flatten E[1/N].",
        ),
    },
}


def screen(approach: str, degree: str) -> int:
    kind = regime(degree)
    verdict, reason = CHECKS[approach][kind]
    print(f"{verdict.upper()} {approach} at {degree}")
    print(reason)
    return 0 if verdict == "clear" else 2


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("approach", choices=[*CHECKS, "middle"])
    parser.add_argument("--degree", default="n/2")
    args = parser.parse_args()
    if args.approach == "middle":
        code = 0
        for name in CHECKS:
            code = max(code, screen(name, args.degree))
            print()
        return code
    return screen(args.approach, args.degree)


if __name__ == "__main__":
    sys.exit(main())
