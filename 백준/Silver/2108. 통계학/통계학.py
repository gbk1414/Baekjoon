from collections import Counter
from sys import stdin
input = stdin.readline


def get_avg(arr: list[int]) -> int:
    return round(sum(arr) / len(arr))


def get_mid(arr: list[int]) -> tuple[int, int]:
    arr.sort()
    return arr[len(arr) // 2], arr[-1]-arr[0]


def get_most(arr: list[int]) -> int:
    num_cnt = Counter(arr).most_common(2)
    if len(num_cnt) == 1 or num_cnt[0][1] > num_cnt[1][1]:
        return num_cnt[0][0]
    return num_cnt[1][0]


def main():
    N = int(input())
    arr = [int(input()) for _ in range(N)]

    mid_val, range_val = get_mid(arr)
    print(get_avg(arr))
    print(mid_val)
    print(get_most(arr))
    print(range_val)


if __name__ == "__main__":
    main()
