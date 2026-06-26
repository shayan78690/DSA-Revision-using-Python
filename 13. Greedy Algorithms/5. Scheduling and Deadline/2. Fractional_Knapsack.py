class Pair:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight


class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        n = len(val)
        items = []
        
        for i in range(n):
            items.append(Pair(val[i], wt[i]))
        
        items.sort(key=lambda x: x.ratio, reverse = True)
        
        total = 0.0
        for item in items:
            if capacity >= item.weight:
                total += item.value
                capacity -= item.weight
            else:
                total += item.ratio * capacity
                break
        return total
        
