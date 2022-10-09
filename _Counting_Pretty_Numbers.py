t=int(input())
for j in range(t):
    a,b=map(int,input().split())
    count=0
    for i in range(a,b+1):
        c=0
        r=i%10
        if r==2 or r==3 or r==9:
            c+=1
        if c==1:
            count+=1
    print(count)        