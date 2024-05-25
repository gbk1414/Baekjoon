from collections import Counter

def solution(want, number, discount):
    answer = 0
    for i in range(0,len(discount)-9):
        counted_number = Counter(discount[i:i+10])
        flag = True
        for j in range(len(want)):
            if counted_number[want[j]] < number[j] and flag:
                flag = False
        if flag:
            answer += 1
    return answer