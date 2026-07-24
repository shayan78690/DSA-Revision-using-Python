from collections import deque

class Solution:
    def minTime(self, root, target):
        if not root:
            return 0

        parentMap = {}
        self.findParent(root, parentMap)

        targetNode = self.findTarget(root, target)

        return self.bfs(targetNode, parentMap)

    def findParent(self, root, parentMap):
        q = deque([root])

        while q:
            node = q.popleft()

            if node.left:
                parentMap[node.left] = node
                q.append(node.left)

            if node.right:
                parentMap[node.right] = node
                q.append(node.right)

    def findTarget(self, root, target):
        if not root:
            return None

        if root.data == target:
            return root

        left = self.findTarget(root.left, target)
        if left:
            return left

        return self.findTarget(root.right, target)

    def bfs(self, targetNode, parentMap):
        q = deque([targetNode])
        visited = set([targetNode])

        time = 0

        while q:
            burned = False

            for _ in range(len(q)):
                node = q.popleft()

                if node.left and node.left not in visited:
                    visited.add(node.left)
                    q.append(node.left)
                    burned = True

                if node.right and node.right not in visited:
                    visited.add(node.right)
                    q.append(node.right)
                    burned = True

                if node in parentMap and parentMap[node] not in visited:
                    visited.add(parentMap[node])
                    q.append(parentMap[node])
                    burned = True

            if burned:
                time += 1

        return time
