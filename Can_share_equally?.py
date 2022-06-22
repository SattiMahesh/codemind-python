a,b=map(int,input().split())
z=a+b*2
if a==0 and b%2==0:
    print('YES')
elif b%2!=0 and a==0:
    print('NO')
elif z%2==0:
    print('YES')
else:
    print('NO')