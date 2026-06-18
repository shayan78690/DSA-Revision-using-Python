class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n-1
        total = 0
        leftmax = 0
        rightmax = 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] >= leftmax:
                    leftmax = height[left]
                else:
                    total += leftmax-height[left]
                left += 1
            else:
                if height[right] >= rightmax:
                    rightmax = height[right]
                else:
                    total += rightmax-height[right]
                right -= 1
        return total
