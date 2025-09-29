class Solution:
    def findUnion(self, a, b):
        s = set()          # use set to store unique elements
        for i in a:
            s.add(i)       # add elements of a
        for i in b:
            s.add(i)       # add elements of b
        return list(s)     # convert set to list



class Solution1:
    def findUnion(self, a, b):
        freq = {}
        for i in a:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for i in b:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        
        ans = []
        for i in freq:
            ans.append(i)
        return ans
    
    
    
class Solution2:
    def findUnion(self, a, b):
        n = len(a)
        m = len(b)
        i = 0
        j = 0
        ans = []
        while i < n and j < m:
            if a[i] <= b[j]:
                if len(ans) == 0 or ans[-1] != a[i]: 
                    ans.append(a[i])
                i += 1
            else:
                if len(ans) == 0 or ans[-1] != b[j]:
                    ans.append(b[j])
                j += 1
        
        while i < n:
            if len(ans) == 0 or ans[-1] != a[i]:
                ans.append(a[i])
            i += 1
        
        while j < m:
            if len(ans) == 0 or b[j] != ans[-1]:
                ans.append(b[j])
            j += 1
        
        
        return ans
