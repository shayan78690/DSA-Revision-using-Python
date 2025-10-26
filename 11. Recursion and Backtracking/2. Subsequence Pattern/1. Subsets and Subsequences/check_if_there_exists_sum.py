class Solution(object):
    @staticmethod
    def checkSubsequenceSum(N, a, K):
        """
        :type N: int
        :type a: List[int]
        :type K: int
        :rtype: bool
        """
        def backtrack(n, k, a, current_sum, lst, idx):
            if idx == len(a):
                return current_sum == k

            # Include a[idx]
            lst.append(a[idx])
            current_sum += a[idx]
            if backtrack(n, k, a, current_sum, lst, idx + 1):
                return True

            # Exclude a[idx]
            lst.pop()
            current_sum -= a[idx]
            if backtrack(n, k, a, current_sum, lst, idx + 1):
                return True

            return False

        return backtrack(N, K, a, 0, [], 0)


# Example usage
if __name__ == "__main__":
    N = int(input("Enter number of elements: "))
    a = list(map(int, input("Enter array elements: ").split()))
    K = int(input("Enter target sum K: "))
    
    print(Solution.checkSubsequenceSum(N, a, K))
