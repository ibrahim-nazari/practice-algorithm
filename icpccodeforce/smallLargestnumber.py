m, s = map(int, input().split())

# Impossible cases
if (s == 0 and m > 1) or s > 9 * m:
    print("-1 -1")
    exit()
if s == 0 and m == 1:
    print("0 0")
    exit()

# Build maximum
sum_ = s
max_num = ''
for _ in range(m):
    d = min(9, sum_)
    max_num += str(d)
    sum_ -= d

# Build minimum
sum_ = s
min_num = ''
for i in range(m):
    for d in range(0 if i else 1, 10):
        if sum_ - d <= 9 * (m - i - 1) and sum_ - d >= 0:
            min_num += str(d)
            sum_ -= d
            break

print(min_num, max_num)
