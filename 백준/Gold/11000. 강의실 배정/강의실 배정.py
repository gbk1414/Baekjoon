import heapq
from sys import stdin

input = stdin.readline


def cnt_lecture_room(time_list: list[int]) -> int:
    time_list.sort()
    course_room = []

    for start, end in time_list:
        if course_room and course_room[0] <= start:
            heapq.heappop(course_room)
        heapq.heappush(course_room, end)

    return len(course_room)


def main():
    N = int(input())
    time_list = [list(map(int, input().split())) for _ in range(N)]
    print(cnt_lecture_room(time_list))


if __name__ == "__main__":
    main()
