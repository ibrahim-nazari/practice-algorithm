

n=int(input())
grid=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]* n for _ in range(n)]
for j in range(n):
    dp[0][j]=grid[0][j]
for i in range(1,n):
    for j in range(n):
        leftDiagnol= dp[i-1][j-1] if j-1 >=0 else 0
        rightDiagnol= dp[i-1][j+1] if j+1 < n else 0
        dp[i][j]=max(leftDiagnol,rightDiagnol)+grid[i][j]
print(max(dp[n-1]))



# 4  
# 5   6   1   7  
# -2   10   8   -1  
# 3   -7   -9   11  
# 12   -4   2   6 