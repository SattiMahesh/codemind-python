n=int(input())
sum=0
pro=1
while n>0:
    r=n%10
    sum=sum+r
    pro=pro*r
    n=n//10
result=pro-sum
print(result)