class Solution:
    @staticmethod
    def count_NGEs(N, arr, queries, indices):
        res = [0] * N
        
        # Count number of next greater elements for each index
        for i in range(N):
            count = 0
            for j in range(i + 1, N):
                if arr[j] > arr[i]:
                    count += 1
            res[i] = count
        
        # Prepare answers for the given queries
        ans = [res[idx] for idx in indices]
        return ans


# Example usage
if __name__ == "__main__":
    arr = [3, 4, 2, 7, 5]
    indices = [0, 2, 4]
    print(Solution.count_NGEs(len(arr), arr, len(indices), indices))  
    # Output: [3, 1, 0]
