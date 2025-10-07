from collections import defaultdict, deque

def topological_sort(num_jobs, dependencies, jobs):
    # Step 1: Create the graph and in-degree map
    graph = defaultdict(list)  # Adjacency list
    in_degree = {job: 0 for job in jobs}  # In-degree map

    # Step 2: Build the graph and populate in-degrees
    for j, d in dependencies:
        graph[j].append(d)
        in_degree[d] += 1

    # Step 3: Initialize a queue with nodes having 0 in-degree
    queue = deque([job for job in jobs if in_degree[job] == 0])
    sorted_order = []  # Store the topological order

    # Step 4: Perform Kahn's Algorithm (BFS for Topological Sort)
    while queue:
        current_job = queue.popleft()
        sorted_order.append(current_job)

        for neighbor in graph[current_job]:
            in_degree[neighbor] -= 1  # Decrease the in-degree
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 5: Check if all jobs were processed
    if len(sorted_order) == len(jobs):
        return ",".join(map(str, sorted_order))
    else:
        return "Impossible"

# Input handling
def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = int(input())  # Number of dependencies
        dependencies = [tuple(map(int, input().split())) for _ in range(n)]
        jobs = list(map(int, input().split(',')))  # Job list

        result = topological_sort(n, dependencies, jobs)
        print(result)

# Run the main function to handle input and output
if __name__ == "__main__":
    main()
