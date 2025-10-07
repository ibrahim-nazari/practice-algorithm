import heapq

def prim_minimum_spanning_tree(provinces, routes):
    # Create adjacency list representation of the graph
    adj = {i: [] for i in range(provinces)}
    total_budget = 0  # To keep track of the total budget
    for route in routes:
        src, dest, cost = route
        adj[src].append((cost, dest))
        adj[dest].append((cost, src))
        total_budget += cost

    # Prim's algorithm to find the MST cost
    mst_cost = 0
    min_heap = [(0, 0)]  # (cost, starting province)
    visited = [False] * provinces
    edges_used = 0

    while edges_used < provinces:
        cost, province = heapq.heappop(min_heap)

        if visited[province]:
            continue

        # Mark the province as visited and add the cost
        visited[province] = True
        mst_cost += cost
        edges_used += 1

        # Add all neighboring unvisited provinces to the heap
        for next_cost, neighbor in adj[province]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (next_cost, neighbor))

    # The amount saved is the difference between the total budget and the MST cost
    money_saved = total_budget - mst_cost
    return money_saved

# Input parsing
def main():
    P, R = map(int, input().split())
    routes = [tuple(map(int, input().split())) for _ in range(R)]
    
    # Calculate money saved
    result = prim_minimum_spanning_tree(P, routes)
    
    print(result)

# Sample Input
# 3 3
# 0 2 2
# 0 1 4
# 1 2 1
# Expected Output: 4
main()
