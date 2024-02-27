def calculate_digit_sum(number):
    return sum(map(int, str(number)))


def find_special_number(N):
    answer = N
    n_str = str(N)
    limit = int(n_str[0]) + 9 * len(n_str[1:])

    for num in range(N, N - limit, -1):
        if num + calculate_digit_sum(num) == N:
            answer = num
    return answer


def main():
    N = int(input())
    result = find_special_number(N)
    if result == N:
        print(0)
    else:
        print(result)


if __name__ == "__main__":
    main()
