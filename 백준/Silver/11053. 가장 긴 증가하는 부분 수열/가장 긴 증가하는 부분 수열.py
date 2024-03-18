def longest_asc_num(N: int, A: list[int]) -> int:
    dp = [1 for _ in range(N)]
    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp) if dp else 0

def main():
    N = int(input())
    A = list(map(int,input().split()))
    answer = longest_asc_num(N, A)
    print(answer)

if __name__ == "__main__":
    main()