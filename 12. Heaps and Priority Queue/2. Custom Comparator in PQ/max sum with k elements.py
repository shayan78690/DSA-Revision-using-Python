import heapq

class Node:
    def __init__(self, val):
        self.val = val

    # max-heap behavior
    def __lt__(self, other):
        return self.val > other.val


class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = []

        # push all nums into max-heap
        for num in nums:
            heapq.heappush(pq, Node(num))

        maxSum = 0

        for _ in range(k):
            top_node = heapq.heappop(pq)
            top = top_node.val
            maxSum += top

            # push back top + 1
            heapq.heappush(pq, Node(top + 1))

        return maxSum
