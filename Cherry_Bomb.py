t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    fixed_x = -1
    for i in range(n):
        if b[i] != -1:
            if fixed_x == -1:
                fixed_x = a[i] + b[i]
            elif fixed_x != a[i] + b[i]:
                fixed_x = -2 
                break

    if fixed_x == -2:
        print(0)
        continue

    if fixed_x != -1:
        valid = True
        for i in range(n):
            if b[i] == -1:
                need = fixed_x - a[i]
                if not (0 <= need <= k):
                    valid = False
                    break
        print(1 if valid else 0)
    else:
        min_poss = max(a)  
        max_poss = min(a[i] + k for i in range(n)) 

        if min_poss > max_poss:
            print(0)
        else:
            print(max_poss - min_poss + 1)
