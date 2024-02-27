def padoban(n):
    dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0 for _ in range(n-10)]

    for i in range(8, n+1):
        dp[i] = dp[i-1] + dp[i-5]

    return dp[n]


def main():
    T = int(input())
    for _ in range(T):
        print(padoban(int(input())))


if __name__ == "__main__":
    main()
