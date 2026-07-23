# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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

    def distanceK(self, root, target, k):
        parentMap = {}
        self.findParent(parentMap, root)

        visited = set()
        q = deque([target])
        visited.add(target)

        level = 0

        while q:
            size = len(q)

            if level == k:
                break

            level += 1

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

        ans = []

        while q:
            ans.append(q.popleft().val)

        return ans
