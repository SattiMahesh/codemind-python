n=int(input())
s=input()
x=s.split()
for i in x:
    c=0
    for j in i:
        if j in '0123456789':
            c+=1
    print(c,end=' ')    