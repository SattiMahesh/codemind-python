t1=int(input())
l1=list(map(int,input().split()))
t2=int(input())
l2=list(map(int,input().split()))
k=int(input())
c=0
for i in range(t1):
    if l1[i]<=k and l2[i]>=k:
        c+=1
print(c)        