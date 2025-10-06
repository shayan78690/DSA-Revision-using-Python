class Solution:
    def countAtMostK(self, arr, k):
        n = len(arr)
        map = {}
        count = 0
        left = 0
        right = 0
        
        while right < n:
            num = arr[right]
            map[num] = map.get(num, 0) + 1
            
            while len(map) > k:
                temp = arr[left]
                map[temp] = map[temp] - 1
                if map[temp] == 0:
                    del map[temp]
                left += 1
            
            count += (right - left + 1)
            right += 1
        
        return count
        