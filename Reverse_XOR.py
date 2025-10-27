for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print("YES"); 
        continue
    s = bin(n)[2:].rstrip('0')  
    print("YES" if s == s[::-1] and s.count('1') % 2 == 0 else "NO")
