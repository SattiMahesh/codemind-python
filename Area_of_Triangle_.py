a,b,c=map(float,input().split())
s=(a+b+c)/2
g=(s*(s-a)*(s-b)*(s-c))**0.5
print("%.2f"%g)