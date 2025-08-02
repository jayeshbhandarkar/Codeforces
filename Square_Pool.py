for t in range(int(input())):
  n, s = map(int, input().split())
  count = 0
  
  for i in range(n):
    dx, dy, x, y = map(int, input().split())
    k = (dx * x - dy * y) % s
    
    if k == 0 : count += 1
  print(count)
