# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        self.prev = None
        self.ans = float('inf')
        self.func(root)
        return self.ans
    
    def func(self, root):
        if not root:
            return
        self.func(root.left)
        if self.prev:
            self.ans = min(self.ans, root.val-self.prev.val)
        self.prev = root
        self.func(root.right)
