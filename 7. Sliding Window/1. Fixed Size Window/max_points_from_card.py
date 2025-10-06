class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        leftsum = 0
        rightsum = 0
        max_sum = 0
        for i in range(k):
            leftsum += cardPoints[i]
        
        max_sum = leftsum
        rightIdx = n-1
        for i in range(k-1, -1, -1):
            leftsum -= cardPoints[i]
            rightsum += cardPoints[rightIdx]
            rightIdx -= 1
            max_sum = max(max_sum, leftsum+rightsum)
        return max_sum