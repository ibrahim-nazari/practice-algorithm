t=int(input())
for _ in range(t):
    distanceSpeedlimit={}
    query=[]
    while True:
        data=input().split(":")
        if data==['']:
            break
        point1,point2=data[0][0],data[0][-1]
        if len(data[1].split(",")) > 1:
            distance,speedlimit=map(int,data[1].split(","))
            distanceSpeedlimit[(point1,point2)]=(distance,speedlimit)
        else:
            time=int(data[1])
            query.append(((point1,point2),time))
    res=[]
    for key,time in query:
        h=time / 60
        distance,speed=distanceSpeedlimit[key]
        if distance <= speed * h:
            res.append("YES")
        else:
            res.append("NO")
    for rs in res:
        print(rs)


    
        
#  2 
# a->b:5,10 
# a->c:100,60 
# b->c:10,15 
# a->b:30 
# a->c:60 

# a->b:10,10 
# a->b:61 
