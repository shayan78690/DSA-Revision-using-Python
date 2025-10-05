class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        ans = []
        for i in range(len(words)-1, -1, -1):
            ans.append(words[i])
            if i > 0:
                ans.append(" ")
        return "".join(ans)