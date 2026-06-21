from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        ans = []
        
        left = head
        right = self.findTail(head)
        
        while left is not None and right is not None and left.data < right.data:
            if left.data + right.data == target:
                ans.append([left.data, right.data])
                left = left.next
                right = right.prev
            elif left.data + right.data < target:
                left = left.next
            else:
                right = right.prev
                
        return ans
        
    def findTail(self, head):
        if head is None:
            return None
        tail = head
        while tail.next is not None:
            tail = tail.next
        return tail
    
        
