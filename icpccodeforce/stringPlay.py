T = int(input())
for _ in range(T):
    s, k = input().split()
    k = int(k)
    n = len(s)
    
    if n > 26:
        print("NOPE")
        continue
    
    s_set = set(s)
    all_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    remaining = [ch for ch in all_letters if ch not in s_set]
    
    # If we can’t fill required letters
    if len(remaining) + min(k, len(s)) < n:
        print("NOPE")
        continue
    
    # Choose smallest k from s and fill rest from remaining
    chosen = sorted(s)[:min(k, n)] + remaining[:n - min(k, n)]
    chosen.sort()
    print("".join(chosen))