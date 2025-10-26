class Solution(object):
    @staticmethod
    def findAllSubsequences(arr, target_sum):
        """
        :type arr: List[int]
        :type target_sum: int
        :rtype: bool
        """
        def backtrack(arr, n, idx, target_sum, lst, current_sum):
            if idx == n:
                if current_sum == target_sum:
                    print(lst[:])  # print a copy of current list
                    return True
                else:
                    return False

            # Include arr[idx]
            lst.append(arr[idx])
            current_sum += arr[idx]
            if backtrack(arr, n, idx + 1, target_sum, lst, current_sum):
                return True

            # Exclude arr[idx]
            lst.pop()
            current_sum -= arr[idx]
            if backtrack(arr, n, idx + 1, target_sum, lst, current_sum):
                return True

            return False

        return backtrack(arr, len(arr), 0, target_sum, [], 0)


# Example usage
if __name__ == "__main__":
    n = int(input("How many elements you want? "))
    arr = list(map(int, input("Enter array elements: ").split()))
    target_sum = int(input("Enter the value of sum: "))
    
    print(Solution.findAllSubsequences(arr, target_sum))
