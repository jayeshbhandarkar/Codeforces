import math
 
def calculate_good(N):
    if N == 0:
        return 0
 
    primes = [2, 3, 5, 7]
    total_good = N
    
    for i in range(1, 1 << len(primes)): 
        product = 1
        num_set_bits = 0 
        
        for j in range(len(primes)):
            if (i >> j) & 1: 
                product *= primes[j]
                num_set_bits += 1
        
        if num_set_bits % 2 == 1:
            total_good -= (N // product)
        else:
            total_good += (N // product)
            
    return total_good
 
def solve():
    l, r = map(int, input().split())
    result = calculate_good(r) - calculate_good(l - 1)
    print(result)
 
t = int(input())
for _ in range(t):
    solve()
