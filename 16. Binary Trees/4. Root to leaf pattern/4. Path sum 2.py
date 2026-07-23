# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        ans = []

        def dfs(node, remaining, path):
            if node is None:
                return

            path.append(node.val)
            remaining -= node.val

            if node.left is None and node.right is None:
                if remaining == 0:
                    ans.append(path[:])
            else:
                dfs(node.left, remaining, path)
                dfs(node.right, remaining, path)

            path.pop()

        dfs(root, targetSum, [])
        return ans
