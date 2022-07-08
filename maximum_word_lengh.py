s=input()
x=s.split()
max=0
for i in x:
    c=0
    for j in i:
        c+=1
    if c>max:
        max=c
print(max)        