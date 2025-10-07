from collections import deque, defaultdict

def topological_sort(num_tasks, prerequisites):
    # Step 1: Create adjacency list and in-degree count
    adj_list = defaultdict(list)
    in_degree = [0] * num_tasks

    for dest, src in prerequisites:
        adj_list[src].append(dest)
        in_degree[dest] += 1

    # Step 2: Add all tasks with in-degree 0 to the queue
    queue = deque([i for i in range(num_tasks) if in_degree[i] == 0])
    topological_order = []

    # Step 3: Process the queue
    while queue:
        node = queue.popleft()
        topological_order.append(node)

        # Decrease the in-degree of neighbors
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Check if topological sort is valid (no cycles)
    if len(topological_order) == num_tasks:
        return topological_order
    else:
        return []  # Cycle detected, no valid task order

# Example usage
num_tasks = 6
prerequisites = [(2, 5), (0, 5), (0, 4), (1, 4), (3, 2), (1, 3)]
print(topological_sort(num_tasks, prerequisites))
