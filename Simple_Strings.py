def make_simple_string(s):
    s = list(s)
    n = len(s)
    
    for i in range(1, n):
        if s[i] == s[i - 1]:
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != s[i - 1] and (i + 1 == n or c != s[i + 1]):
                    s[i] = c
                    break
    return ''.join(s)
 
s = input()
print(make_simple_string(s))
