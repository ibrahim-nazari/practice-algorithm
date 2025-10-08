

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    dp=[[0]* m for _ in range(n)]
    for i in range(1,n):
        dp[i][0]=1
    for j in range(1,m):
        dp[0][j]=1

    for i in range(1,n):
        for j in range(1,m):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    print(dp[n-1][m-1])