#Back-end complete function Template for Python 3

'''
# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
		        self.prev = None
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        current = head
        while current and current.next:
            if current.data == current.next.data:
            # Skip the duplicate node
                current.next = current.next.next
                if current.next:
                    current.next.prev = current
            else:
                current = current.next
        return head