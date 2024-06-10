def solution(arr):
    answer = 0
    i = 0
    while i < len(arr):
        answer += arr[i]
        i += 1
    return answer/i