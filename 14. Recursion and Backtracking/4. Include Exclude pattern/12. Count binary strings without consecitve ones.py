class Solution:
    def countStrings(self, n):
        return self.func(n, "", 0)
    def func(self, n, string, idx):
        if idx == n:
            return 1
        first = self.func(n, string+"0", idx+1)
        second = 0
        if not string or string[-1] != "1":
            second = self.func(n, string+"1", idx+1)
        return first+second



class Solution:
    def countStrings(self, n):
        return self.func(n, 0, False)

    def func(self, n, idx, prevOne):
        if idx == n:
            return 1

        # Always place 0
        count = self.func(n, idx + 1, False)

        # Place 1 only if previous wasn't 1
        if not prevOne:
            count += self.func(n, idx + 1, True)

        return count
