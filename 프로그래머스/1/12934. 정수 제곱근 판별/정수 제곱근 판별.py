def solution(n):
    answer = 0
    #다른 언어의 경우 long으로 형변환)
    while answer**2 < n:
        answer += 1
    if answer**2  == n:
        return (answer+1)**2
    return -1