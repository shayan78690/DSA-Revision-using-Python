# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        self.prev = None
        self.first = None
        self.second = None
        self.inorder(root)

        self.first.val, self.second.val = self.second.val, self.first.val

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if self.prev and root.val < self.prev.val:
            if not self.first:
                self.first = self.prev
            self.second = root
        self.prev = root 
        self.inorder(root.right)
        
