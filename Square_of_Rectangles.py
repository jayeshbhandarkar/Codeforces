import sys
 
for s in sys.stdin.readlines()[1:]:
    a = list(map(int, s.split()))
    group1 = a[::2]
    group2 = a[1::2]
    (a, b, c), (d, e, f) = sorted((group1, group2))
    condition = {e, f, a + b + c} != {d} != {e + f, a + b, a + c}
    print('YNEOS'[condition::2])
