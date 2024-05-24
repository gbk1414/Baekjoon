from collections import deque

def solution(s):
    answer = 0
    def checker(strings):
        stack = deque()
        for strs in strings:
            if strs in ["(", "[", "{"]:
                stack.append(strs)
            elif strs in [")", "]", "}"]:
                if not stack:
                    return False
                last_one = stack.pop()
                if last_one + strs not in ["()","[]","{}"]:
                    return False
        return len(stack)==0
    
    new_s = s+s[:-1]
    for i in range(len(s)):
        if checker(new_s[i:len(s)+i]):
            answer += 1
    return answer