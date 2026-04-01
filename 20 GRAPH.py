def get_graph():
    try:
        # Get nodes (n) and edge count (m)
        n, m = map(int, input("Enter nodes (n) and edges (m): ").split())
        
        # Build Adjacency List & Matrix simultaneously
        adj = [[] for _ in range(n)]
        matrix = [[0] * n for _ in range(n)]
        
        print(f"Enter {m} edges (u v):")
        for _ in range(m):
            u, v = map(int, input().split())
            if 0 <= u < n and 0 <= v < n:
                adj[u].append(v)
                adj[v].append(u)
                matrix[u][v] = matrix[v][u] = 1
        
        return n, matrix, adj
    except (ValueError, EOFError):
        return 0, [], []

def display(n, matrix, adj):
    print("\nAdjacency Matrix:")
    [print(*(row)) for row in matrix]
    
    print("\nAdjacency List:")
    for i, neighbors in enumerate(adj):
        print(f"{i}: {', '.join(map(str, sorted(neighbors))) or 'None'}")

n, mat, adj = get_graph()
if n: display(n, mat, adj)