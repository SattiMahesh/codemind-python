t=int(input())
a=[]
for i in range(t):
    x=int(input())
    a.append(x)
c=0
n=int(input())
for j in a:
    if j<=n:
        c+=1
    else:
        c+=2
print(c)