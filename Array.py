n = int(input())
arr = list(map(int, input().split()))

neg = []
pos = []
zero = []

for num in arr:
    if num < 0:
        neg.append(num)
    elif num > 0:
        pos.append(num)
    else:
        zero.append(num)

set1 = [neg.pop()]

if len(pos) >= 1:
    set2 = pos
else:
    set2 = [neg.pop(), neg.pop()]

set3 = neg + zero

print(len(set1), *set1)
print(len(set2), *set2)
print(len(set3), *set3)
