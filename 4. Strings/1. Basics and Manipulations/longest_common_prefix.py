class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        n = len(strs)
        lis = []
        first = strs[0]
        last = strs[n-1]
        for i in range(len(first)):
            if first[i] != last[i]:
                return "".join(lis)
            else:
                lis.append(first[i])
        return "".join(lis)