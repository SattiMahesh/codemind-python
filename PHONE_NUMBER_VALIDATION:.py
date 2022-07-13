n=int(input())
temp=n
c=0
while temp>0:
    r=temp%10
    c+=1
    temp//=10
r=n%10
if c==10:
    print("Valid")
else:
    print("Invalid")