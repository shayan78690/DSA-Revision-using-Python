# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        s = set()
        temp = head
        while temp:
            if temp in s:
                return True
            s.add(temp)
        return False
        
        
    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False