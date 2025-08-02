t=int(input())
for _ in range(t):
	n=int(input())
	a=list(map(int,input().split()))
	s=""
	l=0
	r=n-1
	i=0
	while l<=r:
		if i%2==0:
			if a[l]>a[r]:
				s+="L";l+=1
			else:
				s+="R";r-=1
		else:
			if a[l]>a[r]:
				s+="R";r-=1
			else:
				s+="L";l+=1
		i+=1
	print(s)
