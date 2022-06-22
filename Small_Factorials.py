n=int(input())
for i in range(1,n+1):
    a=int(input())
    p=1
    for a in range(a,0,-1):
        p=p*a
    print(p)