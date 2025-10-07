from collections import defaultdict, deque

def airport_connections(airports, routes, starting_airport):
    # Step 1: Build the graph (adjacency list) from routes.
    graph = defaultdict(list)
    for route in routes:
        src, dest = route.split(",")
        graph[src].append(dest)

    # Step 2: Find all airports reachable from the starting airport using DFS.
    def dfs(airport, visited):
        stack = [airport]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)

    # Set of all airports reachable from the starting airport.
    reachable_from_start = set()
    dfs(starting_airport, reachable_from_start)

    # Step 3: Find all disconnected components (airports not reachable from start).
    unreachable_airports = set(airports) - reachable_from_start

    # Step 4: Group unreachable airports into their own components using DFS.
    def get_component(airport, visited):
        component = set()
        stack = [airport]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                component.add(current)
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return component

    visited = set(reachable_from_start)  # Start with the already visited airports.
    components = []  # Store all unreachable components.

    for airport in unreachable_airports:
        if airport not in visited:
            component = get_component(airport, visited)
            components.append(component)

    # Step 5: Sort components by size in descending order to minimize connections.
    components.sort(key=lambda x: -len(x))

    # Step 6: Add the minimum number of connections to cover all components.
    connections_needed = 0
    for component in components:
        # If the component is not reachable, we need one new connection to connect it.
        if component.isdisjoint(reachable_from_start):
            connections_needed += 1
            reachable_from_start.update(component)  # Simulate adding a new connection.

    return connections_needed

# Sample input
airports = [
    "BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND",
    "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"
]
routes = [
    "DSM,ORD", "ORD,BGI", "BGI,LGA", "SIN,CDG", "CDG,SIN", "CDG,BUD",
    "DEL,DOH", "DEL,CDG", "TLV,DEL", "EWR,HND", "HND,ICN", "HND,JFK",
    "ICN,JFK", "JFK,LGA", "EYW,LHR", "LHR,SFO", "SFO,SAN", "SFO,DSM", "SAN,EYW"
]
starting_airport = "LGA"

# Call the function and print the output
print(airport_connections(airports, routes, starting_airport))



"""
1
BGI,CDG,DEL,DOH,DSM,EWR,EYW,HND,ICN,JFK,LGA,LHR,ORD,SAN,SFO,SIN,TLV,BUD
19
DSM,ORD
ORD,BGI
BGI,LGA
SIN,CDG
CDG,SIN
CDG,BUD
DEL,DOH
DEL,CDG
TLV,DEL
EWR,HND
HND,ICN
HND,JFK
ICN,JFK
JFK,LGA
EYW,LHR
LHR,SFO
SFO,SAN
SFO,DSM
SAN,EYW
LGA


"""