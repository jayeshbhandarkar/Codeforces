import heapq
 
def solve():
    a, b, x, y = map(int, input().split())
 
    if a == b:
        print(0)
        return
 
    if a > b:
        if a % 2 == 0:
            print(-1)
            return
        else: 
            if b == a - 1:
                print(y)
                return
            else: 
                print(-1)
                return
 
    MAX_NODES = 120 
    dist = [float('inf')] * MAX_NODES
    
    pq = [(0, a)]
    dist[a] = 0
 
    while pq:
        current_cost, current_val = heapq.heappop(pq)
 
        if current_cost > dist[current_val]:
            continue
 
        if current_val == b:
            print(current_cost)
            return
 
        next_val_add = current_val + 1
        if next_val_add < MAX_NODES:
            new_cost = current_cost + x
            if new_cost < dist[next_val_add]:
                dist[next_val_add] = new_cost
                heapq.heappush(pq, (new_cost, next_val_add))
 
        next_val_xor = current_val ^ 1
        if 0 <= next_val_xor < MAX_NODES: 
            new_cost = current_cost + y
            if new_cost < dist[next_val_xor]:
                dist[next_val_xor] = new_cost
                heapq.heappush(pq, (new_cost, next_val_xor))
              
    print(-1)
 
t = int(input())
for _ in range(t):
    solve()
