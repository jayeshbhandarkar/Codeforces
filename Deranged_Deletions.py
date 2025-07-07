import sys
 
def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
 
    is_sorted_non_decreasing = True
    inversion_pair = None
 
    for i in range(n - 1):
        if a[i] > a[i+1]:
            is_sorted_non_decreasing = False
            inversion_pair = (a[i], a[i+1])
            break
    
    if is_sorted_non_decreasing:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        sys.stdout.write("2\n")
        sys.stdout.write(f"{inversion_pair[0]} {inversion_pair[1]}\n")
 
num_test_cases = int(sys.stdin.readline())
for _ in range(num_test_cases):
    solve()
