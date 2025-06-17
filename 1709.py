import sys
input = sys.stdin.read
 
def solve():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
 
    results = []
 
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        b = list(map(int, data[idx:idx + n]))
        idx += n
 
        operations = []
 
        for i in range(n):
            if a[i] > b[i]:
                a[i], b[i] = b[i], a[i]
                operations.append((3, i + 1))
 
        for i in range(n):
            for j in range(n - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    operations.append((1, j + 1))
 
        for i in range(n):
            for j in range(n - 1):
                if b[j] > b[j + 1]:
                    b[j], b[j + 1] = b[j + 1], b[j]
                    operations.append((2, j + 1))
 
        results.append(f"{len(operations)}")
        for op in operations:
            results.append(f"{op[0]} {op[1]}")
 
    print('\n'.join(results))
 
solve()
