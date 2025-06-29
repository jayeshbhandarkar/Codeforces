t = int(input())
for _ in range(t):
    a, b = input().split()
 
    if a == b:
        print("=")
        
    elif a[-1] == 'M' or b[-1] == 'M':
        if a[-1] == 'M':
            print(">" if b[-1] == 'S' else "<")
            
        else:
            print("<" if a[-1] == 'S' else ">")
            
    elif a[-1] == 'S' and b[-1] == 'S':
        print("<" if len(a) > len(b) else ">")
        
    elif a[-1] == 'L' and b[-1] == 'L':
        print(">" if len(a) > len(b) else "<")
        
    else:
        print("<" if a[-1] == 'S' else ">")
