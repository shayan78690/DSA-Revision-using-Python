class NumArray(object):
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.prefix = [0] * n
        self.prefix[0] = nums[0]

        for i in range(1, n):
            self.prefix[i] = self.prefix[i - 1] + nums[i]
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)