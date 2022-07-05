n=int(input())
l=list(map(int,input().split()))
sum=0
j=n-1
for i in range(len(l)):
    if j>=0:
        sum=sum+(l[i]*(2**j))
        j-=1
print(sum)