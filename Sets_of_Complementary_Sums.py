import sys
input = sys.stdin.readline
 
t = int(input())
mod = 998244353
 
for _ in range(t):
    n, x = map(int, input().split())
    
    y = n * (n + 1) // 2 - 1  # Minimum sum required
    
    if y > x:
        print(0)
        continue
 
    if n == 1:
        print(x)
        continue
 
    remaining_sum = x - y
    dp = [0] * (remaining_sum + 1)
    dp[remaining_sum] = 1
 
    for sz in range(n - 1, 0, -1):
        for current_sum in range(remaining_sum - sz, -1, -1):
            dp[current_sum] += dp[current_sum + sz]
            dp[current_sum] %= mod
 
    result = 0
    for current_sum in range(remaining_sum + 1):
        result += (current_sum + 1) * dp[current_sum]
        result %= mod
 
    print(result)
