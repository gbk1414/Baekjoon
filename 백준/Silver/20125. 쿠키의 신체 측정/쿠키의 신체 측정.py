def find_heart(board):
    N = len(board)
    for i in range(N):
        for j in range(N):
            if board[i][j] == "*":
                return i+1, j

def get_left_arm_length(board, x, y):
    N = len(board)
    cnt = 0
    y -= 1
    while y >= 0 and board[x][y] == "*":
        cnt += 1
        y -= 1
    return cnt

def get_right_arm_length(board, x, y):
    N = len(board)
    cnt = 0
    y += 1
    while y < N and board[x][y] == "*":
        cnt += 1
        y += 1
    return cnt

def get_hurry(board,x,y):
    cnt = 0
    while board[x+1][y] == "*":
        cnt += 1
        x += 1
    return cnt, x, y

def get_left_leg(board, x, y):
    N = len(board)
    cnt = 0
    x += 1
    while x < N and board[x][y-1] == "*":
        cnt += 1
        x += 1
    return cnt

def get_right_leg(board, x, y):
    N = len(board)
    cnt = 0
    x += 1
    while x < N and board[x][y+1] == "*":
        cnt += 1
        x += 1
    return cnt


def main():
    M = int(input())
    board = []
    for _ in range(M):
        board.append(list(input()))

    heart_x, heart_y = find_heart(board)

    left_arm, right_arm = get_left_arm_length(board, heart_x, heart_y), get_right_arm_length(board, heart_x, heart_y)
    hurry, hurry_x, hurry_y = get_hurry(board, heart_x, heart_y)
    left_leg, right_leg = get_left_leg(board, hurry_x, hurry_y), get_right_leg(board, hurry_x, hurry_y)
    
    print(heart_x + 1, heart_y + 1)
    print(left_arm, right_arm,hurry, left_leg, right_leg)

main()

