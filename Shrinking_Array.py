def solve():
    n = int(input())
    a = list(map(int, input().split()))
 
    for i in range(n - 1):
        if abs(a[i] - a[i+1]) <= 1:
            print(0)
            return
 
    if n == 2:
        print(-1)
        return
 
    for i in range(n - 1): 
        l = min(a[i], a[i+1])
        r = max(a[i], a[i+1])
 
        if i > 0:
            if not (r < a[i-1] - 1 or l > a[i-1] + 1):
                print(1)
                return
 
        if i < n - 2: 
            if not (r < a[i+2] - 1 or l > a[i+2] + 1):
                print(1)
                return
        
    print(-1)
 
t = int(input())
for _ in range(t):
    solve()
  
