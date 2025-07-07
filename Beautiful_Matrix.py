matrix = []
 
for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        if row[j] == 1:
            x, y = i, j
 
moves = abs(x - 2) + abs(y - 2)
print(moves)
