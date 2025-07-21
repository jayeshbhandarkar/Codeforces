t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    if a[0] == a[1]:
        majority = a[0]
    elif a[0] == a[2]:
        majority = a[0]
    else:
        majority = a[1]
 
    for i in range(n):
        if a[i] != majority:
            print(i + 1)  
            break
