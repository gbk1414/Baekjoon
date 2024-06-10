from collections import deque

def solution(s):
    stack = deque()
    
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    
    if stack:
        return False
    
    return True