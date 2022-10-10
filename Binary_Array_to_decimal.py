t=int(input())
l=list(map(int,input().split()))
l1=l[::-1]
s=0
for i in range(t):
    a=2**i
    r=l1[i]*a
    s=s+r
print(s)    