dp = [0,0] + [1 for _ in range(999999)]

M, N = map(int, input().split())

for i in range(2, N):
    if dp[i] == 1:
        for new_i in range(i*i, N+1, i):
            dp[new_i] = 0

for i in range(M,N+1):
    if dp[i] == 1:
        print(i)