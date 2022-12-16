n=int(input())
a=list(map(int,input().split()))
k=[]
for i in a:
    k.append(len(str(i)))
k=max(k)
m=[]
for i in a:
    if len(str(i))==k:
        m.append(i)
l=sorted(m)
print(*l)
        