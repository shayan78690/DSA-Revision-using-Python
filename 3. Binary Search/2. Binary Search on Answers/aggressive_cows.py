class Solution:
    
    def possible(self, stalls, k, dist):
        cows = 1
        last = stalls[0]
        for i in range(1, len(stalls)):
            if stalls[i]-last >= dist:
                cows += 1
                last = stalls[i]
            if cows >= k:
                return True
        return False
    
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        low = 1
        high = stalls[len(stalls)-1] - stalls[0]
        ans = low
        while low <= high:
            mid = (low+high)//2
            if self.possible(stalls, k, mid):
                ans = mid
                low = mid+1
            else:
                high = mid-1
        return ans
        