def fib(n):
    a,b=0,1
    i=3
    while True:
        c=a+b
        a,b=b,c
        if b>n and (b-n)>(n-a):
            print(a)
            break
        if b>n and (b-n)<(n-a):
            print(b)
            break
        elif b>n:
            print(a,c)
            break
    i+=1
n=int(input())
fib(n)
        