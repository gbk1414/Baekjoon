import heapq
from sys import stdin

MAX_VAL = 10**9 + 1
input_ = stdin.readline


def find_min(graph, V, start_node):
    visited = [MAX_VAL for _ in range(V + 1)]
    visited[start_node] = 0
    heap = []
    heapq.heappush(heap, (0, start_node))

    while heap:
        cur_weight, cur_node = heapq.heappop(heap)
        if visited[cur_node] < cur_weight:
            continue

        for weight, next_node in graph[cur_node]:
            new_weight = cur_weight + weight
            if new_weight < visited[next_node]:
                visited[next_node] = new_weight
                heapq.heappush(heap, (new_weight, next_node))

    return visited


def main():
    V, E = map(int, input_().split())
    start_node = int(input_())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        cur_node, next_node, weight = map(int, input_().split())
        graph[cur_node].append((weight, next_node))

    dist_list = find_min(graph, V, start_node)
    for idx in range(1, len(dist_list)):
        if dist_list[idx] == MAX_VAL:
            print("INF")
        else:
            print(dist_list[idx])


if __name__ == "__main__":
    main()
