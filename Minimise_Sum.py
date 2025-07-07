import sys
 
def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
 
    P = [0] * n
    S_prefix = [0] * n 
 
    current_min = float('inf')
    current_sum_P = 0
 
    for k in range(n):
        current_min = min(current_min, a[k])
        P[k] = current_min
        current_sum_P += P[k]
        S_prefix[k] = current_sum_P
    
    min_overall_sum = S_prefix[n-1]
    
    for i in range(n - 1):
        sum_P_before_i = S_prefix[i-1] if i > 0 else 0
        P_before_i = P[i-1] if i > 0 else float('inf')
 
        new_val_at_i = a[i] + a[i+1]
        P_prime_i = min(P_before_i, new_val_at_i)
 
        current_op_sum = sum_P_before_i + P_prime_i
        min_overall_sum = min(min_overall_sum, current_op_sum)
 
    sys.stdout.write(str(min_overall_sum) + "\n")
 
num_test_cases = int(sys.stdin.readline())
for _ in range(num_test_cases):
    solve()
