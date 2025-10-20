"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        m = {}
        temp = head
        while temp:
            copy = Node(temp.val)
            m[temp] = copy
            temp = temp.next
        
        temp = head
        while temp:
            copy = m[temp]
            copy.next = m.get(temp.next)
            copy.random = m.get(temp.random)
            temp = temp.next
        return m[head]