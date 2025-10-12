class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = n
        fast = n
        while True:
            slow = self.findSquare(slow)
            fast = self.findSquare(self.findSquare(fast))
            if slow == fast:
                break
        return slow == 1
    
    def findSquare(self, n):
        ans = 0
        while n > 0:
            rem = n % 10
            ans += rem * rem
            n = n // 10
        return ans

        