# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        return self.func(root, float('-inf'), float('inf'))
    
    def func(self, root, mini, maxi):
        if not root:
            return True
        if root.val <= mini or root.val >= maxi:
            return False
        return self.func(root.left, mini, root.val) and self.func(root.right, root.val, maxi)
