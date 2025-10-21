class Solution:
    def generateBinaryStrings(self, n):
        result = []
        self._recur(n, "", 0, result)
        return result

    def _recur(self, n, current, last_place, result):
        if n == 0:
            result.append(current)
            return

        # Add '0' at current position
        self._recur(n - 1, current + "0", 0, result)

        # Add '1' only if last_place was '0'
        if last_place == 0:
            self._recur(n - 1, current + "1", 1, result)
