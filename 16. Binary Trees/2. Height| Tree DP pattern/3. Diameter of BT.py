# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        diameter = [0]
        self.dfs(root, diameter)
        return diameter[0]
    
    def dfs(self, root, diameter):
        if not root:
            return 0
        
        left = self.dfs(root.left, diameter)
        right = self.dfs(root.right, diameter)

        diameter[0] = max(diameter[0], left+right)

        return 1 + max(left, right)
        
