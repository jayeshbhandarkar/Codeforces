t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    
    result = []

    for i in range(x):
        result.append(i)
    
    for i in range(n-1, x, -1):
        result.append(i)
    
    if x < n:
        result.append(x)
    
    print(' '.join(map(str, result)))
