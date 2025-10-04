class Solution(object):
    
    def possible(self, arr, m, k, mid):
        count_of_days = 0
        no_of_Boquets = 0
        for i in range(len(arr)):
            if arr[i] <= mid:
                count_of_days += 1
            else:
                no_of_Boquets += (count_of_days//k)
                count_of_days = 0
        no_of_Boquets += (count_of_days//k)
        return no_of_Boquets >= m

    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if self.possible(bloomDay, m, k, mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans

        