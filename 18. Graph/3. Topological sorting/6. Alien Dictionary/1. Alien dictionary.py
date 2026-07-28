from collections import deque, defaultdict

class Solution:
    def findOrder(self, words):
        graph = defaultdict(set)
        indegree = {}
        
        for word in words:
            for ch in word:
                indegree[ch] = 0
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break
            
        q = deque()
        for ch in indegree:
            if indegree[ch] == 0:
                q.append(ch)
        
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        return "".join(order) if len(order) == len(indegree) else "" 
