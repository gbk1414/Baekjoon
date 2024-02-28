MAX_N = 40


def fibo(n):
    fibo_list = [1, 1] + [0 for _ in range(n-1)]
    for i in range(2, n+1):
        fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]
    return fibo_list


def main():
    path_list = fibo(MAX_N)
    while True:
        N = int(input())
        if N == 0:
            break
        print(path_list[N])


if __name__ == "__main__":
    main()
