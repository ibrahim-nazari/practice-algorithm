
def study_plan():
    while True:
        # Read T (available hours) and R (number of references)
        T, R = map(int, input().split())
        if T == 0 and R == 0:
            break
        
        references = []
        for _ in range(R):
            # Read time required (C) and problems value (P) for each reference
            C, P = map(int, input().split())
            references.append((C, P))
        
        # Initialize DP array to store maximum problems solved for each time
        dp = [0] * (T + 1)
        
        # Process each reference
        for C, P in references:
            # Update dp array in reverse to prevent using the same reference multiple times
            for j in range(T, C - 1, -1):

                dp[j] = max(dp[j], dp[j - C] + P)
        
        # The result is the maximum number of problems that can be solved in T hours
        print(dp[T])

# Example usage:
# Input:
# 3 2
# 1 5
# 3 8
# 5 3
# 2 5
# 2 5
# 4 9
# 0 0
study_plan()
