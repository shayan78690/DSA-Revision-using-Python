# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def distanceK(self, root, target, k):
        if not root:
            return []
        parentMap = {}
        self.findParent(root, parentMap)
        return self.bfs(root, target, k, parentMap)

    

    def findParent(self, root, parentMap):
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.left:
                parentMap[node.left] = node
                q.append(node.left)
            if node.right:
                parentMap[node.right] = node
                q.append(node.right)

    def bfs(self, root, target, k, parentMap):
        q = deque()
        visited = set()
        q.append(target)
        visited.add(target)
        level = 0
        while q:
            if level == k:
                break
            for _ in range(len(q)):
                node = q.popleft()
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    q.append(node.left)
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    q.append(node.right)
                
                if node in parentMap and parentMap[node] not in visited:
                    visited.add(parentMap[node])
                    q.append(parentMap[node])
            level += 1
        
        result = []
        while q:
            node = q.popleft()
            result.append(node.val)
        return result

                
        
