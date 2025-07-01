import collections
import heapq
 
def solve():
    n = int(input())
    a = list(map(int, input().split()))
 
    cnt = collections.Counter(a)
 
    prefix_zeros = [0] * (n + 2)
    current_prefix_zeros = 0
    
    sum_extras_lt = [0] * (n + 2) 
    current_sum_extras_lt = 0
 
    for i in range(n + 1):
        prefix_zeros[i] = current_prefix_zeros 
        sum_extras_lt[i] = current_sum_extras_lt 
        
        if cnt[i] == 0:
            current_prefix_zeros += 1
        if cnt[i] > 1:
            current_sum_extras_lt += (cnt[i] - 1)
    
    prefix_zeros[n+1] = current_prefix_zeros
    sum_extras_lt[n+1] = current_sum_extras_lt
 
    suffix_total = [0] * (n + 3) 
    for i in range(n, -1, -1):
        suffix_total[i] = suffix_total[i+1] + cnt[i]
 
    events = []
 
    for m in range(n + 2):
        if prefix_zeros[m] > 0:
            continue
 
        p_m = cnt[m] if m <= n else 0
        a_m = sum_extras_lt[m] + suffix_total[m+1]
        
        min_k_for_m = p_m
        max_k_for_m = p_m + a_m
        
        events.append((min_k_for_m, 1))
        events.append((max_k_for_m + 1, -1)) 
    
    events.sort()
 
    ans = [0] * (n + 1) 
    current_active_mexes = 0
    event_idx = 0
 
    for k in range(n + 1): 
        while event_idx < len(events) and events[event_idx][0] == k:
            current_active_mexes += events[event_idx][1]
            event_idx += 1
        ans[k] = current_active_mexes
 
    print(*(ans))
 
t = int(input())
for _ in range(t):
    solve()
