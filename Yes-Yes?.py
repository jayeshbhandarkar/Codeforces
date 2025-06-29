t = int(input())
base = "Yes" * 20
 
for _ in range(t):
    s = input()
    if s in base:
        print("YES")
    else:
        print("NO")
