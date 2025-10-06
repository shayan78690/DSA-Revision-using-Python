def kDistinctChars(k, str):
    n = len(str)
    map = {}
    left = 0
    right = 0
    maxLen = 0
    
    while right < n:
        map[str[right]] = map.get(str[right], 0) + 1
        
        while len(map) > k:
            map[str[left]] = map[str[left]] - 1
            if map[str[left]] == 0:
                del map[str[left]]
            left += 1
        
        maxLen = max(maxLen, right - left + 1)
        right += 1
    
    return maxLen
