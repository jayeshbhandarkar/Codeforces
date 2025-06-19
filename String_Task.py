s = input().lower()
vowels = {'a', 'o', 'y', 'e', 'u', 'i'}
 
result = ""
for ch in s:
    if ch not in vowels:
        result += "." + ch
 
print(result)
