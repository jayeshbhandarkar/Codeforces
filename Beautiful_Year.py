y = int(input())
 
def has_unique_digits(year):
    return len(set(str(year))) == len(str(year))
 
while True:
    y += 1
    if has_unique_digits(y):
        print(y)
        break
