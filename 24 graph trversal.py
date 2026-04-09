def traversal():
    print("--- File System Tree Builder ---")
    
    try:
        n = int(input("Enter the total number of nodes: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    tree = {}
    root = None

    print("\nEnter each node and its children in the format: [node] [left] [right]")
    print("Use -1 if a child does not exist.")
    
    for i in range(n):
        line = input(f"Node entry {i+1}: ").split()
        if len(line) != 3:
            print("Error: Please provide exactly three values.")
            return
            
        node, left, right = map(int, line)
        
        # Set the first node entered as the root
        if i == 0:
            root = node
            
        tree[node] = (left, right)

    # Traversal Logic
    output = []
    def pre_order(current):
        if current == -1:
            return
        output.append(str(current))
        left, right = tree.get(current, (-1, -1))
        pre_order(left)
        pre_order(right)

    print("\n--- Processing Traversal ---")
    pre_order(root)
    
    print("file system traversal (pre-order)")
    print(" ".join(output))

if __name__ == "__main__":
    traversal()