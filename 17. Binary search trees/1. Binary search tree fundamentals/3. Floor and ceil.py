'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        if not root:
            return -1
        ans = -1
        while root:
            if root.data == k:
                return root.data
            elif root.data > k:
                root = root.left
            else:
                ans = root.data
                root = root.right
        return ans



'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self,root, x):
        if not root:
            return -1
        ans = -1
        while root:
            if root.data == x:
                return root.data
            elif root.data < x:
                root = root.right
            else:
                ans = root.data
                root = root.left
        return ans
