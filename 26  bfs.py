from collections import deque

def min_rook_moves():
    # Input handling
    try:
        n = int(input())
        start_row, start_col = map(int, input().split())
        target_row, target_col = map(int, input().split())
    except EOFError:
        return

    # Edge case: Already at destination
    if (start_row, start_col) == (target_row, target_col):
        print(0)
        return

    # BFS Setup
    queue = deque([(start_row, start_col, 0)])
    visited = set([(start_row, start_col)])
    
    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c, dist = queue.popleft()

        for dr, dc in directions:
            # A rook can move any number of steps (i) in a direction
            for i in range(1, n):
                nr, nc = r + dr * i, c + dc * i
                
                # Check boundaries
                if 0 <= nr < n and 0 <= nc < n:
                    if (nr, nc) == (target_row, target_col):
                        print(dist + 1)
                        return
                    
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc, dist + 1))
                else:
                    # Out of bounds, stop looking in this direction
                    break

# Execute
min_rook_moves()