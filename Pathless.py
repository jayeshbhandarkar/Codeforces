def solve():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
 
    counts = {0: 0, 1: 0, 2: 0}
    total_sum = 0
    for x in a:
        counts[x] += 1
        total_sum += x
 
    if s < total_sum:
        result = []
        result.extend([0] * counts[0])
        result.extend([1] * counts[1])
        result.extend([2] * counts[2])
        print(*(result))
    elif s == total_sum:
        print(-1)
    else:
        K = s - total_sum
        if K == 1:
            result = []
            result.extend([0] * counts[0])
            result.extend([2] * counts[2])
            result.extend([1] * counts[1])
            print(*(result))
        else:
            print(-1)
 
t = int(input())
for _ in range(t):
    solve()
