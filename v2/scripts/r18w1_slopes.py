import glob, math, os
d = os.path.dirname(os.path.abspath(__file__))
KK = {'P3': 3, 'P4': 4, 'P5': 5, 'P6': 6, '2e': 2, 'P2+P2': 4, 'P3+e': 4}
for f in sorted(glob.glob(d + '/r18w1_out_*.txt')):
    name = os.path.basename(f)[10:-4]
    k = KK[name]
    r = [(int(l.split()[1]), float(l.split()[2][2:])) for l in open(f)]
    print(name)
    for (a, x), (b, y) in zip(r, r[1:]):
        s = -math.log(abs(y / x)) / math.log(b / a) if x * y > 0 else float('nan')
        print(' n %d->%d slope %.2f  n^%d*u(b)=%.4g' % (a, b, s, k - 2, b ** (k - 2) * y))
