class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        for i in range(len(s)):
            ch = s[i]
            ans.append(ch.lower())
        return "".join(ans)
        