# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        temp = dummy
        carry = 0
        while l1 or l2:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            newnode = ListNode(s % 10)
            carry  = s // 10
            temp.next = newnode
            temp = temp.next
        if carry > 0:
            node = ListNode(carry)
            temp.next = node
        return dummy.next
        