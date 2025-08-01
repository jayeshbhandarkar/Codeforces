class Tree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 2)
 
    def update(self, idx, delta):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx
 
    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res
 
t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    invA = [0] * n
    invB = [0] * n
 
    BIT = Tree(n)
    for i in range(n-1, -1, -1):
        invA[i] = BIT.query(p[i] - 1)
        BIT.update(p[i], 1)
 
    BIT = Tree(n)
    for i in range(n):
        invB[i] = i - BIT.query(p[i])
        BIT.update(p[i], 1)
 
    deg = [invA[i] + invB[i] for i in range(n)]
    total_inv = sum(deg) // 2
 
    w_sum = 0
    for i in range(n):
        w = (n - 1 - i) - deg[i]
        if w < 0:
            w_sum += w
 
    print(total_inv + w_sum, end=' ')
