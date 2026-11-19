# r14w3: nearest zero of the polynomial, R*L/n (exact enumeration)

Data: `r14w3_data.txt`; scripts: `scripts/r14w3_gen.c`, `scripts/r14w3_zeros.py`.

| L | n | labeled graphs | R | R*L/n |
|---|---|---|---|---|
| 2 | 8 | 3507 | 1.8184 | 0.4546 |
| 2 | 9 | 30016 | 1.9464 | 0.4325 |
| 2 | 10 | 286884 | 2.2095 | 0.4419 |
| 3 | 8 | 19355 | 1.1406 | 0.4277 |
| 3 | 10 | 11180820 | 1.4302 | 0.4290 |
| 4 | 9 | 1024380 | 0.9600 | 0.4266 |
| 4 | 10 | 66462606 | 1.0712 | 0.4285 |

R*L/n stays in 0.427-0.455 across all rows; L=2 n=8, L=2 n=9 and L=3 n=8 reproduce r13w2.

Correction to r13w2: its "286,884 labeled graphs for L=4 n=9" is really L=2 n=10; L=4 n=9 has 1,024,380.
No L=5 data: smallest non-degenerate case is n=12, too large to enumerate exactly.
