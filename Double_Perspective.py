import sys
 
parent = []
sz = []
edges_count = []
 
def make_set(v):
    global parent, sz, edges_count
    parent[v] = v
    sz[v] = 1
    edges_count[v] = 0
 
def find_set(v):
    if v == parent[v]:
        return v
    parent[v] = find_set(parent[v])
    return parent[v]
 
def union_sets(a, b):
    a = find_set(a)
    b = find_set(b)
    if a != b:
        if sz[a] < sz[b]:
            a, b = b, a
        parent[b] = a
        sz[a] += sz[b]
        edges_count[a] += edges_count[b]
        return a
    return a 
 
def solve():
    n = int(sys.stdin.readline())
    pairs = []
    max_coord_val = 0
    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        pairs.append((a, b, i + 1))
        max_coord_val = max(max_coord_val, b)
 
    pairs.sort(key=lambda x: (x[1] - x[0], x[0], x[1]), reverse=True) 
 
    global parent, sz, edges_count
    parent = [0] * (max_coord_val + 1)
    sz = [0] * (max_coord_val + 1)
    edges_count = [0] * (max_coord_val + 1)
    
    for i in range(1, max_coord_val + 1):
        make_set(i)
    
    covered_points_global = [False] * (max_coord_val + 1)
    
    current_selected_indices = []
    
    best_overall_score = 0
    best_selected_indices = []
 
    for a, b, original_idx in pairs:
        f_gain = 0
        for x in range(a, b):
            if not covered_points_global[x]:
                f_gain += 1
 
        root_a = find_set(a)
        root_b = find_set(b)
        
        g_cost = 0 
        
        if root_a == root_b:
            if edges_count[root_a] == sz[root_a] - 1:
                g_cost = sz[root_a]
        else:
            old_g_contribution_sum = 0
            if edges_count[root_a] >= sz[root_a]:
                old_g_contribution_sum += sz[root_a]
            if edges_count[root_b] >= sz[root_b]:
                old_g_contribution_sum += sz[root_b]
            
            potential_new_size = sz[root_a] + sz[root_b]
            potential_new_edges = edges_count[root_a] + edges_count[root_b] + 1
            
            new_g_contribution_sum = 0
            if potential_new_edges >= potential_new_size:
                new_g_contribution_sum = potential_new_size
            
            g_cost = new_g_contribution_sum - old_g_contribution_sum
        
        if f_gain - g_cost > 0:
            current_selected_indices.append(original_idx)
            
            for x in range(a, b):
                covered_points_global[x] = True
            
            if root_a == root_b:
                edges_count[root_a] += 1
            else:
                new_root = union_sets(a, b)
                edges_count[new_root] += 1 
 
    final_f = 0
    for x in range(1, max_coord_val):
        if covered_points_global[x]:
            final_f += 1
 
    final_g = 0
    visited_roots = set()
    for v in range(1, max_coord_val + 1):
        root_v = find_set(v)
        if root_v not in visited_roots:
            visited_roots.add(root_v)
            if edges_count[root_v] >= sz[root_v]:
                final_g += sz[root_v]
 
    actual_overall_score = final_f - final_g
    
    if actual_overall_score > best_overall_score:
        best_overall_score = actual_overall_score
        best_selected_indices = current_selected_indices
    
    if best_overall_score < 0:
        best_overall_score = 0
        best_selected_indices = []
 
    sys.stdout.write(str(len(best_selected_indices)) + '\n')
    sys.stdout.write(' '.join(map(str, best_selected_indices)) + '\n')
 
num_test_cases = int(sys.stdin.readline())
for _ in range(num_test_cases):
    solve()
