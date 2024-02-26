import heapq as hq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(cave, N):
    min_cost = [[float('inf')] * N for _ in range(N)]
    min_cost[0][0] = cave[0][0]
    heap = [(cave[0][0], 0, 0)]  # (비용, x좌표, y좌표)를 저장하는 최소 힙

    while heap:
        cost, x, y = hq.heappop(heap)

        if min_cost[x][y] < cost:  # 이미 더 작은 비용으로 갱신된 경우
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                new_cost = cost + cave[nx][ny]
                if new_cost < min_cost[nx][ny]:
                    min_cost[nx][ny] = new_cost
                    hq.heappush(heap, (new_cost, nx, ny))

    return min_cost[N-1][N-1]

def main():
    cnt = 0
    while True:
        cnt += 1
        N = int(input())

        if N == 0:
            break

        cave = []

        for _ in range(N):
            row = list(map(int, input().split()))
            cave.append(row)

        print("Problem {}:".format(cnt), dijkstra(cave, N))

if __name__ == "__main__":
    main()
