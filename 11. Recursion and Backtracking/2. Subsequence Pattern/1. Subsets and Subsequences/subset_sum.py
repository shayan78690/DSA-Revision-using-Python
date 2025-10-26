class Solution(object):
    def subsetSums(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def backtrack(index, current_sum, arr, result):
            if index == len(arr):
                result.append(current_sum)
                return
            
            # Include arr[index]
            backtrack(index + 1, current_sum + arr[index], arr, result)
            # Exclude arr[index]
            backtrack(index + 1, current_sum, arr, result)
        
        result = []
        backtrack(0, 0, arr, result)
        result.sort()
        return result


# Example usage
if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    solution = Solution()
    print(solution.subsetSums(arr))
