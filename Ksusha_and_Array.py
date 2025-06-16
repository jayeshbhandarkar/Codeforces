import math
from functools import reduce

def find_number(arr):
    gcd_all = reduce(math.gcd, arr)
    if gcd_all in arr:
        return gcd_all
    else:
        return -1

n = int(input())
arr = list(map(int, input().split()))
print(find_number(arr))
