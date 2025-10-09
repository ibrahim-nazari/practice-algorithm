

t=int(input())
for _ in range(t):
    floors=input().strip().split()
    start=floors[0]
    requested=floors[1:]

    direction="up" if  requested[0] > start else "down"
    up=[a for a in requested if a > start]
    down=[a for a in requested if a < start]
    up.sort()
    down.sort(reverse=True)
    result=[]
    if direction=="up":
        result=[start]+up+down
    else:
        result=[start]+down+up
    print(*result)
     
    