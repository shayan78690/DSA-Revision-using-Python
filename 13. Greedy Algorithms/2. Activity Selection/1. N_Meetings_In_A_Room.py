class Solution:
    def maximumMeetings(self,start,end):
        n = len(start)
        meetings = []
        for i in range(n):
            meetings.append([start[i], end[i]])
        
        meetings.sort(key = lambda x : x[1])
        
        lastEnd = -1
        count = 0
        for s, e in meetings:
            if s > lastEnd:
                count += 1
                lastEnd = e
                
        return count



class Solution:
    def maxMeetings(self, s: list[int], f: list[int]) -> list[int]:
        n = len(s)
        meetings = []
        for i in range(n):
            meetings.append([s[i], f[i], i+1])
        meetings.sort(key = lambda x: x[1])
        result = []
        lastend = -1
        for start, end, idx in meetings:
            if start > lastend:
                result.append(idx)
                lastend = end
        result.sort()
        return result
