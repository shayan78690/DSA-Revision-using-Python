class Solution:
    def totalElements(self, arr):
        map = {}
        left = 0
        right = 0
        maxLen = 0
        
        while right < len(arr):
            map[arr[right]] = map.get(arr[right], 0) + 1
            
            if len(map) > 2:
                map[arr[left]] = map[arr[left]] - 1
                if map[arr[left]] == 0:
                    del map[arr[left]]
                left += 1
            
            maxLen = max(maxLen, right - left + 1)
            right += 1
        
        return maxLen