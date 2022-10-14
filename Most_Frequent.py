t=int(input())
l=list(map(int,input().split()))
max=0
for i in l:
    c=0
    for j in l:
        if i==j:
            c+=1
    if c>max:
        max=c
        ele=i
    elif c==max:
        ele=min(ele,i)
print(ele)        