n=int(input())
l=list(map(int,input().split()))
m=int(input())
for i in range(len(l)):
    if l[i]==m:
        print('True')
        break
else:
    print('False')