import math
import sys
 
def gcd(a, b):
    return math.gcd(a, b)
 
def solve():
    try:
        n_str = sys.stdin.readline()
        if not n_str: return
        n = int(n_str)
        p = list(map(int, sys.stdin.readline().split()))
        s = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        return
 
    if n <= 0 or not p or not s:
        print("NO")
        return
 
    for i in range(1, n):
        if p[i-1] % p[i] != 0:
            print("NO")
            return
 
    for i in range(n - 1):
        if s[i+1] % s[i] != 0:
            print("NO")
            return
    
    if p[n-1] != s[0]:
        print("NO")
        return
    
    if n == 1:
        print("YES")
        return
 
    global_gcd = s[0]
    
    if gcd(p[0], s[1]) != global_gcd:
        print("NO")
        return
        
    if gcd(p[n-2], s[n-1]) != p[n-1]:
        print("NO")
        return
 
    for i in range(1, n - 1):
        if gcd(p[i], s[i]) != global_gcd:
            print("NO")
            return
        
        if gcd(p[i-1] // p[i], s[i] // global_gcd) != 1:
            print("NO")
            return
 
        if gcd(p[i] // global_gcd, s[i+1] // s[i]) != 1:
            print("NO")
            return
 
    print("YES")
 
def main():
    try:
        t_str = sys.stdin.readline()
        if not t_str: return
        t = int(t_str)
        for _ in range(t):
            solve()
    except (IOError, ValueError):
        return
 
if __name__ == "__main__":
    main()
