import collections
rooms=[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

q=collections.deque()
Rows,Cols=len(rooms),len(rooms[0])
visit=set()
for r in range(Rows):
    for c in range(Cols):
        if rooms[r][c]==0:
            q.append((r,c))
            visit.add((r,c))
def addRoom(r,c):
    if r < 0 or c < 0 or r==Rows or c==Cols or (r,c) in visit or rooms[r][c]== -1:
        return 
    visit.add((r,c))
    q.append((r,c))
    
dist=0
while q:
    for i in range(len(q)):
        r,c =q.popleft()
        rooms[r][c]=dist
        addRoom(r,c+1)
        addRoom(r,c-1)
        addRoom(r+1,c)
        addRoom(r-1,c)
    dist +=1
print(rooms)

