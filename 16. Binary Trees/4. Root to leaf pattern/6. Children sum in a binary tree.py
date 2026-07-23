'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        left = root.left.data if root.left else 0
        right = root.right.data if root.right else 0

        return (root.data == left + right and
                self.isSumProperty(root.left) and
                self.isSumProperty(root.right))
