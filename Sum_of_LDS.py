for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x=n*(n+1) //2
    y=0
    for i in range(n-1):
        if a[i]>a[i+1]:
            y+= (i+1)*(n-i-1)
    print(x+y)
