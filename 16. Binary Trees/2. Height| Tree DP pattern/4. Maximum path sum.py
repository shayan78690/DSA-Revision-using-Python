# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.maxSum = float('-inf')
        self.dfs(root)
        return self.maxSum
    
    def dfs(self, root):
        if not root:
            return 0
        left = max(0, self.dfs(root.left))
        right = max(0, self.dfs(root.right))
        self.maxSum = max(self.maxSum, left+right+root.val)

        return root.val + max(left, right)

