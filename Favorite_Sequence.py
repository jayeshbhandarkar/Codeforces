t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    a = []
    l, r = 0, n - 1
    for i in range(n):
        if i % 2 == 0:
            a.append(b[l])
            l += 1
        else:
            a.append(b[r])
            r -= 1
    print(*a)
