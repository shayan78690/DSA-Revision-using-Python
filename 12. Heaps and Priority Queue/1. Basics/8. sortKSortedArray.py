import heapq

class Solution:
    def nearlySorted(self, arr, k):  
        #code here
        n = len(arr)
        pq = []
        index = 0

        for i in range(n):
            heapq.heappush(pq, arr[i])
            if len(pq) > k:
                arr[index] = heapq.heappop(pq)
                index += 1

        while pq:
            arr[index] = heapq.heappop(pq)
            index += 1
