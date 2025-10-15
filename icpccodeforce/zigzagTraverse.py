grid=[
    [1,2,3,4],
    [5,6,7,9],
    [10,11,12,13],
    ]

res=[]
isDown=True
r,c=0,0
height=len(grid)-1
width=len(grid[0])-1
def isOutofBound(r,c,height,width):
    return r < 0 or c < 0 or r > height or c > width
while not isOutofBound(r,c,height,width):
    res.append(grid[r][c])
    if isDown:
        if r==height or c==0:
            isDown=False
            if r==height:
                c+=1
            else:
                r+=1
        else:
            r+=1
            c-=1
    else:
        if r==0 or c==width:
            isDown=True
            if c==width:
                r+=1
            else:
                c+=1
        else:
            r -=1
            c+=1
print(res)
    


