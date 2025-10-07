class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        freq = {}
        for m in magazine:
            freq[m] = freq.get(m, 0) + 1
        
        for i in range(len(ransomNote)):
            if ransomNote[i] not in freq or freq[ransomNote[i]] == 0:
                return False
            freq[ransomNote[i]] -= 1
        return True
            
        