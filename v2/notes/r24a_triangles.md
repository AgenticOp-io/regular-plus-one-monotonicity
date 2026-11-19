# r24a: first-order constants of E[t] (triangles) and E[q] (4-cycles) -- NUMERICALLY pinned, NOT proved
G uniform simple D-regular on [n]. Targets from r23a: E q=(D-1)^4/8(1+f1/n+O(n^-2)), E t=(D-1)^3/6(1+e1/n+O(n^-2)).

## Result (numerical, exact DP, v2/scripts/r23a_f1.py; Richardson = least-squares a+b/n+c/n^2 on the last 6 n)
| D | n range | f1 | e1 |
|---|---|---|---|
| 3 | 36..80 | 2.000007 | 1.99973 |
| 4 | 36..80 | 2.00010 | 2.25017 |
| 5 | 20..40 | 2.0021 | 2.4042 |
| 6 | 12..32 | 2.0050 | 2.539 (unconverged) |
Conjecture (fits all four, errors shrink with n range): **f1 = 2 for all D;  e1(D) = 3(D-1)/D = 3 - 3/D**  (2, 9/4, 12/5, 5/2).
This is the "r1 = 3(D-1)/D" guess of r23b; it is now supported by data, not derived.

## Equivalent form via the pairing model (algebra, exact)
E t = C(n,3) D^3 (D-1)^3 /((N-1)(N-3)(N-5)) * Q(K3),  N=nD, Q(K3)=P(simple | triangle placed)/P(simple).
Prefactor = (D-1)^3/6 (1 + (9/D - 3)/n + O(n^-2)). So e1=3(D-1)/D  <=>  Q(K3) = 1 + 6(D-2)/(D n) + O(n^-2).
Rigorous proof therefore needs the 1/n-coefficient of P(simple|U)/P(simple) for U=K3 (and 4-cycle for f1), i.e. an expansion of
the simple-probability of a pairing with 3 degree-deficient vertices to relative error O(n^-2). McKay-Wormald's enumeration gives only O(D^3/n).

## What I did NOT do (honest gaps)
- No proof of either constant. Route (a) needs the above sharper expansion (not available to me); route (c) (self-consistency): the r23a identities are affine in (t,q) with no relation fixing t or q, so they cannot pin them -- checked by inspection, the 4-edge identities all introduce at least as many new unknowns as equations.
- Literature (Wormald 1981; McKay-Wormald-Wysocka 2004) NOT read this round: from memory they give relative error O(1/n) (so E t=(D-1)^3/6(1+O(1/n)) for fixed D is covered), not the 1/n constants.
- Next step for a proof: switching/generating-function expansion of P(simple|U) with loops/double edges as Poisson with explicit 1/n corrections; test the conjecture Q(K3)=1+6(D-2)/(Dn) first against exact DP (cheap).
- D-dependence and growing D untouched. e2,f2 not estimated (irrelevant at the n^-2 level per r23a).
