t = int(input())
for _ in range(t):
    n = int(input())
    S = list(map(int, input().split()))
    
    zero_count = S.count(0)
    non_zero_sum = sum(x for x in S if x != 0)
    
    max_score = zero_count + non_zero_sum
    print(max_score)
