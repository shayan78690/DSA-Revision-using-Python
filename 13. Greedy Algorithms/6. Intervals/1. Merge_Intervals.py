class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        intervals.sort()
        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if ans and end <= ans[-1][1]:
                continue
            for j in range(i+1, len(intervals)):
                if intervals[j][0] <= end:
                    end = max(end, intervals[j][1])
                else:
                    break
            ans.append([start, end])
        return ans



class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        intervals.sort()
        for i in range(len(intervals)):
            if not ans or intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
        return ans



class Solution(object):
    def merge(self, intervals):
        n = len(intervals)
        intervals.sort()
        result = []
        result.append(intervals[0])
        for i in range(1, n):
            start = intervals[i][0]
            end = intervals[i][1]
            if start <= result[-1][1]:
                result[-1][0] = min(result[-1][0], start)
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])
        return result
