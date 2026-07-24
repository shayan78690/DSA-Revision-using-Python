'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

from collections import deque
class Solution:
    def bottomView(self, root):
        if not root:
            return []
        q = deque()
        q.append((root, 0))
        mp = {}
        while q:
            node, col = q.popleft()
            mp[col] = node.data
            if node.left:
                q.append((node.left, col-1))
            if node.right:
                q.append((node.right, col+1))
        
        return [mp[col] for col in sorted(mp.keys())]
