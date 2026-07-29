import heapq
class Solution(object):
    def minimumEffortPath(self, heights):
        n, m = len(heights), len(heights[0])
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        minheap = []
        heapq.heappush(minheap, (0, 0, 0))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while minheap:
            effort, r, c = heapq.heappop(minheap)
            if r == n-1 and c == m-1:
                return dist[r][c]
            if effort > dist[r][c]:
                continue
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < n and 0 <= nc < m:
                    edge_cost = abs(heights[r][c]-heights[nr][nc])
                    new_effort = max(effort, edge_cost)
                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(minheap, (new_effort, nr, nc))
        return -1
