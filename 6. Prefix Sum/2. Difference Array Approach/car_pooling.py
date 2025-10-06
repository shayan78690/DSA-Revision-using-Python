class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        prefix = [0] * 1001

        # Step 2: Apply boundary updates for each trip
        for trip in trips:
            val = trip[0]    # number of passengers
            start = trip[1]  # pick-up location
            end = trip[2]    # drop-off location

            prefix[start] += val
            prefix[end] -= val

        # Step 3: Compute running sum to check capacity at every point
        total = 0
        for i in range(len(prefix)):
            total += prefix[i]
            if total > capacity:
                return False

        return True

        