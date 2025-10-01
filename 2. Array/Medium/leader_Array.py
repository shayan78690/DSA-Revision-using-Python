class Solution:
    def leaders(self, arr):
        ans = []
        n = len(arr)
        for i in range(n):
            isLeader = True
            for j in range(i+1, n):
                if arr[j] > arr[i]:
                    isLeader = False
            if isLeader:
                ans.append(arr[i])
        
        return ans
    
    
class Solution1:
    def leaders(self, arr):
        ans = []
        n = len(arr)
        ans.append(arr[n-1])
        leader = arr[n-1]
        for i in range(n-2, -1, -1):
            if arr[i] >= leader:
                ans.append(arr[i])
                leader = arr[i]
        
        
        start = 0
        end = len(ans)-1
        while start < end:
            ans[start], ans[end] = ans[end], ans[start]
            start += 1
            end -= 1
        return ans
        
        


