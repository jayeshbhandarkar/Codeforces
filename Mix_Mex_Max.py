def solve():
    n = int(input())
    a = list(map(int, input().split()))
 
    fixed_value = -1
 
    for x in a:
        if x != -1:
            if fixed_value == -1:
                fixed_value = x
            elif fixed_value != x:
                print("NO")
                return
 
    if fixed_value == -1:
        print("YES")
        
    elif fixed_value == 0:
        print("NO")
        
    else: 
        print("YES")
 
t = int(input())
for _ in range(t):
    solve()
