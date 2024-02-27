def count_point(stairs):
    if len(stairs) == 1:
        return stairs[0]
    elif len(stairs) == 2:
        return sum(stairs)
    
    dp = [0] * len(stairs)
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, len(stairs)):
        dp[i] = max(stairs[i] + dp[i - 2], stairs[i] + stairs[i - 1] + dp[i - 3])

    return dp[-1]


def main():
    N = int(input())
    stairs = [int(input()) for _ in range(N)]
    print(count_point(stairs))


if __name__ == "__main__":
    main()
