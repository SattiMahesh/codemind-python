n=int(input())
for i in range(0,n):
    m=int(input())
    k=m
    s=0
    while m>0:
        r=m%10
        s=s*10+r
        m=m//10
    if(s==k):
        print('True')
    else:
        print('False')
    