import math
 
def solve():
    a, b, k = map(int, input().split())
    common_divisor = math.gcd(a, b)
    
    if (a // common_divisor <= k) and (b // common_divisor <= k):
        print(1)
    else:
        print(2)
 
num_test_cases = int(input())
for _ in range(num_test_cases):
    solve()
