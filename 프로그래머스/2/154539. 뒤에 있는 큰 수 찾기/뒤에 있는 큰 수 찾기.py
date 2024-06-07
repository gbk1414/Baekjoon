from collections import deque

def solution(numbers):
    stack = deque()
    answer = [-1 for _ in range(len(numbers))]
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
        
    return answer
        
        
    
    
    return answer