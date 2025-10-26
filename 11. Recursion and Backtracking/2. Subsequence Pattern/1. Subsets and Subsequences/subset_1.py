class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        lst = []
        self.backtrack(nums, len(nums), ans, lst, 0)
        return ans

    def backtrack(self, nums, n, ans, lst, index):
        if index == n:
            ans.append(lst[:])  # copy of current list
            return
        
        # Include nums[index]
        lst.append(nums[index])
        self.backtrack(nums, n, ans, lst, index + 1)
        
        # Exclude nums[index]
        lst.pop()
        self.backtrack(nums, n, ans, lst, index + 1)
