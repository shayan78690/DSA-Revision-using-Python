
import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Pair:
    def __init__(self, value, node):
        self.value = value
        self.node = node

    # Min-heap behavior (same as Java compareTo)
    def __lt__(self, other):
        return self.value < other.value


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists) == 0:
            return None

        pq = []

        # Push the head of each list into min-heap
        for node in lists:
            if node is not None:
                heapq.heappush(pq, Pair(node.val, node))

        dummy = ListNode(-1)
        temp = dummy

        # Merge using PQ
        while pq:
            p = heapq.heappop(pq)

            temp.next = p.node
            temp = temp.next

            if p.node.next:
                heapq.heappush(pq, Pair(p.node.next.val, p.node.next))

        return dummy.next
