t=int(input())
for i in range(t):
    s=input()
    s1=s[::-1]
    if s==s1:
        print("YES",end=' ')
        if len(s)%2==0:
            print("EVEN")
        else:
            print("ODD")
    else:
        print("NO")

