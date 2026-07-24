# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        result = []
        if not root:
            return result
        q = deque()
        q.append(root)
        count = 0
        while q:
            path = []
            for _ in range(len(q)):
                node = q.popleft()
                path.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            count += 1
            if count % 2 != 0:
                result.append(path[:])
            else:
                path.reverse()
                result.append(path[:])
        return result
            
        
