# 서류 1등의 면접등수보다 같거나 높은 and 면접 1등의 서류점수 보다 같거나 높은사람

import sys

input = sys.stdin.readline


def get_new_worker(scores: list[int]) -> int:
    scores.sort()
    cnt = 1
    min_score = scores[0][1]
    for x,y in scores:
        if min_score > y:
            cnt += 1 
            min_score = y
    return cnt


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        scores = [list(map(int, input().split())) for _ in range(N)]
        print(get_new_worker(scores))


if __name__ == "__main__":
    main()
