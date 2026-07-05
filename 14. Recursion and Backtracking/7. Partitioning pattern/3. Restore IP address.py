class Solution:
    def restoreIpAddresses(self, s):
        result = []
        self.func(s, 0, [], result)
        return result

    def func(self, s, start, current, result):
        # If we already have 4 segments
        if len(current) == 4:
            if start == len(s):
                result.append(".".join(current))
            return

        # Try segment lengths of 1, 2, and 3
        for end in range(start, min(start + 3, len(s))):
            part = s[start:end + 1]

            if self.isValid(part):
                current.append(part)
                self.func(s, end + 1, current, result)
                current.pop()

    def isValid(self, part):
        # Leading zero check
        if len(part) > 1 and part[0] == '0':
            return False

        # Value check
        if int(part) > 255:
            return False

        return True
