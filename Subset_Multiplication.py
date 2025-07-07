import math
 
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
 
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return (a * b) // gcd(a, b)
 
def solve():
    n = int(input())
    b = list(map(int, input().split()))
 
    x_candidate = 1
 
    for i in range(n - 1):
        current_b = b[i]
        next_b = b[i+1]
        
        if next_b % current_b != 0: 
            x_candidate = lcm(x_candidate, current_b // gcd(current_b, next_b))
 
    print(x_candidate)
 
num_test_cases = int(input())
for _ in range(num_test_cases):
    solve()
