The problem "Number Of Ways To Traverse Graph" is a classic combinatorial problem where you are given a grid, and you need to determine how many different ways you can traverse the grid from the top-left corner to the bottom-right corner, moving only to the right or down at each step.

### Problem Breakdown:

- The grid has a **width** `W` and a **height** `H`.
- You can only move **right** or **down**.
- You need to find how many distinct paths can be taken to traverse from the top-left to the bottom-right.

### Key Observations:

1. **Total Number of Steps**:

   - To go from the top-left corner to the bottom-right corner, you need to make exactly `W-1` moves to the right and `H-1` moves downward.
   - This is because you start at `(0, 0)` and want to reach `(H-1, W-1)`.

2. **Combinatorics Approach**:
   - The problem is equivalent to selecting positions for either right or down moves in a total of `(W-1) + (H-1)` steps. This is a combinatorial problem where you need to choose either `W-1` positions for right moves (and the rest will be down moves), or `H-1` positions for down moves.
3. **Formula**:
   - The number of ways to do this is given by **binomial coefficient**:
     \[
     C(W + H - 2, W - 1) = \frac{(W + H - 2)!}{(W - 1)!(H - 1)!}
     \]
   - This is because you are choosing `(W-1)` positions for right moves out of `(W-1) + (H-1)` total steps, or equivalently `(H-1)` positions for down moves.

### Solution Outline:

1. **Input Parsing**:

   - We read multiple test cases, where each test case gives the width and height of the grid.

2. **Mathematical Calculation**:
   - For each test case, calculate the number of ways to traverse the grid using the binomial coefficient formula.
3. **Efficiency**:
   - We need to handle large inputs where the width and height can go up to `105`, which requires efficient computation of factorials and combinations. Using an iterative approach for factorial computation and Python’s built-in arbitrary precision arithmetic can help.

### Python Code:

```python
import math

# Function to compute the number of ways using the binomial coefficient
def number_of_ways(width, height):
    # Calculate the binomial coefficient C(W + H - 2, W - 1)
    total_steps = (width - 1) + (height - 1)
    right_moves = width - 1
    # C(total_steps, right_moves) = total_steps! / (right_moves! * (total_steps - right_moves)!)
    return math.comb(total_steps, right_moves)

# Main function to process the test cases
def main():
    # Read number of test cases
    t = int(input().strip())

    # Iterate over each test case
    for _ in range(t):
        # Read width and height
        w, h = map(int, input().split())

        # Output the result for each test case
        print(number_of_ways(w, h))

# Uncomment the following line to run the program
# main()
```

### Explanation:

1. **`number_of_ways` function**:

   - This function computes the number of ways to traverse the grid using the binomial coefficient formula. We calculate the binomial coefficient using Python's `math.comb` function, which efficiently computes combinations.

2. **`main` function**:
   - We first read the number of test cases.
   - For each test case, we read the width (`W`) and height (`H`) of the grid and calculate the number of ways using the `number_of_ways` function.
   - The result is printed for each test case.

### Time Complexity:

- **Factorial Computation**: Python’s `math.comb` function computes combinations in an efficient manner, so the time complexity per test case is approximately \(O(\min(W, H))\) due to the nature of combination calculations.

### Example Walkthrough:

**Input:**

```
1
4 3
```

**Explanation**:

- You have a grid with width `4` and height `3`, meaning you need to make `3` moves to the right and `2` moves downward.
- The total number of moves is `3 + 2 = 5`, and you need to choose `3` positions for right moves. This is given by the binomial coefficient:
  \[
  C(5, 3) = \frac{5!}{3!(5-3)!} = \frac{5 \times 4}{2 \times 1} = 10
  \]

**Output:**

```
10
```

### Additional Example:

**Input:**

```
2
4 3
2 2
```

**Output:**

```
10
2
```

### Conclusion:

This approach uses combinatorics to efficiently calculate the number of ways to traverse the grid from the top-left to the bottom-right corner, given the constraints. The time complexity is reduced by using Python's built-in functions for combination calculations, making it suitable for large inputs up to the constraints \( W, H \leq 10^5 \).
