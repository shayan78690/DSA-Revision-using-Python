from collections import deque

class Solution(object):
    def widthOfBinaryTree(self, root):
        if not root:
            return 0

        q = deque()
        q.append((root, 0))

        maxWidth = 0

        while q:
            first = last = 0
            size = len(q)
            for i in range(size):
                node, idx = q.popleft()
                if i == 0:
                    first = idx
                if i == size-1:
                    last = idx
                if node.left:
                    q.append((node.left, 2*idx+1))
                if node.right:
                    q.append((node.right, 2*idx+2))
            maxWidth = max(maxWidth, last-first+1)

        return maxWidth















from collections import deque

class Solution(object):
    def widthOfBinaryTree(self, root):
        if not root:
            return 0

        q = deque()
        q.append((root, 0))

        maxWidth = 0
# To avoid huge numbers, normalize the indices at each level:
        while q:
            first = last = 0
            size = len(q)
            start = q[0][1]
            for i in range(size):
                node, idx = q.popleft()
                idx -= start
                if i == 0:
                    first = idx
                if i == size-1:
                    last = idx
                if node.left:
                    q.append((node.left, 2*idx+1))
                if node.right:
                    q.append((node.right, 2*idx+2))
            maxWidth = max(maxWidth, last-first+1)

        return maxWidth
