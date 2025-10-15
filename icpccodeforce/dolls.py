s,x=map(int,input().split())
if s==0:
    print(0)
elif x==0:
    print(0)
else:
    count=0
    while s> 0:
        print(s)
        count +=1
        s//=x
    print(count)