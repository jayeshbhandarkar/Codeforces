import sys
 
def solve():
    n, j, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
 
    target_strength = a[j - 1]
    max_strength = 0
    for x in a:
        if x > max_strength:
            max_strength = x
 
    if k == 1:
        if target_strength == max_strength:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
 
t = int(sys.stdin.readline())
for _ in range(t):
    solve()
