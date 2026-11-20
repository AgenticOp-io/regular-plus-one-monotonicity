# r28: exact test of the growing-D claim (r27) for the 4-cycle

Script: `v2/scripts/r28_growing_D_exact.py D nmax`. It uses the exact degree-sequence DP from r5w3 and r23a and rational arithmetic.

The quantity is g(n) = n (E q · 8/(D-1)^4 − 1). The fit g = f1 + c(D)/n + c2/n² runs through the last three exact n values.

| D | n range used | f1 | c(D) |
|---|---|---|---|
| 3 | 26–30 | 2.0010 | 4.03 |
| 4 | 28–30 | 2.0017 | 3.98 |
| 5 | 26–30 | 2.0017 | 3.91 |
| 6 | 28–30 | 2.0007 | 3.88 |
| 7 | 20–24 | 1.9984 | 3.94 (falling) |
| 8 | 18–20 | 1.9866 | 4.41 (falling, n/D too small) |

The D=8 value is not converged. At n=20, the D=4 and D=6 fits also read c = 3.69 and 3.75, so n=20 is short of the asymptote. D=7 at n=24 takes 134 s and D=8 at n=20 takes 113 s. Cost grows about like n^D.

## Reading

- f1(4) = 2 holds exactly for every D tested. This agrees with Proposition cycle-first-order and with D-independence.
- The 1/n² coefficient is c(D) ≈ 4, with no visible growth in D. r27 needed only that there be no D²/n² term. The data show more than that: the D/n² term is also absent or very small for k=4. A guess consistent with the data is E q = (D−1)^4/8 · (1 + 2/n + 4/n² + o(n⁻²)). This is a guess, not fitted to high precision.
- This is numerical evidence at D ≤ 8. It does not prove the D = o(n) conjecture.
