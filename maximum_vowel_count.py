n=input()
n=n.split()
c=0
s=[]
for i in n:
    c=0
    for j in i:
        if j in "aeiouAEIOU":
            c+=1
    s.append(c)
print(max(s))