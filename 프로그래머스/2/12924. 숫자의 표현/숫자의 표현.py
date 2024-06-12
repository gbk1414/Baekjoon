def solution(n):
    answer = 0
    i = 1
    while i <= n:
        sum = 0
        j = i
        while sum < n:
            sum += j
            j += 1
        if sum == n:
            answer += 1
        i += 1
    return answer