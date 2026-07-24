'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
        
    def left(self, root, result):
        current = root.left
        while current:
            if current.left or current.right:
                result.append(current.data)
            if current.left:
                current = current.left
            else:
                current = current.right
    
    def leaf(self, root, result):
        if not root:
            return None
        if not root.left and not root.right:
            result.append(root.data)
        self.leaf(root.left, result)
        self.leaf(root.right, result)
    
    def right(self, root, result):
        current = root.right
        stack = []
        while current:
            if current.left or current.right:
                stack.append(current.data)
            if current.right:
                current = current.right
            else:
                current = current.left
        while stack:
            result.append(stack.pop())
        
    def boundaryTraversal(self, root):
        if not root:
            return []
        result = []
        if root.left or root.right:
            result.append(root.data)
        self.left(root, result)
        self.leaf(root, result)
        self.right(root, result)
        return result
