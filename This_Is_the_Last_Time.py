import sys
import heapq
 
def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        n, k = map(int, line1.split())
        
        casinos = []
        for _ in range(n):
            l, r, real = map(int, sys.stdin.readline().split())
            casinos.append((l, r, real))
 
    except (IOError, ValueError):
        return
 
    casinos.sort(key=lambda x: x[0])
 
    current_coins = k
    max_coins = k
    pool_pq = []
    casino_idx = 0
 
    while True:
        while casino_idx < n and casinos[casino_idx][0] <= current_coins:
            l, r, real = casinos[casino_idx]
            heapq.heappush(pool_pq, (-real, l, r))
            casino_idx += 1
        
        found_play = False
        while pool_pq:
            neg_real, l, r = heapq.heappop(pool_pq)
            real = -neg_real
            
            if r >= current_coins:
                current_coins = real
                max_coins = max(max_coins, current_coins)
                found_play = True
                break
        
        if not found_play:
            break
 
    print(max_coins)
 
 
def main():
    try:
        t_str = sys.stdin.readline()
        if not t_str:
            return
        t = int(t_str)
        for _ in range(t):
            solve()
    except (IOError, ValueError):
        return
 
if __name__ == "__main__":
    main()
