import sys
MOD = 998244353
 
def mod_inv(n):
    return pow(n, MOD - 2, MOD)
 
def solve():
    n, m = map(int, sys.stdin.readline().split())
    segments_by_end = [[] for _ in range(m + 1)]
    total_prob_not_exist = 1 
    
    for _ in range(n):
        l, r, p, q = map(int, sys.stdin.readline().split())
        prob_q_inv = mod_inv(q)
        prob_not_exist_k = (q - p) * prob_q_inv % MOD
        total_prob_not_exist = (total_prob_not_exist * prob_not_exist_k) % MOD
        v_i = p * mod_inv(q - p) % MOD
        segments_by_end[r].append((l, v_i))
        
    dp = [0] * (m + 1)
    dp[0] = 1 
 
    for j in range(1, m + 1):
        for l_s, v_s in segments_by_end[j]:
            dp[j] = (dp[j] + dp[l_s - 1] * v_s) % MOD
            
    ans = (dp[m] * total_prob_not_exist) % MOD
    print(ans)
 
solve()
