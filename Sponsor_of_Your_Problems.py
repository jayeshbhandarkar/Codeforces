def solve():
    left_str, right_str = input().split()
    n = len(left_str)
 
    res = float('inf')
 
    def rec(i, tl, tr, f1, f2):
        nonlocal res
 
        if i == n:
            res = min(res, f1 + f2)
            return
 
        low = int(left_str[i]) if tl else 0
        high = int(right_str[i]) if tr else 9
 
        for dig in range(low, high + 1):
            new_tl = tl and (dig == low)
            new_tr = tr and (dig == high)
 
            new_f1 = f1 + (1 if dig == int(left_str[i]) else 0)
            new_f2 = f2 + (1 if dig == int(right_str[i]) else 0)
 
            rec(i + 1, new_tl, new_tr, new_f1, new_f2)
            
            if res <= f1 + f2:
                return
 
    rec(0, True, True, 0, 0)
    print(res)
 
t = int(input())
for _ in range(t):
    solve()
