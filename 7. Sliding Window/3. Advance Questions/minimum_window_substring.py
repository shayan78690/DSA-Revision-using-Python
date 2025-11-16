class Solution:
    def func(self, s, t):
        n = len(s)
        m = len(t)
        freq = [0] * 256
        for i in range(m):
            ch = t[i]
            freq[ord(ch)] += 1
        count = 0
        left = 0
        right = 0
        start = -1
        mini = float('inf')
        while right < n:
            ch = s[right]
            if freq[ord(ch)] > 0:
                count += 1
            freq[ord(ch)] -= 1
            while count == m:
                if right-left+1 < mini:
                    mini = right-left+1
                    start = left
                freq[ord(s[left])] += 1
                if freq[ord(s[left])] > 0:
                    count -= 1
                left += 1
            right += 1
        return "" if mini == float('inf') else s[start:start+mini]




sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
ans = sol.func(s, t)
print(ans)
