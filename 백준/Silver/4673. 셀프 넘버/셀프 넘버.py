def d(n):
    value = 0
    org_n = n
    while n>0:
        value += n%10
        n = n//10
    return value

dp = [1 for _ in range(10001)]

for i in range(1,10001):
    new_i = i+d(i)
    if new_i < 10001:
        dp[new_i] = 0
    if dp[i] == 1:
        print(i)
