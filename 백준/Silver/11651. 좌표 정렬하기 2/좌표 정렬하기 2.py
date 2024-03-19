def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]

    points.sort(key=lambda point: (point[1], point[0]))

    for point in points:
        print("{} {}".format(point[0], point[1]))

if __name__ == "__main__":
    main()
