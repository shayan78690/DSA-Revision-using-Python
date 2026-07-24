# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        result = []
        if not root:
            return result
        q = deque()
        q.append(root)
        while q:
            s = 0.0
            size = 0
            for _ in range(len(q)):
                node = q.popleft()
                s += node.val
                size += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(s / size)
        return result
