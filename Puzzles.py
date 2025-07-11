n, m = map(int, input().split())
puzzles = list(map(int, input().split()))
 
puzzles.sort()
min_diff = float('inf')
 
for i in range(m - n + 1):
    diff = puzzles[i + n - 1] - puzzles[i]
    min_diff = min(min_diff, diff)
 
print(min_diff)
