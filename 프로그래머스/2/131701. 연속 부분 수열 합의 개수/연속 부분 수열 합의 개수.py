def solution(elements):
    answer = 0
    answer_set = set()
    for i in range(len(elements)):
        new_elements = elements + elements[:i]
        for j in range(len(elements)):
            answer_set.add(sum(new_elements[j:j+i]))
    return len(answer_set)