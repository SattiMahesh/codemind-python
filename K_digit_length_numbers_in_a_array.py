n,k=map(int,input().split())
s=input()
x=s.split()
s=0
for i in x:
    c=0
    for j in i:
        if j in '0123456789':
            c+=1
    if c==k:
        s+=1
print(s)        