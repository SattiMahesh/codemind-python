n=int(input())
while (n//10 !=0):
    s=0
    while n>0:
        r=n%10
        s=s+r
        n=n//10
    n=s
print(s)
    