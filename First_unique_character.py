l=input()
l=l.lower()
d=1

for i in l:
    c=0
    for j in l:
        if i==j and i!=' ':
            c+=1
    if c==1:
        print(i)
        d=1
        break
else:
    print('-1')