def cmp1(a):
    return a['x']
 
def cmp2(a):
    return a['y']
 
def cmp3(a):
    return -a['y']
 
def solve():
    n = int(input())
    a = [None] * (n + 10)
 
    for i in range(1, n + 1):
        x, y = map(int, input().split())
        a[i] = {'x': x, 'y': y, 'id': i}
 
    a[1:n+1] = sorted(a[1:n+1], key=cmp1)
    a[1:n//2 + 1] = sorted(a[1:n//2 + 1], key=cmp2)
    a[n//2 + 1:n+1] = sorted(a[n//2 + 1:n+1], key=cmp3)
 
    for i in range(1, n // 2 + 1):
        print(a[i]['id'], a[i + n // 2]['id'])
 
def main():
    t = int(input())
    for _ in range(t):
        solve()
 
if __name__ == "__main__":
    main()
