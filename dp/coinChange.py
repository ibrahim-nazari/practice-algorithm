
def find_min_coin(amount,coins):

    dp=[amount+1] * (amount +1)
    dp[0]=0
    for i in range(amount +1):
        for coin in coins:
            if i - coin>=0:
                dp[i]=min(dp[i],1 + dp[i-coin])
    return dp[amount] if dp[amount] !=amount +1 else -1


def main():
    amount=int(input())
    coins=list(map(int,input().split(",")))
    res=find_min_coin(amount,coins)
    print(res)


if __name__=="__main__":
    main()