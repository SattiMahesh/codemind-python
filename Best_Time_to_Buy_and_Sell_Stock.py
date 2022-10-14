n=int(input())
l=list(map(int,input().split()))
max=0
for i in range(n):
    for j in range(i+1,n):
        if l[j]-l[i]>max:
            max=l[j]-l[i]
print(max)            
        