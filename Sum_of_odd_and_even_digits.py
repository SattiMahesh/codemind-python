n=input()
a=list(map(int,input().split()))
sum=0
add=0
for i in range(0,len(a)):
    if i%2==0:
        sum=sum+a[i]
    else:
        add=add+a[i]
if(sum-add==0):
    print('YES')
else:
    print('NO')
    