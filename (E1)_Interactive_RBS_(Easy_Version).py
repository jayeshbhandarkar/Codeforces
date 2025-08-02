def solve():
    a = int(input())
    l, r = 1, a
    while r >= l:
        m = (l + r) // 2
        print("?", m, end=" ")
        print(" ".join(str(i) for i in range(1, m + 1)))
        y = int(input())
        if y == 0:
            l = m + 1
        else:
            r = m - 1
 
    b = l
    if b == a + 1:
        b = 1
 
    s = ""
    for i in range(1, a, 2):
        print("?", 12, end=" ")
        for _ in range(3):
            print(i, b, b, end=" ")
        print(i + 1, b, b)
        y = int(input())
        if y == 4:
            s += "(("
        elif y == 3:
            s += "()"
        elif y == 1:
            s += ")("
        else:
            s += "))"
 
    if a % 2 == 1:
        print("?", 2, a, b)
        y = int(input())
        if y:
            s += "("
        else:
            s += ")"
 
    print("!", s)
 
def main():
    t = int(input())
    for _ in range(t):
        solve()
 
if __name__ == "__main__":
    main()
