from collections import deque

class Solution:
    def firstNegInt(self, arr, k): 
        n = len(arr)
        dq = deque()
        result = [0] * (n-k+1)
        idx = 0
        for i in range(n):
            if arr[i] < 0:
                dq.append(i)
                
            if dq and dq[0] <= i-k:
                dq.popleft()
            
            if i >= k-1:
                if dq:
                    result[idx] = arr[dq[0]]
                else:
                    result[idx] = 0
                idx += 1
            
        return result
