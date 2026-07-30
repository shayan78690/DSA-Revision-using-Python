class Solution:
    def bellmanFord(self, V, edges, src):
        # Step 1: Initialize distance array
        dist = [100000000] * V
        dist[src] = 0

        # Step 2: Relax all edges V-1 times
        for _ in range(V - 1):
            for u, v, wt in edges:
                # If u is reachable and going through u gives a shorter path to v
                if dist[u] != 100000000 and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt

        # Step 3: Check for Negative Weight Cycle
        for u, v, wt in edges:
            if dist[u] != 100000000 and dist[u] + wt < dist[v]:
                return [-1]

        # Step 4: Return shortest distances
        return dist


