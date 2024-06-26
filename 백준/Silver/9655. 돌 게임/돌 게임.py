val = int(input())

answer = ["SK", "CY"]
dp = [-1 for _ in range(1001)]

dp[1] = 0
dp[2] = 1

for i in range(3, 1001):
    dp[i] = dp[i-2]

print(answer[dp[val]])
