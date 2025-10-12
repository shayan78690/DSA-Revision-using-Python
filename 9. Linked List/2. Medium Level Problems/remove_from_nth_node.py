# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        temp = head
        size = 0
        while temp:
            temp = temp.next
            size += 1
        if n == size:
            head = head.next
            return head
        
        prev = head
        index = 1
        while index < size-n:
            prev = prev.next
            index += 1
        prev.next = prev.next.next
        return head