class Solution(object):
    def sumSubarrayMins(self, arr):
        n = len(arr)
        total = 0
        mod = 10**9+7
        nse = self.NSE(arr)
        pse = self.PSE(arr)
        for i in range(n):
            first = nse[i]-i
            last = i-pse[i]
            total = (total + arr[i]*first*last) % mod
        return total
    
    def NSE(self, arr):
        n = len(arr)
        stack = []
        nse = [0]*n
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nse[i] = stack[-1] if stack else n
            stack.append(i)
        return nse
    
    def PSE(self, arr):
        n = len(arr)
        stack = []
        pse = [0] * n
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            pse[i] = stack[-1] if stack else -1
            stack.append(i)
        return pse
