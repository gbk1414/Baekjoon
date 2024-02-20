from sys import stdin

input = stdin.readline

def spread(room,pos):
    """
    Fine dust diffusion result return function
    """
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    new_room = [[0] * C for _ in range(R)]
    new_room[pos][0] = -1
    new_room[pos+1][0] = -1
    for x in range(R):
        for y in range(C):
            if room[x][y] > 0:
                new_room[x][y] += room[x][y]
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != -1:
                        new_room[nx][ny] += room[x][y] // 5
                        new_room[x][y] -= room[x][y] // 5
    return new_room

def rotate(room,pos):
    """
    Fine dust circulation function
    """
    # Upward circulation: counterclockwise
    for x in range(pos - 1, 0, -1):
        room[x][0] = room[x - 1][0]
    for y in range(C - 1):
        room[0][y] = room[0][y + 1]
    for x in range(pos):
        room[x][-1] = room[x + 1][-1]
    for y in range(C - 1, 0, -1):
        room[pos][y] = room[pos][y - 1]

    # Downward circulation: clockwise
    for x in range(pos + 1 + 1, R - 1):
        room[x][0] = room[x + 1][0]
    for y in range(C - 1):
        room[-1][y] = room[-1][y + 1]
    for x in range(R - 1, pos+1, -1):
        room[x][-1] = room[x - 1][-1]
    for y in range(C - 1, 0, -1):
        room[pos+1][y] = room[pos+1][y - 1]

    # The wind from the air purifier is reset to 0 because it is free of fine dust.
    room[pos][1] = 0
    room[pos+1][1] = 0

def main():
    global R, C, T
    R, C, T = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(R)]
    for i in range(R):
        if room[i][0] == -1:
            pos = i
            break
    for _ in range(T):
        room = spread(room,pos)
        rotate(room,pos)
    print(sum(map(sum, room)) + 2)

if __name__ == "__main__":
    main()