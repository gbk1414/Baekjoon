def solution(storey):
    answer = 0
    while storey > 0:
        storey_left = storey%10
        storey = storey//10
        
        if storey_left == 5:
            answer += 5
            if storey%10 > 4:
                storey += 1
        elif storey_left > 5:
            answer += 10-storey_left
            storey += 1
        else:
            answer += storey_left
        
    return answer