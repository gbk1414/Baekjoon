import heapq

def solution(s):
    answer = ''
    num_list = [int(i) for i in s.split(" ")]
    
    num_list.sort()
    
    answer = str(num_list[0]) + " " + str(num_list[-1])
    
    return answer