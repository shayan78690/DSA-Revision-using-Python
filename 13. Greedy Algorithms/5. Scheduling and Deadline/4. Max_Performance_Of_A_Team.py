import heapq

class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        mod = 10**9 + 7
        engineers = list(zip(efficiency, speed))
        engineers.sort(reverse = True)
        
        maxheap = []
        speedSum = 0
        ans = 0
        for eff, speed in engineers:
            speedSum += speed
            heapq.heappush(maxheap, speed)

            if len(maxheap) > k:
                speedSum -= heapq.heappop(maxheap)

            ans = max(ans, speedSum * eff)
        return ans % mod
