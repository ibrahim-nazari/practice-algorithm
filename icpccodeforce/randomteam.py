# Read input values
n, m = map(int, input().split())

# Minimum number of friend pairs
a = n // m
r = n % m
kmin = r * (a + 1) * a // 2 + (m - r) * a * (a - 1) // 2

# Maximum number of friend pairs
kmax = (n - m + 1) * (n - m) // 2

# Output the results
print(kmin, kmax)
