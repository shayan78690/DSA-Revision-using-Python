class Solution:
    def removeCoveredIntervals(self, intervals):
        # Step 1: sort intervals
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        max_end = 0

        # Step 2: traverse intervals
        for start, end in intervals:
            if end > max_end:
                count += 1
                max_end = end

        return count

