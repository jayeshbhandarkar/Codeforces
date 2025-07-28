import math
import heapq
 
class Bag:
    def __init__(self, initial_weight, max_free_step):
        self.initial_weight = initial_weight
        self.max_free_step = max_free_step
 
    def __lt__(self, other):
        if self.max_free_step != other.max_free_step:
            return self.max_free_step < other.max_free_step
        return self.initial_weight < other.initial_weight
 
def solve():
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
 
    bags_info = []
    for weight in a:
        if weight > c:
            max_free_step = -1  
            
        else:
            max_free_step = math.floor(math.log2(c / weight))
        bags_info.append(Bag(weight, max_free_step))
 
    bags_info.sort(key=lambda bag: bag.max_free_step)
    total_cost = 0
    pq = [] 
 
    for bag in bags_info:
        current_weight = bag.initial_weight
        current_max_free_step = bag.max_free_step
 
        heapq.heappush(pq, -current_weight) 
 
        if current_max_free_step < 0 or len(pq) > (current_max_free_step + 1):
            heapq.heappop(pq) 
            total_cost += 1
 
    print(total_cost)
 
t = int(input())
for _ in range(t):
    solve()
  
