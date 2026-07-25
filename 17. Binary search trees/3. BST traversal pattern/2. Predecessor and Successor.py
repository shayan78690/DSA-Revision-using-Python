class Solution:
    def findPreSuc(self, root, key):
        predecessor = None
        successor = None

        curr = root

        while curr:
            if key < curr.data:
                successor = curr
                curr = curr.left
            else:
                curr = curr.right

        curr = root

        while curr:
            if key > curr.data:
                predecessor = curr
                curr = curr.right
            else:
                curr = curr.left

        return predecessor, successor
