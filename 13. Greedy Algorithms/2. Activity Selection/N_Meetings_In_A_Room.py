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
