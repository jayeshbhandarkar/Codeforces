t = int(input())
 
for _ in range(t):
    x = input()
    digits_in_x = set(x) 
    for y in range(10):
        if str(y) in digits_in_x:
            print(y)
            break
