# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        self.index = 0
        return self.func(preorder, float('inf'))
    
    def func(self, preorder, maxi):
        if self.index == len(preorder) or preorder[self.index] > maxi:
            return None
        root = TreeNode(preorder[self.index])
        self.index += 1
        root.left = self.func(preorder, root.val)
        root.right = self.func(preorder, maxi)
        return root
