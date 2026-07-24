# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        self.sum = 0
        self.func(root)
        return self.sum
    
    def func(self, root):
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            self.sum += root.left.val
        
        self.func(root.left)
        self.func(root.right)
        
