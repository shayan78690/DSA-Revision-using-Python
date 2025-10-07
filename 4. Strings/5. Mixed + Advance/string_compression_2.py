class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        write = 0
        read = 0
        while read < n:
            count = 1
            current = chars[read]
            while read + 1 < n and current == chars[read + 1]:
                count += 1
                read += 1
            chars[write] = current
            write += 1
            if count > 1:
                countStr = str(count)
                for ch in countStr:
                    chars[write] = ch
                    write += 1
            read += 1
        return write