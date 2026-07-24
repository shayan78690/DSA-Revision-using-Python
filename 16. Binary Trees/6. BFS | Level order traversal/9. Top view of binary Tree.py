'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque
class Solution:
    def topView(self, root):
        if not root:
            return []
        q = deque()
        q.append((root, 0))
        mp = {}
        while q:
            node, col = q.popleft()
            if col not in mp:
                mp[col] = node.data
            if node.left:
                q.append((node.left, col-1))
            if node.right:
                q.append((node.right, col+1))
        
        return [mp[col] for col in sorted(mp.keys())]
