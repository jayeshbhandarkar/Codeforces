n, k = map(int, input().split())
 
from string import ascii_lowercase
letters = ascii_lowercase[:k]
password = ''
 
for i in range(n):
    password += letters[i % k]
 
print(password)
