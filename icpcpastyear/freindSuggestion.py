from collections import defaultdict
import heapq
n=int(input())
adj=defaultdict(list)
for _ in range(n):
    a,b,w=map(int,input().split())
    adj[a].append((b,w))
    adj[b].append((a,w))

src=int(input())
nquery=int(input())
queries=[int(input()) for _ in range(nquery)]
dist={node:float("inf") for node in adj}
dist[src]=0
pq=[(0,src)]
while pq:
    d,node=heapq.heappop(pq)
    if d> dist[node]:
        continue
    for ne,w in adj.get(node,[]):
        new_dist=d+w
        if new_dist < dist[ne]:
            dist[ne]=new_dist
            heapq.heappush(pq,(new_dist,ne))
for query in queries:
    if query in dist and dist[query] !=float("inf"):
        print(dist[query])
    else:
        print('---')