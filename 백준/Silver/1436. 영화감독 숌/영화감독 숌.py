def find_movie_title(n):
    count = 0
    title = 665

    while True:
        title += 1
        if '666' in str(title):
            count += 1

        if count == n:
            return title


def main():
    n = int(input())

    result = find_movie_title(n)

    print(result)


if __name__ == "__main__":
    main()
