def solution(cacheSize, cities):
    answer = 0
    i = 0              # 초기 캐시 인덱스
    cache = []
    if cacheSize == 0:                # 캐시 사이즈가 0이면,
        return len(cities)*5
    for c in cities:              
        city = c.upper()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            answer += 5 
            if i < cacheSize:
                cache.append(city)
                i += 1
            else:
                cache.pop(0)
                cache.append(city)

    return answer