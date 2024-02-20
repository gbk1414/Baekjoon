def find_shark(space: list[int]):
    for i in range(len(space)):
        for j in range(len(space)):
            if space[i][j] == 9:
                space[i][j] = 0
                return i, j


def find_food(point, space: list[int], shark_size):
    x, y = point
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    visited = [[False] * len(space) for _ in range(len(space))]  # Fix: Use len(space) instead of n
    visited[x][y] = True
    start = [point]
    time = 0
    while start:
        time += 1
        new_start = []
        can_eat = []
        for x, y in start:
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if 0 <= nx < len(space) and 0 <= ny < len(space) and space[nx][ny] <= shark_size and not visited[nx][ny]:
                    if 0 < space[nx][ny] < shark_size:
                        can_eat.append((nx, ny))
                    visited[nx][ny] = True
                    new_start.append([nx, ny])
        if can_eat:
            # 거리 우선 -> 가장 위 -> 가장 왼쪽 물고기 먹어야 함
            can_eat.sort()
            x, y = can_eat[0]
            space[x][y] = 0
            return x, y, time
        start = new_start[:]
    return None


def main():
    n = int(input())
    space = [list(map(int, input().split())) for _ in range(n)]

    position = find_shark(space)
    result = 0
    eat = 0
    shark_size = 2
    while True:
        food = find_food(position, space, shark_size)
        if food is None:
            break
        *position, t = food
        result += t
        eat += 1
        if eat == shark_size:
            shark_size += 1
            eat = 0
    print(result)


if __name__ == "__main__":
    main()
