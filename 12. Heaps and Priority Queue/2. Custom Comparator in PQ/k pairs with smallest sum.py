import heapq

class Tuple:
    def __init__(self, first, second, sum_):
        self.first = first
        self.second = second
        self.sum = sum_

    def __lt__(self, other):
        return self.sum < other.sum


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        n = len(nums1)
        m = len(nums2)

        pq = []  # min-heap

        # Insert first element paired with up to k elements of nums2
        for i in range(min(m, k)):
            heapq.heappush(pq, Tuple(0, i, nums1[0] + nums2[i]))

        ans = []

        while pq and k > 0:
            t = heapq.heappop(pq)
            ans.append([nums1[t.first], nums2[t.second]])

            if t.first + 1 < n:
                heapq.heappush(
                    pq,
                    Tuple(t.first + 1, t.second, nums1[t.first + 1] + nums2[t.second])
                )

            k -= 1

        return ans
