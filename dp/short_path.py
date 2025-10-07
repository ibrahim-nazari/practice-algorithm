import heapq
import math

# Function to calculate the shortest time using Dijkstra's algorithm
def dijkstra(graph, start, target):
    # Priority queue for the minimum time to reach each point
    heap = [(0, start)]  # (current_time, point)
    min_time = {start: 0}
    
    while heap:
        curr_time, curr_point = heapq.heappop(heap)

        # If we've reached the target, return the current time
        if curr_point == target:
            return curr_time
        
        # Visit all neighbors
        for neighbor, (distance, speed_limit) in graph.get(curr_point, {}).items():
            travel_time = distance / speed_limit * 60  # convert to minutes
            new_time = curr_time + travel_time
            
            if neighbor not in min_time or new_time < min_time[neighbor]:
                min_time[neighbor] = new_time
                heapq.heappush(heap, (new_time, neighbor))
    
    # Return infinity if target is not reachable
    return math.inf

# Function to process each test case
def process_test_case(lines, queries):
    # Build the graph from the input
    graph = {}
    for line in lines:
        if "->" in line:
            # Parse the connection
            connection, details = line.split(":")
            point1, point2 = connection.split("->")
            distance, speed_limit = map(float, details.split(","))
            
            # Add the directional route to the graph
            if point1 not in graph:
                graph[point1] = {}
            graph[point1][point2] = (distance, speed_limit)
    
    # Process the queries
    result = []
    for query in queries:
        point1, rest = query.split("->")
        point2, time = rest.split(":")
        time = float(time)

        # Calculate the shortest time from point1 to point2
        shortest_time = dijkstra(graph, point1, point2)

        # If the shortest time is less than or equal to the given time, print Yes
        if shortest_time <= time:
            result.append("Yes")
        else:
            result.append("No")
    
    return result

# Main function to read input and process all test cases
def main():
    N = int(input())  # Number of test cases
    for _ in range(N):
        lines = []
        queries = []
        while True:
            line = input().strip()
            if line == "":
                break
            if "->" in line and ":" in line and "," in line:
                lines.append(line)
            else:
                queries.append(line)

        # Process the test case and print the results
        results = process_test_case(lines, queries)
        print("\n".join(results))
        if _ != N - 1:
            print()  # Print an empty line between test cases

# Sample Input
# 2
# a->b:5,10
# a->c:100,60
# b->c:10,15
# a->b:30
# a->c:60
# 
# a->b:10,10
# a->b:61
#
# Expected Output:
# Yes
# No
# Yes

main()
