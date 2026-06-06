class Solution(object):
    def canWeDistribute(self, arr, m, force):
        balls = 1
        lastBall = arr[0]

        for i in range(1, len(arr)):
            if arr[i] - lastBall >= force:
                balls += 1
                lastBall = arr[i]

        return balls >= m

    def maxDistance(self, position, m):
        position.sort()

        low = 1
        high = position[-1] - position[0]
        ans = 1

        while low <= high:
            mid = (low + high) // 2

            if self.canWeDistribute(position, m, mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
