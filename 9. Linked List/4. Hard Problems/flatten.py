# Definition for Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None

class Solution:
    # Function to flatten a linked list
    def flatten(self, root):
        if root is None or root.next is None:
            return root
        
        mergedRoot = self.flatten(root.next)
        return self.merge(root, mergedRoot)
    
    def merge(self, l1, l2):
        dummy = Node(-1)
        res = dummy
        while l1 is not None and l2 is not None:
            if l1.data < l2.data:
                res.bottom = l1
                res = l1
                l1 = l1.bottom
            else:
                res.bottom = l2
                res = l2
                l2 = l2.bottom
            res.next = None
        
        if l1 is not None:
            res.bottom = l1
        else:
            res.bottom = l2
        
        return dummy.bottom
