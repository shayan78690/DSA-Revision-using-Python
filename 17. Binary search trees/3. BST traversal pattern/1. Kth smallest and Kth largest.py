# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        self.i = 0
        return self.func(root, k)
    
    def func(self, root, k):
        if not root:
            return -1
        left = self.func(root.left, k)
        if left != -1:
            return left
        self.i += 1
        if self.i == k:
            return root.val
        return self.func(root.right, k)
        

'''Structure of a Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def kthLargest(self, root, k):
        self.count = 0
        return self.func(root, k)
    
    def func(self, root, k):
        if not root:
            return -1
        right = self.func(root.right, k)
        if right != -1:
            return right
        self.count += 1
        if self.count == k:
            return root.data
        return self.func(root.left, k)
        
