class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def addOne(self,head):
        carry = 1
        head = self.reverse(head)
        
        temp = head
        while temp:
            temp.data += carry
            if temp.data < 10:
                carry = 0
                break
            else:
                temp.data = 0
                carry = 1
            temp = temp.next
        
        if carry == 1:
            node = Node(1)
            head = self.reverse(head)
            node.next = head
            head = node
            return head
        head = self.reverse(head)
        return head
    
    def reverse(self, head):
        current = head
        prev = None
        while current:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
            head = prev
        return head