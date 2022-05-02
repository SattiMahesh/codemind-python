n=int(input())
p=1
s=0
while n>0:
    d=n%10
    s=s+d
    p=p*d
    n=n//10
if s==p:
    print('Spy Number')
else:
    print('Not Spy Number')