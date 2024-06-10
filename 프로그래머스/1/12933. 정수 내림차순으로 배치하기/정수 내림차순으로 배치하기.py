def solution(n):
    answer = ''
    num_dict = {i:0 for i in range(10)}
    while n>0:
        num_dict[n%10] += 1
        n = n // 10
    for i in range(9,-1,-1):
        answer += str(i)*num_dict[i]
    return int(answer)