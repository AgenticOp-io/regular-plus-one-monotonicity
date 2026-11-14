"""
sharp_rate.py -- the provable 1/(6 delta^3) rate and its exact error budget.

Target: Conjecture residual-factor-sharp
    Var Z / (E Z)^2 = 1/(6 delta^3) (1+o(1)) + O(delta^2 m/n),  m = o(delta^{3/2}).

The o(1) conclusion is Theorem growing-degree-factor.  What is NOT yet tracked is
the LEADING COEFFICIENT 1/(6 delta^3): showing the error in the theorem's proof is
o(delta^{-3}), not merely o(1).

The exact identity (Lemma mckay-exponent) already yields
    E[Z^2]/E[Z]^2 = exp(sum_{k>=3} x^k/(2k)) = 1 + 1/(6 delta^3) + O(delta^{-4}),
    x = 1/(delta-1),
at the typical overlap (class sums at their means).  So the coefficient 1/(6 delta^3)
is already correct; the only question is whether the ERROR terms in the proof are
o(delta^{-3}).

This script computes each error term's threshold in delta and identifies the binding
constraint, i.e. the provable range of delta for the sharp rate.
"""

from sympy import symbols, Rational, simplify

n, delta = symbols('n delta', positive=True)
m = symbols('m', positive=True)

errors = {
    # name: coefficient form, and the resulting delta-constraint for o(delta^-3)
    "McKay enumeration": (delta**3/n, "delta^6/n = o(1) => delta = o(n^{1/6})"),
    "pairing-sum (F2^o)": (m**5/(delta**2*n), "m^5 delta/n = o(1)"),
    "class-sum (lambda(g)^2)": (m**4/n, "m^4 delta^3/n = o(1)"),
    "K-dependence": (m**2*delta/n, "m^2 delta^4/n = o(1)"),
}

print("Each error term E must satisfy E * delta^3 = o(1) for the sharp 1/(6 delta^3) rate:")
print()
for name, (E, note) in errors.items():
    print(f"  {name:24s} {E}   ;  {note}")

print()
print("With m = delta^{3/2} (the conjectured envelope):")
for name, (E, _) in errors.items():
    val = simplify(E.subs(m, delta**Rational(3, 2)))
    # constraint val * delta^3 = o(1)
    cons = simplify(val * delta**3)
    print(f"  {name:24s} {cons} = o(1)")

print()
print("Binding constraint at m = delta^{3/2}:")
print(f"  class-sum    delta^9/n     -> delta = o(n^{1/9})    [1/9  = 0.1111]  <-- BINDING")
print(f"  pairing-sum  delta^{17/2}/n-> delta = o(n^{2/17})   [2/17 = 0.1176]")
print(f"  K-dep        delta^7/n     -> delta = o(n^{1/7})    [1/7  = 0.1429]")
print(f"  McKay        delta^6/n     -> delta = o(n^{1/6})    [1/6  = 0.1667]")
print()
print("=> binding is delta = o(n^{1/9}) at the extreme m ~ delta^{3/2} (class-sum term).")
print("=> binding is delta = o(n^{1/6}) (McKay) when m = o(sqrt(delta)), since then")
print("   class-sum m^4 delta^3/n = o(delta^5/n) and pairing-sum m^5 delta/n = o(delta^{7/2}/n)")
print("   are both o(delta^-3) automatically under delta = o(n^{1/6}).")

# check: m = o(sqrt(delta)) => class-sum m^4 delta^3/n = o(delta^2 * delta^3/n) = o(delta^5/n);
# need delta^5/n = o(delta^-3) => delta^8/n = o(1) => delta = o(n^{1/8}) = o(n^{0.125}),
# which is INSIDE delta=o(n^{1/6})=o(n^{0.1667}).  So McKay is truly binding there.
print()
print("For m = o(sqrt(delta)): class-sum needs delta = o(n^{1/8}), pairing-sum delta = o(n^{2/13}),")
print("  both inside delta = o(n^{1/6}); hence McKay delta = o(n^{1/6}) is binding.")
