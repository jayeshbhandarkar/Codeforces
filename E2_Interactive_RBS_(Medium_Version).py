import sys
 
pivot = 0  # Previously 'obi'
 
def q1(left, right):
    print(f"? {right - left + 1} {' '.join(str(i) for i in range(left, right + 1))}")
    sys.stdout.flush()
    return int(input())
 
def q2(left, right):
    global pivot
    indices = []
    factor = 1
    for i in range(left, right + 1):
        indices.extend([pivot] * factor)
        indices.extend([i] * factor)
        indices.append(pivot)
        factor *= 2
    print(f"? {len(indices)} {' '.join(str(i) for i in indices)}")
    sys.stdout.flush()
    return int(input())
 
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        global pivot
        pivot = 0
 
        if q1(1, n) == 0:
            pivot = n
        else:
            step = 1
            while step <= n:
                step *= 2
            step //= 2
            while step > 0:
                if pivot + step < n and q1(pivot + step, n) > 0:
                    pivot += step
                step //= 2
 
        result = ""
        i = 1
        while i <= n:
            l = i
            r = min(n, i + 6)
            value = q2(l, r)
            for _ in range(l, r + 1):
                if value % 2:
                    result += ")"
                else:
                    result += "("
                value //= 2
            i += 7
 
        print(f"! {result}")
        sys.stdout.flush()
 
if __name__ == "__main__":
    main()
