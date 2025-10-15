import math

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Generate primes up to 10^6 using Sieve of Eratosthenes
MAX = 10**6
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX + 1, i):
            is_prime[j] = False

# Precompute all T-primes (squares of primes)
t_primes = set(i*i for i in range(2, MAX + 1) if is_prime[i])

# Check each number
for x in arr:
    print("YES" if x in t_primes else "NO")
