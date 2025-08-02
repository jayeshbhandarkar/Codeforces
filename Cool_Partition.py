for s in[*open(0)][2::2]:
  t=c={r:=0}
  for x in s.split():
   t|={x};c|={x}
   if t==c:r+=1;t={0}
  print(r)
