
t=int(input())
for _ in range(t):
    time,n=map(int,input().split())
    weightValue=[list(map(int,input().split())) for _ in range(n)]
    dp=[[0]* (time+1) for _ in range(n)]
    for j in range(weightValue[0][0],time+1):
        dp[0][j]=weightValue[0][1]
    for i in range(1,n):
        for j in range(time+1):
            val=weightValue[i][1]
            wei=weightValue[i][0]
            if wei <=j:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-wei]+val)
            else:
                dp[i][j]=dp[i-1][j]
    print(dp[n-1][time])
# 2
# 3 2 
# 1 5 
# 3 8 
# 5 3 
# 2 5 
# 2 5 
# 4 9 
# 0 0 