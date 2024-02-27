import sys
input = sys.stdin.readline


def calculate_w():
    w = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):
                if i < j and j < k:
                    w[i][j][k] = w[i][j][k-1] + w[i][j-1][k-1] - w[i][j-1][k]
                else:
                    w[i][j][k] = w[i-1][j][k] + w[i-1][j-1][k] + \
                        w[i-1][j][k-1] - w[i-1][j-1][k-1]
    return w


def adjust_w(a, b, c, w):
    if a <= 0 or b <= 0 or c <= 0:
        a = b = c = 0
    if a > 20 or b > 20 or c > 20:
        a = b = c = 20
    return w[a][b][c]


def main():
    w = calculate_w()
    while True:
        a, b, c = map(int, input().split())
        if (a, b, c) == (-1, -1, -1):
            break
        print("w({}, {}, {}) = {}".format(a, b, c, adjust_w(a, b, c, w)))


if __name__ == "__main__":
    main()
