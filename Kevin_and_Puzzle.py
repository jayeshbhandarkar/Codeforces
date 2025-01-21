from collections import defaultdict
MOD = 998244353

def solve_single_test():
    n = int(input())
    a = list(map(int, input().split()))  
    ph = defaultdict(int)
    pl = defaultdict(int)
    ph[0] = 1
    
    for i in range(n):
        ai = a[i]
        wh = (ph[ai] + pl[ai]) % MOD
        ch = defaultdict(int)
        cl = defaultdict(int)
        
        if wh > 0:
            ch[ai] = wh
        
        for l, c in ph.items():
            cl[l + 1] = (cl[l + 1] + c) % MOD
        
        ph = ch
        pl = cl
    
    tt = 0
    for c in ph.values():
        tt = (tt + c) % MOD
    for c in pl.values():
        tt = (tt + c) % MOD
    
    print(tt)

def main():
    t = int(input())
    for _ in range(t):
        solve_single_test()

if __name__ == "__main__":
    main()
