The **Levenshtein Distance** problem is a classic **dynamic programming** problem that calculates the minimum number of edit operations (insertions, deletions, and substitutions) needed to transform one string into another.

### Problem Overview:

Given two strings `s1` and `s2`, the goal is to find the minimum number of operations required to convert `s1` into `s2`. The three possible operations are:

1. **Insertion**: Insert a character into `s1`.
2. **Deletion**: Remove a character from `s1`.
3. **Substitution**: Replace a character in `s1` with another character from `s2`.

### Approach:

1. **Dynamic Programming Table**: We'll use a 2D DP table `dp[i][j]`, where:

   - `i` is the length of a prefix of `s1`.
   - `j` is the length of a prefix of `s2`.
   - `dp[i][j]` will store the minimum number of edit operations required to convert the first `i` characters of `s1` into the first `j` characters of `s2`.

2. **Recurrence Relation**:

   - If the characters `s1[i-1]` and `s2[j-1]` are the same, no edit is needed: `dp[i][j] = dp[i-1][j-1]`.
   - If the characters are different, we need to consider the three operations:
     1. **Insert** a character: `dp[i][j] = dp[i][j-1] + 1`.
     2. **Delete** a character: `dp[i][j] = dp[i-1][j] + 1`.
     3. **Substitute** a character: `dp[i][j] = dp[i-1][j-1] + 1`.
   - The final result will be `min(insert, delete, substitute)`.

3. **Base Case**:
   - `dp[i][0] = i`: If `s2` is an empty string, we need `i` deletions to transform `s1` into an empty string.
   - `dp[0][j] = j`: If `s1` is an empty string, we need `j` insertions to transform an empty string into `s2`.

### Solution Code:

```python
def levenshtein_distance(s1, s2):
    # Get lengths of both strings
    n = len(s1)
    m = len(s2)

    # Create a 2D dp array of size (n+1) x (m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize base cases
    for i in range(n + 1):
        dp[i][0] = i  # Need i deletions to convert s1[:i] to an empty string
    for j in range(m + 1):
        dp[0][j] = j  # Need j insertions to convert an empty string to s2[:j]

    # Fill the dp array
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                # Characters match, no edit needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Minimum of insertion, deletion, and substitution
                dp[i][j] = min(dp[i][j - 1] + 1,  # Insert
                               dp[i - 1][j] + 1,  # Delete
                               dp[i - 1][j - 1] + 1)  # Substitute

    # The answer is the value in dp[n][m]
    return dp[n][m]

# Input parsing
def main():
    t = int(input())  # number of test cases

    for _ in range(t):
        s1 = input().strip()  # first string
        s2 = input().strip()  # second string
        print(levenshtein_distance(s1, s2))

# Uncomment below to run with user input from the console
# main()
```

### Explanation:

1. **DP Table Initialization**:

   - We initialize the `dp` table to store the minimum edit distance for each prefix of `s1` and `s2`.
   - The base case is that if either string is empty, the number of edits required is the length of the other string.

2. **DP Table Filling**:

   - For each character in `s1` and `s2`, we fill the table by checking if the current characters match.
   - If they match, we carry over the value from `dp[i-1][j-1]` (no edit needed).
   - If they don't match, we consider the three operations (insertion, deletion, substitution) and take the minimum.

3. **Time Complexity**:
   - The time complexity is \(O(n \times m)\), where `n` is the length of `s1` and `m` is the length of `s2`, because we iterate over all pairs of indices.
   - The space complexity is also \(O(n \times m)\) due to the DP table.

### Example Walkthrough:

**Input:**

```
1
Abc
yabd
```

1. **Step 1**: Initialize the DP table for `s1 = "Abc"` and `s2 = "yabd"`.

```
     y a b d
  0  1 2 3 4
A 1
b 2
c 3
```

2. **Step 2**: Fill the table by comparing characters and applying the recurrence relation.

```
     y a b d
  0  1 2 3 4
A 1  1 2 3 4
b 2  2 2 2 3
c 3  3 3 3 3
```

3. **Step 3**: The answer is in `dp[3][4] = 2`, meaning two edits are required:
   - Insert 'y' at the beginning.
   - Substitute 'c' with 'd'.

**Output:**

```
2
```

### Edge Cases:

1. **Identical Strings**: If the two strings are identical, no edits are required, and the result is `0`.
2. **One Empty String**: If one string is empty, the number of edits is equal to the length of the other string (all insertions or deletions).
3. **Different Lengths**: The algorithm handles strings of different lengths efficiently by using dynamic programming.

This solution efficiently computes the minimum edit distance between two strings. Let me know if you'd like more details on any part of it!
