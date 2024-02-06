import heapq 
import sys

N = int(sys.stdin.readline())
h = []

def update_heap(x: int) -> None:
    if x == 0:
        if h:
            heap_val = (-1) * heapq.heappop(h)
            print(heap_val)
        else:
            print(0)
    else:
        heapq.heappush(h,(-1)*x)

for _ in range(N):
    x = int(sys.stdin.readline())
    update_heap(x)