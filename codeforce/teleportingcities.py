# Dijkstra with road edges and zero-cost directed teleport edges
 
import heapq

def main():
    N,M,K=list(map(int,input().split()))
    adj = [[] for _ in range(N+1)]  # 1-indexed

    # Read M undirected roads: u v t
    for _ in range(M):
        u,v,t=list(map(int,input().split()))
        adj[u].append((v, t))
        adj[v].append((u, t))

    # Read K directed teleport portals u -> v with cost 0
    for _ in range(K):
        u,v=map(int,input().split())
        adj[u].append((v, 0))

    INF = 10**30
    dist = [INF] * (N+1)
    dist[1] = 0
    pq = [(0, 1)]  # (distance, node)
 
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    ans = dist[N]
    if ans >= INF:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    main()
