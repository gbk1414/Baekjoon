def solution(s):
    answer = s[0].upper()
    i = 1
    while i < len(s):
        if s[i] == " ":
            answer += " "
        elif s[i-1] == " " and s[i] != " ":
            answer += s[i].upper()
        else:
            answer += s[i].lower()
        i += 1
    
    return answer