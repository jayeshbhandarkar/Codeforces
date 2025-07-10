n = int(input())
count = 0
 
for _ in range(n):
    opinions = list(map(int, input().split()))
    if sum(opinions) >= 2:
        count += 1
 
print(count)
