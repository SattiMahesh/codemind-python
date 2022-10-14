t=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    c=0
    if i==1:
        s+=i
    for j in range(1,i//2+1):
        if j*j==i and i//j==j:
            if i%j==0:
                c+=1
    if c==1:
        s+=i
print(s)        