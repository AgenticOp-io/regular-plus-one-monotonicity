"""r16w2: exact pairing-level E[Z^2 | x]/E[Z|x]^2 for a two-type host (n/2 cells of degree delta+t, n/2 of delta-t),
conditioned on x = #cross (P-Q) pairs.  Lambda = sum_{edges} y_i y_j = t^2(total_pairs - 2x) is a function of x alone,
so conditioning on x IS conditioning on the assortativity.  Factor-complement residual r_v = h_v - D, D=delta-m.
Also computes the unconditional ratio (sum over x) and checks it against r4w2_pairing_shift.log_ratio."""
import sys, numpy as np
from math import lgamma
sys.path.insert(0, 'v2/scripts')
from r4w2_pairing_shift import log_ratio, hyp_pmf
lg = lambda v: np.array([lgamma(k) for k in np.atleast_1d(v)])
def ldf(m): m = np.asarray(m, float); return lg(2*m+1) - m*np.log(2) - lg(m+1)
def lc(a, b): return lg(a+1) - lg(b+1) - lg(a-b+1)
def logW(a, b, x):  # pairings of a P-pts, b Q-pts with exactly x cross pairs (log); -inf if impossible
    x = np.asarray(x); ok = (x >= 0) & (x <= min(a, b)) & ((a-x) % 2 == 0) & ((b-x) % 2 == 0)
    xx = np.where(ok, x, 0)
    v = lc(a, xx) + lc(b, xx) + lg(xx+1) + ldf((a-xx)/2) + ldf((b-xx)/2)
    return np.where(ok, v, -np.inf)
def conv_logs(pairs, X):
    """log of coefficient array (len X+1) of prod_c sum_x W(a_c,b_c,x) z^x, windowed around each peak."""
    acc, sc = np.array([1.0]), 0.0; off = 0
    for a, b in pairs:
        pk = int(a*b/(a+b+1e-9)); w = int(14*np.sqrt(pk+5)) + 4
        lo, hi = max(0, pk-w), min(min(a, b), pk+w)
        xs = np.arange(lo, hi+1); l = logW(a, b, xs); m = l.max()
        if not np.isfinite(m): return np.full(X+1, -np.inf)
        arr = np.exp(l-m)
        acc = np.convolve(acc, arr); sc += m; off += lo
    out = np.full(X+1, -np.inf); idx = off + np.arange(len(acc))
    with np.errstate(divide='ignore'): lv = np.log(acc) + sc
    k = idx <= X; out[idx[k]] = lv[k]; return out
def lse(a, axis=None):
    m = np.max(a); return m + np.log(np.sum(np.exp(a-m))) if np.isfinite(m) else -np.inf
def run(n, delta, m, t):
    nP = nQ = n//2; hP, hQ = delta+t, delta-t; D = delta-m; rP, rQ = hP-D, hQ-D
    A, B = nP*hP, nQ*hQ; X = min(A, B)
    sP, sQ = nP*rP, nQ*rQ; cP, cQ = A-sP, B-sQ
    lWt = logW(A, B, np.arange(X+1))                          # all pairings, cross count x
    lc1 = conv_logs([(sP, sQ), (cP, cQ)], X)                  # E[Z|x] numerator (x-dependent part)
    # law of total overlap over nc identical cells: log-convolution by repeated squaring
    def pi_law(nc, h, r):
        base = hyp_pmf(np.arange(max(0, 2*r-h), r+1), h, r, r); res = np.array([1.0]); e = nc
        while e:
            if e & 1: res = np.convolve(res, base)
            base = np.convolve(base, base); e >>= 1
        lo = max(0, 2*r-h)*nc; return lo, res
    loP, pP = pi_law(nP, hP, rP); loQ, pQ = pi_law(nQ, hQ, rQ)
    EP = loP + (np.arange(len(pP))*pP).sum(); EQ = loQ + (np.arange(len(pQ))*pQ).sum()
    sdP = np.sqrt(((np.arange(len(pP))+loP-EP)**2*pP).sum()); sdQ = np.sqrt(((np.arange(len(pQ))+loQ-EQ)**2*pQ).sum())
    bP = [b for b in range(len(pP)) if abs(b+loP-EP) <= 7*sdP+2]; bQ = [b for b in range(len(pQ)) if abs(b+loQ-EQ) <= 7*sdQ+2]
    acc = np.full(X+1, -np.inf)
    for i in bP:
        BP = i+loP
        for j in bQ:
            BQ = j+loQ; w = np.log(pP[i]) + np.log(pQ[j])
            if not np.isfinite(w): continue
            cls = [(BP, BQ), (sP-BP, sQ-BQ), (sP-BP, sQ-BQ), (cP-(sP-BP), cQ-(sQ-BQ))]
            if min(min(c) for c in cls) < 0: continue
            acc = np.logaddexp(acc, w + conv_logs(cls, X))
    # R(x) = Wt(x) * c2(x) / c1(x)^2   (all in log)
    lR = lWt + acc - 2*lc1
    # first moment exponents: P(x) under pairing
    lPx = lWt - lse(lWt); Px = np.exp(lPx); xs = np.arange(X+1)
    mu = (xs*Px).sum(); sd = np.sqrt(((xs-mu)**2*Px).sum())
    # unconditional: E Z^2 = sum_x c2*Cp^2/Wall, E Z = sum_x c1*Cp/Wall -> ratio = Wall*sum c2 / (sum c1)^2
    lWall = lse(lWt); unc = lWall + lse(acc) - 2*lse(lc1)
    return unc, lR, mu, sd, Px
if __name__ == "__main__":
    for delta, m, t in [(40, 6, 3)]:
        for n in [int(a) for a in sys.argv[1:]] or [100, 200, 400]:
            unc, lR, mu, sd, Px = run(n, delta, m, t)
            ex, _ = log_ratio([delta+t]*(n//2) + [delta-t]*(n//2), delta-m)
            print(f"delta={delta} m={m} t={t} n={n}: uncond log R={unc:.3f} (r4w2 exact {ex:.3f}); x mean={mu:.1f} sd={sd:.1f}")
            for z in (-2, -1, 0, 1, 2):
                x = int(round(mu + z*sd)); v = [lR[k] for k in (x, x+1) if np.isfinite(lR[k])]
                print(f"   x=mean{z:+d}sd (x~{x}): log R(x|x)= {v[0] if v else float('nan'):.3f}")
