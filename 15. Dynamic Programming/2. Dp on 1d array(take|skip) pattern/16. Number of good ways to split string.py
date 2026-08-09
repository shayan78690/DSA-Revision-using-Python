class Solution(object):
    def numSplits(self, s):
        n = len(s)
        right = [0] * n
        seen = set()
        for i in range(n-1, -1, -1):
            seen.add(s[i])
            right[i] = len(seen)
        
        left = set()
        count = 0
        for i in range(n-1):
            left.add(s[i])
            left_count = len(left)
            right_count = right[i+1]
            if left_count == right_count:
                count += 1
        return count
