class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x : x[1])
        maxintervals = 0
        lastend = float('-inf')
        for start, end in intervals:
            if start >= lastend:
                maxintervals += 1
                lastend = end
        return len(intervals)-maxintervals
        
