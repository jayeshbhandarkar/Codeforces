t = int(input())
for _ in range(t):
    k, a, b, x, y = map(int, input().split())
    
    if x > y:
        a, b = b, a
        x, y = y, x
    
    count = 0
    if k >= a:
        count += (k - a) // x + 1
        k = k - x * ((k - a) // x + 1)
    
    if k >= b:
        count += (k - b) // y + 1

    print(count)
