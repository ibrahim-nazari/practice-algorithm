def can_measure_exactly(test_cases):
    results = []
    
    for case in test_cases:
        cups, low, high = case

        # Step 1: Initialize a DP array where dp[i] tells whether we can measure exactly 'i' ml
        max_volume = high + 1  # We only care up to 'high'
        dp = [False] * (max_volume)
        dp[0] = True  # We can always measure 0 ml

        # Step 2: Process each cup and update the dp array
        for l, h in cups:
            new_dp = dp[:]  # Use a copy of dp to avoid overwriting in the same iteration

            for i in range(max_volume):
                if dp[i]:
                    # Mark new ranges that can be achieved by adding this cup
                    if i + l < max_volume:
                        new_dp[i + l] = True
                    if i + h < max_volume:
                        new_dp[i + h] = True

            dp = new_dp  # Update dp with new possibilities

        # Step 3: Check if any volume between 'low' and 'high' is achievable
        print("dp[low:high + 1]",dp[low:high + 1])
        can_measure = any(dp[low:high + 1])
        results.append(can_measure)

    return results

# Read input
test_cases = []
num_cases = int(input())
for _ in range(num_cases):
    n = int(input())
    cups = [tuple(map(int, input().split(','))) for _ in range(n)]
    low = int(input())
    high = int(input())
    test_cases.append((cups, low, high))

# Get results for each test case and print them
results = can_measure_exactly(test_cases)
for result in results:
    print(result)
