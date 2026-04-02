import heapq
from collections import defaultdict

def solve_dijkstra():
    # Input handling
    try:
        n, e = map(int, input("Enter Nodes and Edges: ").split())
        adj = defaultdict(list)
        
        print(f"Enter {e} edges (u v w):")
        for _ in range(e):
            u, v, w = map(int, input().split())
            adj[u].append((v, w))
            adj[v].append((u, w)) # Remove this if the graph is directed

        source = int(input("Enter Source Node: "))
    except ValueError:
        return "Invalid Input"

    # Dijkstra's Algorithm
    distances = {i: float('inf') for i in range(n)}
    distances[source] = 0
    pq = [(0, source)] # (distance, node)

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        # Skip if we found a better path already
        if curr_dist > distances[curr_node]:
            continue

        for neighbor, weight in adj[curr_node]:
            distance = curr_dist + weight
            
            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    # Output formatting
    print("\nShortest distances from source:")
    for node, dist in sorted(distances.items()):
        print(f"Node {node}: {dist if dist != float('inf') else 'Unreachable'}")

solve_dijkstra()