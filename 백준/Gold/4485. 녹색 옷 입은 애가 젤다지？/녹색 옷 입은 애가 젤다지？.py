from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_least_coin(cave, N):
    min_cost = [[float('inf')] * N for _ in range(N)]
    min_cost[N-1][N-1] = cave[N-1][N-1]
    queue = deque([(N-1, N-1)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and min_cost[nx][ny] > min_cost[x][y] + cave[nx][ny]:
                min_cost[nx][ny] = min_cost[x][y] + cave[nx][ny]
                queue.append((nx, ny))

    return min_cost[0][0]

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

        print("Problem {}:".format(cnt), get_least_coin(cave, N))

if __name__ == "__main__":
    main()
