a="0125689"
n=int(input())
c=6

if(n>6):
    c=7
    num=11
    an=11
    m=True
    while(n!=c):
        m=True
        an=num
        ans=num
        while(ans!=0):
            r=ans%10
            if str(r) not in a:
                m=False
                break
            ans//=10
        if(m):
            c+=1
        num+=1
    print(an)
else:
    print(a[n])

      

        



