class Solution:
    def generateParenthesis(self, n):
        ans = []
        self.backtrack(n, 0, 0, ans, "")
        return ans

    def backtrack(self, n, open_count, close_count, ans, curr):
        if len(curr) == n * 2:
            ans.append(curr)
            return

        if open_count < n:
            self.backtrack(n, open_count + 1, close_count, ans, curr + "(")
        if close_count < open_count:
            self.backtrack(n, open_count, close_count + 1, ans, curr + ")")
