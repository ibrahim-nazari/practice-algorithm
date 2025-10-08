t=int(input())
for _ in range(t):
    n=int(input())
    cups=[list(map(int,input().split(","))) for _ in range(n)]
    low=int(input())
    high=int(input())
    def dfs(low,high,memo={}):
        if low <=0 and high <=0:
            return False
        if (low,high) in memo:
            return memo[(low,high)]
         
        for l,h in cups:
            if low <=l and h <=high:
                return True
            if dfs(low-l,high-h,memo):
                return True
        memo[(low,high)]=False
        return memo[(low,high)]

    res= dfs(low,high)
    print(res)