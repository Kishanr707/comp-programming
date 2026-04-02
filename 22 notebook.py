from collections import defaultdict

def check_connection():
    # Using defaultdict prevents KeyError if IDs are non-sequential
    adj = defaultdict(list)
    
    line1 = input("Enter Users and Friendships (e.g., 4 4): ").split()
    if not line1: return "No input"
    n, e = map(int, line1)
    
    print(f"Enter {e} connections (u v):")
    for _ in range(e):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    s, d = map(int, input("Enter Source and Destination: ").split())

    # BFS Logic
    visited = {s}
    queue = [s]
    
    for curr in queue:
        if curr == d:
            return "Connection Exists"
        for neighbor in adj[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return "No Connection"

print(f"\nResult: {check_connection()}")