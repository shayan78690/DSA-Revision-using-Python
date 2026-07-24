'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''        

class Solution:
    def leafSum(self, root):
        self.sum = 0
        self.func(root)
        return self.sum
    
    def func(self, root):
        if not root:
            return 0
        
        if not root.left and not root.right:
            self.sum += root.data
        
        self.func(root.left)
        self.func(root.right)
