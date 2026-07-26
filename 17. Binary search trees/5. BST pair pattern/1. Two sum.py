# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        if not root:
            return False
        sorted_list = []
        self.inorder(root, sorted_list)
        left = 0
        right = len(sorted_list)-1
        while left < right:
            s = sorted_list[left] + sorted_list[right]
            if s == k:
                return True
            elif s < k:
                left = left + 1
            else:
                right = right - 1
        return False
    def inorder(self, root, sorted_list):
        if not root:
            return
        self.inorder(root.left, sorted_list)
        sorted_list.append(root.val)
        self.inorder(root.right, sorted_list)





# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        hashset = set()
        return self.dfs(root, k, hashset)
    
    def dfs(self, root, k, hashset):
        if not root:
            return False
        if k-root.val in hashset:
            return True
        hashset.add(root.val)
        return self.dfs(root.left, k, hashset) or self.dfs(root.right, k, hashset)

        
