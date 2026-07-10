class Solution:
    def longestCommonSubsequence(self, text1, text2):
        return self.func(text1, text2, 0, 0)

    def func(self, s1, s2, i, j):
        if i == len(s1) or j == len(s2):
            return ""

        if s1[i] == s2[j]:
            return s1[i] + self.func(s1, s2, i + 1, j + 1)

        skip1 = self.func(s1, s2, i + 1, j)
        skip2 = self.func(s1, s2, i, j + 1)

        if len(skip1) > len(skip2):
            return skip1
        else:
            return skip2
