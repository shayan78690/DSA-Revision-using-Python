# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution(object):
    def verticalTraversal(self, root):
        if not root:
            return []
        
        mp = defaultdict(list)
        q = deque()
        q.append((root, 0)) # root and col
        while q:
            node, col = q.popleft()
            mp[col].append(node.val)
            if node.left:
                q.append((node.left, col-1))
            if node.right:
                q.append((node.right, col+1))
        result = []
        for col in sorted(mp.keys()):
            result.append(mp[col])
        return result




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution(object):
    def verticalTraversal(self, root):
        if not root:
            return []
        
        mp = defaultdict(list)
        q = deque()
        q.append((root, 0, 0)) 
        while q:
            node, row, col = q.popleft()
            mp[col].append((row, node.val))
            if node.left:
                q.append((node.left, row+1, col-1))
            if node.right:
                q.append((node.right, row+1, col+1))
        result = []
        for col in sorted(mp.keys()):
            mp[col].sort()
            temp = []
            for row, val in mp[col]:
                temp.append(val)
            result.append(temp)
        return result
