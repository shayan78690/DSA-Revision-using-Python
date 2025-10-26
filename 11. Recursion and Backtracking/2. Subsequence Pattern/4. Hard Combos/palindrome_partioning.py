class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(s, start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def backtrack(index, ans, path, s):
            if index == len(s):
                ans.append(path[:])  # add a copy of the current path
                return

            for i in range(index, len(s)):
                if isPalindrome(s, index, i):
                    path.append(s[index:i+1])
                    backtrack(i + 1, ans, path, s)
                    path.pop()

        ans = []
        backtrack(0, ans, [], s)
        return ans


# Example usage
if __name__ == "__main__":
    s = "aab"
    solution = Solution()
    print(solution.partition(s))
