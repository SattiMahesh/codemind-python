n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,len(a)):
    c=0
    for j in range(0,len(a)):
        if a[i]==a[j]:
            c+=1
    if c==2:
        print(a[i])
        break