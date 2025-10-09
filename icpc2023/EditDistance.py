
t=int(input())
for _ in range(t):
    s1=input().strip().lower()
    s2=input().strip().lower()
    n,m=len(s1),len(s2)
    dp=[[0] *(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        dp[i][0]=i
    for j in range(1,m+1):
        dp[0][j]=j
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+ min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
    print(dp[n][m])