def word_checker(s1, s2):
        answer = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                answer += 1
        return answer    

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = [0] * len(words)
    
    def dfs(begin, target):
        if begin == target:
            return 1
        
        min_cnt = float('inf')
        for i in range(len(words)):
            if visited[i] == 0 and word_checker(words[i],begin) == 1:
                visited[i] = 1
                cnt = dfs(words[i], target)
                if cnt != 0:
                    min_cnt = min(min_cnt, 1+cnt)
                visited[i] = 0
        return min_cnt if min_cnt != float('inf') else 0
    
    answer = dfs(begin, target)
    if answer != 0:
        answer -= 1
    
    return answer