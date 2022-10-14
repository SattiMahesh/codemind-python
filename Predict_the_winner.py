t=int(input())
l=list(map(int,input().split()))
x=0
y=0
for i in range(t):
    if i%2==0 or i==0:
        y+=l[i]
    else:
        x+=l[i]
if (abs(x-y)%4)==0:
    print("X")
else:
    print("Y")