import math
 
def count_polycarp_likes(t, test_cases):
    results = []
    for n in test_cases:
        squares = set(i * i for i in range(1, int(n**0.5) + 1))
        cubes = set(i * i * i for i in range(1, int(n**(1/3)) + 2) if i * i * i <= n)
        liked_numbers = squares.union(cubes)
        results.append(len(liked_numbers))
    return results
 
t = int(input())
test_cases = [int(input()) for _ in range(t)]
results = count_polycarp_likes(t, test_cases)
for res in results:
    print(res)
