
def find_max_value(k,values,weights):
    n=len(values)
    dp =[[0] * (k+1) for _ in range(len(values))]
    for j in range(weights[0],k+1):
        dp[0][j]=weights[0]
    for i in range(1,n):
        for j in range(k+1):
            if weights[i]> j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i],values[i]+ dp[i-1][j-weights[i]])
    return dp[n-1][k]



def main():
    t=int(input())
    for _ in range(t):
        k=int(input())
        values=list(map(int,input.split()))
        weights=list(map(int,input.split()))
        res=find_max_value(k,values,weights)
        print(res)