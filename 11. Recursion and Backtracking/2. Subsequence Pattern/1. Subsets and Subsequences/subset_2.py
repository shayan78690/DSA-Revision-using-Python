class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        lst = []
        nums.sort()  # sort to handle duplicates
        self.backtrack(nums, len(nums), ans, lst, 0)
        return ans

    def backtrack(self, nums, n, ans, lst, index):
        ans.append(lst[:])  # add copy of current list

        for i in range(index, n):
            if i > index and nums[i] == nums[i - 1]:
                continue
            lst.append(nums[i])
            self.backtrack(nums, n, ans, lst, i + 1)
            lst.pop()
