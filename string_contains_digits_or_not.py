t=int(input())
for i in range(t):
    s=input()
    c=0
    for j in s:
        if j in '0123456789':
            c+=1
    if c>=1:
        print("Yes")
    else:
        print("No")