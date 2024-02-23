import math
from sys import stdin
input = stdin.readline

# 인접한 구역간 거리를 구해서 최댓값부터 나열
# k -1 개를 없앤다.


def cal_min_distance(coordinates: list[int], k: int):
    coordinates.sort()
    dist_coordinates = [coordinates[i+1]-coordinates[i]
                        for i in range(len(coordinates)-1)]
    dist_coordinates.sort(reverse=True)
    selected_distances = dist_coordinates[:k - 1]
    min_range = coordinates[-1] - coordinates[0]
    for dist in selected_distances:
        min_range -= dist
    return min_range


def main():
    N = int(input())
    K = int(input())
    coordinates = list(map(int, input().split()))
    print(cal_min_distance(coordinates, K))


if __name__ == "__main__":
    main()
