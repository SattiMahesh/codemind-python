n=int(input())
a,b,c=1,1,2
if n==0:
    print("1")
elif n<=2:
    print(n)
else:
    for i in range(3,n+1):
        r=a+b+c;
        a=b
        b=c
        c=r
    print(r)