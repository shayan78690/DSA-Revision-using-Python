class Solution(object):
    def findAllSubsequences(self, arr, target_sum):
        """
        :type arr: List[int]
        :type target_sum: int
        """
        def backtrack(arr, n, idx, current_sum, lst):
            if idx == n:
                if current_sum == target_sum:
                    print(lst[:])  # print a copy of current list
                return

            # Include arr[idx]
            lst.append(arr[idx])
            backtrack(arr, n, idx + 1, current_sum + arr[idx], lst)

            # Exclude arr[idx]
            lst.pop()
            backtrack(arr, n, idx + 1, current_sum, lst)

        backtrack(arr, len(arr), 0, 0, [])


# Example usage
if __name__ == "__main__":
    n = int(input("How many elements you want? "))
    arr = list(map(int, input("Enter Array Elements: ").split()))
    target_sum = int(input("Enter the value of sum: "))
    
    solution = Solution()
    solution.findAllSubsequences(arr, target_sum)
