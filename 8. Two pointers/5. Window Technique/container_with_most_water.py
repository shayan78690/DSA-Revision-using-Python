class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = float('-inf')
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                water = (j-i) * min(height[i], height[j])
                max_water = max(water, max_water)
        return max_water
    
class Solution1(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n-1
        max_water = float('-inf')
        while left < right:
            h = min(height[left], height[right])
            w = right-left
            area = h * w
            max_water = max(max_water, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water