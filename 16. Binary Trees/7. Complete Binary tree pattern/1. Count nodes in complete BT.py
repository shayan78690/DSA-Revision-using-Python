# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        return self.dfs(root)
    
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return 1 + left + right


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def leftHeight(self, root):
        h = 0
        while root:
            h += 1
            root = root.left
        return h
    
    def rightHeight(self, root):
        h = 0
        while root:
            h += 1
            root = root.right
        return h

    def countNodes(self, root):
        if not root:
            return 0
        left = self.leftHeight(root)
        right = self.rightHeight(root)
        if left == right:
            return 2**left-1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
