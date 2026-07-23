# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        if root is None:
            return 0

        def countPaths(node, remaining):
            if node is None:
                return 0

            count = 0

            if node.val == remaining:
                count += 1

            count += countPaths(node.left, remaining - node.val)
            count += countPaths(node.right, remaining - node.val)

            return count

        return (countPaths(root, targetSum) +
                self.pathSum(root.left, targetSum) +
                self.pathSum(root.right, targetSum))
