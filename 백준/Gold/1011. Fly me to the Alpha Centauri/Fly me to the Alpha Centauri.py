import math


def calculate_flights(start: int, end: int) -> int:
    distance = end - start
    num_flights = math.floor(math.sqrt(distance))

    if num_flights**2 == distance:
        return 2*num_flights-1
    elif num_flights**2 + num_flights < distance:
        return 2*num_flights+1
    return 2*num_flights


def main():
    N = int(input())

    for _ in range(N):
        start, end = map(int, input().split())
        print(calculate_flights(start, end))


if __name__ == "__main__":
    main()
