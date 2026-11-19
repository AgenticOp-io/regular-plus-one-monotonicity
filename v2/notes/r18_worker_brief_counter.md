# r18 worker brief: faster exact counter for u_T (D=3 paths), reach n>=40

Read first: v2/notes/r17w1_logPsimple_status.md, v2/scripts/r16_longpath.py, v2/scripts/r5w3_exact.py.
Write only v2/notes/r18w1_* and v2/scripts/r18w1_*. Do not edit paper/main.tex. Commit when done.

## Do
1. Write a faster exact counter of D-regular simple labeled graphs containing a prescribed edge set U
   (paths P3..P6 and disjoint shapes P2+P2, P3+e), D=3. Ideas: transfer/DP over degree-sequence
   states, or exact count of 3-regular graphs with prescribed edges via degree-sequence recursion
   with memoized residual-degree multisets. Exact integers only (Python ints/Fractions).
2. Validate: it must match r5w3_exact contains() at every n<=28 tested.
3. Run P3..P6 for the largest feasible even n (target n=40 or more), compute u_T and local exponents
   (log-slope between consecutive n). Report whether n^(k-2) u flattens for P5, P6.

Report: what was validated, what was only run, max n reached, runtimes. Do not claim an exponent the data doesn't support.
