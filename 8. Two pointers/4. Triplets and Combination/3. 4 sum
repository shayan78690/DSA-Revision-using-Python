class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j+1
                m = n-1
                while k < m:
                    s = nums[i] + nums[j]
                    s += nums[k]
                    s += nums[m]
                    if s == target:
                        temp = [nums[i], nums[j], nums[k], nums[m]]
                        ans.append(temp)
                        k += 1
                        m -= 1
                        while k < m and nums[k] == nums[k-1]:
                            k += 1
                        while k < m and nums[m] == nums[m+1]:
                            m -= 1
                    elif s < target:
                        k += 1
                    else:
                        m -= 1
        return ans
