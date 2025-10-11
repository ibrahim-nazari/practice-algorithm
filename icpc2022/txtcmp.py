t=int(input())
for _ in range(t):
    placeholder=0
    n,string=input().strip().split()
    n=int(n)
    mapObject={}
    res=[]
    for i in range(0,len(string),n):
        key=string[i:i+n]
        if key in mapObject:
            res.append(mapObject[key])
        else:
            placeholder +=1
            mapObject[key]=placeholder
            res.append(placeholder)
    print(*res)

