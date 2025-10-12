# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def findMidNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow:
            return slow
        return None

    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        midNode = self.findMidNode(head)

        prev = None
        current = midNode
        while current:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        right = prev
        left = head
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True