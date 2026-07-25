# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        if not root:
            return []
        freq = {}
        self.inorder(root, freq)
        maxFreq = max(freq.values())
        result = []
        for key in freq.keys():
            if freq[key] == maxFreq:
                result.append(key)
        return result

    def inorder(self, root, freq):
        if not root:
            return
        self.inorder(root.left, freq)
        freq[root.val] = freq.get(root.val, 0) + 1
        self.inorder(root.right, freq)
        
