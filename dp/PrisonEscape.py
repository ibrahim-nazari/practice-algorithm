import heapq
def dijkstra(graph,Ncells,E):
    dist=[float("inf")] * (Ncells +1)
    dist[E]=0
    pq=[(0,E)]
    while pq:
        current_dist,node=heapq.heappop(pq)
        if current_dist > dist[node]:
            continue
        for neighbor, time in graph[node]:
            newDist=current_dist + time
            if newDist < dist[neighbor]:
                dist[neighbor]=newDist
                heapq.heappush(pq,(newDist,neighbor))
    return dist
def prisoner_escape(Ncells,E,T,connections):
    graph=[[] for _ in range(Ncells +1)]

    for A,B, time in connections:
        graph[A].append((B,time))

    exite_distance=dijkstra(graph,Ncells,E)
    prisoner_counts=sum( 1 for d in exite_distance if d <=T)
    return prisoner_counts


def main():
    Ncells=int(input())
    E=int(input())
    T=int(input())
    M=int(input())
    connections=[]
    for _ in range(M):
        A,B,time=map(int,input().split())
        connections.append((A,B,time))
    
    print(prisoner_escape(Ncells,E,T,connections))

main()
