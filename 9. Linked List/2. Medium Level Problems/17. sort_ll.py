# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None or head.next == None:
            return head
        
        mid = self.findMidNode(head)
        righthead = mid.next
        mid.next = None

        left = self.sortList(head)
        right = self.sortList(righthead)

        return self.merge(left, right)
    
    def findMidNode(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, left, right):
        dummy = ListNode(-1)
        temp = dummy
        while left and right:
            if left.val <= right.val:
                temp.next = left
                left = left.next
                temp = temp.next
            else:
                temp.next = right
                right = right.next
                temp = temp.next
        
        while left:
            temp.next = left
            left = left.next
            temp = temp.next
        
        while right:
            temp.next = right
            right = right.next
            temp = temp.next
        
        return dummy.next
