import sys
import heapq
 
def solve():
    n, k = map(int, sys.stdin.readline().split())
    k -= 1
    h = list(map(int, sys.stdin.readline().split()))
 
    max_h = 0
    height_groups = {}
    unique_heights_set = set()
 
    for i in range(n):
        if h[i] > max_h:
            max_h = h[i]
        
        if h[i] not in height_groups:
            height_groups[h[i]] = []
        height_groups[h[i]].append(i)
        unique_heights_set.add(h[i])
 
    if h[k] == max_h:
        print("YES")
        return
 
    dist = {i: float('inf') for i in range(n)}
    pq = [(0, k)]
    dist[k] = 0
    processed_heights = set()
 
    unique_heights = sorted(list(unique_heights_set))
 
    while pq:
        t, u = heapq.heappop(pq)
 
        if t > dist[u]:
            continue
 
        if h[u] == max_h:
            print("YES")
            return
 
        if h[u] not in processed_heights:
            processed_heights.add(h[u])
            for v in height_groups[h[u]]:
                if t < dist[v]:
                    dist[v] = t
                    heapq.heappush(pq, (t, v))
        
        current_h = h[u]
 
        import bisect
        idx_up = bisect.bisect_right(unique_heights, current_h)
        if idx_up < len(unique_heights):
            h_target_up = unique_heights[idx_up]
            if h_target_up <= 2 * current_h - t:
                for v in height_groups[h_target_up]:
                    travel_time = h_target_up - current_h
                    new_time = t + travel_time
                    if new_time < dist[v] and new_time <= h[v] - 1:
                        dist[v] = new_time
                        heapq.heappush(pq, (new_time, v))
        
        idx_down = bisect.bisect_left(unique_heights, current_h)
        if idx_down > 0:
            h_target_down = unique_heights[idx_down - 1]
            
            min_h_down = max(t, (t + current_h + 1) // 2)
 
            if h_target_down >= min_h_down:
                for v in height_groups[h_target_down]:
                    travel_time = current_h - h_target_down
                    new_time = t + travel_time
                    if new_time < dist[v] and new_time <= h[v] - 1:
                        dist[v] = new_time
                        heapq.heappush(pq, (new_time, v))
    
    print("NO")
 
def main():
    try:
        t_str = sys.stdin.readline()
        if not t_str:
            return
        t = int(t_str)
        for _ in range(t):
            solve()
    except (IOError, ValueError) as e:
        pass
 
if __name__ == "__main__":
    main()
