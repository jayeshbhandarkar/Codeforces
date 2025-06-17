t = int(input())
 
for _ in range(t):
    n = int(input())
    s = input()
    found = False
    
    for i in range(1, n - 1):
        for j in range(i + 1, min(i + 3, n)):  
            a = s[:i]
            b = s[i:j]
            c = s[j:]
            
            if b in (a + c):
                found = True
                break
            
        if found:
            break
        
    print("Yes" if found else "No")
