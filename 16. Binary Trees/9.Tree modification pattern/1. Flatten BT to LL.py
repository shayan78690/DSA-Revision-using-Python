# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        if not root:
            return
        stack = [root]
        prev = None
        while stack:
            node = stack.pop()
            if prev:
                prev.right = node
                prev.left = None
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            prev = node
