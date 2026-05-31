class Solution:

	def anagram(self, s, t):
	    count = [0] * 26
	    for i in range(len(s)):
	        count[ord(s[i])-ord('a')] += 1
	        count[ord(t[i])-ord('a')] -= 1
	       
	    for i in range(len(count)):
	        if count[i] != 0:
	            return False
	    return True
	    
	def search(self,pat, txt):
	    n = len(txt)
	    m = len(pat)
	    count = 0
	    left = 0
	    right = 0
	    while right < n:
	        if right-left+1 > m:
	            left += 1
	        if right-left+1 == m:
	            if self.anagram(txt[left:right+1], pat):
	                count += 1

class Solution:
	    
	def search(self,pat, txt):
	    n = len(txt)
	    m = len(pat)
	    if m > n:
	        return 0
	    pat_freq = [0] * 26
	    for i in range(m):
	        pat_freq[ord(pat[i])-ord('a')] += 1
	    
	    window_freq = [0] * 26
	    left = 0
	    count = 0
	    for right in range(n):
	        window_freq[ord(txt[right])-ord('a')] += 1
	        while right-left+1 > m:
	            window_freq[ord(txt[left])-ord('a')] -= 1
	            left += 1
	        if right-left+1 == m:
	            if window_freq == pat_freq:
	                count += 1
	    
	    return count
	            


	        right += 1
	    return count
	            
