t = int(input())
 
for _ in range(t):
    n = int(input())
    s = input()
 
    count = 0
    for i in range(n):
        balance = 0
        pairs = 0
        for j in range(i, n):
            if s[j] == '+':
                balance += 1
            else:
                balance -= 1
                if j > i and s[j - 1] == '-' and s[j] == '-':
                    pairs += 1
 
            if balance <= 0 and (balance % 3 == 0) and (-balance) // 2 <= pairs:
                count += 1
 
    print(count)
