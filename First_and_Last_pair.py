n=int(input())
a=list(map(int,input().split()))
k=l=[]
for i in range(0,len(a)//2):
    k.append(a[i])
for j in range(len(a)//2,len(a)):
    l.append(a[j])
l=l[::-1]
i=j=0
while i<len(k) or j<len(l):
    if i<len(k):
        print(k[i],end=' ')
        i+=1
    if j<len(l):
        print(l[j],end=' ')
        j+=1
if(n%2!=0):
    print(0)