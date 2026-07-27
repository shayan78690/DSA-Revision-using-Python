from collections import deque

class Solution:
    def eventualSafeNodes(self, graph):
        # Number of nodes
        n = len(graph)

        # Reverse graph
        # reverse[v] = list of nodes that point to v
        reverse = [[] for _ in range(n)]

        # This actually stores the OUTDEGREE of every node.
        # (The variable name "indegree" is commonly used in many solutions,
        # but technically it represents the number of outgoing edges.)
        indegree = [0] * n

        # -----------------------------
        # Build reverse graph
        # Count outgoing edges
        # -----------------------------
        for u in range(n):

            # Number of outgoing edges from node u
            indegree[u] = len(graph[u])

            # Reverse every edge
            #
            # Original:
            # u -----> v
            #
            # Reverse:
            # v -----> u
            #
            # This helps us move BACKWARDS from safe nodes.
            for v in graph[u]:
                reverse[v].append(u)

        # Queue for BFS (Topological Sort)
        queue = deque()

        # -----------------------------
        # Terminal nodes are safe
        # -----------------------------
        #
        # Terminal node = no outgoing edges
        #
        # Example:
        # 5 ->
        #
        # indegree[5] = 0
        #
        # Safe immediately.
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        # Stores all safe nodes
        safe = []

        # -----------------------------
        # BFS
        # -----------------------------
        while queue:

            # Current safe node
            node = queue.popleft()

            # Store answer
            safe.append(node)

            # Who points to this safe node?
            #
            # Example:
            #
            # Original:
            # 4 -> 5
            #
            # Reverse:
            # 5 -> 4
            #
            # If 5 is safe,
            # then maybe 4 also becomes safe.
            for parent in reverse[node]:

                # One outgoing edge of parent now leads
                # to a confirmed safe node.
                #
                # So reduce its remaining outgoing count.
                indegree[parent] -= 1

                # If parent has NO remaining outgoing edges
                # leading to unsafe nodes,
                # then parent itself becomes safe.
                if indegree[parent] == 0:
                    queue.append(parent)

        # Return answer in sorted order
        return sorted(safe)
