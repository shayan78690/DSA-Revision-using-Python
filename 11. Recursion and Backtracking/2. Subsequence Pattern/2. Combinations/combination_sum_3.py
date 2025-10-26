class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def backtrack(k, n, ans, lst, element):
            if len(lst) >= k:
                if n == 0:
                    ans.append(lst[:])  # add copy of current list
                return

            for i in range(element, 10):  # 1 to 9 inclusive
                if i > n:
                    break
                lst.append(i)
                backtrack(k, n - i, ans, lst, i + 1)
                lst.pop()

        ans = []
        lst = []
        backtrack(k, n, ans, lst, 1)
        return ans


# Example usage
if __name__ == "__main__":
    k = 3
    n = 7
    solution = Solution()
    print(solution.combinationSum3(k, n))
