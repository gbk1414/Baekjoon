import heapq 
import sys

def update_heap(h: list[int], x: int) -> None:
    if x == 0:
        if h:
            heap_val = (-1) * heapq.heappop(h)
            print(heap_val)
        else:
            print(0)
    else:
        heapq.heappush(h, (-1) * x)

def main():
    N = int(sys.stdin.readline())
    h = []

    for _ in range(N):
        x = int(sys.stdin.readline())
        update_heap(h, x)

if __name__ == "__main__":
    main()