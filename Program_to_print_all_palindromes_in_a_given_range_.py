m=int(input())
n=int(input())
for i in range(m,n):
    sum=0
    temp=i
    while temp>0:
        r=temp%10
        sum=sum*10+r
        temp=temp//10
    if i==sum:
        print("%d "%i,end='')