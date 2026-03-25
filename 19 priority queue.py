import heapq

def auction_system():
    # Input handling
    try:
        n = int(input().strip())
        if n <= 0:
            return
        
        bids = list(map(int, input().split()))
        
        # Inverting values because heapq is a min-heap by default
        # -100 becomes the "smallest" value, allowing us to treat it as a max-heap
        max_heap = [-bid for bid in bids]
        heapq.heapify(max_heap)
        
        # 1. Get and remove the highest bid
        highest = -heapq.heappop(max_heap)
        print(highest)
        
        # 2. Get the next highest bid if it exists
        if max_heap:
            next_highest = -max_heap[0] # Peek at the new root
            print(next_highest)
            
    except EOFError:
        pass

if __name__ == "__main__":
    auction_system()