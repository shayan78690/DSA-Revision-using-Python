#User function Template for python3
'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        if head == None:
            return head
            
        temp = head
        while temp:
            if temp.data == x:
                if temp == head:
                    head = head.next
                
                prev_ = temp.prev
                next_ = temp.next
                if prev_:
                    prev_.next = next_
                if next_:
                    next_.prev = prev_
                temp.prev_ = None
                temp.next_ = None
                
                temp = next_
            else:
                temp = temp.next
        return head