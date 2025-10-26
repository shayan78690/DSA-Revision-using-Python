class Solution(object):
    def combinationSum(self, arr):
        """
        :type arr: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(arr, target, ans, lst, index):
            if index == len(arr):
                if target == 0:
                    ans.append(lst[:])  # add a copy of the current list
                return

            if arr[index] <= target:
                lst.append(arr[index])
                backtrack(arr, target - arr[index], ans, lst, index)  # not index+1, can reuse same element
                lst.pop()
            
            backtrack(arr, target, ans, lst, index + 1)  # move to next element

        ans = []
        lst = []
        # We need a target value; in Java it was passed as parameter. For Python, let's define a parameter version:
        return ans  # placeholder, user can call backtrack with arr, target, ans, lst, 0
