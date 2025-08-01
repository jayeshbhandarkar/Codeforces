def solve():
    n = int(input())
    a = []
    b = []
    c = []
    d = []
 
    for _ in range(n):
        ai, bi, ci, di = map(int, input().split())
        a.append(ai)
        b.append(bi)
        c.append(ci)
        d.append(di)
 
    ans = 0
    for i in range(n):
        if d[i] < b[i]:
            ans += b[i] - d[i] + a[i]
        elif c[i] < a[i]:
            ans += a[i] - c[i]
 
    print(ans)
 
def main():
    ONE_T = False 
    t = 1
    if not ONE_T:
        t = int(input())
    for _ in range(t):
        solve()
 
if __name__ == "__main__":
    main()
