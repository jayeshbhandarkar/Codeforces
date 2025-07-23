s = input()
i = 0
res = ""
 
while i < len(s):
    if s[i] == '.':
        res += '0'
        i += 1
    elif s[i] == '-':
        if s[i + 1] == '.':
            res += '1'
        else:
            res += '2'
        i += 2
 
print(res)
