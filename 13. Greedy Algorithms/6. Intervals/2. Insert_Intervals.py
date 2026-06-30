class Solution(object):
    def insert(self, intervals, newInterval):
        result = []
        for start, end in intervals:
            result.append([start, end])
        result.append(newInterval)
        result.sort()
        ans = []
        ans.append(result[0])
        for i in range(len(result)):
            start = result[i][0]
            end = result[i][1]
            if start <= ans[-1][1]:
                ans[-1][0] = min(ans[-1][0], start)
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([start, end])
        return ans
        

class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)

        # Add all intervals that end before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        # Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result

