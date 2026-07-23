# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        left = self.height(root.left)
        right = self.height(root.right)

        if abs(left-right) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        result = self.helper(root)
        return result != -1
    
    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        if left == -1:
            return -1
        right = self.helper(root.right)
        if right == -1:
            return -1
        if abs(left-right) > 1:
            return -1
        return 1 + max(left, right)
        
