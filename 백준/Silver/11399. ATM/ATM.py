import heapq
import sys

input = sys.stdin.readline

def atm_time(positions):
    heapq.heapify(positions)
    total_time = 0
    waiting_time = 0
    while positions:
        time = heapq.heappop(positions)
        waiting_time += time
        total_time += waiting_time
    return total_time

def main():
    N = int(input())
    positions = list(map(int, input().split()))
    print(atm_time(positions))

if __name__ == "__main__":
    main()