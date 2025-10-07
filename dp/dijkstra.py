
import heapq

class Graph:

    def __init__(self,v) -> None:
        self.v=v
        self.adj=[[] for _ in range(v)]
       
    def addEdge(self, u,v,w):
        self.adj[v].append((u,w))
        self.adj[u].append((v,w))
    
    def shortestPath(self,src):
        
        pq=[]
        heapq.heappush(pq,(0,src))
        dist= [float("inf")] * self.v
        dist[src]=0

        while pq:
            d,u=heapq.heappop(pq)
            

            for v,weight in self.adj[u]:
                if dist[v] > weight + dist[u]:
                    dist[v]=weight + dist[u]
                    heapq.heappush(pq,(dist[v],v))
        for i in range(self.v):
            print(f" {i} \t\t {dist[i]}")



# Driver's code
if __name__ == "__main__":
    # create the graph given in above figure
    V = 9
    g = Graph(V)

    # making above shown graph
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)

    g.shortestPath(0)