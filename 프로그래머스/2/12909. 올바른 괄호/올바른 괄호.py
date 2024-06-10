from collections import deque

def solution(s):
    stack = deque()
    
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    
    return True