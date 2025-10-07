class Solution:
    def compressedString(self, word):
        n = len(word)
        sb = []
        i = 0
        while i < n:
            count = 1
            ch = word[i]
            while i + 1 < n and ch == word[i + 1] and count < 9:
                count += 1
                i += 1
            sb.append(str(count))
            sb.append(ch)
            i += 1
        return ''.join(sb)
