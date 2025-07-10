n = input()  
count = 0
for digit in n:
    if digit == '4' or digit == '7':
        count += 1
 
def is_lucky(x):
    for ch in str(x):
        if ch != '4' and ch != '7':
            return False
    return True
 
if is_lucky(count):
    print("YES")
else:
    print("NO")
