class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        ans = []
        for i in range(len(words)):
            string = words[i]
            for j in range(len(string)-1, -1, -1):
                ans.append(string[j])
            if i < len(words)-1:
                ans.append(" ")
        return "".join(ans)