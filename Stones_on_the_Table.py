n = int(input())
s = input()
 
removals = 0
for i in range(n - 1):
    if s[i] == s[i + 1]:
        removals += 1
 
print(removals)
