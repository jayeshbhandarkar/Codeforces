import sys
lines = sys.stdin.readlines()[1:]
 
for n in lines:
    n = int(n.strip())
    
    result = list(range(2, n + 1))  
    result.append(1)              
 
    print(*result)
