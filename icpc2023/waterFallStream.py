t=int(input())
for _ in range(t):
    source=int(input())
    R,C=map(int,input().split())
    water=[[0.0] * C for _ in range(R)]
    grid=[list(map(int,input().split())) for _ in range(R)]
    water[0][source]=100.0
    for r in range(R-1):
        for c in range(C):
            if water[r][c] ==0:
                continue
            if grid[r+1][c]==0:
                water[r+1][c]=water[r][c]
            else:
                split_amount= water[r][c]/2
                # go left
                lc=c 
                while lc > 0:
                    lc -=1
                    if grid[r][lc]==1:
                        break
                    if grid[r+1][lc]==0:
                        water[r+1][lc]=split_amount
                        break
                # got right
                rc=c  
                while rc<C -1:
                    rc+=1
                    if grid[r][rc]==1:
                        break
                    if grid[r+1][rc]==0:
                        water[r+1][rc]=split_amount
                        break
    print(" ".join(list(map(str,water[R-1]))))

# 1 
# 3 
# 7 7 
# 0 0 0 0 0 0 0 
# 1 0 0 0 0 0 0 
# 0 0 1 1 1 0 0 
# 0 0 0 0 0 0 0 
# 1 1 1 0 0 1 0 
# 0 0 0 0 0 0 1 
# 0 0 0 0 0 0 0 