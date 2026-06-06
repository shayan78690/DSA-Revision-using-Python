class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        n = len(answerKey)
        left = 0
        right = 0
        maxi = 0
        max_freq = 0
        freq = [0] * 26
        while right < n:
            freq[ord(answerKey[right])-ord('A')] += 1
            max_freq = max(max_freq, freq[ord(answerKey[right])-ord('A')])
            while (right-left+1)-max_freq > k:
                freq[ord(answerKey[left])-ord('A')] -= 1
                max_freq = max(freq)
                left += 1
            if (right-left+1)-max_freq <= k:
                maxi = max(maxi, right-left+1)
            right += 1
        return maxi

        
