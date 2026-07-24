# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):

    def findParent(self, root, parentMap):
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.left:
                parentMap[node.left] = node
                queue.append(node.left)
            if node.right:
                parentMap[node.right] = node
                queue.append(node.right)
    
    def findTargetNode(self, root, start):
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.val == start:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return None
    
    def bfs(self, root, target, parentMap):
        queue = deque()
        visited = set()
        queue.append(target)
        visited.add(target)
        time = -1
        while queue:
            time += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)
                if node in parentMap and parentMap[node] not in visited:
                    visited.add(parentMap[node])
                    queue.append(parentMap[node])
        return time

    def amountOfTime(self, root, start):
        if not root:
            return 0
        parentMap = {}
        self.findParent(root, parentMap)
        targetNode = self.findTargetNode(root, start)
        return self.bfs(root, targetNode, parentMap)
        
