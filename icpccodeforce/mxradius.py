n, l = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

# Maximum gap between consecutive lanterns
max_gap = max(a[i+1] - a[i] for i in range(n-1))

# Distance to edges
d_start = a[0] - 0
d_end = l - a[-1]

# Minimum radius needed
d = max(max_gap / 2, d_start, d_end)

print(f"{d:.10f}")
