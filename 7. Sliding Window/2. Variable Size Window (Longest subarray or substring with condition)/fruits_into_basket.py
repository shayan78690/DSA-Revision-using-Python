class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        n = len(fruits)
        left = 0
        right = 0
        maxLength = 0
        map = {}
        
        while right < n:
            map[fruits[right]] = map.get(fruits[right], 0) + 1
            
            if len(map) > 2:
                while len(map) > 2:
                    map[fruits[left]] = map[fruits[left]] - 1
                    if map[fruits[left]] == 0:
                        del map[fruits[left]]
                    left += 1
            
            if len(map) <= 2:
                maxLength = max(maxLength, right - left + 1)
            
            right += 1
        
        return maxLength