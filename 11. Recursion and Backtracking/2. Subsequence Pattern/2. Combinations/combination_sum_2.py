class Solution(object):
    def combinationSum2(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(arr, n, target, ans, lst, index):
            if target == 0:
                ans.append(lst[:])  # add copy of current list
                return
            
            for i in range(index, len(arr)):
                if i > index and arr[i] == arr[i - 1]:
                    continue
                if arr[i] > target:
                    break
                lst.append(arr[i])
                backtrack(arr, n, target - arr[i], ans, lst, i + 1)
                lst.pop()
        
        arr.sort()
        ans = []
        lst = []
        backtrack(arr, len(arr), target, ans, lst, 0)
        return ans


# Example usage
if __name__ == "__main__":
    arr = [10,1,2,7,6,1,5]
    target = 8
    solution = Solution()
    print(solution.combinationSum2(arr, target))
