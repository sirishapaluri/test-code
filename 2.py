
a,b=list(map(str,input().split(",")))
last=b[-2]
c=0
for i in a:
    if(i==last and i!='"'):
        c+=1
print(c)