t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    x = list(map(int, input().split()))
    min_x = x[0]
    max_x = x[-1]
    steps = min(abs(s - min_x), abs(s - max_x)) + (max_x - min_x)
    print(steps)
