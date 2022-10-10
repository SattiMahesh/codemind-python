n=int(input())
l=list(map(int,input().split()))
s=sum(l)
r=int(s/n)
if r in l:
    print(True)
else:
    print(False)