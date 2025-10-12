# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        current = mid.next
        mid.next = None
        prev = None
        while current:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        
        left = head
        right = prev
        while left and right:
            nextL = left.next
            left.next = right
            nextR = right.next
            right.next = nextL

            left = nextL
            right = nextR