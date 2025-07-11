n = int(input())
heights = list(map(int, input().split()))
 
max_height = max(heights)
max_index = heights.index(max_height)
 
min_height = min(heights)
min_index = n - 1 - heights[::-1].index(min_height)
 
swaps = max_index + (n - 1 - min_index)
 
if min_index < max_index:
    swaps -= 1
 
print(swaps)
