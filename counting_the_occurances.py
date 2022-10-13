s=input()
ch=input()
c=0
for i in s:
    if i==ch:
        c+=1
if c>0:        
    print(c)    
else:
    print("-1")