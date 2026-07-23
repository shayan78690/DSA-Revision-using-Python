# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.maxSum = float('-inf')
        self.bfs(root)
        return self.maxSum
    
    def bfs(self, root):
        if not root:
            return 0
        left = max(0, self.bfs(root.left))
        right = max(0, self.bfs(root.right))
        self.maxSum = max(self.maxSum, left+right+root.val)

        return root.val + max(left, right)
        
