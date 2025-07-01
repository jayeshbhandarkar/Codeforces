def s(n):
    l = [0] * (n + 1)
    for i in range(2, n + 1):
        if l[i] == 0:
            for j in range(i, n + 1, i):
                l[j] = i
 
    p = [0] * (n + 1)
    u = [False] * (n + 1)
    p[1] = 1
    u[1] = True
 
    g = {}
    for i in range(2, n + 1):
        if not u[i]:
            v = l[i]
            if v not in g:
                g[v] = []
            g[v].append(i)
 
    for v in sorted(g.keys(), reverse=True):
        c = g[v]
        a = [x for x in c if not u[x]]
 
        if not a:
            continue
 
        if len(a) == 1:
            e = a[0]
            p[e] = e
            u[e] = True
        else:
            for k in range(len(a)):
                ce = a[k]
                ne = a[(k + 1) % len(a)]
                p[ce] = ne
            for e in a:
                u[e] = True
    
    print(*(p[1:]))
 
t = int(input())
for _ in range(t):
    n = int(input())
    s(n)
