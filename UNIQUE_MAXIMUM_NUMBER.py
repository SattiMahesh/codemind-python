t=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    c=0
    for j in l:
        if i==j:
            c+=1
    if c==1:
        a.append(i)
if len(a)==0:
    print("-1")
else:
    print(max(a))