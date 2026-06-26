class Solution(object):
    def minimumCost(self, cost):
        n = len(cost)
        cost.sort(reverse=True)
        i = 0
        j = 1
        candies = 0
        while i < n:
            candies += cost[i] 
            if j < n:
                candies += cost[j]
            i += 3
            j += 3
        return candies
