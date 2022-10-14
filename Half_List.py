t=int(input())
l=list(map(int,input().split()))
l1=l[:t//2-1:-1]
for i in l1:
    print(i,end=' ')
for i in range(t//2,t):
    print(l[i-(t//2)],end=' ')