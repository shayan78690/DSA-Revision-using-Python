
class Solution:
    
    def subArrayExists(self,arr):
        n = len(arr)
        s = 0
        hashset = set()
        for a in arr:
            s += a
            if s == 0:
                return True
            if s in hashset:
                return True
            hashset.add(s)
        return False
        
