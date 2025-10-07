class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        leftmax = [0] * n
        leftmax[0] = height[0]
        for i in range(1, n):
            leftmax[i] = max(leftmax[i-1], height[i])
        
        rightmax = [0] * n
        rightmax[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            rightmax[i] = max(rightmax[i+1], height[i])
        
        water_trapped = 0
        for i in range(n):
            water = min(leftmax[i], rightmax[i])
            water_trapped += water - height[i]
        return water_trapped
    
class Solution1(object):
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
