import math
t=int(input())
def calcScore(cordinate,r):
    x,y=cordinate
    d= math.sqrt(x**2 + y**2)
    if d==r:
       d=0
    if d > r:
        d=-1
    return d


def findScore(cordinates):
    scores=[]
    for f,s in cordinates:
        r=5
        firstScore=calcScore(f,r)
        secondScore=calcScore(s,r)
        total=firstScore+secondScore
        format=None
      
        if total==int(total):
            format=f"{total:.1f}"
        else:
            format=f"{total:.5f}"
        scores.append(format) 
    return scores
        
for _ in range(t):
    n=int(input())
    cordinates=[]
    for i in range(n):
        first=list(map(int,input().split(",")))
        second=list(map(int,input().split(",")))
        cordinates.append([first,second])
    res=findScore(cordinates)
    for rs in res:
        print(rs)
# 1 
# 3 
# 1,2 
# 3,2 
# 7,1 
# 1,3 
# 0,3 
# 0,0 