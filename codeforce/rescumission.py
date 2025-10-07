from collections import deque

def solve():
    # Read input
    N, M = map(int, input().split())
    grid = [list(input().strip()) for _ in range(N)]

    # Locate S, T, and all portals
    portals = []
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'T':
                target = (r, c)
            elif grid[r][c] == 'P':
                portals.append((r, c))

    # BFS setup
    q = deque()
    dist = [[-1] * M for _ in range(N)]
    q.append(start)
    dist[start[0]][start[1]] = 0


    # BFS
    while q:
        r, c = q.popleft()
        d = dist[r][c]
        if (r, c) == target:
            print(d)
            return

        # Normal 4-direction moves
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != '#':
                if dist[nr][nc] == -1:
                    dist[nr][nc] = d + 1
                    q.append((nr, nc))

        # Teleport between portals (once, expand all at zero extra cost)
        if grid[r][c] == 'P':
            for pr, pc in portals:
                if dist[pr][pc] == -1:
                    dist[pr][pc] = d   # same distance (teleport cost = 0)
                    q.appendleft((pr, pc))  # put in front since cost 0

    # If we exit BFS without reaching T
    print(-1)

solve()
