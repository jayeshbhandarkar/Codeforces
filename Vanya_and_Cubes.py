n = int(input())
level = 0
used = 0
 
while True:
    level += 1
    required = level * (level + 1) // 2
    if used + required > n:
        break
    used += required
 
print(level - 1)
