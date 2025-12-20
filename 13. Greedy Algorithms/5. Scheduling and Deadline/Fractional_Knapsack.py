class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight


class Solution:
    # Function to get the maximum total value in the knapsack
    def fractionalKnapsack(self, val, wt, capacity):
        n = len(val)
        items = []

        for i in range(n):
            items.append(Item(val[i], wt[i]))

        # sort items by value/weight ratio (descending)
        items.sort(key=lambda x: x.ratio, reverse=True)

        totalVal = 0.0

        for item in items:
            if capacity >= item.weight:
                totalVal += item.value
                capacity -= item.weight
            else:
                totalVal += item.ratio * capacity
                break

        return totalVal

