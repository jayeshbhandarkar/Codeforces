s = input()
stack = []
moves = 0
 
for c in s:
    if stack and stack[-1] == c:
        stack.pop()
        moves += 1
    else:
        stack.append(c)
 
print("Yes" if moves % 2 == 1 else "No")
