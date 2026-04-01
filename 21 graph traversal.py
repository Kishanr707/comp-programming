from collections import deque, defaultdict

class GraphTraversal:
    def __init__(self):
        # defaultdict handles missing keys automatically
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        if u != v:  # Avoid duplicate entries for self-loops
            self.adj[v].append(u)

    def bfs(self, start):
        visited = {start}
        queue = deque([start])
        res = []

        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        print(f"BFS Traversal: {' '.join(map(str, res))}")

    def dfs(self, start):
        visited = set()
        res = []

        def walk(node):
            visited.add(node)
            res.append(node)
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    walk(neighbor)

        walk(start)
        print(f"DFS Traversal: {' '.join(map(str, res))}")

if __name__ == "__main__":
    gt = GraphTraversal()
    edges = [(5, 4), (0, 1), (0, 2), (1, 3), (2, 4), (0, 0)]

    for u, v in edges:
        gt.add_edge(u, v)

    gt.bfs(1)
    gt.dfs(1)