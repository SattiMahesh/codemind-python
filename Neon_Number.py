n=int(input())
s=n*n
sum=0
for i in range(len(str(s))):
    r=s%10
    sum=sum+r
    s=s//10
if n==sum:
    print("Neon Number")
else:
    print("Not Neon Number")