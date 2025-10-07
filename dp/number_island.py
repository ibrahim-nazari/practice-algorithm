
from collections import deque
def count_number_island(grid):
    visited=set()
    def bfs(r,c):
        visited.add((r,c))
        q=deque()
        q.append((r,c))
        while q:
          row,col=q.popleft()
          directions=[[1,0],[0,1],[-1,0],[0,-1]]
          for dr,dc in directions:
            r,c=row + dr,col +dc
            if (r < len(grid) and c < len(grid[0]) and (r,c) not in visited and grid[r][c]=="1"):
                visited.add((r,c))
                q.append((r,c))

    island=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=="1" and (i,j) not in visited:
                bfs(i,j)
                island +=1
    print("island ---",island)


grid = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"]
]

count_number_island(grid)
 