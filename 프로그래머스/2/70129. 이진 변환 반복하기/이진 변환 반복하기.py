def solution(s):
    binary_cnt = 0
    zero_cnt = 0
    
    def binary_change(s):
        answer = ""
        cnt = 0
        for i in s:
            if i == "0":
                cnt += 1
            elif i == "1":
                answer += i
        return [str(bin(len(answer)))[2:], cnt]
    
    while s != "1":
        result = binary_change(s)
        s = result[0]
        zero_cnt += result[1]
        binary_cnt += 1
    
    return [binary_cnt, zero_cnt]