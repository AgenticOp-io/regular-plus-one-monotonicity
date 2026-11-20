# r27: leading D-growth of the n^-2 term of ln R for a host H (edge, path P3, k-cycle). Heuristic; see v2/notes/r27_growing_D.md.
# ln P_d(simple) ~ G0(s) + F3 with McKay-Wormald's D^3/n term
#   F3 = -M2^2 M3/(2M1^4) + M2^4/(4M1^5) + M3^2/(6M1^3),  M_r = sum_v (d_v)_r   (regular value -D^3/(12n)).
# Its own error O(d^3/M) is not differentiable, so the local variation used here is heuristic.
# Exact anchors: P(uv in G) = D/(n-1) and P(P3 in G) = D(D-1)/((n-1)(n-2)) have no D^2/n^2 term in ln R.
import sympy as sp

n, D = sp.symbols('n D', positive=True)
ff = lambda d, r: sp.prod([d - i for i in range(r)])
M = lambda r, defs: (n - len(defs)) * ff(D, r) + sum(ff(D - c, r) for c in defs)
F3 = lambda defs: (-M(2, defs)**2 * M(3, defs) / (2 * M(1, defs)**4) + M(2, defs)**4 / (4 * M(1, defs)**5)
                   + M(3, defs)**2 / (6 * M(1, defs)**3))
assert sp.limit(F3([]) * n / D**3, D, sp.oo) == sp.Rational(-1, 12)

def lead(expr):  # coefficient of D^2/n^2 in expr
    d = sp.series(sp.simplify(expr), n, sp.oo, 3).removeO()
    assert sp.simplify(d.coeff(n, -1)) == 0
    return sp.limit(d.coeff(n, -2) / D**2, D, sp.oo)

# (b) Z-shift: given a rest pair e parallel to a host edge, P(A|e)/P(A) = exp(dG0 - [one more forbidden parallel]):
#     dG0 = (D-1)/n, forbidden parallel ~ D/n  ->  leading D/n cancels, so the shift is O(D/n^2): no D^2/n^2 term.
G0 = lambda s1, s2: -s2 / (2 * s1) - s2**2 / (4 * s1**2)
dG0e = sp.limit(n * (G0(D - 2 / n, D * (D - 1) - 4 * (D - 1) / n) - G0(D, D * (D - 1))), n, sp.oo)
assert sp.simplify(dG0e - (D - 1)) == 0 and sp.limit(dG0e / D, D, sp.oo) == 1  # cancels the +1 of the extra parallel
# (c) Z factorial cumulant: two rest pairs on the same host edge form a double edge, excluded by A,
#     so each host edge contributes -(E Z_edge)^2/2 = -D^2/(2n^2).
cum_per_edge = sp.Rational(-1, 2)

hosts = {'edge': ([1, 1], 1), 'P3': ([1, 2, 1], 2)}
hosts.update({'C%d' % k: ([2] * k, k) for k in range(3, 8)})
for name, (defs, edges) in hosts.items():
    a = lead(F3(defs) - F3([]))
    total = sp.simplify(a + edges * cum_per_edge)
    print(name, ' dF3:', a, ' Z-cumulant:', edges * cum_per_edge, ' total D^2/n^2 coefficient:', total)
    assert total == 0
print('OK: D^2/n^2 terms cancel for edge, P3 (exact anchors) and C3..C7')
