n=int(input())
l=list(map(int,input().split()))
b=sum(l)//n
c=0
for i in range(n):
    if l[i]<=b:
        c+=1
print(c)