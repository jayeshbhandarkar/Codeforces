import sys
input_lines = sys.stdin.read().splitlines()[1:]
 
for line in input_lines:
    a, b = sorted(map(int, line.split()))
    
    if b < 3 or a < 2:
        print("NO")
    else:
        print("YES")
