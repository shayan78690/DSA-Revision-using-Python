class Solution:
    def subarrayXor(self, arr, k):
        freq = {}
        freq[0] = 1
        count = 0
        xor = 0
        for i in arr:
            xor = xor ^ i
            x = xor ^ k
            if x in freq:
                count += freq[x]
                
            freq[xor] = freq.get(xor, 0) +1
        return count