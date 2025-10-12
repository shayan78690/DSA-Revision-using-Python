class Solution:
    def reverse(self, head):
        current = head
        prev = None
        while current:
            next_ = current.next
            current.next = prev
            current.prev = next_
            prev = current
            current = next_
        
        return prev
        