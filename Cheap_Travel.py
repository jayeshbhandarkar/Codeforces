n, m, a, b = map(int, input().split())
option1 = n * a
 
option2 = ((n + m - 1) // m) * b
option3 = (n // m) * b + (n % m) * a
 
print(min(option1, option2, option3))
