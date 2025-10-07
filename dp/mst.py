class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(provinces, routes):
    # Sort routes by budget (ascending)
    routes.sort(key=lambda x: x[2])
    
    # Union-Find to track connected components
    uf = UnionFind(provinces)
    
    mst_cost = 0  # Minimum cost for the MST
    mst_edges = 0  # Count of edges in the MST
    
    for u, v, budget in routes:
        if uf.find(u) != uf.find(v):  # If they are in different sets, add the edge
            uf.union(u, v)
            mst_cost += budget
            mst_edges += 1
            if mst_edges == provinces - 1:  # Stop when MST has P-1 edges
                break
    
    return mst_cost

# Input
def main():
    P, R = map(int, input().split())
    routes = []
    
    total_cost = 0
    for _ in range(R):
        u, v, budget = map(int, input().split())
        routes.append((u, v, budget))
        total_cost += budget

    # Get the MST cost using Kruskal's algorithm
    mst_cost = kruskal(P, routes)
    
    # Amount saved = total cost - MST cost
    savings = total_cost - mst_cost
    print(savings)

# Sample test case
if __name__ == "__main__":
    main()
