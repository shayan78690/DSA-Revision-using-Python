# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        result = []
        self.func(root, targetSum, result, [])
        return result
    
    def func(self, root, targetSum, result, path):
        if not root:
            return
        
        path.append(root.val)
        targetSum -= root.val
        if not root.left and not root.right:
            if targetSum == 0:
                result.append(path[:])
        else:
            self.func(root.left, targetSum, result, path)
            self.func(root.right, targetSum, result, path)
        path.pop()
