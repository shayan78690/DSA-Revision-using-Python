class Solution:
    def count_NGE(self, arr, indices):
        n = len(arr)
        result = [0] * n
        for i in range(n):
            count = 0
            for j in range(i+1, n):
                if arr[j] > arr[i]:
                    count += 1
            result[i] = count
        
        ans = [0] * len(indices)
        for i in range(len(indices)):
            ans[i] = result[indices[i]]
        return ans
        
