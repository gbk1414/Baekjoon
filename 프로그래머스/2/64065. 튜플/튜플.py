def solution(s):
    answer = []
    
    new_s = s[2:-2].split("},{")
    
    new_s.sort(key = lambda x: len(x))
    
    for small_s in new_s:
        small_s_list = list(map(int, small_s.split(",")))
        for ss in small_s_list:
            if ss not in answer:
                answer.append(ss)
    
    return answer