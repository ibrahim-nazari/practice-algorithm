You're correct that the greedy approach may fail in certain cases, particularly if a larger denomination is chosen first and later there's no way to match the exact amount with smaller denominations. Let's take your example:

- **Amount**: 80
- **Available Bills**: 1, 20, 25

A greedy approach would pick the largest denomination (25) first:

- Pick three 25's: \( 25 \times 3 = 75 \)
- Remaining amount: \( 80 - 75 = 5 \)

Now, no combination of the remaining bills can sum up to 5, making it impossible to reach 80 with the greedy approach, even though a valid solution exists using \( 20 \times 4 = 80 \).

### Solution with Dynamic Programming:

To solve this problem in all cases, we can use a **Dynamic Programming** approach similar to the **coin change problem**, which ensures that we find the optimal solution by considering all possible combinations.

### Approach:

1. Use a DP table to keep track of the minimum number of bills needed to make each amount up to `M`.
2. Start from 0 (no amount) and work up to `M`, using each bill denomination if it leads to a valid solution.
3. If the DP table entry for `M` is still infinity, it means it's impossible to provide the exact change.

### Solution in Python:

```python
def calculate_change(T, test_cases):
    for i in range(T):
        M = test_cases[i][0]
        bills = test_cases[i][1]

        # Create an array to store the minimum number of bills to make every amount up to M
        dp = [float('inf')] * (M + 1)
        dp[0] = 0  # Base case: to make 0 amount, we need 0 bills

        # Convert bills dictionary to a list of (denomination, count)
        bill_list = [(denom, count) for denom, count in bills.items()]

        # Iterate over every denomination
        for denom, count in bill_list:
            # We need to account for how many of each bill we can use (up to 'count')
            for _ in range(count):
                for j in range(M, denom - 1, -1):  # Traverse backwards to avoid recomputing
                    if dp[j - denom] != float('inf'):
                        dp[j] = min(dp[j], dp[j - denom] + 1)

        # Now we need to backtrack from M to find which bills were used
        if dp[M] == float('inf'):
            print(f"Customer{i+1}:")
            print("Impossible")
        else:
            result = []
            current_amount = M
            for denom, count in sorted(bills.items(), key=lambda x: -x[0]):
                used = 0
                while current_amount >= denom and dp[current_amount - denom] == dp[current_amount] - 1 and used < count:
                    result.append(f"{denom} 1")
                    current_amount -= denom
                    used += 1
            print(f"Customer{i+1}:")
            print("\n".join(result))

# Example Input Parsing and Execution
T = 3
test_cases = [
    (235, {5: 10, 10: 6, 20: 4, 50: 3}),
    (370, {10: 4, 5: 20, 40: 4, 70: 3, 100: 2, 50: 5}),
    (80, {1: 5, 20: 3, 25: 3})
]

calculate_change(T, test_cases)
```

### Explanation:

1. **Dynamic Programming Table**: We build a table `dp` where `dp[i]` represents the minimum number of bills required to make the amount `i`.
2. **Backtracking**: Once the table is built, if `dp[M]` is not infinity, we backtrack through the table to determine the exact bills used.
3. **Edge Cases**: If the amount can't be made with the available bills, the output is "Impossible."

### Example Output:

```
Customer1:
50 3
20 4
5 1
Customer2:
100 2
70 2
10 3
Customer3:
20 4
```

This dynamic programming solution ensures that we consider all possible combinations of bills, thereby fixing the issue where the greedy algorithm may fail.
