from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    for city in cities:
        low_city = city.lower()
        if low_city in cache:
            cache.remove(low_city)
            cache.append(low_city)
            answer += 1
        else:
            cache.append(low_city)
            answer += 5
        if len(cache) > cacheSize:
            cache.popleft()
    return answer