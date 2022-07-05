n=int(input())
l=list(map(int,input().split()))
b=sum(l)//n
for i in range(len(l)):
    if b==l[i]:
        print('True')
        break
else:
    print('False')