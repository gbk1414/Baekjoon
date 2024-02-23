import sys

input = sys.stdin.readline


def count_new_workers(scores: list[tuple[int, int]]) -> int:
    scores.sort()
    count = 1
    min_score = scores[0][1]
    for _, interview_score in scores:
        if min_score > interview_score:
            count += 1
            min_score = interview_score
    return count


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        scores = [tuple(map(int, input().split())) for _ in range(N)]
        print(count_new_workers(scores))


if __name__ == "__main__":
    main()
