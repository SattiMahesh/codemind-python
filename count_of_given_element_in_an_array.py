n=int(input())
l=list(map(int,input().split()))
m=int(input())
c=0
for i in range(len(l)):
    if l[i]==m:
        c+=1
print(c)