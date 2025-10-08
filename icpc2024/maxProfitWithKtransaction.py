
t=int(input())
def findMaxProfitWithKTransaction(k,prices):
    n=len(prices)
    dp=[[0] *(n) for _ in range(k+1)]
    for t in range(1,k+1):
        maxDiff=-prices[0]
        for d in range(1,n):
            dp[t][d]=max(dp[t][d-1],prices[d]+maxDiff)
            maxDiff=max(maxDiff, dp[t-1][d]-prices[d])
    return dp[k][n-1]

for _ in range(t):
    k=int(input().strip())
    prices=list(map(int,input().strip().split(",")))
    res=findMaxProfitWithKTransaction(k,prices)
    print(res)