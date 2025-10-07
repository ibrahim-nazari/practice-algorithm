To solve the **Palindrome Partitioning Min Cuts** problem, we need to find the minimum number of cuts required to partition a given string such that each substring is a palindrome. This problem can be efficiently solved using **Dynamic Programming (DP)**.

### Key Insights:

1. **Palindrome Check**: If a substring is a palindrome, no cuts are needed for that substring.
2. **Dynamic Programming Table**:
   - We'll maintain two DP arrays:
     - One to store whether a substring is a palindrome.
     - Another to store the minimum cuts required for partitioning up to a specific index.

### Approach:

1. **Palindrome DP Array**: We'll use a 2D DP array `isPalindrome[i][j]` where `i` is the starting index and `j` is the ending index. This array tells us whether the substring from index `i` to `j` is a palindrome.
2. **Min Cuts DP Array**: We'll use another DP array `minCuts[i]`, where `minCuts[i]` represents the minimum number of cuts required to partition the substring from index `0` to `i`.
3. **Transition**:
   - If `isPalindrome[0][i]` is `True`, it means the whole substring from `0` to `i` is a palindrome, so no cuts are required: `minCuts[i] = 0`.
   - If `isPalindrome[j + 1][i]` is `True` (meaning the substring from `j + 1` to `i` is a palindrome), then we can update `minCuts[i] = min(minCuts[i], minCuts[j] + 1)`.

### Solution Code:

```python
def min_palindrome_cuts(s):
    n = len(s)

    # isPalindrome[i][j] will be True if s[i:j+1] is a palindrome
    isPalindrome = [[False] * n for _ in range(n)]

    # minCuts[i] will hold the minimum cuts required for the substring s[0:i+1]
    minCuts = [0] * n

    for i in range(n):
        minCuts[i] = i  # At worst, every character is a separate palindrome

        for j in range(i + 1):
            # Check if s[j:i] is a palindrome
            if s[j] == s[i] and (i - j <= 1 or isPalindrome[j + 1][i - 1]):
                isPalindrome[j][i] = True
                # If it's a palindrome, then either no cuts needed if j == 0 or we update minCuts
                if j == 0:
                    minCuts[i] = 0
                else:
                    minCuts[i] = min(minCuts[i], minCuts[j - 1] + 1)

    return minCuts[n - 1]

# Input Parsing
def main():
    t = int(input())  # number of test cases

    for _ in range(t):
        s = input().strip()  # non-empty string input
        print(min_palindrome_cuts(s))

# Uncomment the below line to run the program with input from console
# main()
```

### Explanation:

1. **isPalindrome DP Table**:

   - This 2D table keeps track of whether each substring `s[i:j+1]` is a palindrome.
   - We initialize each substring of length 1 (single characters) as a palindrome by default.
   - Then, for substrings of length 2 and more, we check whether the first and last characters are the same and whether the substring between them is a palindrome.

2. **minCuts DP Table**:

   - `minCuts[i]` keeps track of the minimum cuts required for the substring `s[0:i+1]`.
   - If `s[j:i+1]` is a palindrome, we update the minimum cuts using `minCuts[j-1] + 1`.

3. **Time Complexity**:
   - Checking all substrings and updating the `minCuts` array takes \(O(n^2)\) time, where \(n\) is the length of the string.

### Example Walkthrough:

**Input:**

```
1
Noonabbad
```

**Process:**

1. The string is `"Noonabbad"`.
2. We will build the `isPalindrome` table and `minCuts` array:
   - `isPalindrome[0][3]` will be `True` for "Noon" because "Noon" is a palindrome.
   - `isPalindrome[4][7]` will be `True` for "abba" because "abba" is also a palindrome.
   - After calculating the `minCuts`, we find that the minimum number of cuts required is `2` (i.e., "Noon | abba | d").

**Output:**

```
2
```

### Sample Input:

```
1
Noonabbad
```

### Sample Output:

```
2
```

### Edge Cases:

1. **Single character string**: Requires `0` cuts because it’s already a palindrome.
2. **Palindrome string**: No cuts are needed, so the result is `0`.
3. **String with alternating characters**: In the worst case, every character will need a cut.

Let me know if you need further clarification!
