def solve():
    T = int(input().strip())
    ALL = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    for _ in range(T):
        s, k = input().split()
        k = int(k)
        n = len(s)

        if n > 26:
            print("NOPE")
            continue

        S = set(s)
        chosen = []
        chosen_set = set()
        overlap = 0

        for i, ch in enumerate(ALL):
            if len(chosen) == n:
                break

            new_overlap = overlap + (1 if ch in S else 0)
            new_count = len(chosen) + 1
            needed_after = n - new_count

            remaining_total = 0
            remaining_nonS = 0
            for j in range(i + 1, 26):
                cj = ALL[j]
                remaining_total += 1
                if cj not in S:
                    remaining_nonS += 1

            

            extra_overlap_needed = max(0, needed_after - remaining_nonS)
            min_possible_overlap = new_overlap + extra_overlap_needed

            if min_possible_overlap <= k:
                chosen.append(ch)
                chosen_set.add(ch)
                if ch in S:
                    overlap += 1

        if len(chosen) != n:
            print("NOPE")
        else:
            print("".join(chosen))


if __name__ == "__main__":
    solve()
