from collections import Counter

T = int(input())

for _ in range(T):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    # Initialize frequency map for non-zero elements
    freq = Counter()
    for num in a:
        if num != 0:
            freq[num] += 1

    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            p = int(query[1]) - 1
            v = int(query[2])

            old_val = a[p]
            if old_val != 0:
                freq[old_val] -= 1
                if freq[old_val] == 0:
                    del freq[old_val]

            a[p] = v
            if v != 0:
                freq[v] += 1
        else:  # query type 2
            print(len(freq))
