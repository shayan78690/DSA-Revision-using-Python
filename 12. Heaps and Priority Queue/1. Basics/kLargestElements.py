import heapq

class Solution:
	def kLargest(self, arr, k):
		pq = []
		for a in arr:
		    heapq.heappush(pq, a)
		    if len(pq) > k:
		        heapq.heappop(pq)
		
		result = [0] * k
		index = k-1
		while len(pq) > 0:
		    val = heapq.heappop(pq)
		    result[index] = val
		    index -= 1
		return result
