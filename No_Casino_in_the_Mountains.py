t = int(input())
 
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    count = 0
    zeros = 0
    i = 0
    
    for j in range(k):
        if a[j] == 0:
            zeros += 1
    
    while i + k <= n:
        if zeros == k:
            count += 1
            i += k + 1
            if i + k <= n:
                zeros = sum(1 for x in a[i:i + k] if x == 0)
        else:
            if i + k < n:
                if a[i] == 0:
                    zeros -= 1
                if a[i + k] == 0:
                    zeros += 1
            i += 1
    
    print(count)
