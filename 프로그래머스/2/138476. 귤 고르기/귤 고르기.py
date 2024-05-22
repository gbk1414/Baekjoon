from collections import Counter
def solution(k, tangerine):
    count = Counter(tangerine)
    sorted_counts = sorted(count.values(), reverse=True)
    
    total_counts = 0
    for i in range(len(sorted_counts)):
        total_counts += sorted_counts[i]
        if total_counts >= k:
            return i+1
        
    return 0