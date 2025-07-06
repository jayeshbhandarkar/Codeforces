import math
 
def solve():
    n = int(input())
    px, py, qx, qy = map(int, input().split())
    a = list(map(int, input().split()))
 
    dx = qx - px
    dy = qy - py
    target_dist_sq = dx*dx + dy*dy
 
    sum_a = sum(a)
    max_reachable_dist = sum_a
    
    max_val_a = 0
    if n > 0: 
        max_val_a = max(a)
    
    min_reachable_dist = abs(max_val_a - (sum_a - max_val_a)) 
    if max_val_a <= (sum_a - max_val_a):
        min_reachable_dist = 0
    else:
        min_reachable_dist = max_val_a - (sum_a - max_val_a)
 
    min_reachable_dist_sq = min_reachable_dist * min_reachable_dist
    max_reachable_dist_sq = max_reachable_dist * max_reachable_dist
 
    if min_reachable_dist_sq <= target_dist_sq <= max_reachable_dist_sq:
        print("Yes")
    else:
        print("No")
 
num_test_cases = int(input())
for _ in range(num_test_cases):
    solve()
