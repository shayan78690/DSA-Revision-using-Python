''' 
class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''
from collections import deque
class Solution:
    def leftView(self, root):
        if not root:
            return []
        result = []
        q = deque()
        q.append(root)
        while q:
            count = 0
            for _ in range(len(q)):
                node = q.popleft()
                count += 1
                if count == 1:
                    result.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result




''' 
class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''
from collections import deque
class Solution:
    def leftView(self, root):
        if not root:
            return []
        result = []
        self.dfs(root, result, 0)
        return result
    
    def dfs(self, root, result, level):
        if not root:
            return
        if level == len(result):
            result.append(root.data)
        self.dfs(root.left, result, level+1)
        self.dfs(root.right, result, level+1)
