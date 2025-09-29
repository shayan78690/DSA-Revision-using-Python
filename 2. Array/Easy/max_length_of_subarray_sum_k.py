class Solution:
    def longestSubarray(self, arr, k):  
        n = len(arr)
        max_len = 0
        for i in range(n):
            for j in range(i, n):
                s = 0
                for m in range(i, j+1):
                    s += arr[m]
                
                if s == k:
                    max_len = max(max_len, j-i+1)
        
        return max_len
    




class Solution1:
    def longestSubarray(self, arr, k):  
        max_len = 0
        n = len(arr)
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += arr[j]
                
                if s == k:
                    max_len = max(max_len, j-i+1)
                    
        return max_len
    


class Solution2:
    def longestSubarray(self, arr, k):  
        n = len(arr)
        maxi = 0
        hashmap = {}
        prefix_sum = 0
        for i in range(n):
            prefix_sum += arr[i]
            
            if prefix_sum == k:
                maxi = max(maxi, i+1)
            
            rem = prefix_sum - k
            if rem in hashmap:
                length = i - hashmap[rem]
                maxi = max(maxi, length)
            
            if prefix_sum not in hashmap:
                hashmap[prefix_sum] = i
            
        return maxi
    
