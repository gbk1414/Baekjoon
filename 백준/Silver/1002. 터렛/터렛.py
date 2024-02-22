import math


def sq_distance(p1, p2):
    return math.dist(p1, p2)


def count_intersection(x_1, y_1, r_1, x_2, y_2, r_2) -> int:
    dist = sq_distance([x_1, y_1], [x_2, y_2])
    if dist == 0:
        return -1 if r_1 == r_2 else 0
    elif dist < abs(r_1-r_2) or dist > r_1+r_2:
        return 0
    elif dist == r_1+r_2 or dist == abs(r_1-r_2):
        return 1
    else:
        return 2


def main():
    T = int(input())
    for _ in range(T):
        x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())
        print(count_intersection(x_1, y_1, r_1, x_2, y_2, r_2))


if __name__ == "__main__":
    main()
