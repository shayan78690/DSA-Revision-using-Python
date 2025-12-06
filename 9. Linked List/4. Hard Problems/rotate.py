# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k == 0:
            return head
        
        size = 1
        tail = head
        while tail.next:
            tail = tail.next
            size += 1
        
        k = k % size
        if k == 0:
            return head
        
        tail.next = head
         
        steps_to_newhead = size-k-1
        newtail = head
        while steps_to_newhead > 0:
            newtail = newtail.next
            steps_to_newhead -= 1
        head = newtail.next
        newtail.next = None
        return head
