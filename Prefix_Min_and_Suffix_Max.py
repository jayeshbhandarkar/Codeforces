t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    min_pref = [0]*n
    max_suff = [0]*n
    min_pref[0] = a[0]
    for i in range(1, n):
        min_pref[i] = min(min_pref[i-1], a[i])
    max_suff[-1] = a[-1]
    for i in range(n-2, -1, -1):
        max_suff[i] = max(max_suff[i+1], a[i])
    ans = ['0']*n
    for i in range(n):
        if min_pref[i] == a[i] or max_suff[i] == a[i]:
            ans[i] = '1'
    print(''.join(ans))
