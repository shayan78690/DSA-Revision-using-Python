# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        return self.func(nums, 0, len(nums)-1)
    
    def func(self, nums, low, high):
        if low > high:
            return None
        maxi = float('-inf')
        idx = -1
        for i in range(low, high+1):
            if nums[i] > maxi:
                maxi = nums[i]
                idx = i
        root = TreeNode(maxi)
        root.left = self.func(nums, low, idx-1)
        root.right = self.func(nums, idx+1, high)
        return root
        
