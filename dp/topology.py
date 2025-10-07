def num_binary_tree_topologies(n):
    # Array to store number of topologies for each N
    dp = [0] * (n + 1)
    dp[0] = 1  # There's one topology with 0 nodes (empty tree)

    for nodes in range(1, n + 1):
        total_trees = 0
        for left_subtree in range(nodes):
            right_subtree = nodes - 1 - left_subtree
            total_trees += dp[left_subtree] * dp[right_subtree]
        dp[nodes] = total_trees

    return dp

# Input handling
t = int(input())  # Number of test cases
test_cases = [int(input()) for _ in range(t)]

# Precompute topologies for all N up to the largest test case input
max_n = max(test_cases)
topology_counts = num_binary_tree_topologies(max_n)

# Output results for each test case
for n in test_cases:
    print(topology_counts[n])