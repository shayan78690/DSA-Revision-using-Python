class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        n = len(arr)
        left = 0
        right = 0
        count = 0
        s = 0
        while right < n:
            s += arr[right]

            if right-left+1 > k:
                s -= arr[left]
                left += 1

            if right-left+1 == k:
                if s/k >= threshold:
                    count += 1

            right += 1
        return count