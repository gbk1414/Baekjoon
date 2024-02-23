from collections import deque
import sys

input = sys.stdin.readline


def calculate_moves_to_target(dq, target):
    # 타겟까지의 이동 횟수 계산
    left_moves = dq.index(target)
    right_moves = len(dq) - left_moves
    return min(left_moves, right_moves)


def circle_queue(positions, N):
    dq = deque(range(1, N+1))
    moves = 0
    for target in positions:
        moves += calculate_moves_to_target(dq, target)
        dq.rotate(-dq.index(target))
        dq.popleft()
    return moves


def main():
    N, M = map(int, input().split())
    positions = list(map(int, input().split()))
    print(circle_queue(positions, N))


if __name__ == "__main__":
    main()
