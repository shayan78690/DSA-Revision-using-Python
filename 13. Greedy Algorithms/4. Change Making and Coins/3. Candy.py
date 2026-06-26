class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        return sum(candies)


class Solution:
    def candy(self, arr):
        n = len(arr)
        left = [0] * n
        right = [0] * n

        left[0] = 1
        right[n - 1] = 1

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1

        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                right[i] = right[i + 1] + 1
            else:
                right[i] = 1

        candies = 0
        for i in range(n):
            candies += max(left[i], right[i])

        return candies

