a, b = map(int, input().split())
 
fashion_days = min(a, b)
same_color_days = abs(a - b) // 2
 
print(fashion_days, same_color_days)
