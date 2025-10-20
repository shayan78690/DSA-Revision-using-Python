# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reverse(self, head):
        current = head
        prev = None
        while current:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        return prev
    
    def getKthNode(self, temp, k):
        k -= 1
        while temp and k > 0:
            k -= 1
            temp = temp.next
        return temp

    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        temp = head
        prevLast = None
        while temp:
            kthNode = self.getKthNode(temp, k)
            if kthNode == None:
                if prevLast:
                    prevLast.next = temp
                    break
            nextNode = kthNode.next
            kthNode.next = None

            self.reverse(temp)

            if temp == head:
                head = kthNode
            else:
                prevLast.next = kthNode
            prevLast = temp
            temp = nextNode
        return head
        