import sys
 
def solve():
    n = int(sys.stdin.readline())
 
    if n % 4 == 0:
        sys.stdout.write("Bob\n")
    else:
        sys.stdout.write("Alice\n")
 
t = int(sys.stdin.readline())
for _ in range(t):
    solve()
