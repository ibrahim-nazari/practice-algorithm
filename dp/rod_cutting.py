def rod_cutting(prices, n):
    # Initialize a dp array to store the max revenue for each length
    dp = [0] * (n + 1)

    # Build the dp table from bottom up
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(i):
            max_val = max(max_val, prices[j] + dp[i - j - 1])
        dp[i] = max_val
    print(dp)
    return dp[n]

# Example usage
prices = [1, 5, 8, 9,10,5,11]
n = 7
print(f"Maximum Revenue: {rod_cutting(prices, n)}")
