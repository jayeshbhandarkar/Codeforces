import sys
import heapq
 
def solve():
    n, k = map(int, sys.stdin.readline().split())
    k -= 1
 
    h = list(map(int, sys.stdin.readline().split()))
    max_h = max(h)
 
    if h[k] == max_h:
        print("YES")
        return
 
    sorttower = sorted((val, idx) for idx, val in enumerate(h))
 
    sortedpos = [0] * n
    for i, (_, idx) in enumerate(sorttower):
        sortedpos[idx] = i
 
    min_time = [float('inf')] * n
    pq = []
    min_time[k] = 0
    heapq.heappush(pq, (0, k))
 
    possible = False
 
    while pq:
        time, u_idx = heapq.heappop(pq)
 
        if time > min_time[u_idx]:
            continue
 
        if h[u_idx] == max_h:
            possible = True
            break
 
        current_height = h[u_idx]
        current_pos = sortedpos[u_idx]
 
        l_idx = current_pos - 1
        r_idx = current_pos + 1
 
        neighbors = []
        if l_idx >= 0:
            neighbors.append(sorttower[l_idx][1])
        if r_idx < n:
            neighbors.append(sorttower[r_idx][1])
 
        for v_idx in neighbors:
            cost = abs(h[u_idx] - h[v_idx])
            new_time = time + cost
 
            if h[u_idx] >= new_time and h[v_idx] >= new_time + 1:
                if new_time < min_time[v_idx]:
                    min_time[v_idx] = new_time
                    heapq.heappush(pq, (new_time, v_idx))
 
    print("YES" if possible else "NO")
 
def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()
 
if __name__ == "__main__":
    main()
