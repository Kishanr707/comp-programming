import sys

def read_input_interactive():
    print("--- Graph Data Entry ---")
    try:
        # Prompt for number of nodes and edges
        line = input("Enter number of nodes (n) and edges (m) separated by space: ").split()
        if not line:
            return 0, 0, []
        
        n = int(line[0])
        m = int(line[1])
        
        edges = []
        print(f"Please enter the {m} edges (format: u v):")
        for i in range(m):
            while True:
                try:
                    edge_input = input(f"Edge {i+1}: ").split()
                    u, v = map(int, edge_input)
                    edges.append((u, v))
                    break # Success, move to next edge
                except (ValueError, IndexError):
                    print("Invalid input. Please enter two integers separated by a space.")
                    
        return n, m, edges
    
    except EOFError:
        return 0, 0, []
    except (ValueError, IndexError):
        print("Error: Initial input must contain two integers (n and m).")
        return 0, 0, []

def build_graph(n, edges):
    # Initialize structures
    matrix = [[0] * n for _ in range(n)]
    adj = [[] for _ in range(n)]
    
    for u, v in edges:
        if 0 <= u < n and 0 <= v < n:
            # Undirected graph logic
            matrix[u][v] = 1
            matrix[v][u] = 1
            adj[u].append(v)
            adj[v].append(u)
        else:
            print(f"Warning: Edge ({u}, {v}) ignored (index out of range for {n} nodes).")
            
    # Optional: Sort adjacency list for cleaner output
    for list_entry in adj:
        list_entry.sort()
        
    return matrix, adj

def print_results(matrix, adj):
    print("\n--- Adjacency Matrix ---")
    for row in matrix:
        print(" ".join(str(x) for x in row))

    print("\n--- Adjacency List ---")
    for i, neighbors in enumerate(adj):
        neighbor_str = " ".join(str(x) for x in neighbors)
        print(f"Node {i}: {neighbor_str if neighbor_str else 'No neighbors'}")

if __name__ == "__main__":
    n, m, edges = read_input_interactive()
    
    if n > 0:
        matrix, adj = build_graph(n, edges)
        print_results(matrix, adj)
    else:
        print("No graph to process.")