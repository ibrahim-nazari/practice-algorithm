
import heapq

def dijkstra(graph,person,N):
    dist=[float("inf")] * (N+1)
    dist[person]=0
    pq=[(0,person)]

    while pq:
        current_dist,p=heapq.heappop(pq)
        if current_dist > dist[p]:
            continue

        for neighbour,w in graph[p]:
            newDist=current_dist + w
            if newDist < dist[neighbour]:
                dist[neighbour]=newDist
                heapq.heappush(pq,(newDist,neighbour))
    return dist

def find_closeness(people,person,N):
    graph=[[] for _ in range(N +1)]
    for A,B,w in people:
        graph[A].append((B,w))
    
    closeness=dijkstra(graph,person,N)
    return closeness

def main():
    N=int(input())
    people=[tuple(map(int,input().split())) for _ in range(N)]
    person=int(input())
    numPsug=int(input())
    suggestion=[int(input()) for _ in range(numPsug)]
    closeness=find_closeness(people,person,N)
    for p in suggestion:
        if closeness[p] == float("inf"):
            print("----")
        else:
         print(closeness[p])

main()