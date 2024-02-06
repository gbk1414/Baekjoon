import heapq 
import sys

N = int(sys.stdin.readline())
h = []

def update_heap(x: int) -> None:
    if x == 0:
        if h:
            heap_val = heapq.heappop(h)
            print(heap_val)
        else:
            print(0)
    else:
        heapq.heappush(h,x)

for _ in range(N):
    x = int(sys.stdin.readline())
    update_heap(x)

