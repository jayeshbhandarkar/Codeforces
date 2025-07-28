import sys
 
def solve():
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
 
    if n == 1:
        sys.stdout.write("YES\n")
        return
 
    current_min_prefix_val = b[0]
 
    for i in range(1, n):
        if b[i] >= 2 * current_min_prefix_val:
            sys.stdout.write("NO\n")
            return
        current_min_prefix_val = min(current_min_prefix_val, b[i])
 
    sys.stdout.write("YES\n")
 
num_test_cases = int(sys.stdin.readline())
for _ in range(num_test_cases):
    solve()
