import heapq
from collections import defaultdict

def solve_single_test():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    max_heap = []
    for val in b:
        heapq.heappush(max_heap, -val)
    
    freq_map = defaultdict(int)
    for num in a:
        freq_map[num] += 1
    
    F = True

    for _ in range(n - m + n):
        if not max_heap:
            F = False
            break
        
        x = -heapq.heappop(max_heap)
        if freq_map[x] == 0:
            heapq.heappush(max_heap, -(x // 2))
            heapq.heappush(max_heap, -((x + 1) // 2))
        else:
            freq_map[x] -= 1

    if F and not max_heap:
        print("Yes")
    else:
        print("No")

def main():
    t = int(input())
    for _ in range(t):
        solve_single_test()

if __name__ == "__main__":
    main()