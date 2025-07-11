import math
 
n, m, a = map(int, input().split())
tiles_along_length = math.ceil(n / a)
tiles_along_width = math.ceil(m / a)
 
total_tiles = tiles_along_length * tiles_along_width
print(total_tiles)
