n, k = map(int, input().split())
max_joy = -float('inf')
 
for _ in range(n):
    f, t = map(int, input().split())
    if t <= k:
        joy = f
    else:
        joy = f - (t - k)
    max_joy = max(max_joy, joy)
 
print(max_joy)
