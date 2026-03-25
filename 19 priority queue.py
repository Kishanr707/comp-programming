import heapq

def auction_system():
    try:
        n = int(input().strip())
        if n <= 0:
            return

        bids = list(map(int, input().split()))

        max_heap = [-bid for bid in bids]
        heapq.heapify(max_heap)

        highest = -heapq.heappop(max_heap)
        print(highest)

        if max_heap:
            next_highest = -max_heap[0]
            print(next_highest)

    except EOFError:
        pass

if __name__ == "__main__":
    auction_system()