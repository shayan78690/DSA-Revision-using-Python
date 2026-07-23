from collections import deque
"""
Definition of Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def paths(self, root):
        ans = []
        path = []
        self.func(root, ans, path)
        return ans
    
    def func(self, root, ans, path):
        if not root:
            return
        path.append(root.data)
        if not root.left and not root.right:
            ans.append(path[:])
        else:
            self.func(root.left, ans, path)
            self.func(root.right, ans, path)
        path.pop()
