class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        ans = []
        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def backtrack(digits, index, ans, path):
            if len(path) == len(digits):
                ans.append("".join(path))
                return

            possible = mapping[int(digits[index])]
            for c in possible:
                path.append(c)
                backtrack(digits, index + 1, ans, path)
                path.pop()

        backtrack(digits, 0, ans, [])
        return ans


# Example usage
if __name__ == "__main__":
    digits = "23"
    solution = Solution()
    print(solution.letterCombinations(digits))
