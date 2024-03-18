def max_value_backpack(N: int, K: int, toy_list: list[list[int]]) -> int:
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        weight, value = toy_list[i - 1]
        for j in range(1, K + 1):
            if weight > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])

    return dp[N][K]

def main():
    N, K = map(int, input().split())
    toy_list = [list(map(int, input().split())) for _ in range(N)]
    
    answer = max_value_backpack(N, K, toy_list)
    print(answer)

if __name__ == "__main__":
    main()