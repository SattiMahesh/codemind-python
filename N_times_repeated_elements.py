n=int(input())
l=list(map(int,input().split()))
k=int(input())
h=0
for i in range(n):
    c=0
    for j in range(n):
        if l[i]==l[j]:
            c+=1
    if c==k:
        print(l[i],end=' ')
        l[i]=0
        h+=1
if h==0:
    print('-1')