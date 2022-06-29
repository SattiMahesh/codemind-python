n=int(input())
l=list(map(int,input().split()))
s=0
s1=0
for i in range(n):
    if l[i]%2==0:
        s+=l[i]
    else:
        s1+=l[i]
if s1>s:
    print(s1-s)
else:
    print(s-s1)