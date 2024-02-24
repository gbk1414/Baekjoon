import sys
input = sys.stdin.readline


def cutting_wood(tree_list: list[int], M: int) -> int:
    tree_list.sort()
    start = tree_list[-1] - M//len(tree_list)
    end = 0
    while start >= end:
        mid = (start+end)//2
        if sum(x-mid if x > mid else 0 for x in tree_list) < M:
            start = mid - 1
        else:
            end = mid + 1
    return start


def main():
    N, M = map(int, input().split())
    tree_list = list(map(int, input().split()))
    print(cutting_wood(tree_list, M))


if __name__ == "__main__":
    main()
