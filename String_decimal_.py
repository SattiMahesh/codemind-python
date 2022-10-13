t=int(input())
for i in range(t):
    s=input()
    l=len(s)
    c=0
    for i in s:
        if i in "0123456789":
            c+=1
    if l==c:
        print("True")
    else:
        print("False")