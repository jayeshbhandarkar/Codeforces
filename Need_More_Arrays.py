import sys
input = sys.stdin.readline
 
t = int(input())
results = []
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    count = 0
    last = None
 
    for x in a:
        if last is None or x > last + 1:
            count += 1
            last = x
 
    results.append(str(count))
 
print("\n".join(results))
