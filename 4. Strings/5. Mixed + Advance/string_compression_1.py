class Solution:
    @staticmethod
    def compressTheString(s):
        result = []
        i = 0
        while i < len(s):
            count = 1
            while i < len(s) - 1 and s[i] == s[i + 1]:
                count += 1
                i += 1
            result.append(s[i])
            if count > 1:
                result.append(str(count))
            i += 1
        return ''.join(result)
