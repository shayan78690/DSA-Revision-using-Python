# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        result = []

        if root:
            self.dfs(root, "", result)

        return result

    def dfs(self, node, path, result):
        if not node.left and not node.right:
            result.append(path + str(node.val))
            return

        if node.left:
            self.dfs(node.left, path + str(node.val) + "->", result)

        if node.right:
            self.dfs(node.right, path + str(node.val) + "->", result)
