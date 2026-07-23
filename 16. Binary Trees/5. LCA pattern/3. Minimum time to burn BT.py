# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):

    def findParent(self, parentMap, root):
        q = deque([root])

        while q:
            node = q.popleft()

            if node.left:
                parentMap[node.left] = node
                q.append(node.left)

            if node.right:
                parentMap[node.right] = node
                q.append(node.right)

    def findStart(self, root, start):
        if not root:
            return None

        if root.val == start:
            return root

        left = self.findStart(root.left, start)
        if left:
            return left

        return self.findStart(root.right, start)

    def amountOfTime(self, root, start):
        parentMap = {}
        self.findParent(parentMap, root)

        startNode = self.findStart(root, start)

        visited = set()
        q = deque([startNode])
        visited.add(startNode)

        time = -1

        while q:
            size = len(q)
            time += 1

            for _ in range(size):
                node = q.popleft()

                if node.left and node.left not in visited:
                    visited.add(node.left)
                    q.append(node.left)

                if node.right and node.right not in visited:
                    visited.add(node.right)
                    q.append(node.right)

                parent = parentMap.get(node)
                if parent and parent not in visited:
                    visited.add(parent)
                    q.append(parent)

        return time
